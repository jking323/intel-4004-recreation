#!/bin/bash
# Usage: ./scripts/snapshot-reports.sh risc4_alu

MACRO=$1
if [ -z "$MACRO" ]; then
    echo "Usage: $0 <macro_name>"
    exit 1
fi

REPO_ROOT=$(git rev-parse --show-toplevel)
RUN=$(ls -t $REPO_ROOT/openlane/openlane/$MACRO/runs/ | head -1)
RUNDIR=$REPO_ROOT/openlane/openlane/$MACRO/runs/$RUN
DEST=$REPO_ROOT/reports/$MACRO/$RUN

if [ ! -d "$RUNDIR" ]; then
    echo "No runs found for $MACRO"
    exit 1
fi

mkdir -p $DEST

cp $RUNDIR/54-openroad-stapostpnr/*.rpt $DEST/timing.rpt 2>/dev/null
cp $RUNDIR/70-checker-setupviolations/*.rpt $DEST/setup_violations.rpt 2>/dev/null
cp $RUNDIR/71-checker-holdviolations/*.rpt $DEST/hold_violations.rpt 2>/dev/null
cp $RUNDIR/62-magic-drc/*.rpt $DEST/drc.rpt 2>/dev/null
cp $RUNDIR/68-netgen-lvs/*.rpt $DEST/lvs.rpt 2>/dev/null
cp $RUNDIR/final/metrics.csv $DEST/metrics.csv 2>/dev/null
cp $RUNDIR/final/metrics.json $DEST/metrics.json 2>/dev/null

echo "Reports saved to reports/$MACRO/$RUN/"
ls -la $DEST/
