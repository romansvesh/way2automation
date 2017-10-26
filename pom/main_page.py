# -*- coding: utf-8 -*-

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pom.base_page import BasePage


class MainPage(BasePage):
    # Locators
    BUTTON_LOGIN = '//header//*[contains(@href,"sign_in")]'  # Before SignIn
    GRAVATAR = '//*[@id="navbar"]//*[@class="gravatar"]//parent::*'  # After SignIn

    def press_button_sign_in(self):
        element = self._driver.find_element(By.XPATH, self.BUTTON_LOGIN)
        element.click()

    def gravatar_presence(self):
        try:
            self._driver.find_element(By.XPATH, self.GRAVATAR)
        except NoSuchElementException:
            return False
        return True
