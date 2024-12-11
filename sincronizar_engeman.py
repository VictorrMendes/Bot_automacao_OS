import pyautogui
import time


def sincronizar():
    pyautogui.moveTo(706,746)
    pyautogui.click()
    pyautogui.sleep(0.7)
    pyautogui.moveTo(408,437)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.moveTo(408,437)
    pyautogui.click()

sincronizar()