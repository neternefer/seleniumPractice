from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from locators import Login, Create
import time
import unittest

class LoginTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('./chromedriver')
        self.addCleanup(self.browser.quit)

    def test_userLogin(self):
        self.browser.get('http://localhost:8000')
        username = self.browser.find_element(*Login.Username)
        password = self.browser.find_element(*Login.Password)
        submit = self.browser.find_element(*Login.Submit)

        username.send_keys('registeredUser')
        password.send_keys('1234')
        submit.click()

        time.sleep(5)
        welcome_message = self.browser.find_element(*Login.Message)
        self.assertIn("Welcome back", welcome_message.text)

    def test_loginFail(self):
        self.browser.get('http://localhost:8000')
        username = self.browser.find_element(*Login.Username)
        password = self.browser.find_element(*Login.Password)
        submit = self.browser.find_element(*Login.Submit)

        username.send_keys('otherUser')
        password.send_keys('asdf')
        submit.click()

        time.sleep(5)
        message = self.browser.find_element(*Login.Message)
        self.assertIn("Account not found", message.text)
        
        create_account_link = self.browser.find_element(*Login.CreateAccount)
        create_account_link.click()

        time.sleep(5)
        header = self.browser.find_element(*Create.Header)
        self.assertIn("Create an Account", header.text)

if __name__ == '__main__':
    unittest.main(verbosity=2)
