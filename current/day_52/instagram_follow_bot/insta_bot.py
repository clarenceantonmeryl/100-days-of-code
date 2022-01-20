import time
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

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass
