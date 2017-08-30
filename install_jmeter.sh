#!/bin/bash

echo "This script will install Jmeter and it's dependencies on the local machine ..."
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

##### Jmeter apt-get version
#vJMETER="2.11-5"
#echo -e ${GREEN}$0 "Install JMETER v" $vJMETER${NOCOL}
#apt-get install -y jmeter=$vJMETER

#### Jmeter latest version

echo -e ${GREEN}$0 "Checking locale machine locale ..."${NOCOL}

vJMETER="3.2"
downloadJMETERloc="http://mirror.easyname.ch/apache//jmeter/binaries/apache-jmeter-3.2.tgz"
JMETER="apache-jmeter-3.2"
echo -e ${GREEN}$0 "Installation Jmeter $vJMETER"${NOCOL}
echo -e ${GREEN}$0 "Installing JRE 8 headless"${NOCOL}
apt-get install -y openjdk-8-jre-headless

sudo rm -R /opt/apache-jmeter
sudo mkdir /opt/apache-jmeter
cd /opt/apache-jmeter

echo -e ${GREEN}$0 "Downloading Jmeter"${NOCOL}
wget -c $downloadJMETERloc

echo -e ${GREEN}$0 "Unpacking & installing Jmeter"${NOCOL}
tar xzf $JMETER.tgz
sudo rm /usr/bin/jmeter
sudo ln -s /opt/apache-jmeter/$JMETER/bin/jmeter /usr/bin/jmeter

echo -e ${GREEN}$0 "Install done..."${NOCOL}
