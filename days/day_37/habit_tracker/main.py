import requests
from datetime import datetime

NOW = datetime.now()
DATE = datetime(year=2021, month=12, day=11).strftime("%Y%m%d")
DAY = NOW.strftime("%Y%m%d")

PIXELA_TOKEN = "tokentokentoken"
PIXELA_USERNAME = "c8a10"
PIXELA_GRAPH_ID = "cyclinggraph1"

PIXELA_USERS_URL = "https://pixe.la/v1/users"
PIXELA_GRAPH_URL = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs"
PIXELA_POST_GRAPH_URL = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}"
PIXELA_PUT_GRAPH_URL = f"{PIXELA_POST_GRAPH_URL}/{DAY}"
PIXELA_DEL_GRAPH_URL = f"{PIXELA_POST_GRAPH_URL}/{DATE}"


HEADERS = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

USER_PARAMS = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

GRAPH_PARAMS = {
    "id": PIXELA_GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "shibafu"

}

GRAPH_DATA = {
    "date": DAY,
    "quantity": "100"
}

UPDATE_DATA = {
    "quantity": "30"
}

print(GRAPH_DATA)


def delete_data(url, headers=None) -> str:
    if headers:
        response = requests.delete(url=url, headers=headers)
    else:
        response = requests.delete(url=url)

    response.raise_for_status()
    print(response.url)
    return response.text


def put_data(url, json, headers=None) -> str:
    if headers:
        response = requests.put(url=url, json=json, headers=headers)
    else:
        response = requests.put(url=url, json=json)

    response.raise_for_status()
    print(response.url)
    return response.text


def post_data(url, json, headers=None) -> str:
    if headers:
        response = requests.post(url=url, json=json, headers=headers)
    else:
        response = requests.post(url=url, json=json)

    response.raise_for_status()
    print(response.url)
    return response.text


def create_user():
    print(post_data(url=PIXELA_USERS_URL, json=USER_PARAMS))


def create_graph():
    print(post_data(url=PIXELA_GRAPH_URL, json=GRAPH_PARAMS, headers=HEADERS))


def post_graph():
    print(post_data(url=PIXELA_POST_GRAPH_URL, json=GRAPH_DATA, headers=HEADERS))


def update_graph():
    print(put_data(url=PIXELA_PUT_GRAPH_URL, json=UPDATE_DATA, headers=HEADERS))


def delete_graph():
    print(delete_data(url=PIXELA_DEL_GRAPH_URL, headers=HEADERS))


delete_graph()
