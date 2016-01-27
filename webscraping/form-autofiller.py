import pyautogui, time

pyautogui.PAUSE = 3
pyautogui.FAILSAFE = True

x, y = (2303, 517)
pyautogui.moveTo(x,y)
pyautogui.click()
time.sleep(5)
