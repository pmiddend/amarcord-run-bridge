from pathlib import Path

from tap import Tap

from run_bridge.logging_util import setup_structlog
from run_bridge.webserver import start_webserver

setup_structlog()


class Arguments(Tap):
    host: str = "localhost"  # Host where to offer the web interface (you might choose localhost to constrain who has access)
    port: int  # Port where to offer the web interface (no default to force people to think about it)
    config_save_file: Path  # Where to save which configuration was active previously (doesn't have to exist)
    config_files_dir: Path  # Where are the config files stored?


def main() -> None:  # pragma: no cover
    args = Arguments().parse_args()

    start_webserver(args.host, args.port, args.config_save_file, args.config_files_dir)


if __name__ == "__main__":  # pragma: no cover
    main()
