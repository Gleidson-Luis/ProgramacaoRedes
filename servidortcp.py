import socket
#socket.AF_INET -> Para usar IPV4
#socket.SOCK_STREAM -> Para usar TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Se associa a um endereço
servidor.bind(("localhost", 5000))

#Iniciar a escuta de pacotes
servidor.listen()
print("Servidor rodando")

conn, addr = servidor.accept()
print(f"Conectado a {addr}")

dados = conn.recv(1024)
print(dados.decode())

conn.sendall("Mensagem recebida")