"""
How to get latitude and longitude for the ISS's current position API response
"""
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
iss_position = (latitude, longitude)

print(iss_position)

"""
Random Kanye quote API response
"""
from tkinter import *
import requests

def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    kanye_quote = response.json()["quote"]
    canvas.itemconfig(quote_text, text=kanye_quote)

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()

"""
Get sunrise and sunset times for your location API response
"""
import requests
from datetime import datetime

CHI_LATITUDE = 41.8781
CHI_LONGITUDE = -87.6298

parameters = {
    "lat": CHI_LATITUDE,
    "lng": CHI_LONGITUDE,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise_hour = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_hour = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()
now_hour = time_now.hour

print(sunrise_hour)
print(sunset_hour)
print(now_hour)
