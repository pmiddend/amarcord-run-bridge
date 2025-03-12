import datetime
from dataclasses import dataclass
from enum import Enum
from statistics import mean
from types import TracebackType
from typing import Any
from typing import TypeAlias

import structlog
from amarcord_open.api.attributi_api import AttributiApi
from amarcord_open.api.runs_api import RunsApi
from amarcord_open.api_client import ApiClient
from amarcord_open.configuration import Configuration
from amarcord_open.models import AttributoType
from amarcord_open.models import JsonAttributoValue
from amarcord_open.models import JsonCreateAttributiFromSchemaInput
from amarcord_open.models import JsonCreateAttributiFromSchemaSingleAttributo
from amarcord_open.models import JsonCreateOrUpdateRun
from amarcord_open.models import JsonRunFile
from amarcord_open.models import JSONSchemaArray
from amarcord_open.models import JSONSchemaBoolean
from amarcord_open.models import JSONSchemaInteger
from amarcord_open.models import JSONSchemaNumber
from amarcord_open.models import JSONSchemaString
from pydantic import BaseModel
from typing_extensions import Self

from run_bridge.logging_util import setup_structlog

setup_structlog()
logger = structlog.stdlib.get_logger(__name__)


class AttributoOperation(Enum):
    TAKE_FIRST = "take-first"
    TAKE_LAST = "take-last"
    AVG = "avg"


class AttributoDescription(BaseModel):
    input_attribute_name: str
    operation: AttributoOperation

    attributo_name: str
    attributo_description: str
    amarcord_type: AttributoType

    # When using types from the OpenAPI generator, we have to take
    # care of them manally: they don't deserialize with the usual
    # pydanctic "Model(**bla)" kwargs from JSON deserializatin, but
    # rather have this "from_dict" function that we call manually
    # here. Ugly, I know.
    def __init__(self, **kwargs: Any) -> None:
        kwargs["amarcord_type"] = AttributoType.from_dict(kwargs["amarcord_type"])
        super().__init__(**kwargs)


class Config(BaseModel):
    amarcord_url: str
    amarcord_basic_auth: str
    attributi: list[AttributoDescription]

    def get_user_name_and_password(
        self,
    ) -> tuple[None | str, None | str]:
        username_and_password = self.amarcord_basic_auth.split(":", maxsplit=2)

        if len(username_and_password) == 2:
            username, password = username_and_password
        else:
            username = None
            password = None
        return username, password


RuntimeAttributoValue: TypeAlias = None | str | int | float | bool


@dataclass(frozen=True)
class RuntimeNamedAttributeValue:
    attribute_name: str
    value: RuntimeAttributoValue


@dataclass(frozen=True)
class RuntimeFilePath:
    source: str
    glob: str


@dataclass
class RuntimeRun:
    run_id: int
    attribute_names_to_values: dict[str, list[RuntimeAttributoValue]]
    attributo_name_to_id: dict[str, int]
    attributi: list[AttributoDescription]
    started: int
    files: list[RuntimeFilePath]


@dataclass(frozen=True)
class CommandStartRun:
    beamtime_id: int
    run_id: int
    started: None | datetime.datetime
    attributo_values: list[RuntimeNamedAttributeValue]
    files: list[RuntimeFilePath]


@dataclass(frozen=True)
class CommandStopRun:
    beamtime_id: int
    stopped: None | datetime.datetime


@dataclass(frozen=True)
class CommandUpdateRun:
    beamtime_id: int
    attributo_values: list[RuntimeNamedAttributeValue]


IncomingCommand: TypeAlias = CommandStartRun | CommandStopRun | CommandUpdateRun


def datetime_to_attributo_int(d: datetime.datetime) -> int:
    return int(d.replace(tzinfo=datetime.timezone.utc).timestamp() * 1000)


def _runtime_run_to_update_request(
    log: structlog.stdlib.BoundLogger,
    beamtime_id: int,
    r: RuntimeRun,
    stopped: None | int,
) -> JsonCreateOrUpdateRun:
    calculated_attributi: list[JsonAttributoValue] = []
    for a in r.attributi:
        alog = log.bind(input_attribute=a.input_attribute_name)
        input_attribute_values = r.attribute_names_to_values.get(a.input_attribute_name)
        if input_attribute_values is None or not input_attribute_values:
            alog.warning("attribute has no values yet")
            continue
        final_value: RuntimeAttributoValue
        match a.operation:
            case AttributoOperation.TAKE_FIRST:
                final_value = input_attribute_values[0]
            case AttributoOperation.TAKE_LAST:
                final_value = input_attribute_values[-1]
            case AttributoOperation.AVG:
                numeric_values: list[int | float] = []
                for v in input_attribute_values:
                    if not isinstance(v, int | float):
                        alog.warning(
                            f'has operation avg, but has non-numerical value "{v}" (type {type(v)})'
                        )
                        continue
                    numeric_values.append(v)
                if not numeric_values:
                    alog.warning(
                        "has no non-numerical values yet (did you enter the wrong type?)"
                    )
                final_value = mean(numeric_values)
        attributo_id = r.attributo_name_to_id.get(a.attributo_name)
        if attributo_id is None:
            alog.error(
                "have no id for this attribute (maybe you forgot to update the schema?)"
            )
            continue
        if final_value is None:
            continue
        # not sure why this would be None, every
        assert a.amarcord_type.actual_instance is not None

        match a.amarcord_type.actual_instance:
            case JSONSchemaArray():
                alog.error("array types not supported yet")
                continue
            case JSONSchemaBoolean():
                if not isinstance(final_value, bool):
                    alog.error(
                        f"attribute should have boolean values, but calculated {final_value}"
                    )
                    continue
                calculated_attributi.append(
                    JsonAttributoValue(
                        attributo_id=attributo_id, attributo_value_bool=final_value
                    )
                )
            case JSONSchemaInteger() as schema:
                if schema.format == "chemical-id":
                    if not isinstance(final_value, int):
                        alog.error(
                            f"attribute should have integral values as chemical IDs, but calculated {final_value}"
                        )
                        continue
                    if final_value == 0:
                        # for chemical IDs we reserve 0 to mean "not there"
                        continue
                    calculated_attributi.append(
                        JsonAttributoValue(
                            attributo_id=attributo_id,
                            attributo_value_chemical=final_value,
                        )
                    )
                elif schema.format == "date-time":
                    if not isinstance(final_value, int | float):
                        alog.error(
                            f"attribute should have numerical values as unix time stamps, but calculated {final_value}"
                        )
                        continue
                    calculated_attributi.append(
                        JsonAttributoValue(
                            attributo_id=attributo_id,
                            attributo_value_datetime=int(final_value),
                        )
                    )
                else:
                    if not isinstance(final_value, int | float):
                        alog.error(
                            f"attribute should have numerical values, but calculated {final_value}"
                        )
                        continue
                    calculated_attributi.append(
                        JsonAttributoValue(
                            attributo_id=attributo_id,
                            # could be float here and we'll allow that for now
                            attributo_value_int=round(final_value),
                        )
                    )
            case JSONSchemaNumber():
                if not isinstance(final_value, int | float):
                    alog.error(
                        f"attribute should have numerical values as chemical IDs, but calculated {final_value}"
                    )
                    continue
                calculated_attributi.append(
                    JsonAttributoValue(
                        attributo_id=attributo_id,
                        attributo_value_float=final_value,
                    )
                )
            case JSONSchemaString() as schema:
                if not isinstance(final_value, str):
                    alog.error(
                        f"attribute should have string values, but calculated {final_value}"
                    )
                    continue
                if schema.enum is not None and final_value not in schema.enum:
                    alog.error(
                        f"attribute not in allowed boundaries: {final_value} not one of "
                        + ", ".join(schema.enum)
                    )
                    continue
                calculated_attributi.append(
                    JsonAttributoValue(
                        attributo_id=attributo_id, attributo_value_str=final_value
                    )
                )
    return JsonCreateOrUpdateRun(
        beamtime_id=beamtime_id,
        files=[JsonRunFile(id=0, glob=f.glob, source=f.source) for f in r.files],
        attributi=calculated_attributi,
        started=r.started,
        stopped=stopped,
    )


class Server:
    @staticmethod
    async def init(config: Config) -> "Server":
        username, password = config.get_user_name_and_password()

        logger.info(f"auth: {username=}, {password=}")
        configuration = Configuration(
            host=config.amarcord_url, username=username, password=password
        )
        api_client = ApiClient(configuration)
        auth_token = configuration.get_basic_auth_token()
        auth_headers: dict[str, str] = (
            {"Authorization": auth_token} if auth_token else {}
        )

        return Server(config, auth_headers, api_client)

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        await self._api_client.close()

    def __init__(
        self,
        config: Config,
        auth_headers: dict[str, str],
        api_client: ApiClient,
    ) -> None:
        self._config = config
        self._api_client = api_client
        self._auth_headers = auth_headers
        self._beamtime_id_to_current_run: dict[int, RuntimeRun] = {}

    async def send_schema(self, beamtime_id: int) -> None:
        api_instance = AttributiApi(self._api_client)

        existing_attributo_names = set(
            a.name
            for a in (
                await api_instance.read_attributi_api_attributi_beamtime_id_get(
                    beamtime_id, _headers=self._auth_headers
                )
            ).attributi
        )

        new_attributi = [
            JsonCreateAttributiFromSchemaSingleAttributo(
                attributo_name=ad.attributo_name,
                description=ad.attributo_description,
                attributo_type=ad.amarcord_type,
            )
            for ad in self._config.attributi
            if ad.attributo_name not in existing_attributo_names
        ]

        if not new_attributi:
            logger.info("no new attributi detected, not doing anything")
        else:
            logger.info(f"sending the following attributi: {new_attributi}")
            create_response = await api_instance.create_attributi_from_schema_api_attributi_schema_post(
                JsonCreateAttributiFromSchemaInput(
                    attributi_schema=new_attributi,
                    beamtime_id=beamtime_id,
                ),
                _headers=self._auth_headers,
            )
            logger.info(f"created {create_response} new attribut(oi)")

    async def _process_start_run(self, c: CommandStartRun) -> None:
        run_logger = logger.bind(run_id=c.run_id, beamtime_id=c.beamtime_id)

        prior_run = self._beamtime_id_to_current_run.get(c.beamtime_id)

        if prior_run is not None:
            run_logger.info(
                f"start run, but prior {prior_run.run_id} is not finished, closing"
            )

        api_instance = AttributiApi(self._api_client)

        attributo_name_to_id: dict[str, int] = {
            a.name: a.id
            for a in (
                await api_instance.read_attributi_api_attributi_beamtime_id_get(
                    c.beamtime_id,
                    _headers=self._auth_headers,
                )
            ).attributi
        }

        new_run = RuntimeRun(
            run_id=c.run_id,
            attribute_names_to_values={
                a.attribute_name: [a.value] for a in c.attributo_values
            },
            attributi=self._config.attributi,
            attributo_name_to_id=attributo_name_to_id,
            files=c.files,
            started=datetime_to_attributo_int(
                c.started
                if c.started is not None
                else datetime.datetime.now(datetime.timezone.utc)
            ),
        )
        self._beamtime_id_to_current_run[c.beamtime_id] = new_run

        api_instance = RunsApi(self._api_client)
        api_response = (
            await api_instance.create_or_update_run_api_runs_run_external_id_post(
                run_external_id=c.run_id,
                json_create_or_update_run=_runtime_run_to_update_request(
                    run_logger, c.beamtime_id, new_run, stopped=None
                ),
                _headers=self._auth_headers,
            )
        )

        run_logger.info(f"response: {api_response}")

    async def _process_update_run(self, c: CommandUpdateRun) -> None:
        bt_logger = logger.bind(beamtime_id=c.beamtime_id)

        run = self._beamtime_id_to_current_run.get(c.beamtime_id)

        if run is None:
            bt_logger.warning(
                "no ongoing run, cannot update it (maybe a small race-condition?)"
            )
            return

        run_logger = bt_logger.bind(run_id=run.run_id)

        for av in c.attributo_values:
            alog = run_logger.bind(input_attribute=av.attribute_name)
            value_list = run.attribute_names_to_values.get(av.attribute_name)

            if value_list is None:
                alog.warning(
                    "this attribute is new, ignoring (the client sends more than the server wants - possibly update config of the server?)"
                )
                continue

            value_list.append(av.value)

        api_instance = RunsApi(self._api_client)
        api_response = (
            await api_instance.create_or_update_run_api_runs_run_external_id_post(
                run_external_id=run.run_id,
                json_create_or_update_run=_runtime_run_to_update_request(
                    run_logger, c.beamtime_id, run, stopped=None
                ),
                _headers=self._auth_headers,
            )
        )

        run_logger.info(f"run updated, response: {api_response}")

    async def _process_stop_run(self, c: CommandStopRun) -> None:
        bt_logger = logger.bind(beamtime_id=c.beamtime_id)

        run = self._beamtime_id_to_current_run.get(c.beamtime_id)

        if run is None:
            bt_logger.warning(
                "no ongoing run, cannot stop it (maybe a small race-condition?)"
            )
            return

        run_logger = bt_logger.bind(run_id=run.run_id)

        api_instance = RunsApi(self._api_client)
        api_response = (
            await api_instance.create_or_update_run_api_runs_run_external_id_post(
                run_external_id=run.run_id,
                json_create_or_update_run=_runtime_run_to_update_request(
                    run_logger,
                    c.beamtime_id,
                    run,
                    stopped=datetime_to_attributo_int(
                        c.stopped
                        if c.stopped is not None
                        else datetime.datetime.now(datetime.timezone.utc)
                    ),
                ),
                _headers=self._auth_headers,
            )
        )
        run_logger.info(f"run stopped, response: {api_response}")

        self._beamtime_id_to_current_run.pop(c.beamtime_id)

    async def process_command(self, command: IncomingCommand) -> None:
        match command:
            case CommandStartRun():
                await self._process_start_run(command)
            case CommandUpdateRun():
                await self._process_update_run(command)
            case CommandStopRun():
                await self._process_stop_run(command)


# with Path("config.json").open("r") as f:
#     config = Config(**json.load(f))

#     asyncio.run(Server.init(config))

# ft = AttributoType.from_dict({"type": "integer", "format": "chemical-id"})
# ft = AttributoType(**{"type": "integer", "format": "chemical-id"})
# ad = AttributoDescription(
#     **{
#         "input_attribute_name": "channel_1_chemical",
#         "operation": "take-first",
#         "attributo_name": "channel_1_chemical_id",
#         "attributo_description": "First channel chemical",
#         "amarcord_type": {"type": "integer", "format": "chemical-id"},
#     }
# )
# logger.info(f"ft: {ad}")
