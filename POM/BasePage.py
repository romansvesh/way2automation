# -*- coding: utf-8 -*-

import pickle

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def wait_for_element(self, locator):
        """This wait the element"""
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))

    def save_cookies(self, name):
        """This save cookies into file"""
        with open(name, 'wb') as f:
            pickle.dump(self.driver.get_cookies(), f)

    def login_with_cookies(self, cookies_file):
        """This login with cookies from file"""
        with open(cookies_file, 'rb') as f:
            cookies = pickle.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()


class MainPage(BasePage):
    # Locators
    BUTTON_LOGIN = '//header//*[contains(@href,"sign_in")]'  # Before SignIn
    GRAVATAR = '//*[@id="navbar"]//*[@class="gravatar"]//parent::*'  # After SignIn

    def press_button_sign_in(self):
        element = self.driver.find_element(By.XPATH, BUTTON_LOGIN)
        element.click()

    def gravatar_presence(self):
        try:
            self.driver.find_element(By.XPATH, GRAVATAR)
        except NoSuchElementException:
            return False
        return True
