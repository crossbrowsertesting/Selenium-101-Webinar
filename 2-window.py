from selenium import webdriver
import time

# Create the webdriver instance
# run test locally against chrome
driver = webdriver.Chrome("./webdrivers/chromedriver")


# run test in CrossBrowserTesting:
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
driver.get("https://example.com")
driver.get("https://card-layout.glitch.me/")

# browser nav actions
driver.back()
time.sleep(1)
driver.forward()
time.sleep(1)
driver.refresh()
time.sleep(1)

print "setting size + pos"
driver.set_window_size(325, 900)
time.sleep(1)

driver.set_window_size(768, 800)
time.sleep(1)

driver.set_window_size(1024, 800)
time.sleep(1)

for i in range(325, 1300, 50):
    driver.set_window_size(i, 800)

time.sleep(2)

driver.quit()

