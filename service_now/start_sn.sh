#!/bin/bash
virtFold="venv"
script=$1

source ../$virtFold/bin/activate
python3 "$script"
deactivate
