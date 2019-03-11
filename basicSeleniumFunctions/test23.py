from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('./chromedriver')
driver.get('http://localhost:8000/23.html')
bike = driver.find_element_by_css_selector('body > form:nth-child(1) > input[type="checkbox"]:nth-child(1)')
bike.click()
if bike.get_attribute('checked'):
    print("Bike is checked")

dis_button = driver.find_element_by_css_selector('#disabled_button')
if dis_button.is_enabled():
    print("Enabled")
else:
    print("Not working")
first = driver.find_element_by_name('firstname')
first.clear()
first.send_keys("JarJar")
