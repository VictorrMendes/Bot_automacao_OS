import tkinter as tk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk


# Funções para cada botão
def opcao_1():
    subprocess.run(["python", "teste.py"], check=True)

def opcao_2():
    subprocess.run(["python", "abertura_os_servico_Interno.py"], check=True)

def opcao_3():
    subprocess.run(["python", "funcionario.py"], check=True)

def opcao_4():
    subprocess.run(["python", "serviçoInterno.py"], check=True)

def opcao_5():
    subprocess.run(["python", "sincronizar_engeman.py"], check=True)

def opcao_6():
    subprocess.run(["python", "encerramento.py"], check=True)

# Função para sair
def sair():
    resposta = messagebox.askyesno("Confirmação", "Deseja realmente sair?")
    if resposta:
        root.destroy()

# Função para alternar entre as duas imagens
def alternar_imagem():
    global imagem_atual, imagens_tk
    imagem_atual = 1 - imagem_atual  # Alterna entre 0 e 1
    canvas.itemconfig(imagem_id, image=imagens_tk[imagem_atual])

# Função para mover a imagem
def mover_imagem():
    global x, direction
    canvas.move(imagem_id, direction, 0)  # Move a imagem
    x += direction

   
    if x <= -largura_imagem:  
        direction = 2  
        alternar_imagem()  
    elif x >= largura_canvas:  # Saiu pela direita
        direction = -2  # Move para a esquerda
        alternar_imagem()  # Altera a imagem ao retornar

    # Chama novamente após 10ms para continuar o movimento
    canvas.after(10, mover_imagem)


# Configuração da janela principal
root = tk.Tk()
root.title("Automação abertura de OS /victor/")
root.geometry("400x500")  # Ajustei a altura para acomodar a imagem e os botões

# Canvas para a animação
largura_canvas = 400  
altura_canvas = 50
canvas = tk.Canvas(root, width=largura_canvas, height=altura_canvas, bg="white")
canvas.pack()

# Carregar as duas imagens para alternar
imagem1 = Image.open("empilhadeira.jpg").resize((50, 50))  
imagem2 = Image.open("empilhadeira_LE.jpg").resize((50, 50))  
imagens_tk = [ImageTk.PhotoImage(imagem1), ImageTk.PhotoImage(imagem2)]

# Adicionar a primeira imagem ao canvas
imagem_atual = 0  # Índice da imagem atual (0 ou 1)
largura_imagem, altura_imagem = 50, 50
x = 0
y = (altura_canvas - altura_imagem) // 2  # Centralizar verticalmente
direction = 2  # Velocidade do movimento (positivo para direita, negativo para esquerda)
imagem_id = canvas.create_image(x, y, anchor="nw", image=imagens_tk[imagem_atual])

# Inicia o movimento da imagem
mover_imagem()

# Rótulo do menu
label = tk.Label(root, text="Escolha uma opção:", font=("Arial", 14))
label.pack(pady=10)

# Botões para cada opção
botao_1 = tk.Button(root, text="Criar OS automatico", command=opcao_1, width=25, bg="lightgreen")
botao_1.pack(pady=5)

botao_2 = tk.Button(root, text="Os servico Interno", command=opcao_2, width=25, bg="lightgreen")
botao_2.pack(pady=5)

botao_3 = tk.Button(root, text="Funcionario", command=opcao_3, width=25, bg="lightgreen")
botao_3.pack(pady=5)

botao_4 = tk.Button(root, text="Serviço Interno", command=opcao_4, width=25, bg="lightgreen")
botao_4.pack(pady=5)

botao_5 = tk.Button(root, text="Sincronizar ENGEMAN", command=opcao_5, width=25, bg="lightgreen")
botao_5.pack(pady=5)

botao_6 = tk.Button(root, text="Encerramento", command=opcao_6, width=25, bg="lightgreen")
botao_6.pack(pady=5)

botao_sair = tk.Button(root, text="Sair", command=sair, width=25, bg="lightcoral")
botao_sair.pack(pady=5)

# Inicia o loop principal
root.mainloop()
