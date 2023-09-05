#!/bin/bash

set -euo pipefail
shopt -s globstar

if [ ! -d ".venv" ]; then
    echo "Warning: folder .venv/ not found, skipping update"
    exit 0
fi

if [ ! -f ".venv/bin/jupytext" ]; then
    echo "Warning: jupytext not found in .venv/, skipping update"
    exit 0
fi

# activate Python venv
source .venv/bin/activate

# add to dvc
dvc add -q ./**/*.ipynb

# sync
out=$(jupytext --to py --use-source-timestamp ./**/*.ipynb)
set +e
changed=$(echo "$out" | grep -P '^\[jupytext\] Updating')
set -e

if [ -n "$changed" ]; then
    echo "$changed"
    exit 1
fi
