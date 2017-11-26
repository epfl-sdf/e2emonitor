#!/bin/bash
virtFold="venv"

source ../$virtFold/bin/activate
python3 isa_scenario.py
deactivate
