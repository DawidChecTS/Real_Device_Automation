import time
from appium.webdriver.common.appiumby import AppiumBy
from Basic.LaunchApp import driver

element = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")

for x in element:
    print(x.text)

time.sleep(2)

for x in element:
    button = x.text
    if button == "ScrollView":
        x.click()
        break

time.sleep(2)

driver.quit()