#!/bin/sh
#git clone https://github.com/grululu/GarminDataExportAndAnalysis
cd /MyApp
export GARMIN_USER=$(echo $GARMIN_USER | tr -d '\040\011\012\015')
export GARMIN_PASSWORD=$(echo $GARMIN_PASSWORD | tr -d '\040\011\012\015')

echo "GCuser=\"$GARMIN_USER\"" > Infos.py
echo "GCpass=\"$GARMIN_PASSWORD\"" >> Infos.py

python3 downloadActivities.py
python3 loadActivitiesOnGoogleDrive.py
python3 triggerUpdate.py
