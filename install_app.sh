#!/bin/bash

# Exit with non-zero status if a simple command fails, even with piping
# https://stackoverflow.com/a/4346420/1664216

set -e
set -o pipefail

# Script to run on the deployed server when the code has been
# updated (or on first deployment)

echo Installing Important stuff

echo Installing more important stuff

echo Installing the most important stuff

echo Building some stuff

echo Done!

