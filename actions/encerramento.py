import pyautogui
from time import sleep

def excel():
    pyautogui.moveTo(646,1053)
    pyautogui.click()
    
def abrir_encerramento():
    pyautogui.moveTo(1314,171)
    pyautogui.click()

#data/inicio
def data_inicio():
    pyautogui.sleep(0.5)
    pyautogui.moveTo(1775,168)
    pyautogui.click()

#////////
def dia():
    excel()
    pyautogui.moveTo(421,522)
    pyautogui.sleep(0.4)
    pyautogui.click()
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')

    pyautogui.moveTo(838,678)
    pyautogui.sleep(0.4)
    pyautogui.click()
    pyautogui.sleep(0.4)
    pyautogui.hotkey('ctrl','v')

#pegar mes
def mes():
    excel()
    pyautogui.moveTo(518,521)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')

    pyautogui.moveTo(961,675)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.sleep(0.4)
    pyautogui.hotkey('ctrl','v')

#pegar ano
def ano():
    excel()
    pyautogui.moveTo(627,523)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')

    pyautogui.sleep(0.4)
    pyautogui.moveTo(1082,672)
    pyautogui.click()
    pyautogui.sleep(0.4)
    pyautogui.hotkey('ctrl','v')

    pyautogui.sleep(0.4)
    pyautogui.moveTo(959,745)
    pyautogui.click()

#data/fim
def data_fim():
    pyautogui.sleep(0.5)
    pyautogui.moveTo(1776,259)
    pyautogui.click()

#////////
def horas_de_inicio():
    pyautogui.sleep(0.5)
    pyautogui.moveTo(1830,170)
    pyautogui.click()

#pegar hora
def hora_inicio():
    excel()
    pyautogui.moveTo(418,605)
    pyautogui.sleep(0.4)
    pyautogui.click()
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')

    pyautogui.moveTo(873,677)
    pyautogui.sleep(0.4)
    pyautogui.click()
    pyautogui.sleep(0.4)
    pyautogui.hotkey('ctrl','v')
    pyautogui.sleep(0.4)

#pegar minuto
def minuto_inicio():
    excel()
    pyautogui.moveTo(515,607)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.sleep(0.5)
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')

    pyautogui.moveTo(1053,678)
    pyautogui.click()
    pyautogui.sleep(0.5)
    pyautogui.hotkey('ctrl','v')
    pyautogui.moveTo(959,747)
    pyautogui.click()

#HORAS/fim
def horas_de_fim():
    pyautogui.sleep(0.5)
    pyautogui.moveTo(1826,259)
    pyautogui.click()

#pegar hora
def hora_fim():
    excel()
    pyautogui.moveTo(729,606)
    pyautogui.sleep(0.4)
    pyautogui.click()
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')

    pyautogui.moveTo(868,676)
    pyautogui.sleep(0.4)
    pyautogui.click()
    pyautogui.sleep(0.4)
    pyautogui.hotkey('ctrl','v')
    pyautogui.sleep(0.4)

#pegar minuto
def minuto_fim():
    excel()
    pyautogui.moveTo(838,607)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.sleep(0.4)
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')

    pyautogui.moveTo(1050,676)
    pyautogui.sleep(0.3)
    pyautogui.click()
    pyautogui.sleep(0.5)
    pyautogui.hotkey('ctrl','v')
    #ok
    pyautogui.moveTo(960,747)
    pyautogui.click()

def voltar():
    pyautogui.moveTo(27,12)
    pyautogui.sleep(0.3)
    pyautogui.click()

def abrir_serviço():
    pyautogui.sleep(0.9)
    pyautogui.moveTo(1310,589)
    pyautogui.sleep(0.8)
    pyautogui.click()

def run():
    abrir_encerramento()
    data_inicio()
    dia()
    mes()
    ano()
    data_fim()
    dia()
    mes()
    ano()
    horas_de_inicio()
    hora_inicio()
    minuto_inicio()
    horas_de_fim()
    hora_fim()
    minuto_fim()
    voltar()
    pyautogui.sleep(0.9)
    abrir_serviço()
    
run()