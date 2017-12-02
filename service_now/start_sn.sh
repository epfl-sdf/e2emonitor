#!/bin/bash
virtFold="venv"
script=$1

if [ -z "$1" ]
then
	echo "Veuillez indiquer le script a executer"
else
	source ../$virtFold/bin/activate
	python3 "$script"
	deactivate
fi
