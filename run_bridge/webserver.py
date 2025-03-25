import asyncio
import json
import sys
from pathlib import Path

import structlog
from aiohttp import web
from aiohttp.web import Request
from aiohttp.web import Response

from run_bridge import amarcord_connector
from run_bridge.bootstrap import BOOTSTRAP_SOURCE
from run_bridge.main_loop import Config
from run_bridge.main_loop import async_main

logger = structlog.stdlib.get_logger(__name__)

_AMARCORD_CURRENT_LOOP_KEY = "AMARCORD_CURRENT_LOOP"
_AMARCORD_CURRENT_CONFIG_FILE = "AMARCORD_CURRENT_CONFIG_FILE"


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
<body>
    {content}
</body>
</html>    """


def generate_config_header_form(request: Request) -> str:
    if len(sys.argv) == 1:
        return (
            "<h1>Please specify a directory as the first argument to the program</h1>"
        )

    config_dir = Path(sys.argv[1])

    try:
        configs = list(config_dir.iterdir())

        if not configs:
            return (
                f"<h1>Directory “{config_dir}” doesn’t have any config files in it</h1>"
            )

        options = "\n".join(
            f'<option value="{filename}">{filename}</option>' for filename in configs
        )
        return f"""
            <div class="container">
            <h1 class="mt-3">Select a configuration</h1>
<form>
            <div class="hstack gap-3">
  <select name="configfile" class="form-select">
    {options}
  </select>
  <button type="submit" class="btn btn-primary">Switch</button>
            </div>
</form>
            </div>
        """
    except:
        return f"<h1>Error reading from directory “{config_dir}”, does it really exist?</h1>"


async def handler_index(request: Request) -> Response:
    config_file_str = request.rel_url.query.getone("configfile", None)
    if config_file_str is None:
        return Response(
            content_type="text/html",
            text=with_skeleton(generate_config_header_form(request)),
        )

    config_file = Path(config_file_str)

    try:
        with config_file.open("r", encoding="utf-8") as f:  # noqa: ASYNC230
            config = Config(**json.load(f))
    except:
        return Response(
            content_type="text/html",
            text=with_skeleton(
                generate_config_header_form(request)
                + f"<h3>Error parsing config file “{config_file}”</h3>"
            ),
        )

    current_loop = request.app[_AMARCORD_CURRENT_LOOP_KEY]
    current_config_file = request.app[_AMARCORD_CURRENT_CONFIG_FILE]

    started_badge = ""
    if current_config_file != config_file:
        if current_loop is not None:
            logger.info("cancelling previous loop")
            current_loop.cancel()
            current_loop = None
        current_loop = asyncio.create_task(async_main(config))
        started_badge = '<div class="container"><span class="badge text-bg-success">Main loop started!</span></div>'
        request.app[_AMARCORD_CURRENT_LOOP_KEY] = current_loop
        request.app[_AMARCORD_CURRENT_CONFIG_FILE] = config_file
    else:
        logger.info(f"main loop still running for file {config_file}")

    async with await amarcord_connector.AmarcordConnector.init(
        config.amarcord_connector_config
    ) as server_instance:
        try:
            beamtimes = await server_instance.retrieve_beamtimes()
        except Exception as e:
            return Response(
                content_type="text/html",
                text=with_skeleton(
                    generate_config_header_form(request)
                    + f"<h3>Error getting beam time information: {e}</h3>"
                ),
            )

        options = "\n".join(
            f'<option value="{beamtime.id}">{beamtime.title}</option>'
            for beamtime in beamtimes
        )
        attributi_list = (
            "<li>"
            + "</li><li>".join(
                a.attributo_name for a in config.amarcord_connector_config.attributi
            )
            + "</li>"
        )
        send_to_beamtime = request.rel_url.query.getone("sendtobeamtime", None)
        if send_to_beamtime is not None:
            beamtime_id = int(send_to_beamtime)

            try:
                await server_instance.send_schema(beamtime_id)
                footer = '<span class="badge text-bg-success">Attributi added!</span>'
            except Exception as e:
                footer = f"<h3>Error sending schema: {e}"
        else:
            footer = ""
        form = f"""
        {started_badge}
        <form>
            <input type="hidden" name="configfile" value="{config_file}" />
            <div class="container">
            <h4 class="mt-3">Add attributi to beamtime</h4>
<form>
            <div class="hstack gap-3 mb-3">
  <select name="sendtobeamtime" class="form-select">
    {options}
  </select>
  <button type="submit" class="btn btn-primary text-nowrap">Send attributi</button>
            </div>
        {footer}
        <p>The following Attributi will be added:</p>
        <ul>
        {attributi_list}
        </ul>
</form>
            </div>
        </form>
        """
        return Response(
            content_type="text/html",
            text=with_skeleton(generate_config_header_form(request) + form),
        )


def start_webserver(host: str, port: int) -> None:
    app = web.Application()
    app[_AMARCORD_CURRENT_LOOP_KEY] = None
    app[_AMARCORD_CURRENT_CONFIG_FILE] = None
    app.add_routes([web.get("/", handler_index)])

    # runner = web.AppRunner(app)
    # await runner.setup()

    # site = web.TCPSite(runner, host, port)
    # logger.info(f"starting web server on {host}:{port}")
    # await site.start()
    # logger.info(f"serving on {host}:{port}")

    web.run_app(app, host=host, port=port)
