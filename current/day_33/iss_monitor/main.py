import requests
from datetime import datetime
import pytz

ISS_ENDPOINT = "http://api.open-notify.org/iss-now.json"
SUN_ENDPOINT = "https://api.sunrise-sunset.org/json"

LOCAL_LATITUDE = -38.030918
LOCAL_LONGITUDE = 145.346115

NOW = datetime.now()


def get_local_datetime(utc_datetime_string):
    datetime_str_utc = utc_datetime_string.split('+')[0]
    datetime_object_utc = datetime.strptime(datetime_str_utc, '%Y-%m-%dT%H:%M:%S')
    tz = pytz.timezone('Australia/Melbourne')
    local_datetime = pytz.utc.localize(datetime_object_utc, is_dst=None).astimezone(tz)
    return local_datetime


def get_response(url, params=None):
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    return response.json()


def get_iss_location():
    data = get_response(ISS_ENDPOINT)
    iss_position = data.get('iss_position', None)
    if iss_position:
        latitude = float(iss_position.get("latitude", 0.0))
        longitude = float(iss_position.get("longitude", 0.0))
        # return latitude, longitude
        return -38.1, 145.6


def is_iss_close(iss_location):
    iss_latitude, iss_longitude = iss_location
    return (iss_latitude - 5 < LOCAL_LATITUDE < iss_latitude + 5) and \
           (iss_longitude - 5 < LOCAL_LONGITUDE < iss_longitude + 5)


def get_sunrise_sunset(latitude, longitude):
    parameters = {
        'lat': latitude,
        'lng': longitude,
        "formatted": 0
    }
    data = get_response(url=SUN_ENDPOINT, params=parameters)
    results = data.get('results', None)
    if results:
        sunrise = get_local_datetime(results.get('sunrise', None))  # results.get('sunrise', None)
        sunset = get_local_datetime(results.get('sunset', None))
        return sunrise.hour, sunset.hour

    #return 18, 22


def is_dark(sun):
    sunrise, sunset = sun
    return NOW.hour < sunrise or NOW.hour > sunset


def send_email():
    print("Send email")


def monitor():
    if is_iss_close(get_iss_location()):
        print("ISS is close")
        if is_dark(get_sunrise_sunset(LOCAL_LATITUDE, LOCAL_LONGITUDE)):
            print("DARK time")
            send_email()
    else:
        print("ISS is far")


monitor()
