import time

from appium.webdriver.common.appiumby import AppiumBy
from Basic.LaunchApp import actions, action

from Basic.LaunchApp import driver, wait

#wait until Grag and drop button is displayed
Drag_and_drop_button = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                    'new UiScrollable(new UiSelector()).scrollIntoView(text("DRAGANDDROP"))'))
Drag_and_drop_button.click()

#wait until element to drag is displayed
element_to_drag = wait.until(lambda x: x.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/ingvw'))

#wait until field for element to be dragged on is displayed
place_to_release = wait.until(lambda x: x.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/layout2'))

#actions.long_press(element_to_drag).move_to(place_to_release).release().perform

action.drag_and_drop(element_to_drag, place_to_release).perform()

time.sleep(4)
driver.quit()