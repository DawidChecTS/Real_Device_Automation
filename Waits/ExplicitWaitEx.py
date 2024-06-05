import time

from appium.webdriver.common.appiumby import AppiumBy

from Basic.LaunchApp import wait, driver


ele = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue"))
ele.click()

ele = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText"))
ele.send_keys("Just Another Test.")

time.sleep(2)

#driver.quit()