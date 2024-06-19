from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'IOS'
desired_caps['platformVersion'] = '13.2'
desired_caps['deviceName'] = 'iPhone 11 Pro'
desired_caps['automationName'] = 'XCUITest'
desired_caps['app'] = ('')

#finding and printing out elements properties
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

ele = driver.find_element_by_accessibility_id("AAPLDatePickerController") # Accessibility ID

print("Is Displayed :", ele.is_displayed())
print("Is Enabled :", ele.is_enabled())
print("Is Selected :", ele.is_selected())
print("Size :", ele.size)
print("Location :", ele.location)