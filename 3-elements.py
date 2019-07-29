from selenium import webdriver
import time

# Create the webdriver instance
# run test locally against chrome
driver = webdriver.Chrome("./webdrivers/chromedriver")


# run test in CBT:
# driver = webdriver.Remote(
#         command_executor = "https://hub.crossbrowsertesting.com/wd/hub",
#         desired_capabilities = { "browser": "chrome",
#                                  "version": "latest",
#                                  "platform": "windows",
#                                  # "deviceName": "Pixel 3",
#                                  "username": "johnreese.vt@gmail.com",
#                                  "password": "u0af4e32dc4fb29d",
#                                  "recordVideo": True})

# navigate
driver.get("http://crossbrowsertesting.github.io/login-form.html")

# find the search box
# ...using xpath
username = driver.find_element_by_xpath('/html/body/div/div/div/div/form/div[1]/input')
password = driver.find_element_by_xpath('/html/body/div/div/div/div/form/div[2]/input')
login    = driver.find_element_by_xpath('/html/body/div/div/div/div/form/div[3]/button')

# ...using css selectors
(username, password) = driver.find_elements_by_css_selector('[name="login-form"] input')
login = driver.find_element_by_css_selector('[name="login-form"] button')

# ...or using ids
username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')
login = driver.find_element_by_id('submit')


username.send_keys('tester@crossbrowsertesting.com')
password.send_keys('test123')
login.click()

raw_input('press enter to quit')

driver.quit()



