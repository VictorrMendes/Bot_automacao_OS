import pyautogui
from time import sleep

#abrir os

def abrirOs():
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

#pegar nome
def coletaNome():
    pyautogui.moveTo(582,740)
    pyautogui.click()
    pyautogui.moveTo(416,364)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')

#responsavel
def responsavel():
    pyautogui.moveTo(1287,338)
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

#descer
def descer():
    pyautogui.scroll(-100)
    pyautogui.sleep(1)

#tipo de manutenção
def manut():
    pyautogui.moveTo(1298, 685)
    pyautogui.click()
    pyautogui.sleep(2)
    pyautogui.moveTo(1298, 665)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.moveTo(1298,660)
    pyautogui.scroll(-600)
    pyautogui.sleep(0.5)

#setor executante
def executante():
    pyautogui.moveTo(1288,612)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.moveTo(1151,323)
    pyautogui.sleep(1)
    pyautogui.click()
    pyautogui.sleep(0.5)

#equipamento
def equipamento():
    #pegar equipamento
    pyautogui.moveTo(582,740)
    pyautogui.click()
    pyautogui.moveTo(501,342)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.sleep(0.4)
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')
    #sistema equipamento
    pyautogui.moveTo(1294,681)
    pyautogui.click()
    pyautogui.sleep(0.5)
    pyautogui.moveTo(668,102)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.sleep(1.5)
    pyautogui.moveTo(1342,99)
    pyautogui.sleep(0.4)
    pyautogui.hotkey('ctrl','v')
    pyautogui.moveTo(1341,101)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.moveTo(704,162)
    pyautogui.click()

#horimetro
def horimetro():
    #pegar horimetro
    pyautogui.moveTo(582,740)
    pyautogui.click()
    pyautogui.moveTo(572,343)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.sleep(0.5)
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')
    #horimetro
    pyautogui.moveTo(529,345)
    pyautogui.sleep(0.4)
    pyautogui.click()
    pyautogui.hotkey('ctrl','v')
    pyautogui.sleep(1)
    pyautogui.scroll(600)
    pyautogui.moveTo(505,232)

#descrição
def descricao():
    #pegar descrição
    pyautogui.moveTo(582,740)
    pyautogui.click()
    pyautogui.moveTo(653,343)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')
    #descrição
    pyautogui.moveTo(954,326)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.hotkey('ctrl','v')
    pyautogui.scroll(200)


def horas():
    pyautogui.moveTo(1292,219)
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
    pyautogui.sleep(0.5)


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
    pyautogui.sleep(0.5)
    pyautogui.hotkey('ctrl','v')
    pyautogui.moveTo(678,558)
    pyautogui.click()

    pyautogui.moveTo(1249,218)
    pyautogui.sleep(0.5)
    pyautogui.click()

#data
def data():
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

    #ok
    pyautogui.sleep(0.4)
    pyautogui.moveTo(682,553)
    pyautogui.click()

#fechar
def fechar():
    pyautogui.sleep(0.4)
    pyautogui.moveTo(23,6)
    pyautogui.click()

#rodar
def run():
    abrirOs()
    solicitante()
    coletaNome()
    responsavel()
    descer()
    manut()
    executante()
    equipamento()
    horimetro()
    descricao()
    horas()
    data()
    fechar()

run()