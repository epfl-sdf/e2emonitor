#!/bin/bash

#Télécharge le fichier d'installation
wget https://s3-us-west-2.amazonaws.com/grafana-releases/release/grafana_4.5.2_amd64.deb
sudo apt-get install -y adduser libfontconfig
sudo dpkg -i grafana_4.5.2_amd64.deb


#Ajouter repository
sudo echo "deb https://packagecloud.io/grafana/stable/debian/ jessie main" >> /etc/apt/sources.list

#Installer Grafana
sudo apt-get update
sudo apt-get install grafana

rm grafana_4.5.2_amd64.deb
