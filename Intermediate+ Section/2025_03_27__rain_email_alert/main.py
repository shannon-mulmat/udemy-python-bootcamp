"""
Topics Covered:
1. Authentication with an API key
2. Sending SMS with Twilio
3. Environment variables (os package)

Project Description:
- Write a program that will email you to bring an umbrella if it's going to rain that day

Completed: 3/27/2025
"""
import requests
import smtplib

WEATHER_APP_API_KEY = "56fb67a4c72ee6616c54da770eed51cf"
CHI_LAT = 41.881832
CHI_LONG = -87.623177
WEATHER_APP_URL = "https://api.openweathermap.org/data/2.5/forecast"
GMAIL_EMAIL = "smpythonproject@gmail.com"
GMAIL_APP_PASSWORD = ""
YAHOO_EMAIL = "smpythonproject@yahoo.com"

parameters = {
    "lat": CHI_LAT,
    "lon": CHI_LONG,
    "appid": WEATHER_APP_API_KEY,
    "cnt": 4
}

response = requests.get(url=WEATHER_APP_URL, params=parameters)
response.raise_for_status()
weather_data = response.json()

for weather_block in weather_data["list"]:
    weather_id = weather_block["weather"][0]["id"]
    weather_codes = [weather_id for weather_block in weather_data["list"]]

if min(weather_codes) < 700:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=GMAIL_EMAIL, password=GMAIL_APP_PASSWORD)
        connection.sendmail(
            from_addr=GMAIL_EMAIL,
            to_addrs=YAHOO_EMAIL,
            msg=f"Subject:Weather Report\n\nIt's going to rain today! Bring an umbrella!"
        )
