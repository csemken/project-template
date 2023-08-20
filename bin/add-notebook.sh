#!/bin/bash

EMPTY_IPNB='{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}
'

set -euxo pipefail

# first argument = file name
FILE=$1

# activate Python venv
if [ ! -d ".venv" ]; then
    echo "Folder .venv/ not found"
    exit 1
fi
set +x && source .venv/bin/activate && set -x

# create notebook if it does not exist
if [ ! -f "$FILE" ]; then
    echo $EMPTY_IPNB > $FILE
fi

# set jupytext format, create paired file
jupytext --set-formats ipynb,py "$FILE"

# track file with dvc
dvc add "$FILE"
