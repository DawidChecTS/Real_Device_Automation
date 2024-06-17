import time

from appium.webdriver.common.appiumby import AppiumBy

from Basic.LaunchApp import driver, wait

#Execute_script driver method - Selenium Python
# This method provides a simple API to write functional/acceptance tests using Selenium WebDriver
# This method synchronously Executes JavaScript in the current window/frame.

Drag_and_drop_button = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                    'new UiScrollable(new UiSelector()).scrollIntoView(text("DRAGANDDROP"))'))

driver.execute_script('mobile: clickGesture', {'x': 800, 'y': 1200})

time.sleep(4)
driver.quit()
