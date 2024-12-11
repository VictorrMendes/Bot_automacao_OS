import pyautogui
from time import sleep

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

#descrição
pyautogui.moveTo(1181,521)
pyautogui.click()
pyautogui.sleep(0.5)
pyautogui.write("SERVICO INTERNO")


#descer
def descer():
    pyautogui.moveTo(1298, 685)
    pyautogui.scroll(-100)
    pyautogui.sleep(1)

descer()
#tipo de manutenção
pyautogui.moveTo(1298, 685)
pyautogui.click()
pyautogui.sleep(2)
pyautogui.moveTo(1140,697)
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
pyautogui.write("servi")
pyautogui.moveTo(1345,100)
pyautogui.click()
pyautogui.moveTo(1145,158)
pyautogui.sleep(0.5)
pyautogui.click()

#Subir
pyautogui.sleep(0.5)
pyautogui.scroll(600)

#pegar nome
pyautogui.moveTo(582,740)
pyautogui.click()
pyautogui.moveTo(416,364)
pyautogui.sleep(0.5)
pyautogui.click()
pyautogui.hotkey('ctrl','c')
pyautogui.hotkey('alt','tab')

#responsavel
pyautogui.moveTo(1289,258)
pyautogui.click()
pyautogui.sleep(1)
pyautogui.moveTo(1179,100)
pyautogui.click()
pyautogui.sleep(1)
pyautogui.hotkey('ctrl','v')
pyautogui.moveTo(1344,101)
pyautogui.click()
pyautogui.sleep(0.5)
pyautogui.moveTo(1118,161)
pyautogui.click()
pyautogui.sleep(0.5)
pyautogui.moveTo(1298, 685)

pyautogui.moveTo(1292,190)
pyautogui.sleep(0.4)
pyautogui.click()

#pegar hora
pyautogui.moveTo(582,740)
pyautogui.click()
pyautogui.moveTo(321,486)
pyautogui.sleep(0.4)
pyautogui.click()
pyautogui.hotkey('ctrl','c')
pyautogui.hotkey('alt','tab')

pyautogui.moveTo(631,495)
pyautogui.sleep(0.4)
pyautogui.click()
pyautogui.hotkey('ctrl','v')
pyautogui.sleep(0.4)


#pegar minuto
pyautogui.moveTo(582,740)
pyautogui.click()
pyautogui.moveTo(417,489)
pyautogui.sleep(0.5)
pyautogui.click()
pyautogui.hotkey('ctrl','c')
pyautogui.hotkey('alt','tab')

pyautogui.moveTo(755,496)
pyautogui.click()
pyautogui.sleep(0.4)
pyautogui.hotkey('ctrl','v')
pyautogui.moveTo(678,558)
pyautogui.click()

pyautogui.moveTo(1251,189)
pyautogui.sleep(0.4)
pyautogui.click()

#////////
#pegar dia
pyautogui.moveTo(582,740)
pyautogui.click()
pyautogui.moveTo(322,431)
pyautogui.sleep(0.4)
pyautogui.click()
pyautogui.hotkey('ctrl','c')
pyautogui.hotkey('alt','tab')

pyautogui.moveTo(584,494)
pyautogui.sleep(0.4)
pyautogui.click()
pyautogui.hotkey('ctrl','v')


#pegar mes
pyautogui.moveTo(582,740)
pyautogui.click()
pyautogui.moveTo(415,430)
pyautogui.sleep(0.5)
pyautogui.click()
pyautogui.hotkey('ctrl','c')
pyautogui.hotkey('alt','tab')

pyautogui.moveTo(678,498)
pyautogui.click()
pyautogui.hotkey('ctrl','v')


#pegar ano
pyautogui.moveTo(582,740)
pyautogui.click()
pyautogui.moveTo(501,429)
pyautogui.sleep(0.5)
pyautogui.click()
pyautogui.hotkey('ctrl','c')
pyautogui.hotkey('alt','tab')
pyautogui.sleep(0.4)
pyautogui.moveTo(782,498)
pyautogui.click()
pyautogui.hotkey('ctrl','v')


pyautogui.sleep(0.4)
pyautogui.moveTo(682,553)
pyautogui.click()

pyautogui.sleep(0.2)
pyautogui.moveTo(22,10)
pyautogui.click()