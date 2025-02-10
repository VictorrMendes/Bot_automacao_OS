import pyautogui
import tkinter as tk
from tkinter import simpledialog

# Criar a janela principa
root = tk.Tk()
root.withdraw()

repeticao = simpledialog.askinteger("Entrada", "Quantas vezes deseja executar a repetição?")


#abrir planilha
def abrir_planilha():
    pyautogui.moveTo(648,1049)
    pyautogui.click()
    
#ir para engeman   
def abrir_engeman():
    pyautogui.moveTo(1033,1051)
    pyautogui.click()
    pyautogui.sleep(0.2)

if repeticao:
    for id in range(repeticao):

#///////////////
#abrir planilha
        abrir_planilha()

#clicar na celula-id
        pyautogui.moveTo(149,423)
        pyautogui.click()
        pyautogui.sleep(0.3)
        pyautogui.hotkey('ctrl','c')

#ir para engeman
        abrir_engeman()

#pesquisar equipamento
        pyautogui.moveTo(1040,124)
        pyautogui.click()

#colar
        pyautogui.hotkey('ctrl','v')

#pesquisar
        pyautogui.moveTo(1892,121)
        pyautogui.click()
        pyautogui.sleep(0.4)


#seleciona
        pyautogui.moveTo(737,225)
        pyautogui.click()
        pyautogui.sleep(0.4)

#novo
        pyautogui.moveTo(1889,65)
        pyautogui.click()
        pyautogui.moveTo(1812,126)
        pyautogui.click()

#data
        pyautogui.moveTo(1789,340)
        pyautogui.sleep(0.5)
        pyautogui.click()
        pyautogui.click()
        pyautogui.sleep(0.5)
#ok
        pyautogui.moveTo(957,747)
        pyautogui.sleep(0.4)
        pyautogui.click()

#/////////////////////////////////////////////////
#pegar o horimetro

#abrir planilha
        abrir_planilha()

#copiar retorno
        pyautogui.moveTo(233,424)
        pyautogui.click()
        pyautogui.sleep(0.3)
        pyautogui.hotkey('ctrl','c')

#ir para engeman
        abrir_engeman()

#digitar horimetro
        pyautogui.moveTo(1089,434)
        pyautogui.sleep(0.5)
        pyautogui.click()
        pyautogui.hotkey('ctrl','v')


#salvar
        pyautogui.moveTo(31,17)
        pyautogui.click()
        pyautogui.sleep(6.1)
        pyautogui.click()
        pyautogui.sleep(1.3)


#limpar pesquisa
        pyautogui.moveTo(725,123)
        pyautogui.click()
        pyautogui.press("backspace", presses=7)

#next
        abrir_planilha()

#finalizar linha
        pyautogui.moveTo(14,422)
        pyautogui.click()
        pyautogui.sleep(0.3)
        pyautogui.moveTo(366,162)
        pyautogui.click()
        pyautogui.sleep(0.4)
        pyautogui.moveTo(15,427)

#ocultar linha
        pyautogui.click(button="right")
        pyautogui.sleep(0.2)
        pyautogui.moveTo(88,866)
        pyautogui.sleep(0.2)
        pyautogui.click()
        abrir_planilha()