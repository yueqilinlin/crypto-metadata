#!/bin/sh

[ ! -d ".venv" ] && virtualenv -p python3 .venv
source .venv/bin/activate
python index.py
