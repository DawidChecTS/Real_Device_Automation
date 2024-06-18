'''
1. Mobile Browser version and ChromeDriver or respective Browser Driver should be in same version.
2.
Two Ways of Identifying locators on webview
i) open chrome browser and type "chrome://inspect/devices"
ii) user Browser inspectors

#UNKNOWN ERROR, WILL DROP THE TOPPIC FOR NOW.
'''
import time

#from Basic.LaunchApp import desired_hybrid_caps, webdriver
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from Basic.LaunchApp import wait, hybrid_driver

#1. Create the Driver object

#2. Create WebDriverWait

#3. Get the list of Contexts in App

Continue_as_Dawid_button = wait.until(lambda x: x.find_element(AppiumBy.ID,
                                                               'com.android.chrome:id/signin_fre_dismiss_button'))
Continue_as_Dawid_button.click()

#4. Switch to webview to perform action on Required URL or on WebView

#5. Do testing on Webview screen in chrome browser or any if we want

#6. Swithc back to native view to perform action








time.sleep(2)
hybrid_driver.quit()