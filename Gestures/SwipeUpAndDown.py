import time

from appium.webdriver.common.appiumby import AppiumBy
from Basic.LaunchApp import actions, action

from Basic.LaunchApp import driver, wait

#wait until Tab Activity button is displayed
ScrollView = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                  'new UiScrollable(new UiSelector()).scrollIntoView(text("ScrollView"))'))
ScrollView.click()

scrolldown = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                 'new UiScrollable(new UiSelector()).scrollIntoView(text("ScrollView"))'))


#scrolling down with screen parameters
driver.swipe(550, 2200, 550, 260, 1000)
time.sleep(1)

#scrolling up with screen parameters
driver.swipe(550, 260,550, 2200, 1000)

time.sleep(2)
driver.quit()

