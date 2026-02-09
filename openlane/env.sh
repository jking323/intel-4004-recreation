#!/bin/bash
# SKY130 Caravel Environment — source this from the openlane/ directory
# Usage: cd ~/intel-4004-recreation/openlane && source env.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

export OPENLANE_ROOT="${SCRIPT_DIR}/dependencies/openlane_src"
export PDK_ROOT="${SCRIPT_DIR}/dependencies/pdks"
export PDK=sky130A
export CARAVEL_ROOT="${SCRIPT_DIR}/caravel"

echo "Environment set:"
echo "  OPENLANE_ROOT = $OPENLANE_ROOT"
echo "  PDK_ROOT      = $PDK_ROOT"
echo "  PDK           = $PDK"
echo "  CARAVEL_ROOT  = $CARAVEL_ROOT"
