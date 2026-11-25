#!/bin/sh
set -eu

usage() { printf '%s\n' 'Usage: sh install.sh [--check]'; }
check=false
if [ "$#" -ne 0 ]; then
    if [ "$#" -ne 1 ]; then usage >&2; exit 2; fi
    case $1 in
        --check) check=true ;;
        -h|--help) usage; exit 0 ;;
        *) usage >&2; exit 2 ;;
    esac
fi

root=$(CDPATH= cd -P "$(dirname "$0")" && pwd -P)
exec python3 -IB "$root/scripts/setup_minimal.py" "$root" "$check"
