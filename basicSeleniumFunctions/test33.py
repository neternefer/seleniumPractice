from selenium import webdriver
import time
driver = webdriver.Chrome('./chromedriver')

driver.get('http://python.org')
driver.maximize_window()
time.sleep(2)
driver.find_element_by_css_selector('a[title="Python Package Index"]').click()
time.sleep(3)
driver.back()
time.sleep(2)
driver.close()
