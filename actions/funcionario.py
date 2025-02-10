import pyautogui
from time import sleep

def excel():
    pyautogui.moveTo(646,1053)
    pyautogui.click()

def abrir_registro():
    pyautogui.moveTo(1889,68)
    pyautogui.click()
    pyautogui.moveTo(1805,122)
    pyautogui.click()

def nome():
    excel()
    pyautogui.moveTo(623,605)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')
    
    #lançar nome
    pyautogui.moveTo(1819,260)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.moveTo(1518,128)
    pyautogui.click()
    pyautogui.hotkey('ctrl','v')
    pyautogui.moveTo(1891,119)
    pyautogui.click()
    pyautogui.sleep(0.5)
    pyautogui.moveTo(1524,212)
    pyautogui.click()


#data/inicio
def data_inicio():
    pyautogui.sleep(0.5)
    pyautogui.moveTo(1769,346)
    pyautogui.click()

#////////
#pegar dia
def dia():
    excel()
    pyautogui.moveTo(421,522)
    pyautogui.sleep(0.4)
    pyautogui.click()
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')

    pyautogui.moveTo(839,677)
    pyautogui.sleep(0.4)
    pyautogui.click()
    pyautogui.sleep(0.3)
    pyautogui.hotkey('ctrl','v')


#pegar mes
def mes():
    excel()
    pyautogui.moveTo(518,521)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')

    pyautogui.moveTo(959,672)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.sleep(0.3)
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
    pyautogui.moveTo(1089,675)
    pyautogui.click()
    pyautogui.sleep(0.3)
    pyautogui.hotkey('ctrl','v')


    pyautogui.sleep(0.5)
    pyautogui.moveTo(955,744)
    pyautogui.click()

#data/fim
def data_fim():
    pyautogui.sleep(0.5)
    pyautogui.moveTo(1767,436)
    pyautogui.click()

#HORAS/inicio
def horas_de_inicio():
    pyautogui.sleep(0.7)
    pyautogui.moveTo(1821,353)
    pyautogui.click()


#pegar hora
def hora_inicio():
    excel()
    pyautogui.moveTo(418,605)
    pyautogui.sleep(0.4)
    pyautogui.click()
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')

    pyautogui.moveTo(868,675)
    pyautogui.sleep(0.4)
    pyautogui.click()
    pyautogui.sleep(0.3)
    pyautogui.hotkey('ctrl','v')
    pyautogui.sleep(0.5)


#pegar minuto
def minuto_inicio():
    excel()
    pyautogui.moveTo(515,607)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.sleep(0.5)
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')

    pyautogui.moveTo(1062,679)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.sleep(0.4)
    pyautogui.hotkey('ctrl','v')

    pyautogui.moveTo(959,748)
    pyautogui.sleep(0.5)
    pyautogui.click()


#HORAS/fim
def horas_de_fim():
    pyautogui.sleep(0.5)
    pyautogui.moveTo(1823,438)
    pyautogui.click()


#pegar hora
def hora_fim():
    excel()
    pyautogui.moveTo(729,606)
    pyautogui.sleep(0.4)
    pyautogui.click()
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')

    pyautogui.moveTo(875,678)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.sleep(0.3)
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

    pyautogui.moveTo(1052,674)
    pyautogui.sleep(0.3)
    pyautogui.click()
    pyautogui.sleep(0.5)
    pyautogui.hotkey('ctrl','v')

    pyautogui.moveTo(963,744)
    pyautogui.sleep(0.5)
    pyautogui.click()

#fechar
def fechar():
    pyautogui.sleep(0.4)
    pyautogui.moveTo(26,17)
    pyautogui.click()
    pyautogui.sleep(0.5)

#ok
def ok():
    pyautogui.sleep(0.4)
    pyautogui.moveTo(868,635)
    pyautogui.click()

#voltar
def voltar():
    pyautogui.sleep(0.8)
    pyautogui.moveTo(26,17)
    pyautogui.click()


def run():
    abrir_registro()
    nome()
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
    fechar()
    ok()
    pyautogui.sleep(0.6)
    voltar()


    

run()