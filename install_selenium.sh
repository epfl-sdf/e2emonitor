#!/bin/bash
virtFold='venv'

echo "This script will install Selenium's dependencies on the local machine ..."
ZVER="290817.1716"
echo -e "enea le  "$ZVER

RED='\033[1;31m'
GREEN='\033[1;32m'
NOCOL='\033[0m'

if [ $(id -u) != "0" ]; then
echo -e ${RED}$0 "You must be the superuser to run this script"${NOCOL} >&2
exit 1
fi

echo -e ${GREEN}$0 "Starting..."${NOCOL}

echo -e ${GREEN}$0 "Apt-get update ..."${NOCOL}
apt-get update

echo -e ${GREEN}$0 "Checking locale machine locale ..."${NOCOL}
if locale -a | grep -Fxq "de_CH.utf8"
then
  echo -e "de_CH.utf8 found, continuing with rest of script"
else
  locale-gen "de_CH.UTF-8"
  dpkg-reconfigure --frontend=noninteractive locales
fi


echo -e ${GREEN}$0 "Installing dependencies needed for selenium"${NOCOL}

apt-get install python3-dev python3-pip
apt-get install xvfb
apt-get install firefox
apt install virtualenv

wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz
tar xf geckodriver-v0.18.0-linux64.tar.gz

if [ -d $virtFold ];
then
    rm -rf $virtFold    
fi

virtualenv -p /usr/bin/python3 $virtFold
source $virtFold/bin/activate
pip install pillow
pip install numpy 
pip install selenium 
pip install pyvirtualdisplay
deactivate
