from appium import webdriver

from appium.options.android import UiAutomator2Options
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.support.wait import WebDriverWait

"""
Part 1:
Create a Dictionary variable "desired_caps = {}" and assign Appium Desired Capabilities to it,
in the form of Key and value pair.
"""

desired_caps = {}  #Dictionary Variable and assigning all Desired Capabilities to it
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

# Part 2 Creating reusable objects:
# "Options and Webdriver object"
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=options, direct_connection=True)

# Creating webdriver wait object
wait = WebDriverWait(driver, 10, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

#Creating actions object for ex. long click
action = ActionChains(driver)

#Creating advanced_actions for ex. move to location method
advanced_actions = ActionBuilder(driver)

actions = TouchAction(driver)

# Step 3 "Action on the App"
#ele_id = driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/EnterValue")

#ele_id.click()
