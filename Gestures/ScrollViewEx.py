import time
from Basic.LaunchApp import driver, wait
from appium.webdriver.common.appiumby import AppiumBy

ScrollViewButton = wait.until(lambda x: x.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/ScrollView'))
ScrollViewButton.click()

#How to define Scroll Function


Button12 = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                               'new UiScrollable(new UiSelector()).scrollIntoView(text("BUTTON12"))'))
Button12.click()
AlertPopUp_Yes = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]')
AlertPopUp_Yes.click()

time.sleep(2)
driver.quit()
