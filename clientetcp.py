import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(("localhost", 5000))

cliente.sendall("Oi, servidor!".encode())

mensagem = cliente.recv(1024)
print