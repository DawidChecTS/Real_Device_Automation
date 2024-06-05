import time
from appium.webdriver.common.appiumby import AppiumBy
from Basic.LaunchApp import driver


ele_id = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(4)")
ele_id.click()

time.sleep(2)

driver.quit()