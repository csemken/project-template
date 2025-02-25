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

# create notebook if it does not exist
if [ ! -f "$FILE" ]; then
    echo $EMPTY_IPNB > $FILE
fi

# set jupytext format, create paired file
jupytext --set-formats ipynb,py "$FILE"
