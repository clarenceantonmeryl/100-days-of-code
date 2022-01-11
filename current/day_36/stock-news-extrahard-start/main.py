import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
AV_API_KEY = "L4N83JVM2WKMVRGJ"
AV_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": AV_API_KEY
}

AV_URL = "https://www.alphavantage.co/query"

NEWS_API_KEY = "6e10c6d5c23f42d583c87a9121b3c41b"

NEWS_API_PARAMETERS = {
    "q": STOCK,
    "apiKey": NEWS_API_KEY
}

NEWS_URL = "https://newsapi.org/v2/everything"

TWILIO_PHONE = "+18646517397"
TWILIO_ACCOUNT_SID = "ACcf62378ca629ecc366e57ea9b642593a"
TWILIO_AUTH_TOKEN = "fd845e1b9849912c6a5ad129d75533e7"
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN


def get_response(url, params):
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    print(response.url)
    return response.json()


def send_message(body):
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=body,
            from_=TWILIO_PHONE,
            to='+61499898919'
    )

    print(message.sid)


def get_stock_data():
    data = get_response(url=AV_URL, params=AV_PARAMETERS)
    daily_stock_data: {} = data["Time Series (Daily)"]

    daily_stock_list = [(key, value) for key, value in daily_stock_data.items()]

    daily_close_values = [day[1]["4. close"] for day in daily_stock_list[:2]]

    return daily_close_values


def process_stock_data():
    close_data = get_stock_data()
    day_1_close = float(close_data[0])
    day_2_close = float(close_data[1])
    difference = abs(day_1_close - day_2_close)

    if day_1_close - day_2_close < 0:
        message = STOCK + " 🔻" + str(round(difference, 2))
    else:
        message = STOCK + " 🔺" + str(round(difference, 2))

    return message, difference >= abs(0.05 * day_1_close)


def get_news():
    message, display_news = process_stock_data()
    print(message, display_news)

    if display_news:
        data = get_response(url=NEWS_URL, params=NEWS_API_PARAMETERS)
        articles = data["articles"][:3]
        news = [article["title"] for article in articles]
        return display_news, message, news
    else:
        return False, None, None


def format_message():
    display_news, message, news = get_news()

    if display_news:
        news_list = '\n\n- '.join(news)
        formatted_message = f"\n\n{message}\n\n- {news_list}"
        send_message(formatted_message)


format_message()


