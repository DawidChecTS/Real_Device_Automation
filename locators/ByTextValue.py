import time
from appium.webdriver.common.appiumby import AppiumBy
from Basic.LaunchApp import driver


ele_text = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ENTER SOME VALUE")')
#ele_text = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'.text("ENTER SOME VALUE")')
ele_text.click()

time.sleep(2)

driver.quit()
