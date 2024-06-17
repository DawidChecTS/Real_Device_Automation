import time

from appium.webdriver.common.appiumby import AppiumBy
from Basic.LaunchApp import actions, action

from Basic.LaunchApp import driver, wait

#wait until Tab Activity button is displayed
TabActivity = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                  'new UiScrollable(new UiSelector()).scrollIntoView(text("TAB ACTIVITY"))'))
TabActivity.click()

#Swiping from home to sport
hometab = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("HomeFragment")'))
driver.execute_script("mobile: swipeGesture", {'elementId': hometab, 'direction': 'left', "percent": 0.98})

#Swiping from Sport to Movie tab
sporttab = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("SportFragment")'))

driver.execute_script("mobile: swipeGesture", {'elementId': sporttab, 'direction': 'left', "percent": 0.98})

#Swiping from Movie to Sport tab
movietab = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("MovieFragment")'))

driver.execute_script("mobile: swipeGesture", {'elementId': movietab, 'direction': 'right', "percent": 0.98})

#swiping from Sport to Home tab
driver.execute_script("mobile: swipeGesture", {'elementId': sporttab, 'direction': 'right', "percent": 0.98})

time.sleep(3)
driver.quit()
