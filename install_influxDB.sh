#!/bin/bash
#petit script a lancer pour installer influxDB ainsi que le module pour python
#lm021217.2041

virtFold="venv"

#Ajouter la repo
curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
source /etc/lsb-release
echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/influxdb.list

#installer influxdb
sudo apt-get update && sudo apt-get install -y influxdb

# Installer module pour python
virtualenv -p /usr/bin/python3 $virtFold
source $virtFold/bin/activate

pip install influxDB

deactivate
