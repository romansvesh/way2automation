# -*- coding: utf-8 -*-

import unittest

from selenium import webdriver

from helper.helper import Helper
from page.main_page import MainPage


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('lib\chromedriver.exe')
        self.driver.get("http://courses.way2automation.com/")
        self.driver.maximize_window()

    def test_login(self):
        help_ = Helper(self.driver)
        main = MainPage(self.driver)

        help_.login()

        self.assertTrue(main.gravatar_presence())

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
