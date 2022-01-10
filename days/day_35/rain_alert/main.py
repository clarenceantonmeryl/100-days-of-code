import requests
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

OWM_API_KEY = "52831a1a7238829c04ca349947d269ec"  # "69f04e4613056b159c2761a9d9e664d2"
OWM_API_URL = "https://api.openweathermap.org/data/2.5/onecall"
OWM_API_PARAMS = {
    "lat": -38.030918,
    "lon": 145.346115,
    "exclude": "current,minutely,daily",
    "appid": OWM_API_KEY
}

TWILIO_PHONE = "+18646517397"
# TWILIO_ACCOUNT_SID = "ACcf62378ca629ecc366e57ea9b642593a"
# TWILIO_AUTH_TOKEN = "fd845e1b9849912c6a5ad129d75533e7"


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

# account_sid = TWILIO_ACCOUNT_SID
# auth_token = TWILIO_AUTH_TOKEN

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]


def send_message():
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain. Remember to take an umbrella",
        from_=TWILIO_PHONE,
        to='+61499898919'
    )

    print(message.sid)


def get_weather_data():
    response = requests.get(url=OWM_API_URL, params=OWM_API_PARAMS)
    # print(response.url)
    response.raise_for_status()
    if response.status_code == 200:
        return response.json()["hourly"]


def process_weather():
    data = get_weather_data()
    # [index]["weather"][0]["id"]

    # code_list = [data[index]["weather"][0]["id"] for index in range(12)]
    # code_list = [hour["weather"][0]["id"] for hour in data[:12]]
    # print(code_list)

    for code in [hour["weather"][0]["id"] for hour in data[:12]]:
        print(code)
        if code < 700:
            print("It will be raining")
            send_message()
            return
    print("It won't be raining")



process_weather()

