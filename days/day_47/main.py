import requests
import lxml
import smtplib
from bs4 import BeautifulSoup

EMAIL = "c.antonmeryl.123@gmail.com"
PASSWORD = "Almond123"


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

website_url = "https://www.amazon.com/Nintendo-Switch-Neon-Red-blue/dp/B07W4CK8KR/ref=sr_1_3?crid=I33JOJEHU5M6&keywords=nintendo+switch&qid=1642486490&sprefix=nintendo+switc%2Caps%2C368&sr=8-3"
# input("Enter the url of product: ")
target_price = 310
# input("Enter price goal: ")

response = requests.get(url=website_url, headers=HEADERS)
response.raise_for_status()
contents = response.text

# print(contents)

soup = BeautifulSoup(contents, "lxml")
price_span = soup.find(name="span", id="priceblock_ourprice")
price_text = price_span.getText()
print(price_text)
print(price_text.split("$"))
price = float(price_text.split("$")[1])
print(price)

product_title_span = soup.find(name="span", id="productTitle")
product_title = product_title_span.getText().strip()
print(product_title)


def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=f"Subject:Price Alert\n\n{product_title} is selling for {price}"
                                f", below the target price {target_price}. Buy at {website_url}")


if target_price >= price:
    send_mail()
