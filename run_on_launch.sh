#!/bin/bash

# Exit with non-zero status if a simple command fails, even with piping
# https://stackoverflow.com/a/4346420/1664216

set -e
set -o pipefail

echo collecting static files
/usr/bin/python3 -m venv python manage.py collectstatic

echo Done!
