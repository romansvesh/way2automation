# -*- coding: utf-8 -*-

import pickle
from pathlib import Path
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Variables import *
from Locators import *


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
    def press_button_sign_in(self):
        element = self.driver.find_element(By.XPATH, BUTTON_LOGIN)
        element.click()

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

    def log_in(self):
        if not Path(COOKIES_FILE_NAME).exists():
            self.press_button_sign_in()
            self.fill_email()
            self.fill_password()
            self.press_button_submit()
            self.wait_for_element(GRAVATAR)
            self.save_cookies(COOKIES_FILE_NAME)
        else:
            self.login_with_cookies(COOKIES_FILE_NAME)

    def gravatar_presence(self):
        try:
            self.driver.find_element(By.XPATH, GRAVATAR)
        except NoSuchElementException:
            return False
        return True
