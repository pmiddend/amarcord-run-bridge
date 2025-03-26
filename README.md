# AMARCORD Run Bridge

## Rationale

This process will listen for [Tango](https://www.tango-controls.org/) device servers and start runs in AMARCORD.

## Installation

If you don't want to install [uv](https://docs.astral.sh/uv/) and stick to pip, you need to make sure to install the `amarcord-open` companion library before, and then the requirements themselves:

```bash
pip install amarcord_open
pip install -r requirements.txt
```

## Usage

The main daemon to run is located in `run_bridge/daemon.py` and it receives these command line parameters:

- `--host` is the host to listen on for the web server; for security purposes you might choose `localhost`. If you want the web server available from somewhere else, specify something like `0.0.0.0`
- `--port` is the port the web server listens on
- `--config_save_file` (note the underscores!) is a _file_ where the bridge stores the latest configuration file chosen for the bridge; choose something like `~/bridge-last-save-file.txt`
- `--config_files_dir` (note the underscores!) is the _directory_ where the bridge looks for JSON files as configuration
