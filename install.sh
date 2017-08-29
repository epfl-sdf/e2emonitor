#!/bin/bash
#petit script a lancer pour installer l'agent datadog sur une machine Ubuntu sous architecture i686 ou x86_64
#zf290817.1130

# Installation de l'agent datadog en pas a pas
# source: https://app.datadoghq.com/signup/agent#ubuntu

# Parametrage de apt pour pouvoir telecharger via https
sudo apt-get update
sudo apt-get install apt-transport-https

# Parametrage du depot datadog et telechargement de la clefs apt pour datadog
sudo sh -c "echo 'deb https://apt.datadoghq.com/ stable main' > /etc/apt/sources.list.d/datadog.list"
sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 C7A7DA52

# Mise a jour du depot local apt et installation de l'agent
sudo apt-get update
sudo apt-get install datadog-agent

# Copie de l'exemple de configuration en place et connection de la clef API local
sudo sh -c "sed 's/api_key:.*/api_key: 53e0adf1b5422095790e787a949d54ea/' /etc/dd-agent/datadog.conf.example > /etc/dd-agent/datadog.conf"

# Demarrage de l'agent datadog
sudo /etc/init.d/datadog-agent start
