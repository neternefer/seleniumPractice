from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from pages.login import Login
import unittest

class LoginTestCase(unittest.TestCase):

    def test_userLogin(self):
        self.login = Login()
        user = 'registeredUser'
        password = '1234'
        self.login.login_as(user, password)
        
        welcome_message = self.login.auth_message()
        self.assertIn("Welcome back", welcome_message.text)
        self.login.quit()

    def test_loginFail(self):
        self.login = Login()
        user = 'otherUser'
        password = 'asdf'
        self.login.login_as(user, password)
        
        message = self.login.auth_message()
        self.assertIn("Account not found", message.text)
        
        sel.login.register_link()
        header = self.login.get_header()
        self.assertIn("Create an Account", header.text)

if __name__ == '__main__':
    unittest.main(verbosity=2)

