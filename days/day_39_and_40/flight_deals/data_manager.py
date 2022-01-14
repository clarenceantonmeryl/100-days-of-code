import requests

SHEETY_GET_API_URL = 'https://api.sheety.co/2e30f2132cff24ad65ca6ac00224676f/flightDeals/prices'

SHEETY_USERS_URL = "https://api.sheety.co/2e30f2132cff24ad65ca6ac00224676f/flightDeals/users"



class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = [
            {"id": 2, 'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54},
            {"id": 3, 'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42},
            {"id": 4, 'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485},
            {"id": 5, 'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551},
            {"id": 6, 'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95},
            {"id": 7, 'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414},
            {"id": 8, 'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240},
            {"id": 9, 'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260},
            {"id": 10, 'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378},
        ]

    def init_destination(self):
        response = requests.get(url=SHEETY_GET_API_URL)
        response.raise_for_status()
        self.destination_data = response.json()['prices']

    def update_destination(self, id, iata_code):
        json = {
            "price": {
                "iataCode": iata_code
            }
        }

        response = requests.put(url=f"{SHEETY_GET_API_URL}/{id}", json=json)
        response.raise_for_status()
        print(response.json())

    def add_user(self, first_name, last_name, email):
        json = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }

        response = requests.post(url=SHEETY_USERS_URL, json=json)
        response.raise_for_status()
        print(response.json())

    def get_users(self) -> list:
        response = requests.get(url=SHEETY_USERS_URL)
        response.raise_for_status()
        return response.json()["users"]