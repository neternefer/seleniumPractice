from selenium import webdriver
import time
driver = webdriver.Chrome('./chromedriver')
driver.get('http://localhost:8000/32.html')
driver.save_screenshot('src32_1.png')
driver.get_screenshot_as_file('src32_2.png')
driver.close()
