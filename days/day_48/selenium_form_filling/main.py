from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "../../../lib/chrome/chromedriver"

# WEBSITE_URL = "https://www.amazon.com/Nintendo-Switch-Neon-Red-blue/dp/B07W4CK8KR/ref=sr_1_3?crid=I33JOJEHU5M6&keywords=nintendo+switch&qid=1642486490&sprefix=nintendo+switc%2Caps%2C368&sr=8-3"
# WEBSITE_URL = "https://www.python.org/"
# WEBSITE_URL = "https://en.wikipedia.org/wiki/Main_Page"
WEBSITE_URL = "https://secure-retreat-92358.herokuapp.com/"

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

driver.get(WEBSITE_URL)

first_name = driver.find_element(By.NAME, "fName")

last_name = driver.find_element(By.NAME, "lName")

email = driver.find_element(By.NAME, "email")

enter_button = driver.find_element(By.CLASS_NAME, "btn")

first_name.send_keys("abc")

last_name.send_keys("def")

email.send_keys("abc@def.com")

enter_button.click()

# driver.quit()





