import pyautogui
from time import sleep

def abri_servico():
    pyautogui.moveTo(1887,60)
    pyautogui.click()
    pyautogui.moveTo(1780,122)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.moveTo(1166,177)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.write("SERVICO INTERNO")

#ocorrencia
def ocorrencia():
    pyautogui.moveTo(1825,424)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.moveTo(1028,123)
    pyautogui.click()
    pyautogui.write("0027")
    pyautogui.moveTo(1893,123)
    pyautogui.click()
    pyautogui.moveTo(928,191)
    pyautogui.sleep(0.5)
    pyautogui.click()

#causa
def causa():
    pyautogui.moveTo(1823,597)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.moveTo(947,125)
    pyautogui.click()
    pyautogui.write("0027")
    pyautogui.moveTo(1892,124)
    pyautogui.click()
    pyautogui.moveTo(881,198)
    pyautogui.sleep(0.5)
    pyautogui.click()

#seviço
def servico():
    pyautogui.moveTo(1825,687)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.moveTo(881,124)
    pyautogui.click()
    pyautogui.write("0024")
    pyautogui.moveTo(1891,120)
    pyautogui.click()
    pyautogui.moveTo(888,186)
    pyautogui.sleep(0.5)
    pyautogui.click()

#sair
def sair():
    pyautogui.moveTo(29,18)
    pyautogui.click()
    pyautogui.sleep(0.7)
    pyautogui.moveTo(25,15)
    pyautogui.click()
    pyautogui.sleep(2)
    pyautogui.moveTo(1886,61)
    pyautogui.click()
    pyautogui.moveTo(1686,201)
    pyautogui.click()
    
def run():
    abri_servico()
    ocorrencia()
    pyautogui.sleep(0.3)
    causa()
    pyautogui.sleep(0.3)
    servico()
    pyautogui.sleep(0.6)
    sair()
    
run()
    