#!/bin/bash

# Exit with non-zero status if a simple command fails, even with piping
# https://stackoverflow.com/a/4346420/1664216

set -e
set -o pipefail

# Script to run on the deployed server when the code has been
# updated (or on first deployment)

python_version=`cat .python-version`

echo Installing pipenv
pip install pipenv

echo Adding user bin to bath (for pip installed commands to work)
PATH=$PATH:/home/ubuntu/.local/bin

echo Setting Python version for pipenv
pipenv --python $python_version

echo Installing requirements
pipenv install

echo collecting static files
pipenv run python manage.py collectstatic

echo Done!
