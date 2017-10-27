# -*- coding: utf-8 -*-

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from helper.helper import Helper


class MainPage(Helper):
    # Locators
    BUTTON_LOGIN = (By.XPATH, '//a[contains(@href,"sign_in")]')  # Before SignIn
    GRAVATAR = (By.CLASS_NAME, 'gravatar')  # After SignIn

    def press_button_sign_in(self):
        element = self._driver.find_element(*self.BUTTON_LOGIN)
        element.click()

    def gravatar_presence(self):
        try:
            self._driver.find_element(*self.GRAVATAR)
        except NoSuchElementException:
            return False
        return True
