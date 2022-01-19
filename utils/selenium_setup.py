from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "../../lib/chrome/chromedriver"

WEBSITE_URL = "https://www.amazon.com/"

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

driver.get(WEBSITE_URL)

driver.quit()
