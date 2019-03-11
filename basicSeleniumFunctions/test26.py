from selenium import webdriver
import time
driver = webdriver.Chrome('./chromedriver')
driver.get('http://localhost:8000/26.html')
el = driver.find_element_by_xpath(
    '//*[text()="Apple"]/preceding-sibling::td/input')
el.click()
time.sleep(3)
driver.quit()
