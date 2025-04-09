import requests

SHEETY_TOKEN = 'sdufhglsiudf89898hadsflaa'
SHEETY_PRICES_URL = 'https://api.sheety.co/1400b306f2f3c80f665a6e924568bea4/flightDeals/prices'
SHEETY_USERS_URL = 'https://api.sheety.co/1400b306f2f3c80f665a6e924568bea4/flightDeals/users'
SHEETY_HEADERS = {
    'Authorization': f'Bearer {SHEETY_TOKEN}'
}

class DataManager:

    def __init__(self):
        # Save your Sheety endpoints an environment variables
        self.prices_endpoint = SHEETY_PRICES_URL
        self.users_endpoint = SHEETY_USERS_URL
        self.authorization = SHEETY_HEADERS
        # Destination and Customer fields data start out empty
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.prices_endpoint, headers=self.authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data,
                headers=self.authorization
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint, headers=self.authorization)
        data = response.json()
        # See how Sheet data is formatted so that you use the correct column name!
        # pprint(data)
        # Name of spreadsheet 'tab' with the customer emails should be "users".
        self.customer_data = data["users"]
        return self.customer_data
