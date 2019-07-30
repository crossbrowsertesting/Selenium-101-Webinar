from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from os import getcwd

# Create the webdriver instance
# instead of running against chrome, we're gonna run on CrossBrowserTesting

user = "johnreese.vt@gmail.com"
auth = "u0af4e32dc4fb29d"

driver = webdriver.Remote(
        desired_capabilities={"browserName": "chrome", "platform": "windows 10"}
        command_executor="https://{}:{}@hub.crossbrowsertesting.com/wd/hub".format(user,auth) )

# navigate
driver.get("http://crossbrowsertesting.github.io/login-form.html")

# find the search box
username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')
login = driver.find_element_by_id('submit')

username.send_keys('not-a-user@crossbrowsertesting.com')
password.send_keys('not-the-password')
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
except Exception:
    print "FAIL: did not log in!"

    screenshot_fpath = getcwd() + '/on-error.png'
    driver.get_screenshot_as_file(screenshot_fpath)

    print ('saved screenshot to ' + screenshot_fpath)

driver.quit()

