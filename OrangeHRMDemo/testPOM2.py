import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pagePOM import HomePage, AboutPage
from locatorsPOM import CommonPageLocators, AboutPageLocators

class TestPyOrgBase(unittest.TestCase):

    def setUp(self):
        #intro settings fo all kinds of pages
        #driver set up
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=chrome_options)
    
    def tearDown(self):
        self.driver.close()

class TestHome(TestPyOrgBase):
    
    def setUp(self):
        
        #use parent class setUp func
        super().setUp()
        #create instance of child class(Home)
        #constructor takes driver as arg -> usual init method for POM
        
        self.home = HomePage(self.driver)
        
    @unittest.skip('demonstrating skipping tests')
    def test_TC001_py3_doc_button(self):
        self.home.hover_over(CommonPageLocators.DOC)
        self.home.assert_elem_text(CommonPageLocators.PY3_DOC_BUTTON, 'Python 3.x Docs')
        self.home.click(CommonPageLocators.PY3_DOC_BUTTON)
        assert self.driver.current_url == 'https://docs.python.org/3/'

    def test_TC002_search_blabla(self):
        self.home.search_for('blabla')
        self.home.assert_elem_text(CommonPageLocators.SEARCH_RESULT_LIST, "No results found.")

    def test_TC004_assert_title(self):
        self.assertEqual(self.home.driver.title, 'Welcome to Python.org')

class TestAbout(TestPyOrgBase):

    def setUp(self):
        super().setUp()
        self.about = AboutPage(self.driver)
        
    def test_TC003_up_events(self):
        self.about.assert_elem_text(AboutPageLocators.UPCOMING_EVENTS, "Upcoming Events")

    def test_TC005_assert_url_contains(self):
        self.assertIn('about', self.about.driver.current_url)
    

if __name__ == '__main__':
    unittest.main()

