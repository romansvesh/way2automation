# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

from constants.constants import LOGIN, PASSWORD
from helper.helper import Helper


class SignInPage:

    def __init__(self, driver):
        self._driver = driver

    # Locators
    INPUT_EMAIL = (By.ID, 'user_email')
    INPUT_PASSWORD = (By.ID, 'user_password')
    BUTTON_SUBMIT = (By.XPATH, '//*[@type="submit"]')

    def fill_email(self):
        help_ = Helper(self._driver)
        help_.wait_for_element(5, self.INPUT_EMAIL)
        element = self._driver.find_element(*self.INPUT_EMAIL)
        element.send_keys(LOGIN)

    def fill_password(self):
        element = self._driver.find_element(*self.INPUT_PASSWORD)
        element.send_keys(PASSWORD)

    def press_button_submit(self):
        element = self._driver.find_element(*self.BUTTON_SUBMIT)
        element.click()


