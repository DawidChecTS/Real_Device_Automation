from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'IOS'
desired_caps['platformVersion'] = '13.2'
desired_caps['deviceName'] = 'iPhone 11 Pro'
desired_caps['automationName'] = 'XCUITest'
desired_caps['app'] = ('')

#Example of how an iOS application could be launched
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


