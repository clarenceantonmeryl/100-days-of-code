import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "../../../lib/chrome/chromedriver"

LOGIN_URL = "https://www.instagram.com/accounts/login/"
PROFILE_URL = "https://www.instagram.com/chefsteps/"

ACCOUNT_EMAIL = "c8a10dev@gmail.com"
ACCOUNT_PASSWORD = "Almond123"


class InstaBot:

    def __init__(self):
        self.service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)

    def login(self):
        self.driver.get(LOGIN_URL)
        time.sleep(5.0)

        username_text = self.driver.find_element(By.NAME, "username")
        username_text.send_keys(ACCOUNT_EMAIL)

        password_text = self.driver.find_element(By.NAME, "password")
        password_text.send_keys(ACCOUNT_PASSWORD)
        password_text.send_keys(Keys.ENTER)

        time.sleep(2.0)

    def find_followers(self):
        print("something")
        self.driver.get(PROFILE_URL)
        print("something else")

        time.sleep(5.0)

        try:
            followers_link = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        except selenium.common.exceptions.NoSuchElementException:
            print("Element not found")
        else:
            followers_link.click()
            time.sleep(3.0)

            scroll_div = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')
            for index in range(10):
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_div)
                time.sleep(2.0)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        index = 1
        for follow_button in follow_buttons:
            try:
                follow_button.click()
                print(index)
                index += 1
                time.sleep(2.0)
            except selenium.common.exceptions.ElementClickInterceptedException:
                close_button = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[1]/div/div[2]/button')
                close_button.click()
                print("Closing")
                break

        time.sleep(10000.0)
