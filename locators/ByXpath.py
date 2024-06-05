import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from Basic.LaunchApp import driver

ele_xp = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Btn5"]')
ele_xp.click()

time.sleep(2)
