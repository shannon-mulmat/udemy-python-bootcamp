"""
Topics Covered:
1. API calls and responses

Project Description:
- Create a program that will send you an email telling you to "look up" when the ISS is overhead at night

Completed: 3/24/2025
"""
import requests
from datetime import datetime
import smtplib
import time

CHI_LAT = 41.881832
CHI_LONG = -87.623177
GMAIL_EMAIL = "smpythonproject@gmail.com"
GMAIL_APP_PASSWORD = "yarxbvegquzkuxiw"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if CHI_LAT - 5 <= iss_latitude <= CHI_LAT + 5 and CHI_LONG - 5 <= iss_longitude <= CHI_LONG + 5:
        return True

def is_night():
    parameters = {
        "lat": CHI_LAT,
        "lng": CHI_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if sunset <= time_now.hour <= sunrise:
        return True

while True:
    time.sleep(60) # executes code every 60 seconds while computer is on and program is running
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=GMAIL_EMAIL, password=GMAIL_APP_PASSWORD)
            connection.sendmail(
                from_addr=GMAIL_EMAIL,
                to_addrs=GMAIL_EMAIL,
                msg="Subject:Look Up!\n\nThe ISS is overhead in the sky!"
            )
