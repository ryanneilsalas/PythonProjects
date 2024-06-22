from tkinter import *
import requests
from datetime import datetime
import os
GENDER = "Male"
WEIGHT_KG = 57
HEIGHT_CM = 161
AGE = 28

exercise_endpoint = os.environ["Nt_exercise_endpoint"]
APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]

exercise_text = input("Tell me which exercises you did: ")
sheet_endpoint = os.environ["NT_sheet_endpoint"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)

# link to google sheet ->
# https://docs.google.com/spreadsheets/d/10QkDVkczSxu8DACzMH3SvaNBgsHek5gBGyhtfrNwKHc/edit?gid=0#gid=0
