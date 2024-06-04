from appium import webdriver
import time

from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

#Step 1 : Create "Desired Capabilities"
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '14'
desired_caps['deviceName'] = 'SM S921B'
desired_caps['app'] = 'C:/Users/Dawid.Chec/Downloads/Android_Demo_App.apk'
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=options,direct_connection=True)

ele_id = driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/EnterValue")

ele_id.click()