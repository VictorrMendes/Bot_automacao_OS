import pyautogui
from time import sleep


def excel():
    pyautogui.moveTo(646,1053)
    pyautogui.click()
#abrir os

def abrirOs():
    pyautogui.moveTo(1888,63)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.moveTo(1802,126)
    pyautogui.click()
    pyautogui.sleep(1)

#solicitante
def solicitante():
    pyautogui.moveTo(1823,515)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.moveTo(1355,127)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.write("victor")
    pyautogui.moveTo(1894,125)
    pyautogui.click()
    pyautogui.sleep(0.5)
    pyautogui.moveTo(1399,204)
    pyautogui.click()
    pyautogui.sleep(0.5)

#pegar nome
def coletaNome():
    excel()
    pyautogui.moveTo(623,605)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')

#responsavel
def responsavel():
    pyautogui.moveTo(1823,434)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.moveTo(1429,127)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.hotkey('ctrl','v')
    pyautogui.moveTo(1889,128)
    pyautogui.click()
    pyautogui.sleep(0.5)
    pyautogui.moveTo(1304,192)
    pyautogui.click()
    pyautogui.sleep(0.5)
    
#tipo de manutenção
def manut():
    pyautogui.moveTo(1824,971)
    pyautogui.click()
    pyautogui.sleep(2)
    pyautogui.moveTo(1757,905)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.moveTo(1298,660)
    pyautogui.scroll(-600)
    pyautogui.sleep(0.5)

#setor executante
def executante():
    pyautogui.moveTo(1829,809)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.moveTo(1043,392)
    pyautogui.sleep(1)
    pyautogui.click()
    pyautogui.sleep(0.5)

#equipamento
def equipamento():

    pyautogui.moveTo(1818,895)
    pyautogui.click()
    pyautogui.sleep(0.5)
    pyautogui.moveTo(1265,127)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.sleep(1.5)
    pyautogui.write("servi")
    pyautogui.moveTo(1893,123)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.moveTo(1088,187)
    pyautogui.click()

#horimetro
def horimetro():
    #horimetro
    pyautogui.moveTo(1036,469)
    pyautogui.sleep(0.4)
    pyautogui.click()
    pyautogui.write("00")
    pyautogui.sleep(1)
    pyautogui.scroll(600)
#descrição
def descricao():
    pyautogui.scroll(200)
    #descrição
    pyautogui.moveTo(864,610)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.write("SERVICO INTERNO")
    

def horas():
    pyautogui.moveTo(1827,344)
    pyautogui.sleep(0.4)
    pyautogui.click()

    #pegar hora
    excel()
    pyautogui.moveTo(417,613)
    pyautogui.sleep(0.4)
    pyautogui.click()
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')

    pyautogui.moveTo(872,677)
    pyautogui.sleep(0.4)
    pyautogui.click()
    pyautogui.hotkey('ctrl','v')
    pyautogui.sleep(0.5)


    #pegar minuto
    excel()
    pyautogui.moveTo(519,604)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')

    pyautogui.moveTo(1063,673)
    pyautogui.click()
    pyautogui.sleep(0.5)
    pyautogui.hotkey('ctrl','v')


    #ok
    pyautogui.moveTo(960,745)
    pyautogui.click()
    
#data
def data():
    
    pyautogui.moveTo(1776,346)
    pyautogui.sleep(0.5)
    pyautogui.click()
    #pegar dia
    excel()
    pyautogui.moveTo(417,522)
    pyautogui.sleep(0.4)
    pyautogui.click()
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')

    pyautogui.moveTo(838,677)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.hotkey('ctrl','v')


    #pegar mes
    excel()
    pyautogui.moveTo(520,519)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')

    pyautogui.moveTo(961,677)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.hotkey('ctrl','v')


    #pegar ano
    excel()
    pyautogui.moveTo(627,522)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')
    pyautogui.sleep(0.4)
    pyautogui.moveTo(1077,672)
    pyautogui.click()
    pyautogui.hotkey('ctrl','v')

    #ok
    pyautogui.sleep(0.4)
    pyautogui.moveTo(960,743)
    pyautogui.click()

#fechar
def fechar():
    pyautogui.sleep(0.4)
    pyautogui.moveTo(29,17)
    pyautogui.click()

#rodar
def run():
    abrirOs()
    solicitante()
    coletaNome()
    responsavel()
    manut()
    executante()
    equipamento()
    horimetro()
    descricao()
    horas()
    data()
    fechar()

run()