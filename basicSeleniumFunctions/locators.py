from selenium.webdriver.common.by import By

class LoginLocators:
    Username = (By.CSS_SELECTOR, '#username')
    Password = (By.CSS_SELECTOR, '#password')
    Submit = (By.NAME, 'submit')
    
    CreateAccount = (By.LINK_TEXT, 'Create an account')
    Message = (By.CSS_SELECTOR, '#auth-message')

class CreateLocators:
    Header = (By.CSS_SELECTOR, '#header')
    
