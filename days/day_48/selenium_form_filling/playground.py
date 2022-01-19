from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time


CHROME_DRIVER_PATH = "../../../lib/chrome/chromedriver"

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")


timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5minutes


#Get upgrade item ids.
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
item_prices = []


# Convert <b> text into an integer price.
for price in all_prices:
    element_text = price.text
    if element_text != "":
        cost = int(element_text.split("-")[1].strip().replace(",", ""))
        item_prices.append(cost)


print(item_prices)

# Create dictionary of store items and prices
cookie_upgrades = {}
for n in range(len(item_prices)):
    cookie_upgrades[item_prices[n]] = item_ids[n]

print(cookie_upgrades)


while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:
        # Get all upgrade <b> tags
        # Get current cookie count
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)
        print(cookie_count)

        #Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                 affordable_upgrades[cost] = id

        print(affordable_upgrades)

        #Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print("Highest Upgrade", highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()

        #Add another 5 seconds until the next check
        timeout = time.time() + 5


    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break




driver.quit()






'''



count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(count.text)

# count.click()

all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# all_portals.click()

search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)



times_list = []

times = driver.find_elements(By.CSS_SELECTOR, "div.event-widget li time")
# times = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time')
for time in times:
    times_list.append(time.text)

events_list = []

events = driver.find_elements(By.CSS_SELECTOR, "div.event-widget li a")
# events = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')
for event in events:
    events_list.append(event.text)

event_dictionary = {
    index: {
        "time": times_list[index],
        "event": events_list[index]
    } for index in range(len(times_list))
}

print(event_dictionary)
'''






# price = driver.find_element(By.NAME, "q")
# print(price.tag_name)
# print(price.get_attribute("placeholder"))
#
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)
#
# link = driver.find_element(By.CSS_SELECTOR, "div.documentation-widget p a")
# print(link.text)
# print(link.get_attribute("href"))

# price = driver.find_element(By.XPATH, '//*[@id="priceblock_ourprice"]')
# print(price.text)

# driver.get("https://orteil.dashnet.org/cookieclicker/")
# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time
