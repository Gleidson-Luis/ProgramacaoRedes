# Cliente TCP que se conecta a um servidor e receba uma list de nomes de dispositivos conectados

import socket

def cliente_tcp(host='127.0.0.1', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        dados = s.recv(1024)  # Recebe até 1024 bytes
        mensagem = dados.decode('utf-8')
        
        # Supondo que os nomes venham separados por vírgula
        dispositivos = mensagem.split(',')
        
        print("Dispositivos conectados:")
        for dispositivo in dispositivos:
            print(f"- {dispositivo.strip()}")

# Executa o script
if __name__ == "__main__":
    cliente_tcp()