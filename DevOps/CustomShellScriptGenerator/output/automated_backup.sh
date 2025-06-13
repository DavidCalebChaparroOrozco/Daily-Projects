#!/bin/bash
# Generated Script - automated_backup
# Description: Automates backup tasks


echo "Executing: Update system packages"
sudo apt update && sudo apt upgrade -y

echo "Executing: Create backup folder"
mkdir -p ~/backups

echo "Executing: Backup documents"
cp -r ~/Documents ~/backups/
