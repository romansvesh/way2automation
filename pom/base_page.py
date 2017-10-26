# -*- coding: utf-8 -*-

import pickle
import os
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from constants import constants


class BasePage:
    def __init__(self, driver):
        self._driver = driver

    def wait_for_element(self, locator):
        """This wait the element"""
        wait = WebDriverWait(self._driver, 5)
        wait.until(EC.element_to_be_clickable((By.XPATH, locator)))

    def save_cookie(self):
        """This save cookies into file"""
        os.makedirs(constants.COOKIES_FOLDER, exist_ok=True)
        with open(constants.COOKIES_FILE_NAME, 'wb') as f:
            pickle.dump(self._driver.get_cookies(), f)

    def login_with_cookie(self):
        """This login with cookies from file"""
        with open(constants.COOKIES_FILE_NAME, 'rb') as f:
            cookies = pickle.load(f)
        for cookie in cookies:
            self._driver.add_cookie(cookie)
        self._driver.refresh()

    @staticmethod
    def is_cookie_file_exist():
        return Path(constants.COOKIES_FILE_NAME).exists()
