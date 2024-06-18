from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'IOS'
desired_caps['platformVersion'] = '13.2'
desired_caps['deviceName'] = 'iPhone 11 Pro'
desired_caps['automationName'] = 'XCUITest'
desired_caps['app'] = ('')


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

#Example of finding elements by different values/id's/names
ele = driver.find_element_by_accessibility_id("AAPLDatePickerController") # Accessibility ID
ele = driver.find_element_by_id("AAPLDatePickerController") # name
ele = driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="AAPLDatePickerController"]') # Xpath - name
ele = driver.find_element_by_xpath('//XCUIElementTypeStaticText[@value="AAPLDatePickerController"]') # Xpath - value
ele = driver.find_element_by_xpath('//XCUIElementTypeStaticText[@label="AAPLDatePickerController"]') # Xpath - Label

