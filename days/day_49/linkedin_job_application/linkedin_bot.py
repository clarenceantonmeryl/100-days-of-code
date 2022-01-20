import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "../../../lib/chrome/chromedriver"

WEBSITE_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

ACCOUNT_EMAIL = "c8a10dev@gmail.com"
ACCOUNT_PASSWORD = "Almond123"

#
# driver.get(WEBSITE_URL)

# time.sleep(5)
# driver.quit()


class LinkedInBot:

    def __init__(self):
        self.service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)

    def login(self):
        self.driver.get(WEBSITE_URL)
        time.sleep(3.0)

        sign_in_button = self.driver.find_element(By.LINK_TEXT, "Sign in")
        sign_in_button.click()

        time.sleep(5.0)

        username_text = self.driver.find_element(By.ID, "username")
        username_text.send_keys(ACCOUNT_EMAIL)

        password_text = self.driver.find_element(By.ID, "password")
        password_text.send_keys(ACCOUNT_PASSWORD)

        sign_in_submit_button = self.driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
        sign_in_submit_button.click()

        time.sleep(5.0)

    def save_job(self):
        save_button = self.driver.find_element(By.CLASS_NAME, "jobs-save-button")
        save_button.click()

        time.sleep(2.0)

        self.driver.quit()