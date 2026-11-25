#!/bin/sh
set -eu

root=$(CDPATH= cd -P "$(dirname "$0")" && pwd -P)
exec python3 -IB "$root/scripts/setup_minimal.py" "$@"
