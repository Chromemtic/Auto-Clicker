import pyautogui
import time

print("Auto clicker starting in 5 seconds")
print("Move your mouse over the target area now.")
time.sleep(5)

print("Clicking started slam mouse into a screen corner to stop")

# this makes the mouse click
while True:
    pyautogui.click()
    time.sleep(0.001)