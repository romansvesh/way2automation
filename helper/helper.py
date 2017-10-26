# -*- coding: utf-8 -*-

import pickle
import os
from pathlib import Path
from constants import constants


class Helper:
    def __init__(self, driver):
        self._driver = driver

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
