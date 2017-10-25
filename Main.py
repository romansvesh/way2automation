# -*- coding: utf-8 -*-

import unittest
from PageObject import *
from selenium import webdriver


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('lib\chromedriver.exe')
        self.driver.get("http://courses.way2automation.com/")

    def test_login(self):
        main_page = MainPage(self.driver)
        main_page.log_in()

        self.assertTrue(main_page.gravatar_presence())

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
