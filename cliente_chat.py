import socket
import threading

def receber_mensagem(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024)
            print(mensagem.decode())
        except:
            cliente.close()
            break

def enviar_mensagem(cliente):
    while True:
        mensagem = input("Mensagem: ")
        cliente.send(mensagem.encode())

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 5000))

thread_receber = threading.Thread(receber_mensagem, args=(cliente, ))
thread_enviar = threading.Thread(enviar_mensagem, args=(cliente, ))

thread_receber.start()
thread_enviar.start()