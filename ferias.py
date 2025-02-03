import pyautogui
from time import sleep


pyautogui.moveTo(1341,46)
pyautogui.click()
pyautogui.moveTo(1279,98)
pyautogui.click()

#pegar nome
pyautogui.moveTo(582,740)
pyautogui.click()
pyautogui.moveTo(487,494)
pyautogui.sleep(0.5)
pyautogui.click()
pyautogui.hotkey('ctrl','c')
pyautogui.hotkey('alt','tab')

pyautogui.moveTo(1284,203)
pyautogui.sleep(0.5)
pyautogui.click()
pyautogui.sleep(1)
pyautogui.moveTo(1015,107)
pyautogui.click()
pyautogui.hotkey('ctrl','v')
pyautogui.moveTo(1343,96)
pyautogui.click()
pyautogui.sleep(0.5)
pyautogui.moveTo(1006,164)
pyautogui.click()



#data/inicio
pyautogui.sleep(0.5)
pyautogui.moveTo(1246,279)
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
pyautogui.sleep(0.3)
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
pyautogui.sleep(0.5)
pyautogui.click()
pyautogui.sleep(0.3)
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
pyautogui.sleep(0.3)
pyautogui.hotkey('ctrl','v')


pyautogui.sleep(0.5)
pyautogui.moveTo(682,553)
pyautogui.click()

#data/fim
pyautogui.sleep(0.5)
pyautogui.moveTo(1245,346)
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
pyautogui.sleep(0.5)
pyautogui.click()
pyautogui.sleep(0.3)
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
pyautogui.sleep(0.5)
pyautogui.click()
pyautogui.sleep(0.3)
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
pyautogui.sleep(0.3)
pyautogui.hotkey('ctrl','v')


pyautogui.sleep(0.5)
pyautogui.moveTo(682,553)
pyautogui.click()


#HORAS/inicio
pyautogui.sleep(0.5)
pyautogui.moveTo(1287,274)
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
pyautogui.sleep(0.3)
pyautogui.hotkey('ctrl','v')
pyautogui.sleep(0.5)


#pegar minuto
pyautogui.moveTo(582,740)
pyautogui.click()
pyautogui.moveTo(417,489)
pyautogui.sleep(0.5)
pyautogui.click()
pyautogui.sleep(0.5)
pyautogui.hotkey('ctrl','c')
pyautogui.hotkey('alt','tab')

pyautogui.moveTo(755,496)
pyautogui.sleep(0.5)
pyautogui.click()
pyautogui.sleep(0.4)
pyautogui.hotkey('ctrl','v')
pyautogui.moveTo(678,558)
pyautogui.click()

pyautogui.moveTo(1249,218)
pyautogui.sleep(0.5)
pyautogui.click()

#HORAS/fim
pyautogui.sleep(0.5)
pyautogui.moveTo(1287,346)
pyautogui.click()


#pegar hora
pyautogui.moveTo(582,740)
pyautogui.click()
pyautogui.moveTo(574,488)
pyautogui.sleep(0.4)
pyautogui.click()
pyautogui.hotkey('ctrl','c')
pyautogui.hotkey('alt','tab')

pyautogui.moveTo(631,495)
pyautogui.sleep(0.5)
pyautogui.click()
pyautogui.sleep(0.3)
pyautogui.hotkey('ctrl','v')
pyautogui.sleep(0.4)


#pegar minuto
pyautogui.moveTo(582,740)
pyautogui.click()
pyautogui.moveTo(654,490)
pyautogui.sleep(0.5)
pyautogui.click()
pyautogui.sleep(0.4)
pyautogui.hotkey('ctrl','c')
pyautogui.hotkey('alt','tab')

pyautogui.moveTo(755,496)
pyautogui.sleep(0.3)
pyautogui.click()
pyautogui.sleep(0.5)
pyautogui.hotkey('ctrl','v')
pyautogui.moveTo(678,558)
pyautogui.click()

pyautogui.moveTo(1249,218)
pyautogui.sleep(0.5)
pyautogui.click()

#fechar
pyautogui.sleep(0.4)
pyautogui.moveTo(23,6)
pyautogui.click()


#ok
pyautogui.sleep(0.4)
pyautogui.moveTo(603,462)
pyautogui.click()

#voltar
pyautogui.sleep(0.4)
pyautogui.moveTo(24,13)
pyautogui.click()




