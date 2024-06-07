from appium.webdriver.common.appiumby import AppiumBy

from Basic.LaunchApp import driver


EnterSomeValue = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")

print("Is Displayed :", EnterSomeValue.is_displayed())
print("Is Enabled :", EnterSomeValue.is_enabled())
print("Is selected :", EnterSomeValue.is_selected())
print("Size :", EnterSomeValue.size)
print("Location :", EnterSomeValue.location)

driver.quit()