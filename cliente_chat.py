import socket
import threading

#Importar módulo tkinter e componentes
import tkinter as tk
from tkinter import scrolledtext, messagebox

def receber_mensagem():
    global cliente
    while True:
        try:
            mensagem = cliente.recv(1024).decode()
            memo_chat.config(state="normal")
            memo_chat.insert(tk.END, mensagem + "\n")
            memo_chat.yview(tk.END)
            memo_chat.config(state="disabled")
        except:
            cliente.close()
            break

def enviar_mensagem():
    global cliente
    mensagem = campo_mensagem.get().strip()
    mensagem = f"[{nome}] {mensagem}"
    try:
        cliente.send(mensagem.encode())
        memo_chat.config(state="normal")
        memo_chat.insert(tk.END, mensagem + "\n")
        memo_chat.yview(tk.END)
        memo_chat.config(state="disabled")
    except Exception as e:
        messagebox.showerror("Erro",f"Erro no envio: {e}")

def conectar():
    global cliente
    global thread_receber
    global nome

    nome = campo_nome.get().strip()
    if not nome:
        messagebox.showwarning("Atenção", "Digite um nome para conectar")
        return

    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect(("10.209.1.20",5000))  

        campo_mensagem.config(state="normal")
        botao_enviar.config(state="normal")
        botao_conectar.config(state="disabled")
        campo_nome.config(state="disabled")

        thread_receber = threading.Thread(target = receber_mensagem)
        thread_receber.daemon = True
        thread_receber.start()
    except Exception as e:
        messagebox.showerror("Erro",f"Não foi possivel conectar com o servidor: {e}")
   
#Configuração e criação da janela
janela = tk.Tk()
janela.title("Chat IFRN Redes")

#Criar campo para entrada do nome do usuário
tk.Label(janela, text="Seu nome:").pack()
campo_nome = tk.Entry(janela, width=30)
campo_nome.pack()

botao_conectar = tk.Button(janela, text="Conectar",command=conectar)
botao_conectar.pack()

memo_chat = scrolledtext.ScrolledText(janela,state="disabled",
                                      width=100,height=20)
memo_chat.pack()

campo_mensagem = tk.Entry(janela,width=40,state="disabled")
campo_mensagem.pack()

botao_enviar = tk.Button(janela,text="Enviar",command=enviar_mensagem,state="disabled")
botao_enviar.pack(side=tk.LEFT)

cliente = None
thread_receber = None
nome = None

janela.mainloop()