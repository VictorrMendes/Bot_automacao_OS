import pyautogui
from time import sleep

nome = "braz"
horimetro = "2584"
equipamento = "2383"
description = " "

#abrir os
pyautogui.moveTo(1339,56)
pyautogui.click()
pyautogui.sleep(1)
pyautogui.moveTo(1271,105)
pyautogui.click()
pyautogui.sleep(1)

#solicitante
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


#responsavel
pyautogui.moveTo(1287,338)
pyautogui.click()
pyautogui.sleep(1)
pyautogui.moveTo(1179,100)
pyautogui.click()
pyautogui.sleep(1)
pyautogui.write(nome)
pyautogui.moveTo(1344,101)
pyautogui.click()
pyautogui.sleep(0.5)
pyautogui.moveTo(1118,161)
pyautogui.click()
pyautogui.sleep(0.5)
pyautogui.moveTo(1298, 685)

#descer
def descer():
    pyautogui.scroll(-100)
    pyautogui.sleep(1)

descer()
#tipo de manutenção
pyautogui.moveTo(1298, 685)
pyautogui.click()
pyautogui.sleep(2)
pyautogui.moveTo(1298, 665)
pyautogui.click()
pyautogui.sleep(1)
pyautogui.moveTo(1298,660)

#descer
pyautogui.scroll(-600)
pyautogui.sleep(0.5)

#setor executante
pyautogui.moveTo(1288,612)
pyautogui.click()
pyautogui.sleep(1)
pyautogui.moveTo(1151,323)
pyautogui.sleep(1)
pyautogui.click()
pyautogui.sleep(0.5)

#equipamento
pyautogui.moveTo(1294,681)
pyautogui.click()
pyautogui.sleep(0.5)
pyautogui.moveTo(668,102)
pyautogui.sleep(0.5)
pyautogui.click()
pyautogui.sleep(1.5)
pyautogui.moveTo(1342,99)
pyautogui.write(equipamento)
pyautogui.moveTo(1341,101)
pyautogui.click()
pyautogui.sleep(1)
pyautogui.moveTo(704,162)
pyautogui.click()

#horimetro
pyautogui.moveTo(529,345)
pyautogui.click()
pyautogui.write(horimetro)
pyautogui.sleep(1)
pyautogui.scroll(600)
pyautogui.moveTo(505,232)


