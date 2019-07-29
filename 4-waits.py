from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create the webdriver instance
# run test locally against chrome
driver = webdriver.Chrome("./webdrivers/chromedriver")

# navigate
driver.get("http://crossbrowsertesting.github.io/login-form.html")

# find the search box
username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')
login = driver.find_element_by_id('submit')

username.send_keys('tester@crossbrowsertesting.com')
password.send_keys('test1234')
login.click()

# selenium needs to wait for the login to finish before checking
# for the logged in message

# We can set the implicit_wait timeout (default: 0)
# driver.implicitly_wait(10)
# logged_in_message = driver.find_element_by_id('logged-in')


# ... or use an explicit wait
logged_in_message = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.ID, "logged-in")))

print logged_in_message.text

raw_input('press enter to quit')

driver.quit()


