import pyautogui
from time import sleep



def play():
    abrirOS()
    solicitante()
    descer100()
    tipoManut()
    descer600()
    setorExecutante()
    equipamento()
    alterarAba()


#abrir os
def abrirOS():
    pyautogui.moveTo(1339,56)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.moveTo(1271,105)
    pyautogui.click()
    pyautogui.sleep(1)

#solicitante
def solicitante():
    pyautogui.moveTo(1286,412)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.moveTo(1268,102)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.write("victor")
    pyautogui.moveTo(1344,101)
    pyautogui.click()
    pyautogui.sleep(0.5)
    pyautogui.moveTo(1296,165)
    pyautogui.click()
    pyautogui.sleep(0.5)
    pyautogui.moveTo(1298, 685)

#descer
def descer100():
    pyautogui.scroll(-100)
    pyautogui.sleep(1)

#tipo de manutenção
def tipoManut():
    pyautogui.moveTo(1298, 685)
    pyautogui.click()
    pyautogui.sleep(2)
    pyautogui.moveTo(1298, 665)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.moveTo(1298,660)

#descer
def descer600():
    pyautogui.scroll(-600)
    pyautogui.sleep(0.5)

#setor executante
def setorExecutante():
    pyautogui.moveTo(1288,612)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.moveTo(1151,323)
    pyautogui.sleep(1)
    pyautogui.click()
    pyautogui.sleep(0.5)

#equipamento
def equipamento():
    pyautogui.moveTo(1294,681)
    pyautogui.click()
    pyautogui.sleep(0.5)
    pyautogui.moveTo(668,102)
    pyautogui.sleep(0.5)
    pyautogui.click()

#alterar aba
def alterarAba():
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
    pyautogui.moveTo(396,388)


play()