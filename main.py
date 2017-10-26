# -*- coding: utf-8 -*-

import unittest
from pom import base_page, main_page, sign_in_page
from selenium import webdriver


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('lib\chromedriver.exe')
        self.driver.get("http://courses.way2automation.com/")
        self.driver.maximize_window()

    def test_login(self):
        base = base_page.BasePage(self.driver)
        main = main_page.MainPage(self.driver)
        sign_in = sign_in_page.SignInPage(self.driver)

        if base.is_cookie_file_exist():
            main.login_with_cookie()
        else:
            main.press_button_sign_in()
            sign_in.login()
            base.save_cookie()

        self.assertTrue(main.gravatar_presence())

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
