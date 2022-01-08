import requests
from datetime import datetime
import time
import pytz


# "sunrise":"2022-01-07T19:04:02+00:00","sunset":"2022-01-08T09:46:14+00:00"





# print("LOCAL", get_local_datetime("2022-01-07T19:04:02+00:00"))

"""



print(
datetime_object.timestamp()
)
print(datetime.utcfromtimestamp(datetime_object.timestamp()))

"""


"""
def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    print(offset)

    print(datetime.fromtimestamp(now_timestamp))
    print(datetime.utcfromtimestamp(now_timestamp))


    # return utc_datetime + offset


print(datetime_from_utc_to_local(19))
"""





"""
now = datetime.now()
print(now)

API_ENDPOINT = "https://api.sunrise-sunset.org/json"

parameters = {
    'lat': -38.030918,
    'lng': 145.346115,
    "formatted": 0
}

response = requests.get(url=API_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
results = data.get('results', None)
if results:
    sunrise = results.get('sunrise', None)
    if sunrise:
        sunrise_time = int(sunrise.split('T')[1].split('+')[0].split(':')[0])
        print(sunrise_time)
    sunset = results.get('sunset', None)
    if sunset:
        sunset_time = int(sunset.split('T')[1].split('+')[0].split(':')[0])
        print(sunset_time)
"""
