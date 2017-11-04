#!/bin/bash
#petit script a lancer pour installer selenium
#zf041117.1310

virtFold="venv"

sudo apt-get update
sudo apt-get upgrade

## installing differnt program
sudo apt-get install python3
sudo apt-get install python3-dev python3-pip
sudo apt-get install xvfb
sudo apt-get install firefox

## Installing Geckodriver for firefox
wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz
	sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.18.0-linux64.tar.gz -O > /usr/bin/geckodriver'
	sudo chmod +x /usr/bin/geckodriver
	rm geckodriver-v0.18.0-linux64.tar.gz

## Installing Chromedriver for chrome
wget https://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip
	unzip chromedriver_linux64.zip
	sudo chmod +x chromedriver
	sudo mv chromedriver /usr/bin/
	rm chromedriver_linux64.zip

## Installing virtualenv and activate a new environment
sudo apt install virtualenv

if [ -d $virtFold ];
then
    rm -rf $virtFold
fi

virtualenv -p /usr/bin/python3 $virtFold
source $virtFold/bin/activate

## Installing selenium and pyvirtualdisplay to emulate a screen
pip install selenium
pip install pyvirtualdisplay
pip install pillow
pip install numpy

## Desactivate virtual environment
deactivate
