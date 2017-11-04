#!/bin/bash
#petit script a lancer pour installer selenium
#zf041117.1310

virtFold="venv"

sudo apt-get update
sudo apt-get upgrade

## installing python 3
sudo apt-get install python3

## Installing virtualenv and activate a new environment
sudo apt install virtualenv

if [ -d $virtFold ];
then
    rm -rf $virtFold
fi

virtualenv -p /usr/bin/python3 $virtFold
source $virtFold/bin/activate

## Installing selenium and pyvirtualdisplay to emulate a screen
sudo apt-get install python3-pip
pip3 install selenium
pip3 install pyvirtualdisplay

## Desactivate virtual environment
deactivate

## Installing Geckodriver for firefox
wget https://github.com/mozilla/geckodriver/releases/download/v0.19.0/geckodriver-v0.19.0-linux64.tar.gz
	sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.19.0-linux64.tar.gz -O > /usr/bin/geckodriver'
	sudo chmod +x /usr/bin/geckodriver
	rm geckodriver-v0.19.0-linux64.tar.gz

## Installing Chromedriver for chrome
wget https://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip
	unzip chromedriver_linux64.zip
	sudo chmod +x chromedriver
	sudo mv chromedriver /usr/bin/
	rm chromedriver_linux64.zip
