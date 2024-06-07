import time

from appium.webdriver.common.appiumby import AppiumBy

from Basic.LaunchApp import driver,wait, action


Button12 = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                               'new UiScrollable(new UiSelector()).scrollIntoView(text("LONG CLICK"))'))
#calling on action object.long_press method + 2 arguments = Button object and time to preform meth
action.click_and_hold(Button12).perform()

time.sleep(4)

driver.quit()