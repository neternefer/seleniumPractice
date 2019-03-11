from selenium import webdriver
import time
#Headless browser
#There are 3 ways for setting webdriver to headless mode:

#CHROME & FIREFOX share the interface
'''
opts = webdriver.ChromeOptions()
#1. SET_HEADLESS() -> DEPRECATED
opts.set_headless()
#2. HEADLESS = TRUE -> SETTER
opts.headless = True
#3. ADD_ARGUMENT('HEADLESS')
opts.add_argument('--headless')
driver = webdriver.Chrome(options=opts)

opts = webdriver.FirefoxOptions()
opts.headless = True
driver = webdriver.Firefox(options=opts)
'''
#GRID
#create hub and nodes by using java server jar
#-role hub -timeout 30 (30 seconds until resource is released
#-role node -hub 'address' -timeout 30 maxSessions 5
#five simultanious sessions available for each driver
#opts = webdriver.FirefoxOptions()
opts = webdriver.ChromeOptions()
opts.headless = True
driver = webdriver.Remote(command_executor:'http://192.168.1.11:4444/wd/hub',
                          desired_capabilities = opts.to_capabilities())
#--------------------


