#!/bin/bash

echo "This script will install Jmeter and it's dependencies on the local machine ..."
ZVER="290817.1716"
echo -e "enea le  "$ZVER

RED='\033[1;31m'
GREEN='\033[1;32m'
NOCOL='\033[0m'

if [ $(id -u) != "0" ]; then
echo "You must be the superuser to run this script" >&2
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

vJMETER="2.11-5"
echo -e ${GREEN}$0 "Install JMETER v" $vJMETER${NOCOL}
apt-get install -y jmeter=$vJMETER


echo -e ${GREEN}$0 "Installation is over. Script exiting." $vJMETER${NOCOL}
