# -*- coding: utf-8 -*-

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Constants.Constants import LOGIN, PASSWORD
from POM.BasePage import BasePage


class SingInPage(BasePage):
    # Locators
    INPUT_EMAIL = '//*[@id="user_email"]'
    INPUT_PASSWORD = '//*[@id="user_password"]'
    BUTTON_SUBMIT = '//*[@type="submit"]'

    def fill_email(self, email):
        self.wait_for_element(email)
        element = self.driver.find_element(By.XPATH, email)
        element.send_keys(LOGIN)

    def fill_password(self, password):
        element = self.driver.find_element(By.XPATH, password)
        element.send_keys(PASSWORD)

    def press_button_submit(self, button):
        element = self.driver.find_element(By.XPATH, button)
        element.click()

    def login(self):
        self.fill_email(self.INPUT_EMAIL)
        self.fill_password(self.INPUT_PASSWORD)
        self.press_button_submit(self.BUTTON_SUBMIT)


