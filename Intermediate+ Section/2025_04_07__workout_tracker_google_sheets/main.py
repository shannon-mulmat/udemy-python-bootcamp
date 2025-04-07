"""
Topics Covered:
1. Interacting with Google Sheets via Sheety API

Project Description:
- Create a program that allows the user to track their workouts
    1. User writes in plain English some workout(s) they did today
    2. Program utilizes the Nutritionix API to figure out the type of exercise that was performed, the duration, and the calories expended
    3. Program writes this data to a google sheet, creating a date and time for each entry of today's date and time
https://docs.google.com/spreadsheets/d/1UrbH3ZRPPi2O0vDQCS3YxbO5PocPoKHu0Av-q9s8p0I/edit?usp=sharing

Completed: 4/7/2025
"""
import requests
from datetime import datetime

NUTRITIONIX_APP_ID = '159432ef'
NUTRITIONIX_API_KEY = '13e8ccae7c95a5cfdc39c3c3ec76149e'
NUTRITIONIX_URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'
WEIGHT_KG = 77.1107
HEIGHT_CM = 167.64
AGE = 30
GENDER = 'Female'
SHEETY_URL = 'https://api.sheety.co/1400b306f2f3c80f665a6e924568bea4/workoutTracking/workouts'
SHEETY_TOKEN = 'o78yehrfusdfhg8uojksadf00'

query = input("Which exercise(s) have you completed? ")

nutritionix_headers = {
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_API_KEY
}

nutritionix_parameters = {
    'query': query,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE,
    'gender': GENDER
}

sheety_headers = {
    'Authorization': f'Bearer {SHEETY_TOKEN}'
}

today = datetime.now()
formatted_time = today.strftime('%X')
formatted_date = today.strftime('%m/%d/%Y')

nutritionix_response = requests.post(
    url=NUTRITIONIX_URL,
    headers=nutritionix_headers,
    json=nutritionix_parameters
)
nutritionix_result = nutritionix_response.json()

for exercise in nutritionix_result['exercises']:
    sheety_params = {
        'workout': {
            'date': formatted_date,
            'time': formatted_time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    sheety_response = requests.post(
        url=SHEETY_URL,
        json=sheety_params,
        headers=sheety_headers
    )
    print(sheety_response.text)
