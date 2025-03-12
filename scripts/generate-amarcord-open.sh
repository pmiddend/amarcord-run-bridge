#!/usr/bin/env bash

# shellcheck disable=SC3040
set -euo pipefail

openapi-generator-cli generate --generator-name python --input-spec openapi.json --config=openapi-generator-config.yaml --package-name amarcord_open --output amarcord-open

rm -r amarcord-open/docs
