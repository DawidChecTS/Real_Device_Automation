import time
from Basic.LaunchApp import driver
from appium.webdriver.common.appiumby import AppiumBy

EnterSomeValue = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Btn1"]')
EnterSomeValue.click()

time.sleep(2)

EnterSomeValueTextField = driver.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/Et1')


print("Text on the button :", EnterSomeValueTextField.text)
print("Text on the button :", EnterSomeValueTextField.get_attribute("resource-id"))
print("Element ID on the button: ", EnterSomeValueTextField.get_attribute("class"))
EnterSomeValueTextField.send_keys("Text to delete.")

EnterSomeValueTextField.click()

driver.press_keycode(67)
driver.press_keycode(67)

time.sleep(1)

EnterSomeValueTextField.clear()

time.sleep(2)
driver.quit()
