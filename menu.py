import tkinter as tk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk
import pyautogui
from tkinter import Tk, Canvas

def retorno():
    pyautogui.moveTo(960,748)
    pyautogui.click()

def executar_script(script):
    try:
        subprocess.run(["python", script], check=True)
        retorno()
    except:
        retorno()

def opcao_1():
    executar_script("teste.py")

def opcao_2():
    executar_script("abertura_os_servico_Interno.py")

def opcao_3():
    executar_script("funcionario.py")

def opcao_4():
    executar_script("encerramento.py")

def opcao_5():
    executar_script("sincronizar_engeman.py")

def opcao_6():
    executar_script("serviçoInterno.py")

def opcao_7():
    executar_script("ferias.py")
    pyautogui.sleep(0.3)
    executar_script("encerramento.py")
    
def opcao_8():
    executar_script("vazamento.py")
    
def opcao_9():
    executar_script("horimetro.py")

def sair():
    resposta = messagebox.askyesno("Confirmação", "Deseja realmente sair?")
    if resposta:
        root.destroy()

def alternar_imagem():
    global imagem_atual, imagens_tk
    imagem_atual = 1 - imagem_atual
    canvas.itemconfig(imagem_id, image=imagens_tk[imagem_atual])

def mover_imagem():
    global x, direction
    canvas.move(imagem_id, direction, 0)
    x += direction

    if x <= -largura_imagem:
        direction = 2
        alternar_imagem()
    elif x >= largura_canvas:
        direction = -2
        alternar_imagem()

    canvas.after(10, mover_imagem)

root = tk.Tk()
root.title("Automação abertura de OS /victor/")
root.geometry("300x475")

largura_canvas = 350
altura_canvas = 50
canvas = tk.Canvas(root, width=largura_canvas, height=altura_canvas, bg="white")
canvas.pack()

imagem_fundo = Image.open("fundo.jpg").resize((300, 60))
imagem_fundo_tk = ImageTk.PhotoImage(imagem_fundo)

canvas.create_image(0, 0, anchor="nw", image=imagem_fundo_tk)

imagem1 = Image.open("empilhadeira.png ").resize((50, 50))
imagem2 = Image.open("empilhadeira_LE.png").resize((50, 50))
imagens_tk = [ImageTk.PhotoImage(imagem1), ImageTk.PhotoImage(imagem2)]

imagem_atual = 0
largura_imagem, altura_imagem = 50, 50
x = 0
y = (altura_canvas - altura_imagem) // 2
direction = 2
imagem_id = canvas.create_image(x, y, anchor="nw", image=imagens_tk[imagem_atual])

mover_imagem()

label = tk.Label(root, text="Escolha uma opção:", font=("Arial", 14))
label.pack(pady=10)

botao_1 = tk.Button(root, text="OS Corretiva", command=opcao_1, width=25, bg="lightgreen")
botao_1.pack(pady=5)

botao_2 = tk.Button(root, text="Os Servico Interno", command=opcao_2, width=25, bg="lightgreen")
botao_2.pack(pady=5)

botao_7 = tk.Button(root, text="Funcionários e Encerramento", command=opcao_7, width=25, bg="lightgreen")
botao_7.pack(pady=5)

botao_3 = tk.Button(root, text="Registrar funcionário", command=opcao_3, width=25, bg="lightgreen")
botao_3.pack(pady=5)

botao_4 = tk.Button(root, text="Encerramento", command=opcao_4, width=25, bg="lightgreen")
botao_4.pack(pady=5)

botao_5 = tk.Button(root, text="Sincronizar ENGEMAN", command=opcao_5, width=25, bg="lightgreen")
botao_5.pack(pady=5)

botao_6 = tk.Button(root, text="Serviço Interno", command=opcao_6, width=25, bg="lightgreen")
botao_6.pack(pady=5)

botao_8 = tk.Button(root, text="Vazamento", command=opcao_8, width=25, bg="lightgreen")
botao_8.pack(pady=5)

botao_9 = tk.Button(root, text="Horimetro", command=opcao_9, width=25, bg="lightgreen")
botao_9.pack(pady=5)

botao_sair = tk.Button(root, text="Sair", command=sair, width=25, bg="lightcoral")
botao_sair.pack(pady=5)

root.mainloop()
