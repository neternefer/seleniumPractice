import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPythonOrg(unittest.TestCase):

    def setUp(self):
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=chrome_options)
        

    def test_TC001_py3_doc_button(self):
        self.driver.get('https://www.python.org/')
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'documentation')))
        #doc = self.driver.find_element_by_xpath('//*[@href="/doc/"]')
        ActionChains(self.driver).move_to_element(element).perform()
        locator = 'Python 3.x Docs'
        py3docbutton = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, locator)))
        assert py3docbutton.text == locator
        py3docbutton.click()
        assert self.driver.current_url == 'https://docs.python.org/3/'
        

    def test_TC002_search_blabla(self):
        self.driver.get('https://www.python.org/')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'id-search-field'))).send_keys('blablabla')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'submit'))).click()
        result = self.driver.find_element_by_xpath('//h3[text()="Results"]/following-sibling::ul')
        assert "No results found." in result.get_attribute('innerHTML')

    def test_TC003_up_events(self):
        self.driver.get('https://www.python.org/about')
        xpath_locator = '//*[text()="Upcoming Events"]'
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath_locator)))
        assert element.text == "Upcoming Events"
        
    def TearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
