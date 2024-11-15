#!/bin/bash

set -euo pipefail
shopt -s globstar

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
