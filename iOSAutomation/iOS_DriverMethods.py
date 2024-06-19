from Basic.LaunchApp import driver

#Different Driver Methods printing out on iOS
element = driver.find_element_by_accessibility_id("AAPLDatePickerController") # Accessibility ID

print("Current Context :", driver.current_context)
print("Current Orientation:", driver.orientation)
print("Check Whether device is locked or not :", driver.is_locked())

