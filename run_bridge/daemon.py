import asyncio
import datetime
from dataclasses import dataclass
from enum import Enum, auto
from pathlib import Path
import sys
from typing import TYPE_CHECKING
from typing import Any
from typing import Final

import aiohttp
import numpy as np
import structlog
from pydantic import BaseModel
from tango import DeviceProxy
from tango import DevState
from tango import GreenMode
from tango.server import Device
from tango.server import command
from tango.server import device_property

from run_bridge.logging_util import setup_structlog

setup_structlog()

logger = structlog.stdlib.get_logger(__name__)

SCHEMA_MODE = True

ATTRIBUTE_ENERGY = "Energy"
ATTRIBUTE_RUNNER_ENERGY = "beam_energy"
ATTRIBUTE_RUNNER_TRANSMISSION = "transmission_percent"

DEFAULT_POLL_INTERVAL_MS = 1000

CHANNEL_ATTRIBUTE_FLOW = "flow"

CHANNEL_ATTRIBUTE_PRESSURE_SET_POINT = "pressure_set_point"
CHANNEL_ATTRIBUTE_CHEMICAL = "chemical"
CHANNEL_ATTRIBUTE_ENABLED = "enabled"

CHANNEL_ATTRIBUTE_FLOW_SET_POINT = "flow_set_point"

CHANNEL_ATTRIBUTE_PRESSURE = "pressure"

ATTRIBUTE_EXPOSURE_TIME = "exposure_time"

ATTRIBUTE_USE_CHOPPER = "use_chopper"

ATTRIBUTE_NUMBER_OF_IMAGES = "number_of_images"

ATTRIBUTE_USE_STREAM = "use_stream"

ATTRIBUTE_RUNNER_DETECTOR_DISTANCE = "detector_tower_measurement_distance"

ATTRIBUTE_TAPE_VELOCITY_AVERAGED = "velocity_mm_per_s"

ATTRIBUTE_DETECTOR_DISTANCE_LASER = "detector_distance_laser"

STATE_POLL_RATE_MS: Final = 250

UPDATE_COMMAND_RATE_MS: Final = 500

NUMBER_OF_CHANNELS: Final = 4


@dataclass
class _ChemicalStatistics:
    chemical_id: int
    pressure_set_point: float
    flow_set_point: float
    pressures_mbar: list[float]
    flows_ul_min: list[float]


@dataclass
class _Statistics:
    beamtime_id: int
    attributo_name_to_id: dict[str, int]
    run_id: int
    run_start: None | datetime.datetime
    run_stopped: None | datetime.datetime
    detector_distances_mm: list[float]
    detector_distance_set_point_mm: float
    energies_kev: list[float]
    transmission_percent: float
    tape_velocities_mm_per_s: list[float]
    eiger_interface: str
    target_frame_count: int
    chopper_enabled: bool
    chemical_statistics: list[None | _ChemicalStatistics]
    raw_file_path: str
    exposure_time_ms: float


class AmarcordRunBridge(Device):
    green_mode = GreenMode.Asyncio

    amarcord_url = device_property(
        dtype="str",
        mandatory=True,
        doc="HTTP URL for the AMARCORD API (should end in /api)",
    )
    p11_runner_device_identifier = device_property(
        dtype="str",
        mandatory=True,
        doc="domain/family/member of the P11 runner device",
    )
    raw_file_path_template: str = device_property(  # pyright: ignore
        dtype="str",
        mandatory=True,
        doc='Template from which to construct the "raw_file_path" (i.e. the path where the detector images are stored). Allowed placeholders are %year%, %beamtime-internal-id%, %beamtime-external-id% and %run-id%',
    )
    tape_drive_runner_device_identifier = device_property(
        dtype="str",
        mandatory=True,
        doc="domain/family/member of the P11 runner device",
    )
    main_tape_device_identifier = device_property(
        dtype="str",
        mandatory=True,
        doc="domain/family/member of the Tape Drive Main Tape",
    )

    # pylint expects init_device to be non-async,
    # but setting init_device as async with the
    # GreenMode.asyncio is correct according to pytango documentation
    async def init_device(self) -> None:  # type: ignore
        # None is not awaitable?
        await super().init_device()  # pyright: ignore[reportGeneralTypeIssues]
        domain, family, member = self.get_name().split("/", maxsplit=3)
        self._logger = structlog.stdlib.get_logger(
            self.__class__.__name__, domain=domain, family=family, member=member
        )

        self._logger.info("starting device server")
        self._session = aiohttp.ClientSession()

        if TYPE_CHECKING or not SCHEMA_MODE:
            self._p11_runner = DeviceProxy(
                self.p11_runner_device_identifier, green_mode=GreenMode.Asyncio
            )
            self._main_tape = DeviceProxy(
                self.main_tape_device_identifier, green_mode=GreenMode.Asyncio
            )
            self._tape_drive_runner = DeviceProxy(
                self.tape_drive_runner_device_identifier, green_mode=GreenMode.Asyncio
            )
            if await self._read_state() == "measuring":
                self._statistics_reliable = False
                self.set_state(DevState.RUNNING)
            else:
                self._statistics_reliable = True
                self.set_state(DevState.ON)

            self._statistics: None | _Statistics = None
            self._runner_state = await self._read_state()

    async def _read_state(self) -> str:
        return (await self._p11_runner.read_attribute("state_enum")).value

    async def _stop_run(self) -> None:
        if self._statistics is None:
            self._logger.info(
                "want to stop run, but have no statistics - shouldn't happen"
            )
            return

        self._statistics.run_stopped = datetime.datetime.now(datetime.timezone.utc)
        try:
            await self._send_to_amarcord(self._statistics)
        finally:
            self._statistics = None

    async def _start_run(self) -> None:
        bound_logger = self._logger.bind(command="start run")
        if self._statistics is not None and self._statistics.run_stopped is None:
            bound_logger.warning(
                "transition to RUNNING, but the current run doesn't have an end; treating as "
                + "superfluous message"
            )
            return
        try:
            run_id = (await self._p11_runner.read_attribute("run_id")).value
            bound_logger.info(f"{run_id=}")
            selected_beamtime_id = (
                await self._tape_drive_runner.read_attribute("selected_beamtime_id")
            ).value
            if selected_beamtime_id <= 0:
                bound_logger.error(
                    "cannot send statistics to AMARCORD, no beam time is selected!"
                )
                return
            external_beamtime_id: None | str = None
            async with self._session.get(f"{self.amarcord_url}/beamtimes") as resp:
                beamtimes_list_response = await resp.json()
                for beamtime in beamtimes_list_response["beamtimes"]:
                    if beamtime["id"] == selected_beamtime_id:
                        external_beamtime_id = beamtime["external_id"]
                        break

            if (
                external_beamtime_id is None
                and "%beamtime-external-id%" in self.raw_file_path_template
            ):
                self.logger.error(
                    f'couldn\'t resolve the internal beamtime ID {selected_beamtime_id} to an external ID, and we have %beamtime-external-id% inside the template "{self.raw_file_path_template}"'
                )
                return

            bound_logger.info(f"{selected_beamtime_id=}")
            raw_file_path = (
                self.raw_file_path_template.replace(
                    "%year%", str(datetime.date.today().year)
                )
                .replace("%beamtime-internal-id%", str(selected_beamtime_id))
                .replace(
                    "%beamtime-external-id%",
                    external_beamtime_id if external_beamtime_id is not None else "",
                )
                .replace("%run-id%", str(run_id))
            )
            bound_logger.info(f"{raw_file_path=}")
            laser_distance = await self._read_detector_distance_laser()
            bound_logger.info(f"{laser_distance=}")
            distance_set_point = (
                await self._p11_runner.read_attribute(
                    ATTRIBUTE_RUNNER_DETECTOR_DISTANCE
                )
            ).value
            bound_logger.info(f"{distance_set_point=}")
            energy = await self._read_energy()
            transmission_percent = await self._read_transmission_percent()
            bound_logger.info(f"{energy=}")
            tape_velocity = await self._read_tape_velocity()
            bound_logger.info(f"{tape_velocity=}")
            use_stream = (
                await self._p11_runner.read_attribute(ATTRIBUTE_USE_STREAM)
            ).value
            bound_logger.info(f"{use_stream=}")
            number_of_images = (
                await self._p11_runner.read_attribute(ATTRIBUTE_NUMBER_OF_IMAGES)
            ).value
            bound_logger.info(f"{number_of_images=}")
            use_chopper = (
                await self._p11_runner.read_attribute(ATTRIBUTE_USE_CHOPPER)
            ).value
            bound_logger.info(f"{use_chopper=}")
            exposure_time = (
                await self._p11_runner.read_attribute(ATTRIBUTE_EXPOSURE_TIME)
            ).value
            bound_logger.info(f"{exposure_time=}")
            chemical_stats = await self._read_all_chemical_stats()
            bound_logger.info(f"{chemical_stats=}")
            async with self._session.get(
                f"{self.amarcord_url}/attributi/{selected_beamtime_id}"
            ) as resp:
                beamtime_attributi_response = await resp.json()
            self._statistics = _Statistics(
                beamtime_id=selected_beamtime_id,
                attributo_name_to_id={
                    a["name"]: a["id"] for a in beamtime_attributi_response["attributi"]
                },
                run_id=run_id,
                run_start=datetime.datetime.now(datetime.timezone.utc),
                run_stopped=None,
                detector_distances_mm=[laser_distance],
                detector_distance_set_point_mm=distance_set_point,
                energies_kev=[energy],
                transmission_percent=transmission_percent,
                tape_velocities_mm_per_s=[tape_velocity],
                eiger_interface="stream" if use_stream else "file writer",
                target_frame_count=number_of_images,
                chopper_enabled=use_chopper,
                chemical_statistics=chemical_stats,
                raw_file_path=raw_file_path,
                exposure_time_ms=exposure_time,
            )
            bound_logger.info(f"Run {run_id} started")
            await self._send_to_amarcord(self._statistics)
        except:
            bound_logger.exception()
            raise

    @command
    async def update(self) -> None:
        old_runner_state = self._runner_state
        new_runner_state = await self._read_state()

        if old_runner_state != new_runner_state:
            if new_runner_state == "measuring":
                await self._start_run()
            elif new_runner_state != "measuring":
                await self._stop_run()
        elif old_runner_state == "measuring":
            if self._statistics is None:
                self._logger.info(
                    "we're in moving, but have no statistics - shouldn't happen"
                )
                return

            self._statistics.energies_kev.append(await self._read_energy())
            self._statistics.detector_distances_mm.append(
                await self._read_detector_distance_laser()
            )
            self._statistics.tape_velocities_mm_per_s.append(
                await self._read_tape_velocity()
            )

            new_chemical_stats = await self._read_all_chemical_stats()
            for existing_stat, new_stat in zip(
                self._statistics.chemical_statistics, new_chemical_stats, strict=False
            ):
                if existing_stat is None or new_stat is None:
                    continue
                existing_stat.pressures_mbar.extend(new_stat.pressures_mbar)
                existing_stat.flows_ul_min.extend(new_stat.flows_ul_min)

        self._runner_state = new_runner_state

    async def _read_chemical_channel_stats(
        self, channel_id: int
    ) -> None | _ChemicalStatistics:
        enabled = (
            await self._tape_drive_runner.read_attribute(
                f"channel_{channel_id}_{CHANNEL_ATTRIBUTE_ENABLED}"
            )
        ).value
        if not enabled:
            return None
        return _ChemicalStatistics(
            chemical_id=(
                await self._tape_drive_runner.read_attribute(
                    f"channel_{channel_id}_{CHANNEL_ATTRIBUTE_CHEMICAL}"
                )
            ).value,
            pressure_set_point=(
                await self._tape_drive_runner.read_attribute(
                    f"channel_{channel_id}_{CHANNEL_ATTRIBUTE_PRESSURE_SET_POINT}"
                )
            ).value,
            flow_set_point=(
                await self._tape_drive_runner.read_attribute(
                    f"channel_{channel_id}_{CHANNEL_ATTRIBUTE_FLOW_SET_POINT}"
                )
            ).value,
            pressures_mbar=[
                (
                    await self._tape_drive_runner.read_attribute(
                        f"channel_{channel_id}_{CHANNEL_ATTRIBUTE_PRESSURE}"
                    )
                ).value
            ],
            flows_ul_min=[
                (
                    await self._tape_drive_runner.read_attribute(
                        f"channel_{channel_id}_{CHANNEL_ATTRIBUTE_FLOW}"
                    )
                ).value
            ],
        )

    async def _read_all_chemical_stats(self) -> list[None | _ChemicalStatistics]:
        return [
            await self._read_chemical_channel_stats(channel_id)
            for channel_id in range(1, NUMBER_OF_CHANNELS + 1)
        ]

    async def _read_detector_distance_laser(self) -> float:
        return (
            await self._p11_runner.read_attribute(ATTRIBUTE_DETECTOR_DISTANCE_LASER)
        ).value

    async def _read_tape_velocity(self) -> float:
        return (
            await self._main_tape.read_attribute(ATTRIBUTE_TAPE_VELOCITY_AVERAGED)
        ).value

    async def _read_energy(self) -> float:
        return (await self._p11_runner.read_attribute(ATTRIBUTE_RUNNER_ENERGY)).value

    async def _read_transmission_percent(self) -> float:
        return (
            await self._p11_runner.read_attribute(ATTRIBUTE_RUNNER_TRANSMISSION)
        ).value

    async def delete_device(self) -> None:  # type: ignore
        self._logger.info("Deleting device, closing HTTP session")
        await self._session.close()

    def _get_schema(self) -> list[dict[str, str | dict[str, str | bool | float]]]:
        def channel_attributes_schema(
            i: int,
        ) -> list[dict[str, str | dict[str, str | bool | float]]]:
            return [
                {
                    "attributo_name": f"channel_{i}_chemical_id",
                    "attributo_type": {"type": "integer", "format": "chemical-id"},
                },
                {
                    "attributo_name": f"channel_{i}_pressure_avg",
                    "attributo_type": {
                        "type": "number",
                        "format": "standard-unit",
                        "suffix": "mbar",
                    },
                    "description": "average fluid pressure value over the course of the whole run",
                },
                {
                    "attributo_name": f"channel_{i}_pressure_stddev",
                    "attributo_type": {
                        "type": "number",
                        "format": "standard-unit",
                        "suffix": "mbar",
                    },
                    "description": "fluid pressure standard deviation over the course of the whole run",
                },
                {
                    "attributo_name": f"channel_{i}_pressure_set_point",
                    "attributo_type": {
                        "type": "number",
                        "format": "standard-unit",
                        "suffix": "mbar",
                        "tolerance": 0.01,
                        "toleranceIsAbsolute": False,
                    },
                    "description": "fluid pressure set point",
                },
                {
                    "attributo_name": f"channel_{i}_flow_avg",
                    "attributo_type": {
                        "type": "number",
                        "format": "standard-unit",
                        "suffix": "ul/min",
                    },
                    "description": "average flow value over the course of the whole run",
                },
                {
                    "attributo_name": f"channel_{i}_flow_stddev",
                    "attributo_type": {
                        "type": "number",
                        "format": "standard-unit",
                        "suffix": "ul/min",
                    },
                    "description": "fluid flow standard deviation over the course of the whole run",
                },
                {
                    "attributo_name": f"channel_{i}_flow_set_point",
                    "attributo_type": {
                        "type": "number",
                        "format": "standard-unit",
                        "suffix": "ul/min",
                        "tolerance": 0.01,
                        "toleranceIsAbsolute": False,
                    },
                    "description": "fluid flow set point",
                },
            ]

        attributi_schema: list[dict[str, str | dict[str, str | bool | float]]] = [
            {
                "attributo_name": "delay time",
                "attributo_type": {
                    "type": "number",
                    "format": "standard-unit",
                    "suffix": "s",
                    "tolerance": 0.05,
                    "toleranceIsAbsolute": False,
                },
                "description": "the delay time between nozzle and beam",
            },
            {
                "attributo_name": "run_stopped_manually",
                "attributo_type": {"type": "boolean"},
                "description": "was the run stopped manually by the user?",
            },
            {"attributo_name": "eiger_interface", "attributo_type": {"type": "string"}},
            {
                "attributo_name": "target_frame_count",
                "attributo_type": {"type": "integer"},
                "description": "frame count the user entered as the target (might be different in reality due to cancelled runs)",
            },
            {
                "attributo_name": "chopper_enabled",
                "attributo_type": {"type": "boolean"},
            },
            {
                "attributo_name": "tape_velocity_avg",
                "attributo_type": {
                    "type": "number",
                    "format": "standard-unit",
                    "suffix": "mm/s",
                    "tolerance": 0.05,
                    "toleranceIsAbsolute": False,
                },
                "description": "average velocity value over the course of the whole run",
            },
            {
                "attributo_name": "exposure_time",
                "attributo_type": {
                    "type": "number",
                    "format": "standard-unit",
                    "suffix": "ms",
                },
            },
            {
                "attributo_name": "transmission",
                "attributo_type": {
                    "type": "number",
                    "suffix": "%",
                    "tolerance": 0.05,
                    "toleranceIsAbsolute": False,
                },
            },
            {
                "attributo_name": "detector_distance_laser_avg",
                "attributo_type": {
                    "type": "number",
                    "format": "standard-unit",
                    "suffix": "mm",
                },
                "description": "average laser distance value over the course of the whole run",
            },
            {
                "attributo_name": "detector_distance",
                "attributo_type": {
                    "type": "number",
                    "format": "standard-unit",
                    "suffix": "mm",
                },
                "description": "detector distance set point (might differ a bit when actually measured, see `detector_distance_laser_avg`)",
            },
            {
                "attributo_name": "x_ray_energy_avg",
                "attributo_type": {
                    "type": "number",
                    "format": "standard-unit",
                    "suffix": "eV",
                },
                "description": "average X-ray energy value over the course of the whole run",
            },
        ]

        for channel_id in range(1, NUMBER_OF_CHANNELS + 1):
            attributi_schema.extend(channel_attributes_schema(channel_id))

        return attributi_schema

    @command(
        dtype_in=int,
        doc_in="Internal ID of the beamtime in AMARCORD",
        dtype_out=bool,
        doc_out="true if it worked, false otherwise",
    )
    async def send_schema(self, beamtime_id: int) -> bool:
        bound_logger = self._logger.bind(command="send_schema", beamtime_id=beamtime_id)
        try:
            bound_logger.info(f"sending schema to AMARCORD: {self._get_schema()}")
            async with self._session.post(
                f"{self.amarcord_url}/attributi/schema",
                json={
                    "attributi_schema": self._get_schema(),
                    "beamtime_id": beamtime_id,
                },
            ) as resp:
                bound_logger.info("successful request to AMARCORD")
                result = await resp.json()
                bound_logger.info(f"request result: {result}")
                return True
        except:
            bound_logger.exception("error sending data to AMARCORD")
            return False

    async def _send_to_amarcord(self, stats: _Statistics) -> None:
        bound_logger = self._logger.bind(run_id=stats.run_id)

        def channel_attributes(i: int) -> list[dict[str, Any]]:
            cstats = stats.chemical_statistics[i - 1]
            if cstats is None:
                return []
            result = [
                {
                    "attributo_id": stats.attributo_name_to_id[
                        f"channel_{i}_pressure_avg"
                    ],
                    "attributo_value_float": float(np.mean(cstats.pressures_mbar)),
                },
                {
                    "attributo_id": stats.attributo_name_to_id[
                        f"channel_{i}_pressure_stddev"
                    ],
                    "attributo_value_float": float(np.std(cstats.pressures_mbar)),
                },
                {
                    "attributo_id": stats.attributo_name_to_id[
                        f"channel_{i}_pressure_set_point"
                    ],
                    "attributo_value_float": cstats.pressure_set_point,
                },
                {
                    "attributo_id": stats.attributo_name_to_id[f"channel_{i}_flow_avg"],
                    "attributo_value_float": float(np.mean(cstats.flows_ul_min)),
                },
                {
                    "attributo_id": stats.attributo_name_to_id[
                        f"channel_{i}_flow_stddev"
                    ],
                    "attributo_value_float": float(np.std(cstats.flows_ul_min)),
                },
                {
                    "attributo_id": stats.attributo_name_to_id[
                        f"channel_{i}_flow_set_point"
                    ],
                    "attributo_value_float": cstats.flow_set_point,
                },
            ]
            if cstats.chemical_id != 0:
                result.append(
                    {
                        "attributo_id": stats.attributo_name_to_id[
                            f"channel_{i}_chemical_id"
                        ],
                        "attributo_value_chemical": cstats.chemical_id,
                    }
                )
            return result

        def datetime_to_attributo_int(d: datetime.datetime) -> int:
            return int(d.replace(tzinfo=datetime.timezone.utc).timestamp() * 1000)

        attributi_values = [
            {
                "attributo_id": stats.attributo_name_to_id["run_stopped_manually"],
                "attributo_value_bool": (
                    await self._p11_runner.read_attribute("run_stopped_manually")
                ).value,
            },
            {
                "attributo_id": stats.attributo_name_to_id["eiger_interface"],
                "attributo_value_str": stats.eiger_interface,
            },
            {
                "attributo_id": stats.attributo_name_to_id["target_frame_count"],
                "attributo_value_int": stats.target_frame_count,
            },
            {
                "attributo_id": stats.attributo_name_to_id["chopper_enabled"],
                "attributo_value_bool": stats.chopper_enabled,
            },
            {
                "attributo_id": stats.attributo_name_to_id["exposure_time"],
                "attributo_value_float": stats.exposure_time_ms,
            },
            {
                "attributo_id": stats.attributo_name_to_id[
                    "detector_distance_laser_avg"
                ],
                "attributo_value_float": np.mean(stats.detector_distances_mm),
            },
            {
                "attributo_id": stats.attributo_name_to_id["detector_distance"],
                "attributo_value_float": stats.detector_distance_set_point_mm,
            },
            {
                "attributo_id": stats.attributo_name_to_id["x_ray_energy_avg"],
                "attributo_value_float": np.mean(stats.energies_kev),
            },
            {
                "attributo_id": stats.attributo_name_to_id["transmission"],
                "attributo_value_float": stats.transmission_percent,
            },
            {
                "attributo_id": stats.attributo_name_to_id["tape_velocity_avg"],
                "attributo_value_float": np.mean(stats.tape_velocities_mm_per_s),
            },
        ]
        delay_time_attr = await self._tape_drive_runner.read_attribute("delay_time")
        delay_time = delay_time_attr.value
        if delay_time is not None:
            attributi_values.append(
                {
                    "attributo_id": stats.attributo_name_to_id["delay time"],
                    "attributo_value_float": delay_time,
                }
            )
        for channel_id in range(1, NUMBER_OF_CHANNELS + 1):
            attributi_values.extend(channel_attributes(channel_id))
        try:
            bound_logger.info(
                f"sending statistics to AMARCORD (beam time {stats.beamtime_id})"
            )
            async with self._session.post(
                f"{self.amarcord_url}/runs/{stats.run_id}",
                json={
                    "attributi": attributi_values,
                    "files": [{"id": 0, "glob": stats.raw_file_path, "source": "raw"}],
                    "beamtime_id": stats.beamtime_id,
                    "started": (
                        datetime_to_attributo_int(stats.run_start)
                        if stats.run_start is not None
                        else None
                    ),
                    "stopped": (
                        datetime_to_attributo_int(stats.run_stopped)
                        if stats.run_stopped is not None
                        else None
                    ),
                },
            ) as resp:
                bound_logger.info("successful request to AMARCORD, decoding JSON")
                result = await resp.json()
                bound_logger.info(f"request result: {result}")
        except:
            bound_logger.exception("error sending data to AMARCORD")


class StaticTangoAttribute(BaseModel):
    device_url: str
    attribute_name: str


class StaticConfigFile(BaseModel):
    measuring_attribute: StaticTangoAttribute
    measuring_attribute_if_measuring: str
    beamtime_id_attribute: StaticTangoAttribute
    run_id_attribute: StaticTangoAttribute
    amarcord_url: str
    raw_file_path_template: str
    attributi: list[StaticAttributoDescription]


class Mode(Enum):
    SEND_SCHEMA = "send-schema"
    OBSERVER = "observe"


async def send_schema(config: ConfigFile) -> None:
    pass


def main() -> None:
    try:
        config_file = Path(sys.argv[1])
        mode = Mode(sys.argv[0])

        match mode:
            case Mode.SEND_SCHEMA:
                asyncio.run(send_schema(config_file))
            case Mode.OBSERVER:
                asyncio.run(observe(config_file))
    except:
        logger.error(
            f'Invalid arguments! I\'m expecting a config file, and then either "{Mode.SEND_SCHEMA.value}" or "{Mode.OBSERVER.value}"'
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
