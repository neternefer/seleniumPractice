from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome('./chromedriver')
'''
driver.get('http://localhost:8000/24_clickable_dropdown.html')
drop = driver.find_element_by_css_selector('div.dropdown > button')
drop.click()
menu = driver.find_element_by_css_selector('#myDropdown  a[href="#about"]')
menu.click()
'''
driver.get('http://localhost:8000/24_hoverable_dropdown.html')
area = driver.find_element_by_css_selector('.dropdown span')
#To find hoverable area, we need to control mouse
ActionChains(driver).move_to_element(area).perform()
menu = driver.find_element_by_css_selector('.dropdown-content p')
print(menu.text)
menu.click()
driver.quit()


