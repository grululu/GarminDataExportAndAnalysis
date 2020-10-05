#!/bin/sh
git clone https://github.com/grululu/GarminDataExportAndAnalysis
cd GarminDataExportAndAnalysis
echo "GCuser=\"$GARMIN_USER\"" > Infos.py
echo "GCpass=\"$GARMIN_PASSWORD\"" >> Infos.py

cp /Credentials/* . 
python3 Garmin.py
python3 loadActivitiesOnGoogleDrive.py
python3 triggerUpdate.py
