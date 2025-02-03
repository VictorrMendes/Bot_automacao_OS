import pyautogui
import tkinter as tk
from tkinter import simpledialog

# Criar a janela principa
root = tk.Tk()
root.withdraw()

repeticao = simpledialog.askinteger("Entrada", "Quantas vezes deseja executar a repetição?")


#abrir planilha
def abrir_planilha():
    pyautogui.moveTo(584,748)
    pyautogui.click()
    
#ir para engeman   
def abrir_engeman():
    pyautogui.moveTo(707,742)
    pyautogui.click()
    pyautogui.sleep(0.2)

if repeticao:
    for id in range(repeticao):

#///////////////
#abrir planilha
        abrir_planilha()

#clicar na celula-id
        pyautogui.moveTo(116,352)
        pyautogui.click()
        pyautogui.sleep(0.3)
        pyautogui.hotkey('ctrl','c')

#ir para engeman
        abrir_engeman()

#pesquisar equipamento
        pyautogui.moveTo(584,103)
        pyautogui.click()

#colar
        pyautogui.hotkey('ctrl','v')

#pesquisar
        pyautogui.moveTo(1344,97)
        pyautogui.click()
        pyautogui.sleep(0.4)


#seleciona
        pyautogui.moveTo(793,202)
        pyautogui.click()
        pyautogui.sleep(0.4)

#novo
        pyautogui.moveTo(1342,51)
        pyautogui.click()
        pyautogui.moveTo(1288,98)
        pyautogui.click()

#data
        pyautogui.moveTo(1261,271)
        pyautogui.sleep(0.5)
        pyautogui.click()
        pyautogui.click()
        pyautogui.sleep(0.5)
#ok
        pyautogui.moveTo(684,552)
        pyautogui.sleep(0.4)
        pyautogui.click()

#/////////////////////////////////////////////////
#pegar o horimetro

#abrir planilha
        abrir_planilha()

#copiar retorno
        pyautogui.moveTo(191,349)
        pyautogui.click()
        pyautogui.sleep(0.3)
        pyautogui.hotkey('ctrl','c')

#ir para engeman
        abrir_engeman()

#digitar horimetro
        pyautogui.moveTo(553,342)
        pyautogui.sleep(0.5)
        pyautogui.click()
        pyautogui.hotkey('ctrl','v')

# #descarte
#         pyautogui.moveTo(1341,52)
#         pyautogui.click()
#         pyautogui.sleep(0.5)
# #
#         pyautogui.moveTo(1295,129)
#         pyautogui.click()
#         pyautogui.sleep(0.1)

#salvar
        pyautogui.moveTo(20,10)
        pyautogui.click()
        pyautogui.sleep(4.5)
        pyautogui.click()
        pyautogui.sleep(0.9)
        pyautogui.sleep(0.9)

#limpar pesquisa
        pyautogui.moveTo(584,103)
        pyautogui.click()
        pyautogui.press("backspace", presses=7)

#next
        abrir_planilha()

#finalizar linha
        pyautogui.moveTo(9,350)
        pyautogui.click()
        pyautogui.sleep(0.3)
        pyautogui.moveTo(298,129)
        pyautogui.click()
        pyautogui.sleep(0.4)
        pyautogui.moveTo(9,350)

#ocultar linha
        pyautogui.click(button="right")
        pyautogui.sleep(0.2)
        pyautogui.moveTo(64,646)
        pyautogui.sleep(0.2)
        pyautogui.click()
        abrir_planilha()