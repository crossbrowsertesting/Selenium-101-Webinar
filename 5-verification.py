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
password.send_keys('test123')
login.click()

try:
    # selenium needs to wait for the login to finish before checking
    logged_in_message = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.ID, "logged-in")))

    header = driver.find_element_by_tag_name('h2')

    # check the angular class is set
    assert header.get_attribute('class') == 'ng-binding'

    # make sure the element isn't hidden
    assert header.is_displayed()

    # verify the text is what we expect
    assert logged_in_message.text == "You are now logged in!"

    print "PASS: successfully logged in!"

except AssertionError:
    print "FAIL: did not log in!"

raw_input()

driver.quit()



