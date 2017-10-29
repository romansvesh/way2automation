# -*- coding: utf-8 -*-

import pickle
import os
from pathlib import Path

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants.constants import COOKIES_FILE_NAME, COOKIES_FOLDER


class Helper:
    def __init__(self, driver):
        self._driver = driver

    def save_cookie(self):
        os.makedirs(COOKIES_FOLDER, exist_ok=True)
        with open(COOKIES_FILE_NAME, 'wb') as f:
            pickle.dump(self._driver.get_cookies(), f)

    def login_with_cookie(self):
        with open(COOKIES_FILE_NAME, 'rb') as f:
            cookies = pickle.load(f)
        for cookie in cookies:
            self._driver.add_cookie(cookie)
        self._driver.refresh()

    @staticmethod
    def is_cookie_file_exist():
        return Path(COOKIES_FILE_NAME).exists()

    def wait_for_element(self, time, locator):
        wait = WebDriverWait(self._driver, time)
        wait.until(expected_conditions.element_to_be_clickable((locator[0], locator[1])))

    def login(self):
        from page import main_page, sign_in_page
        main = main_page.MainPage(self._driver)
        sign_in = sign_in_page.SignInPage(self._driver)
        if self.is_cookie_file_exist():
            self.login_with_cookie()
        else:
            main.press_button_sign_in()
            sign_in.fill_email()
            sign_in.fill_password()
            sign_in.press_button_submit()
            self.save_cookie()
