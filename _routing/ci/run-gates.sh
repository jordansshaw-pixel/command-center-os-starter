#!/bin/sh
set -u

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ATX_ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/../.." && pwd)

cd "$ATX_ROOT"

. "$SCRIPT_DIR/find-python.sh"

ATX_PYTHON=$(find_atx_python) || exit $?

exec "$ATX_PYTHON" _routing/run_gates.py
