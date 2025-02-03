import pyautogui
from time import sleep

pyautogui.moveTo(160,747)
pyautogui.click()
pyautogui.write("google")
pyautogui.sleep(0.5)
pyautogui.press('enter')
pyautogui.sleep(1)

pyautogui.hotkey('ctrl', 'shift', 't')
pyautogui.sleep(0.5)
pyautogui.hotkey('ctrl', 'shift', 't')