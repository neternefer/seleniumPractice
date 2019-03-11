from selenium import webdriver
import time
driver = webdriver.Chrome('./chromedriver')
driver.get('http://localhost:8000/33.html')
driver.execute_script('document.body.style.zoom = "1.5"')
time.sleep(2)
driver.find_element_by_css_selector('button').click()
time.sleep(1)
driver.switch_to_alert().accept()
time.sleep(1)
driver.close()
