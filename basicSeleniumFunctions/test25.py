from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome('./chromedriver')

driver.get('http://localhost:8000/25_radio_buttons.html')
buttons = driver.find_elements_by_css_selector('input')
for b in buttons:
    print('button {} \t checked: {}'.format(b.get_attribute('value'),b.get_attribute('checked')))
time.sleep(3)
#xpath('//*[text()=" Male"]//preceding-sibling::input')
element = driver.find_element_by_xpath('//*[text()=" Male"]//preceding-sibling::input')
element.click()
buttons = driver.find_elements_by_css_selector('input')
for b in buttons:
    print('button {} \t checked: {}'.format(b.get_attribute('value'),b.get_attribute('checked')))
time.sleep(3)
driver.quit()
