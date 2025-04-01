"""
Topics Covered:
1. POST, PUT, and DELETE with the requests module
2. Pixela graph creation, additions, updates, and deletions

Completed: 4/1/2025
"""
import requests
from datetime import datetime

today = datetime.today()
yesterday = datetime(year=2025, month=3, day=31)
# FORMATTED_DATE = today.strftime("%Y%m%d")
FORMATTED_DATE = yesterday.strftime("%Y%m%d")

PIXELA_URL = "https://pixe.la/v1/users"
TOKEN = "A7Hajem9naowmm0077"
USERNAME = "shanmulmat"
GRAPH_ID = "graph1"
CREATE_GRAPH_URL = f"{PIXELA_URL}/{USERNAME}/graphs"
ADD_PIXEL_TO_GRAPH_URL = f"{CREATE_GRAPH_URL}/{GRAPH_ID}"
UPDATE_EXISTING_PIXEL_URL = f"{ADD_PIXEL_TO_GRAPH_URL}/{FORMATTED_DATE}"

# Create a username on the Pixela website
create_user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
create_user_response = requests.post(url=PIXELA_URL, json=create_user_parameters)
print(create_user_response.text)

# Create a graph on the Pixela website for your username
create_graph_parameters = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
create_graph_response = requests.post(url=CREATE_GRAPH_URL, headers=headers, json=create_graph_parameters)
print(create_graph_response.text)

# Add pixels to the graph you created
add_pixel_to_graph_parameters = {
    "date": FORMATTED_DATE,
    "quantity": "7.5"
}
add_pixel_response = requests.post(url=ADD_PIXEL_TO_GRAPH_URL, headers=headers, json=add_pixel_to_graph_parameters)
print(add_pixel_response.text)

# Update existing pixels on your graph (specify date at top)
update_pixel_parameters = {
    "quantity": "9.25"
}
update_pixel_response = requests.put(url=UPDATE_EXISTING_PIXEL_URL, headers=headers, json=update_pixel_parameters)
print(update_pixel_response.text)

# Delete pixels from your graph (specify date at top)
delete_pixel_response = requests.delete(url=UPDATE_EXISTING_PIXEL_URL, headers=headers)
print(delete_pixel_response.text)
