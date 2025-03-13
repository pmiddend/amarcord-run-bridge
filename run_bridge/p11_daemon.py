import asyncio
import datetime
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from typing import TypeAlias

import structlog
from amarcord_open.api.beamtimes_api import BeamtimesApi
from amarcord_open.api_client import ApiClient
from amarcord_open.configuration import Configuration
from pydantic import BaseModel
from tango import DeviceProxy
from tango import GreenMode

from run_bridge import server
from run_bridge.logging_util import setup_structlog

setup_structlog()
logger = structlog.stdlib.get_logger(__name__)


class TangoAttribute(BaseModel):
    attribute_name: str
    # optional polling rate for example


class TangoDevice(BaseModel):
    device_url: str
    attributes: list[TangoAttribute]


class Config(BaseModel):
    tango_devices: list[TangoDevice]
    tape_drive_runner_url: str
    p11_runner_url: str
    raw_file_path_template: str
    server_config: server.Config


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


async def main_loop(
    rc: RuntimeConfig,
    server_instance: server.Server,
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
                logger.info("waiting for run to end, we didn't catch its beginning...")
                await asyncio.sleep(_SLEEP_DURATION_S)
            case [Measuring(beamtime_id=None), False]:
                logger.info("was waiting for run to end, now done...")
                state = NotMeasuring()
                await asyncio.sleep(_SLEEP_DURATION_S)
            case [Measuring(beamtime_id=beamtime_id, stop_sent=True), True]:
                logger.info(
                    "still measuring, but stop sent, waiting for run to finish..."
                )
                await asyncio.sleep(_SLEEP_DURATION_S)
            case [Measuring(beamtime_id=beamtime_id, stop_sent=True), False]:
                logger.info("not measuring after stop...")
                state = NotMeasuring()
                await asyncio.sleep(_SLEEP_DURATION_S)
            case [Measuring(beamtime_id=beamtime_id, stop_sent=False), True]:
                # technically reduntant, but basedpyright doesn't get it (yet)
                assert beamtime_id is not None

                logger.info("still measuring, updating attributi values...")

                attributo_values_to_update: list[server.RuntimeNamedAttributeValue] = [
                    server.RuntimeNamedAttributeValue(
                        attribute_name=a.attribute_name,
                        value=await a.read_value(),
                    )
                    for a in rc.tango_attributes
                ]

                await server_instance.process_command(
                    server.CommandUpdateRun(
                        beamtime_id=beamtime_id,
                        attributo_values=attributo_values_to_update,
                    )
                )
                await asyncio.sleep(_SLEEP_DURATION_S)
            case [Measuring(beamtime_id=beamtime_id), False]:
                assert beamtime_id is not None
                logger.info("not measuring anymore, sending stop")
                await server_instance.process_command(
                    server.CommandStopRun(beamtime_id=beamtime_id, stopped=None)
                )
                await asyncio.sleep(_SLEEP_DURATION_S)
                state = Measuring(beamtime_id=beamtime_id, stop_sent=True)
            case [NotMeasuring(), False]:
                # logger.info("still not measuring")
                await asyncio.sleep(_SLEEP_DURATION_S)
            case [NotMeasuring(), True]:
                logger.info("starting to measure")
                beamtime_id = await rc.beamtime_id_attribute.read_value()

                api_instance = BeamtimesApi(api_client)
                beamtime_info = (
                    await api_instance.read_beamtime_api_beamtimes_beamtime_id_get_with_http_info(
                        beamtime_id, _headers=auth_headers
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

                attributo_values: list[server.RuntimeNamedAttributeValue] = [
                    server.RuntimeNamedAttributeValue(
                        attribute_name=a.attribute_name,
                        value=await a.read_value(),
                    )
                    for a in rc.tango_attributes
                ]
                logger.info(f"sending {attributo_values}")
                state = Measuring(beamtime_id=beamtime_id, stop_sent=False)
                await server_instance.process_command(
                    server.CommandStartRun(
                        beamtime_id=beamtime_id,
                        run_id=run_id,
                        started=None,
                        attributo_values=attributo_values,
                        files=[
                            server.RuntimeFilePath(source="raw", glob=raw_file_path)
                        ],
                    )
                )
            case _:
                logger.error(f"some state was hot handled, but which one? {state}")


async def wait_for_runner(c: Config) -> None:
    counter = 0
    while True:
        counter += 1
        if counter % 100 == 0:
            logger.info(f"still waiting for P11 device on {c.p11_runner_url}")
        try:
            dp = DeviceProxy(c.p11_runner_url, green_mode=GreenMode.Asyncio)
            # this ping method is weird as hell; declared, they way I see it, as a staticmethod, but isn't really static
            await dp.ping()  # type: ignore
            return
        except:
            if counter == 1:
                logger.info(
                    f"didn't get P11 device on {c.p11_runner_url}, waiting for it"
                )
            await asyncio.sleep(10)


async def async_main(c: Config) -> None:
    await wait_for_runner(c)

    config_errors = False
    for a in c.server_config.attributi:
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
            logger.error(
                f"attributo “{a.attributo_name}” refers to input attribute “{tango_name}”, but I cannot find that"
            )
            config_errors = True
    if config_errors:
        sys.exit(1)

    async with await server.Server.init(c.server_config) as server_instance:
        # server_instance = await server.Server.init(c.server_config)

        if len(sys.argv) > 2 and sys.argv[-2] == "send-schema":
            logger.info("sending schema...")
            try:
                beamtime_id = int(sys.argv[-1])
            except:
                logger.error(
                    "send-schema: please specify the beamtime ID as the last argument"
                )

            await server_instance.send_schema(beamtime_id)
            return

        logger.info("initing runtime config...")
        rc = await initialize_runtime_config(c)

        if rc is None:
            logger.error("exiting...")
            sys.exit(1)

        username, password = c.server_config.get_user_name_and_password()

        configuration = Configuration(
            host=c.server_config.amarcord_url, username=username, password=password
        )

        async with ApiClient(configuration) as api_client:
            auth_headers = {"Authorization": configuration.get_basic_auth_token()}

            logger.info("starting main loop...")
            await main_loop(rc, server_instance, api_client, auth_headers)


def main() -> None:  # pragma: no cover
    with Path(sys.argv[1]).open("r", encoding="utf-8") as f:
        config = Config(**json.load(f))

    asyncio.run(async_main(config))


if __name__ == "__main__":  # pragma: no cover
    main()
