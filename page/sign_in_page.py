# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from constants.constants import LOGIN, PASSWORD
from helper.helper import Helper
from selenium.webdriver.support import expected_conditions


class SignInPage(Helper):
    # Locators
    INPUT_EMAIL = 'user_email'
    INPUT_PASSWORD = 'user_password'
    BUTTON_SUBMIT = '//*[@type="submit"]'

    def fill_email(self):
        wait = WebDriverWait(self._driver, 5)
        wait.until(expected_conditions.element_to_be_clickable((By.ID, self.INPUT_EMAIL)))
        element = self._driver.find_element_by_id(self.INPUT_EMAIL)
        element.send_keys(LOGIN)

    def fill_password(self):
        element = self._driver.find_element_by_id(self.INPUT_PASSWORD)
        element.send_keys(PASSWORD)

    def press_button_submit(self):
        element = self._driver.find_element_by_xpath(self.BUTTON_SUBMIT)
        element.click()

    def login(self):
        self.fill_email()
        self.fill_password()
        self.press_button_submit()
