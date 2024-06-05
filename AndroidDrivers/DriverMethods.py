from Basic.LaunchApp import driver

print("Check if device is locked or not :", driver.is_locked())
print("Current Package :", driver.current_package)
print("Current Activity :", driver.current_activity)
print("Current Context :", driver.current_context)
print("Current Orientation :", driver.orientation)
