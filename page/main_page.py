# -*- coding: utf-8 -*-

from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.common.by import By

from helper.helper import Helper


class MainPage:

    def __init__(self, driver):
        self._driver = driver

    # Locators Before SignIn
    BUTTON_LOGIN = (By.XPATH, '//a[contains(@href,"sign_in")]')

    # Locators After SignIn
    GRAVATAR = (By.CLASS_NAME, 'gravatar')

    def press_button_sign_in(self):
        element = self._driver.find_element(*self.BUTTON_LOGIN)
        element.click()

    def gravatar_presence(self):
        help_ = Helper(self._driver)
        help_.wait_for_element(5, self.GRAVATAR)
        return visibility_of_element_located((self.GRAVATAR[0], self.GRAVATAR[1]))
