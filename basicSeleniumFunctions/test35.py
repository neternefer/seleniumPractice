from selenium import webdriver
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver


class MyListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("Before navigate to: {}".format(url))

    def after_navigate_to(self, url, driver):
        print("After navigate to: {}".format(url))


driver = webdriver.Chrome('./chromedriver')
ef = EventFiringWebDriver(driver, MyListener())
ef.get('http://python.org')
driver.close()
