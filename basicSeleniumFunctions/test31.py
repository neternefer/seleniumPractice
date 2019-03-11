from selenium import webdriver
import time
driver = webdriver.Chrome('./chromedriver')
driver.get('http://localhost:8000/31.html')
driver.execute_script('document.body.style.zoom = "1.7"')
time.sleep(3)
driver.execute_script('document.getElementById("demo").innerHTML="JavaScript injection from Selenium";')
time.sleep(5)
driver.close()
