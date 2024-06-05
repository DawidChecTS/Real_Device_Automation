import time

from appium.webdriver.common.appiumby import AppiumBy

from Basic.LaunchApp import desired_caps, wait, driver
from appium.options.android import UiAutomator2Options


options = UiAutomator2Options().load_capabilities(desired_caps)


ele = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue"))
ele.click()

ele = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText"))
ele.send_keys("Just Another Test.")

time.sleep(2)

driver.quit()