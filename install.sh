#!/bin/bash
# Install script for Gom Jabbar for Raspberry Pi
# Author: Michael D'Argenio
# mjdargen@gmail.com

echo "This script will update your packages and install new packages for Python 3."
sleep 5s

# upgrade packages and remove any unnecessary packages
sudo apt-get --assume-yes update
sudo apt-get --assume-yes upgrade
sudo apt-get --assume-yes autoremove
sudo apt-get --assume-yes autoclean

# install dependency packages
sudo apt-get --assume-yes install python3
sudo apt-get --assume-yes install python3-pip
sudo apt-get --assume-yes install python3-dev
sudo apt-get --assume-yes install python3-setuptools
sudo apt-get --assume-yes install pigpio python3-pigpio
sudo apt-get --assume-yes install ffmpeg libavcodec-extra

# install PIP packages in virtual environment
pip3 install -r requirements.txt

# set gpiozero pin factory to pigpio
export GPIOZERO_PIN_FACTORY=pigpio
