from appium import webdriver
import time

from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options


"""
Part 1:
Create a Dictionary variable "desired_caps = {}" and assign Appium Desired Capabilities to it,
in the form of Key and value pair.
"""

desired_caps = {} #Dictionary Variable and assigning all Desired Capabilities to it
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '14'
desired_caps['deviceName'] = 'SM S921B'
desired_caps['app'] = 'C:/Users/Dawid.Chec/Downloads/Android_Demo_App.apk'
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'


"""
Part 2:
Create the object for WebDriver class "driver" to access all the methods in WebDriver class and pass the localhost
and Port number in the form of url to connect to the server and "desired_caps" dictionary variable. 
"""

# Part 2 "Options and Webdriver object"
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=options,direct_connection=True)

# Step 3 "Action on the App"
#ele_id = driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/EnterValue")

#ele_id.click()


