#!/bin/bash
virtFold="venv"

source $virtFold/bin/activate
PATH="$PATH:$(pwd)"
python3 helloWorld.py 
deactivate
