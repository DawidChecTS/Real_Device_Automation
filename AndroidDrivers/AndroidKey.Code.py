import time

from appium.webdriver.common.appiumby import AppiumBy

from Basic.LaunchApp import driver


EnterSomeValue = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
EnterSomeValue.click()

EnterSomeValueTextField = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText['
                                                              '@resource-id="com.code2lead.kwad:id/Et1"]')
EnterSomeValueTextField.send_keys("Test Scouts.")
EnterSomeValueTextField.click()

driver.press_keycode(67)
driver.press_keycode(67)

driver.press_keycode(4)
driver.press_keycode(4)

time.sleep(2)
driver.quit()