#!/bin/bash
export DEBIAN_FRONTEND=noninteractive
apt-get update
#apt-get clean
apt-get -y install vim
apt-get -y install xvfb
apt-get -y install unzip
apt-get -y install wget
apt-get -y install git

wget -N https://chromedriver.storage.googleapis.com/113.0.5672.63/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver

mv -f chromedriver /usr/local/share/chromedriver
ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
ln -s /usr/local/share/chromedriver /usr/bin/chromedriver


wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get install -y ./google-chrome-stable_current_amd64.deb


# Install pip:
apt-get -y install python3-pip
apt-get -y install python3-virtualenv



virtualenv garmin
source garmin/bin/activate
#garmin/bin/pip install google-api-python-client
#garmin/bin/pip install google_auth_oauthlib
#garmin/bin/pip install garminconnect
   

# Install Selenium and pyvirtualdisplay:
pip install pyvirtualdisplay selenium

pip install garth
pip install garminconnect
pip install requests

#install google apis
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib


#install kubernetes APIs
pip install kubernetes

apt-get install -y libnss3-tools
DEBIAN_FRONTEND='noninteractive' apt-get install -y libglib2.0-dev
