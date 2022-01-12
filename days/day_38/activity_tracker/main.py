import requests
from datetime import datetime

NUTRITIONIX_APP_ID = 'dd85dd44'
NUTRITIONIX_API_KEY = '80175107d1cb832659339394f266e93f'
NUTRITIONIX_API_URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'

NUTRIONIX_HEADERS = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "Content-Type": "application/json"
}

text = input("What exercises did you do: ")

NUTRIONIX_PARAMS = {
 "query": text,
 "gender": "male",
 "weight_kg": 42.1,
 "height_cm": 180.1,
 "age": 14
}

POST_WORKOUT_API_URL = 'https://api.sheety.co/2e30f2132cff24ad65ca6ac00224676f/workouts/workouts'


def post_request(url, json, headers=None):
    if headers:
        response = requests.post(url=url, json=json, headers=headers)
    else:
        response = requests.post(url=url, json=json)

    response.raise_for_status()
    return response.json()


def process_workouts():
    data = post_request(url=NUTRITIONIX_API_URL, json=NUTRIONIX_PARAMS, headers=NUTRIONIX_HEADERS)['exercises']
    print(data)

    now = datetime.now()
    now_time = now.strftime("%X")
    now_date = now.strftime("%d/%m/%Y")
    print(now_date)
    print(now_time)

    workouts = [{"workout": {
        'date': now_date,
        'time': now_time,
        'exercise': exercise['name'].title(),
        'duration': exercise['duration_min'],
        'calories': exercise['nf_calories']
    }} for exercise in data]

    return workouts


def post_google_sheet():
    workouts = process_workouts()
    for workout in workouts:
        print(workout)
        data = post_request(url=POST_WORKOUT_API_URL, json=workout)
        print(data)


post_google_sheet()




# ran 5k and cycled 20k
