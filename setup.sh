#!/usr/bin/env bash
set -e
python3 -m pip install --user virtualenv
python3 -m venv venv
./venv/bin/pip install --upgrade pip
./venv/bin/pip install -r requirements.txt
