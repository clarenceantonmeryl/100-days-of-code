import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

CHROME_DRIVER_PATH = "../../../lib/chrome/chromedriver"

WEBSITE_URL = "http://orteil.dashnet.org/experiments/cookie/"

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

driver.get(WEBSITE_URL)

five_sec = time.time() + 5
five_min = time.time() + (9 * 60)  # 5minutes


def get_upgrades():
    store_divs = driver.find_elements(By.CSS_SELECTOR, "div#store div")

    names = [store_div.get_attribute("id") for store_div in store_divs if store_div.text != '']

    # print(names)

    prices = [int(store_div.text.split("\n")[0].split("-")[1].strip().replace(",", ""))
              for store_div in store_divs if store_div.text != '']

    # print(prices)

    upgrade_dict = {prices[index]: names[index] for index in range(len(names))}

    return upgrade_dict


upgrades = get_upgrades()

print(upgrades)

money = driver.find_element(By.ID, "money")
cookie = driver.find_element(By.ID, "cookie")

while True:

    cookie.click()

    if time.time() > five_sec:
        amount = int(money.text.replace(",", ""))
        affordable_upgrades = [upgrades[upgrade] for upgrade in upgrades.keys() if amount >= upgrade]
        print(affordable_upgrades)

        # purchase = driver.find_element(By.ID, affordable_upgrades[-1])
        purchase = driver.find_element(By.ID, random.choice(affordable_upgrades))

        purchase.click()
        five_sec = time.time() + 5

    if time.time() > five_min:
        break


# driver.quit()
