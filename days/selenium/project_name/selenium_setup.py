import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "../../../lib/chrome/chromedriver"

WEBSITE_URL = "https://www.amazon.com/"

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

driver.get(WEBSITE_URL)

# Switch to windows
# all_windows = driver.window_handles
# base_window = all_windows[0]
# new_window = all_windows[1]
# driver.switch_to_window(new_window)


time.sleep(3)
driver.quit()
