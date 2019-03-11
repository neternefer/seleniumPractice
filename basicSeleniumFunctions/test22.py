from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')
driver.get('localhost:8000')

i = driver.find_element_by_xpath(//img[@class='frame']/following-sibling: : img)
j = driver.find_element_by_xpath(//img[@src='yoda.jpg'])
