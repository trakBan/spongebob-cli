#!/usr/bin/env bash

if [[ $EUID -ne 0 ]]; then
   echo "Uninstall script must be run as root" 
   exit 1
fi

# Deletes spongebob-cli executable
rm /usr/bin/spongebob-cli || rm /usr/local/bin/spongebob-cli 

echo "spongebob-cli has been sucesfully uninstalled."
