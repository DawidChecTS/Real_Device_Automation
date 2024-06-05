import time
from appium.webdriver.common.appiumby import AppiumBy
from Basic.LaunchApp import driver


ele_content = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Btn5"]')
# - By using Xpath and Content Description
ele_resource_id = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.code2lead.kwad:id/Zoom"]')
# - By using Xpath and Resource-id
ele_text = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="ZOOM"]')
# - By using Xpath and text value
ele_xpath = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@index="3"]')
# - By using Xpath and index value
ele_xpath.click()

time.sleep(1)

ele_class = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText')
ele_class.send_keys("Testing this Class xpath.")

time.sleep(2)

driver.quit()
