#!/bin/bash
virtFold="venv"

source ../$virtFold/bin/activate
python3 sn_scenario.py
deactivate
