import asyncio
import json
import socket
from dataclasses import dataclass
from functools import partial
from pathlib import Path

import structlog
from aiohttp import web
from aiohttp.web import Request
from aiohttp.web import Response
from amarcord_open import JsonBeamtime

from run_bridge import amarcord_connector
from run_bridge.bootstrap import BOOTSTRAP_SOURCE
from run_bridge.main_loop import Config
from run_bridge.main_loop import LogBackend
from run_bridge.main_loop import async_main

logger = structlog.stdlib.get_logger(__name__)

_AMARCORD_CURRENT_LOOP_TASK = "AMARCORD_CURRENT_LOOP_TASK"
_AMARCORD_CURRENT_CONFIG = "AMARCORD_CURRENT_CONFIG_FILE"
_AMARCORD_LOOP_MESSAGES = "AMARCORD_LOOP_MESSAGES"


def with_skeleton(content: str) -> str:
    return f"""
<!DOCTYPE html>
<html lang="en">
<meta charset="UTF-8">
<title>AMARCORD run bridge configuration</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
    {BOOTSTRAP_SOURCE}
</style>
<body class="mt-3">
    {content}
</body>
</html>    """


def html_response(s: str) -> Response:
    return Response(content_type="text/html", text=s)


def html_surround(s: str) -> Response:
    return html_response(with_skeleton(s))


@dataclass(frozen=True)
class ErrorMessage:
    message: str


@dataclass(frozen=True)
class ConfigWithPath:
    config: Config
    path: Path


@dataclass(frozen=True)
class SelectedData:
    selected_config: ConfigWithPath
    main_loop_started_badge: None | str
    beamtimes: ErrorMessage | list[JsonBeamtime]
    attributi_added_badge: None | ErrorMessage | str


def main_page_html(
    messages: LogBackend,
    config_files_dir: Path,
    config_file_paths: ErrorMessage | list[Path],
    selected_data: None | ErrorMessage | SelectedData,
) -> Response:
    content = ""

    if messages:
        content += '<div class="container">'
        content += "<h4>Status messages</h4>"
        content += (
            "<ul><li>"
            + "</li><li>".join(
                f"{m.time} [{m.level}] {m.message}" for m in messages.messages
            )
            + "</li></ul>"
        )
        content += "</div>"

    if isinstance(config_file_paths, ErrorMessage):
        content += f'<div class="container"><div class="alert alert-danger">{config_file_paths.message}</div></div>'
        return html_surround(content)

    try:
        hostname = socket.gethostname()
    except:
        hostname = "localhost"

    if selected_data is None or isinstance(selected_data, ErrorMessage):
        if isinstance(selected_data, ErrorMessage):
            content += f'<div class="container"><div class="alert alert-danger">{selected_data.message}</div></div>'
        options = "\n".join(
            f'<option value="{filename}">{filename.name}</option>'
            for filename in config_file_paths
        )
        content += f"""
          <div class="container">
            <h1 class="mt-3">Select a configuration</h1>
            <form>
              <div class="hstack gap-3">
                <select name="configfile" class="form-select">{options}</select>
                <button type="submit" class="btn btn-primary">Switch</button>
              </div>
              <div class="form-text">
                Configuration file dir: <code>{hostname}:{config_files_dir}</code>
              </div>
            </form>
          </div>
        """
        return html_surround(content)

    options = "\n".join(
        f'<option value="{filename}" {"selected" if filename == selected_data.selected_config.path else ""}>{filename.name}</option>'
        for filename in config_file_paths
    )
    content += f"""
      <div class="container">
        <h1 class="mt-3">Select a configuration</h1>
        <form>
          <div class="hstack gap-3">
            <select name="configfile" class="form-select">{options}</select>
            <button type="submit" class="btn btn-primary">Switch</button>
          </div>
          <div class="form-text">
            Configuration file dir: <code>{hostname}:{config_files_dir}</code>
          </div>
        </form>
      </div>
    """

    if selected_data.main_loop_started_badge is not None:
        content += f'<div class="container"><span class="badge text-bg-success">{selected_data.main_loop_started_badge}</span></div>'

    match selected_data.beamtimes:
        case ErrorMessage(message):
            content += f'<div class="container mt-3"><div class="alert alert-danger">{message}</div></div>'
        case beamtime_list:
            assert isinstance(beamtime_list, list)

            bt_options = "\n".join(
                f'<option value="{beamtime.id}">{beamtime.title}</option>'
                for beamtime in beamtime_list
            )

            attributi_list = (
                "<li>"
                + "</li><li>".join(
                    a.attributo_name
                    for a in selected_data.selected_config.config.amarcord_connector_config.attributi
                )
                + "</li>"
            )

            if selected_data.attributi_added_badge is not None:
                content += f'<div class="container"><span class="badge text-bg-success">{selected_data.attributi_added_badge}</span></div>'

            form = f"""
              <form>
                <input type="hidden" name="configfile" value="{selected_data.selected_config.path}" />
                <div class="container">
                <h4 class="mt-3">Add attributi to beamtime</h4>
                <div class="hstack gap-3 mb-3">
                  <select name="sendtobeamtime" class="form-select">{bt_options}</select>
                  <button type="submit" class="btn btn-primary text-nowrap">Send attributi</button>
                </div>
                <p>The following Attributi will be added:</p>
                <ul>{attributi_list}</ul>
              </form>
            """

            content += form

    return html_surround(content)


def write_current_config(config_save_file: Path, p: Path) -> None:
    logger.info(f"setting {p} as current config in file {config_save_file}")
    with config_save_file.open("w", encoding="utf-8") as f:
        f.write(str(p))


async def handler_index(
    config_save_file: Path, config_files_dir: Path, request: Request
) -> Response:
    current_loop: None | asyncio.Task[None] = request.app[_AMARCORD_CURRENT_LOOP_TASK]
    assert current_loop is None or isinstance(current_loop, asyncio.Task)

    current_config: None | ConfigWithPath = request.app[_AMARCORD_CURRENT_CONFIG]
    assert current_config is None or isinstance(current_config, ConfigWithPath)

    config_file_query_string = request.rel_url.query.getone("configfile", None)
    config_file_query_path = (
        Path(config_file_query_string) if config_file_query_string is not None else None
    )

    try:
        config_file_paths = list(config_files_dir.iterdir())
    except Exception as e:
        return main_page_html(
            messages=request.app[_AMARCORD_LOOP_MESSAGES],
            config_files_dir=config_files_dir,
            config_file_paths=ErrorMessage(str(e)),
            selected_data=None,
        )

    if config_file_query_path is not None:
        try:
            with config_file_query_path.open("r", encoding="utf-8") as f:
                config_file_query = Config(**json.load(f))

            if current_config is None or config_file_query != current_config.config:
                if current_loop is not None:
                    logger.info("cancelling previous loop")
                    current_loop.cancel()
                logger.info(f"starting loop for file {config_file_query_path}")
                current_loop = asyncio.create_task(
                    async_main(request.app[_AMARCORD_LOOP_MESSAGES], config_file_query)
                )
                main_loop_started_badge = "Configuration updated!"
                current_config = ConfigWithPath(
                    config_file_query, config_file_query_path
                )
                request.app[_AMARCORD_CURRENT_LOOP_TASK] = current_loop
                request.app[_AMARCORD_CURRENT_CONFIG] = current_config
                write_current_config(config_save_file, current_config.path)
            else:
                main_loop_started_badge = None
        except Exception as e:
            return main_page_html(
                messages=request.app[_AMARCORD_LOOP_MESSAGES],
                config_files_dir=config_files_dir,
                config_file_paths=config_file_paths,
                selected_data=ErrorMessage(
                    f"error changing to file '{config_file_query_string}': {e}"
                ),
            )
    else:
        main_loop_started_badge = None

    if current_config is None:
        return main_page_html(
            messages=request.app[_AMARCORD_LOOP_MESSAGES],
            config_files_dir=config_files_dir,
            config_file_paths=config_file_paths,
            selected_data=None,
        )

    async with await amarcord_connector.AmarcordConnector.init(
        current_config.config.amarcord_connector_config
    ) as server_instance:
        try:
            beamtimes = await server_instance.retrieve_beamtimes()
        except Exception as e:
            beamtimes = ErrorMessage(
                f"error getting beam time information from URL {current_config.config.amarcord_connector_config.amarcord_url}: {e}"
            )

        send_to_beamtime = request.rel_url.query.getone("sendtobeamtime", None)
        if send_to_beamtime is not None:
            beamtime_id = int(send_to_beamtime)

            try:
                await server_instance.send_schema(beamtime_id)
                attributi_added_badge = "Attributi added!"
            except Exception as e:
                attributi_added_badge = ErrorMessage(f"error adding attributi: {e}")
        else:
            attributi_added_badge = None
        return main_page_html(
            messages=request.app[_AMARCORD_LOOP_MESSAGES],
            config_files_dir=config_files_dir,
            config_file_paths=config_file_paths,
            selected_data=SelectedData(
                selected_config=current_config,
                main_loop_started_badge=main_loop_started_badge,
                beamtimes=beamtimes,
                attributi_added_badge=attributi_added_badge,
            ),
        )


def _retrieve_previous_config_file(
    config_save_file: Path,
) -> None | ConfigWithPath:
    try:
        with config_save_file.open("r", encoding="utf-8") as f:
            previous_config_file = Path(f.read().strip())

            with previous_config_file.open("r", encoding="utf-8") as g:
                return ConfigWithPath(Config(**json.load(g)), previous_config_file)
    except:
        return None


def start_webserver(
    host: str, port: int, config_save_file: Path, config_files_dir: Path
) -> None:
    app = web.Application()

    loop_messages = LogBackend()

    app[_AMARCORD_LOOP_MESSAGES] = loop_messages

    async def start_stored_loop(c: ConfigWithPath, app_: web.Application) -> None:
        logger.info(f"starting main loop with previous config file: {c.path}")
        current_loop = asyncio.create_task(async_main(loop_messages, c.config))
        # Storing shared mutable state in app is "the preferred" way to go
        # about it according to the aiohttp docs. Here we store it, and in
        # the handlers we access it.
        app_[_AMARCORD_CURRENT_LOOP_TASK] = current_loop
        app_[_AMARCORD_CURRENT_CONFIG] = c

    previous_path_and_config = _retrieve_previous_config_file(config_save_file)
    if previous_path_and_config is not None:
        # documented here:
        # https://docs.aiohttp.org/en/stable/web_advanced.html#application-runners
        app.on_startup.append(partial(start_stored_loop, previous_path_and_config))
    else:
        logger.info("don't have a config, not starting main loop")
        app[_AMARCORD_CURRENT_LOOP_TASK] = None
        app[_AMARCORD_CURRENT_CONFIG] = None

    app.add_routes(
        [
            web.get(
                "/",
                partial(handler_index, config_save_file, config_files_dir.absolute()),
            )
        ]
    )

    web.run_app(app, host=host, port=port)
