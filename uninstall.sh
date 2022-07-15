#!/usr/bin/env bash
if [[ $EUID -ne 0 ]]; then
   echo "Uninstall script must be run as root" 
   exit 1
fi

# Deletes spongebob-cli from /usr/bin/
rm /usr/bin/spongebob-cli

spongebob-cli || echo "spongebob-cli has been sucesfully uninstalled."
