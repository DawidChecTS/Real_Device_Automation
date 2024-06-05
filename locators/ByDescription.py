import time

from appium import webdriver

from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options


desired_caps = {} #Dictionary Variable and assigning all Desired Capabilities to it
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '14'
desired_caps['deviceName'] = 'SM S921B'
desired_caps['app'] = 'C:/Users/Dawid.Chec/Downloads/Android_Demo_App.apk'
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=options,direct_connection=True)


ele_desc = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().description("Btn3")')
ele_desc.click()

time.sleep(2)

driver.quit()