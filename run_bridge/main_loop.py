import asyncio
import datetime
import sys
from collections import deque
from dataclasses import dataclass
from typing import Any
from typing import TypeAlias

import structlog
from amarcord_open import BeamtimesApi
from amarcord_open import Configuration
from amarcord_open.api_client import ApiClient
from pydantic import BaseModel
from tango import DeviceProxy
from tango import GreenMode

from run_bridge import amarcord_connector

logger = structlog.stdlib.get_logger(__name__)


class TangoAttribute(BaseModel):
    attribute_name: str
    # optional polling rate for example


class TangoDevice(BaseModel):
    device_url: str
    attributes: list[TangoAttribute]


class Config(BaseModel):
    description: str = ""
    tango_devices: list[TangoDevice]
    tape_drive_runner_url: str
    p11_runner_url: str
    raw_file_path_template: str
    amarcord_connector_config: amarcord_connector.Config


@dataclass(frozen=True)
class TangoRuntimeAttribute:
    device_proxy: DeviceProxy
    attribute_name: str

    async def read_value(self) -> Any:
        return (await self.device_proxy.read_attribute(self.attribute_name)).value


@dataclass
class RuntimeConfig:
    raw_file_path_template: str
    tango_attributes: list[TangoRuntimeAttribute]
    measuring_attribute: TangoRuntimeAttribute
    beamtime_id_attribute: TangoRuntimeAttribute
    run_id_attribute: TangoRuntimeAttribute


_MEASURING_ATTRIBUTE_NAME = "state_enum"
_MEASURING_ATTRIBUTE_MEASURING_STATE = "measuring"
_BEAMTIME_ID_ATTRIBUTE_NAME = "selected_beamtime_id"
_RUN_ID_ATTRIBUTE_NAME = "run_id"
_SLEEP_DURATION_S = 1


@dataclass(frozen=True)
class Measuring:
    # can be None in case the service was started during an ongoing run
    beamtime_id: None | int
    stop_sent: bool


@dataclass(frozen=True)
class NotMeasuring:
    pass


State: TypeAlias = Measuring | NotMeasuring


async def initialize_runtime_config(c: Config) -> None | RuntimeConfig:
    attributes: list[TangoRuntimeAttribute] = []
    measuring_attribute: None | TangoRuntimeAttribute = None
    beamtime_id_attribute: None | TangoRuntimeAttribute = None
    run_id_attribute: None | TangoRuntimeAttribute = None
    for d in c.tango_devices:
        proxy = DeviceProxy(d.device_url, green_mode=GreenMode.Asyncio)
        for a in d.attributes:
            ra = TangoRuntimeAttribute(proxy, a.attribute_name)
            if (
                a.attribute_name == _MEASURING_ATTRIBUTE_NAME
                and d.device_url == c.p11_runner_url
            ):
                measuring_attribute = ra
            if (
                a.attribute_name == _BEAMTIME_ID_ATTRIBUTE_NAME
                and d.device_url == c.tape_drive_runner_url
            ):
                beamtime_id_attribute = ra
            if (
                a.attribute_name == _RUN_ID_ATTRIBUTE_NAME
                and d.device_url == c.p11_runner_url
            ):
                run_id_attribute = ra
            attributes.append(ra)

    if measuring_attribute is None:
        logger.error(
            f"cannot find the measuring attribute {_MEASURING_ATTRIBUTE_NAME} in the list of defined attributes for runner {c.tape_drive_runner_url}"
        )
        return None

    if beamtime_id_attribute is None:
        logger.error(
            f"cannot find the beamtime ID attribute {_BEAMTIME_ID_ATTRIBUTE_NAME} in the list of defined attributes for runner {c.tape_drive_runner_url}"
        )
        return None

    if run_id_attribute is None:
        logger.error(
            f"cannot find the run ID attribute {_RUN_ID_ATTRIBUTE_NAME} in the list of defined attributes for P11 runner {c.p11_runner_url}"
        )
        return None

    return RuntimeConfig(
        c.raw_file_path_template,
        attributes,
        measuring_attribute,
        beamtime_id_attribute,
        run_id_attribute,
    )


@dataclass(frozen=True)
class LoopMessage:
    time: datetime.datetime
    level: str
    message: str

    @staticmethod
    def info(message: str) -> "LoopMessage":
        return LoopMessage(time=datetime.datetime.now(), level="info", message=message)

    @staticmethod
    def error(message: str) -> "LoopMessage":
        return LoopMessage(time=datetime.datetime.now(), level="error", message=message)


class LogBackend:
    def __init__(self) -> None:
        self.messages: deque[LoopMessage] = deque(maxlen=30)

    def append(self, message: LoopMessage) -> None:
        self.messages.append(message)
        if message.level == "info":
            logger.info(message.message)
        elif message.level == "error":
            logger.error(message.message)
        elif message.level == "warning":
            logger.warning(message.message)
        else:
            logger.info(message.message)


async def main_loop(
    messages: LogBackend,
    rc: RuntimeConfig,
    connector_instance: amarcord_connector.AmarcordConnector,
    api_client: ApiClient,
    auth_headers: dict[str, Any],
) -> None:
    state: State = (
        Measuring(beamtime_id=None, stop_sent=False)
        if await rc.measuring_attribute.read_value()
        == _MEASURING_ATTRIBUTE_MEASURING_STATE
        else NotMeasuring()
    )

    while True:
        now_measuring = (
            await rc.measuring_attribute.read_value()
            == _MEASURING_ATTRIBUTE_MEASURING_STATE
        )

        match [state, now_measuring]:
            case [Measuring(beamtime_id=None), True]:
                messages.append(
                    LoopMessage.info(
                        "waiting for run to end, we didn't catch its beginning..."
                    )
                )
                await asyncio.sleep(_SLEEP_DURATION_S)
            case [Measuring(beamtime_id=None), False]:
                messages.append(
                    LoopMessage.info("was waiting for run to end, now done...")
                )
                state = NotMeasuring()
                await asyncio.sleep(_SLEEP_DURATION_S)
            case [Measuring(beamtime_id=beamtime_id, stop_sent=True), True]:
                messages.append(
                    LoopMessage.info(
                        "still measuring, but stop sent, waiting for run to finish..."
                    )
                )
                await asyncio.sleep(_SLEEP_DURATION_S)
            case [Measuring(beamtime_id=beamtime_id, stop_sent=True), False]:
                messages.append(LoopMessage.info("not measuring after stop..."))
                state = NotMeasuring()
                await asyncio.sleep(_SLEEP_DURATION_S)
            case [Measuring(beamtime_id=beamtime_id, stop_sent=False), True]:
                # technically reduntant, but basedpyright doesn't get it (yet)
                assert beamtime_id is not None

                messages.append(
                    LoopMessage.info("still measuring, updating attributi values...")
                )

                attributo_values_to_update: list[
                    amarcord_connector.RuntimeNamedAttributeValue
                ] = [
                    amarcord_connector.RuntimeNamedAttributeValue(
                        attribute_name=a.attribute_name,
                        value=await a.read_value(),
                    )
                    for a in rc.tango_attributes
                ]

                await connector_instance.process_command(
                    amarcord_connector.CommandUpdateRun(
                        beamtime_id=beamtime_id,
                        attributo_values=attributo_values_to_update,
                    )
                )
                await asyncio.sleep(_SLEEP_DURATION_S)
            case [Measuring(beamtime_id=beamtime_id), False]:
                assert beamtime_id is not None
                messages.append(LoopMessage.info("not measuring anymore, sending stop"))
                await connector_instance.process_command(
                    amarcord_connector.CommandStopRun(
                        beamtime_id=beamtime_id, stopped=None
                    )
                )
                await asyncio.sleep(_SLEEP_DURATION_S)
                state = Measuring(beamtime_id=beamtime_id, stop_sent=True)
            case [NotMeasuring(), False]:
                # messages.append(LoopMessage.info("still not measuring"))
                await asyncio.sleep(_SLEEP_DURATION_S)
            case [NotMeasuring(), True]:
                messages.append(LoopMessage.info("starting to measure"))
                beamtime_id = await rc.beamtime_id_attribute.read_value()

                api_instance = BeamtimesApi(api_client)
                beamtime_info = (
                    await api_instance.read_beamtime_api_beamtimes_beamtime_id_get_with_http_info(
                        beamtime_id,
                        _headers=auth_headers,
                        # Default timeout is 5min and there's no way to set a default
                        _request_timeout=amarcord_connector.AMARCORD_REQUEST_TIMEOUT_S,
                    )
                ).data

                run_id = await rc.run_id_attribute.read_value()
                raw_file_path = (
                    rc.raw_file_path_template.replace(
                        "%year%", str(datetime.date.today().year)
                    )
                    .replace("%beamtime-internal-id%", str(beamtime_id))
                    .replace("%beamtime-external-id%", beamtime_info.external_id)
                    .replace("%run-id%", str(run_id))
                )

                attributo_values: list[
                    amarcord_connector.RuntimeNamedAttributeValue
                ] = [
                    amarcord_connector.RuntimeNamedAttributeValue(
                        attribute_name=a.attribute_name,
                        value=await a.read_value(),
                    )
                    for a in rc.tango_attributes
                ]
                messages.append(
                    LoopMessage.info(
                        f"sending initial attributo values for bt {beamtime_id}, run {run_id}: <pre>{attributo_values}</pre>"
                    )
                )
                state = Measuring(beamtime_id=beamtime_id, stop_sent=False)
                await connector_instance.process_command(
                    amarcord_connector.CommandStartRun(
                        beamtime_id=beamtime_id,
                        run_id=run_id,
                        started=None,
                        attributo_values=attributo_values,
                        files=[
                            amarcord_connector.RuntimeFilePath(
                                source="raw", glob=raw_file_path
                            )
                        ],
                    )
                )
            case _:
                logger.error(f"some state was hot handled, but which one? {state}")


async def wait_for_runner(messages: LogBackend, c: Config) -> None:
    counter = 0
    while True:
        counter += 1
        if counter % 100 == 0:
            messages.append(
                LoopMessage.info(f"still waiting for P11 device on {c.p11_runner_url}")
            )
        try:
            dp = DeviceProxy(c.p11_runner_url, green_mode=GreenMode.Asyncio)
            # this ping method is weird as hell; declared, they way I see it, as a staticmethod, but isn't really static
            await dp.ping()  # type: ignore
            return
        except:
            if counter == 1:
                messages.append(
                    LoopMessage.info(
                        f"didn't get P11 device on {c.p11_runner_url}, waiting for it"
                    )
                )
            await asyncio.sleep(10)


async def async_main(messages: LogBackend, c: Config) -> None:
    await wait_for_runner(messages, c)

    messages.append(LoopMessage.info("starting loop"))

    config_errors = False
    for a in c.amarcord_connector_config.attributi:
        tango_name = a.input_attribute_name

        found = False
        for td in c.tango_devices:
            for ta in td.attributes:
                if ta.attribute_name == tango_name:
                    found = True
                    break
            if found:
                break
        if not found:
            messages.append(
                LoopMessage.error(
                    f"attributo “{a.attributo_name}” refers to input attribute “{tango_name}”, but I cannot find that"
                )
            )
            config_errors = True
    if config_errors:
        sys.exit(1)

    async with await amarcord_connector.AmarcordConnector.init(
        c.amarcord_connector_config
    ) as connector_instance:
        messages.append(LoopMessage.info("initing runtime config..."))
        rc = await initialize_runtime_config(c)

        if rc is None:
            messages.append(LoopMessage.error("exiting"))
            sys.exit(1)

        username, password = c.amarcord_connector_config.get_user_name_and_password()

        configuration = Configuration(
            host=c.amarcord_connector_config.amarcord_url,
            username=username,
            password=password,
            # this might not do the right thing
            # retries=0,
        )

        async with ApiClient(configuration) as api_client:
            auth_headers = {"Authorization": configuration.get_basic_auth_token()}

            messages.append(LoopMessage.info("starting main loop"))
            try:
                await main_loop(
                    messages, rc, connector_instance, api_client, auth_headers
                )
            except:
                logger.exception("unexpected exception, bailing out")
                sys.exit(1)
