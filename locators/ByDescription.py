import time
from appium.webdriver.common.appiumby import AppiumBy
from Basic.LaunchApp import driver


ele_desc = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().description("Btn3")')
ele_desc.click()

time.sleep(2)

driver.quit()