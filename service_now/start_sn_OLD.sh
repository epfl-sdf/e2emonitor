#!/bin/bash
virtFold="venv"
script=$1

python -c 'import selenium; print selenium.__version__'

if [ -z "$1" ]
then
	echo "Veuillez indiquer le script a executer"
else
	source ../$virtFold/bin/activate
	python -c 'import selenium; print selenium.__version__'
	python3 "$script"
	deactivate
fi
