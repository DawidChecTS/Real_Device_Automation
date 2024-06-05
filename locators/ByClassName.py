import time
from appium.webdriver.common.appiumby import AppiumBy
from Basic.LaunchApp import driver


ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
ele_id.click()

time.sleep(2)

ele_classname = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
ele_classname.send_keys("Test")

time.sleep(2)

driver.quit()
