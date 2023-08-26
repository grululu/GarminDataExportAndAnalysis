import datetime
import json
import logging

import requests

from garminconnect import (
    Garmin,
    GarminConnectAuthenticationError,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
)

from Infos import GCuser, GCpass

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

runningActivityType = "running"  # Possible values are: cycling, running, swimming, multi_sport, fitness_equipment, hiking, walking, other
csvFile = "/MyApp/Activities.csv" 



def init_api(userName, password):
    """Initialize Garmin API with your credentials."""
    try:
        api = Garmin(userName, password)
        api.login()
    except (
            GarminConnectConnectionError,
            GarminConnectAuthenticationError,
            GarminConnectTooManyRequestsError,
            requests.exceptions.HTTPError,
    ) as err:
        logger.error("Error occurred during Garmin Connect communication: %s", err)
        return None
    return api

def loadActivities(api):
    today = datetime.date.today()
    startdate = today - datetime.timedelta(days=7) # Select past week

    try:
        activities = api.get_activities_by_date(startdate.isoformat(), today.isoformat(), runningActivityType)
        with open("activities.json", "w", encoding="utf-8") as f:
                json.dump(activities, f, ensure_ascii=False, indent=4)

    except (
            GarminConnectConnectionError,
            GarminConnectAuthenticationError,
            GarminConnectTooManyRequestsError,
            requests.exceptions.HTTPError,
        ) as err:
            logger.error("Error occurred: %s", err)

def writeCSV():
    with open("activities.json") as f:
        activities = json.load(f)
    with open(csvFile, "w") as of:
        firstLine="Tipo di attività,Data,Preferita,Titolo,Distanza,Calorie,Tempo,FC Media,FC max,TE attività aerobica,Cadenza di corsa media,Cadenza di corsa max,Passo medio,Passo migliore,Ascesa totale,Discesa totale,Lunghezza media passo,Rapporto verticale medio,Oscillazione verticale media,Tempo medio di contatto con il suolo,Training Stress Score®,Potenza media,Potenza max,Grit,Flow,Swolf medio,Frequenza media vogate,Ripetizioni totali,Tempo di immersione,Temperatura min,Intervallo di superficie,Decompressione,Tempo Lap migliore,Numero di Lap,Temperatura max,Tempo in movimento,Tempo trascorso,Quota minima,Quota massima\n"
        of.write(firstLine)
        for activity in activities:
            activity_id = activity["activityId"]
            tipo="Corsa"
            startTimeLocal=activity["startTimeLocal"]
            preferita="FALSE"
            activityName=activity["activityName"]
            distance=str(round(activity["distance"]/1000,2))
            calories=str(round(activity["calories"]))
            duration=str(datetime.timedelta(seconds=activity["duration"]))
            averageHR=str(round(activity["averageHR"]))
            maxHR=str(round(activity["maxHR"]))
            aerobicTrainingEffect=str(round(activity["aerobicTrainingEffect"],1))
            averageRunningCadenceInStepsPerMinute=str(round(activity["averageRunningCadenceInStepsPerMinute"]))
            maxRunningCadenceInStepsPerMinute=str(round(activity["maxRunningCadenceInStepsPerMinute"]))
            averageSpeed=str(datetime.timedelta(minutes=round(1/activity["averageSpeed"]*1000)))
            maxSpeed=str(datetime.timedelta(minutes=round(1/activity["maxSpeed"]*1000)))

        #speed1=activity["averageSpeed"]
        #speed2=1/activity["averageSpeed"]*1000/60
        #speed3=datetime.timedelta(minutes=1/activity["averageSpeed"]*1000/60)
        #speed4=str(datetime.timedelta(minutes=1/activity["averageSpeed"]*1000/60))
        #print("speed4: "+speed4)
        #speed5=str(datetime.timedelta(seconds=round(1/activity["averageSpeed"]*1000)))
        #print("speed5: "+speed5)
        #speed6=datetime.datetime.strptime(speed5,"%H:%M:%S")
        #print("speed6: "+str(speed6))
        #averageSpeed=speed6.strftime('%M:%S')
            elevationGain=str(round(activity["elevationGain"]))
            elevationLoss=str(round(activity["elevationLoss"]))
            avgStrideLength=str(round(activity["avgStrideLength"]))
        




            activityCSV=tipo+","+startTimeLocal+","+preferita+","+activityName+","+distance+","+calories+","+duration+","+averageHR+","+maxHR+","+aerobicTrainingEffect+","+averageRunningCadenceInStepsPerMinute+","+maxRunningCadenceInStepsPerMinute+","+averageSpeed+","+maxSpeed+","+elevationGain+","+elevationLoss+","+avgStrideLength+",\"0.0\",\"0.0\",\"0\",\"0.0\",\"0\",\"0\",\"0.0\",\"0.0\",\"0\",\"0\",\"0\",\"0:00\",\"0.0\",\"0:00\",\"No\",\"02:33.86\",\"8\",\"0.0\",\"00:39:58\",\"00:40:27\",\"331\",\"348\"\n"
            of.write(activityCSV)

# Main 
api = init_api(GCuser, GCpass)
loadActivities(api)
writeCSV()
