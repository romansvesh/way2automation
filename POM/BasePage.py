# -*- coding: utf-8 -*-

import pickle

from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Constants.Constants import COOKIES_FILE_NAME


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        """This wait the element"""
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.element_to_be_clickable((By.XPATH, locator)))

    def save_cookie(self, name):
        """This save cookies into file"""
        with open(name, 'wb') as f:
            pickle.dump(self.driver.get_cookies(), f)

    def login_with_cookie(self, cookies_file):
        """This login with cookies from file"""
        with open(cookies_file, 'rb') as f:
            cookies = pickle.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    @staticmethod
    def is_cookie_file_exist(file):
        return Path(file).exists()
