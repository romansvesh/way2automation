# -*- coding: utf-8 -*-

import pickle
from pathlib import Path

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from MainPage import GRAVATAR, BUTTON_LOGIN
from Variables import *





class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def wait_for_element(self, locator):
        """This wait the element"""
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))

    def save_cookies(self, name):
        """This save cookies into file"""
        with open(name, 'wb') as f:
            pickle.dump(self.driver.get_cookies(), f)

    def login_with_cookies(self, cookies_file):
        """This login with cookies from file"""
        with open(cookies_file, 'rb') as f:
            cookies = pickle.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()


class MainPage(BasePage):
    # Locators
    INPUT_EMAIL = '//*[@id="user_email"]'
    INPUT_PASSWORD = '//*[@id="user_password"]'
    BUTTON_SUBMIT = '//*[@type="submit"]'

    def fill_email(self):
        self.wait_for_element(INPUT_EMAIL)
        element = self.driver.find_element(By.XPATH, INPUT_EMAIL)
        element.send_keys(LOGIN)

    def fill_password(self):
        element = self.driver.find_element(By.XPATH, INPUT_PASSWORD)
        element.send_keys(PASSWORD)

    def press_button_submit(self):
        element = self.driver.find_element(By.XPATH, BUTTON_SUBMIT)
        element.click()



    def gravatar_presence(self):
        try:
            self.driver.find_element(By.XPATH, GRAVATAR)
        except NoSuchElementException:
            return False
        return True


