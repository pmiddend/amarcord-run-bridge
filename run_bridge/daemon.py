from run_bridge.logging_util import setup_structlog
from run_bridge.webserver import start_webserver

setup_structlog()


def main() -> None:  # pragma: no cover
    start_webserver("0.0.0.0", 1337)


if __name__ == "__main__":  # pragma: no cover
    main()
