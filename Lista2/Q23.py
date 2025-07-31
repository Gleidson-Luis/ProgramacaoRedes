# Criar cliente UDP que envie a hora local para um servidor

import socket
import threading
from datetime import datetime, timezone
import time

HOST = '127.0.0.1'
PORT = 12345

def servidor_udp():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print(f"[Servidor] Rodando em {HOST}:{PORT}...")

        while True:
            dados, endereco = s.recvfrom(1024)
            hora_local_cliente = dados.decode('utf-8')
            print(f"[Servidor] Recebido do cliente {endereco}: hora local = {hora_local_cliente}")

            horario_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
            s.sendto(horario_utc.encode('utf-8'), endereco)

def cliente_udp():
    time.sleep(1)  # Espera o servidor subir
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        hora_local = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        s.sendto(hora_local.encode('utf-8'), (HOST, PORT))

        dados, _ = s.recvfrom(1024)
        horario_utc = dados.decode('utf-8')
        print(f"[Cliente] Horário UTC recebido do servidor: {horario_utc}")

if __name__ == "__main__":
    # Cria e inicia thread do servidor
    thread_servidor = threading.Thread(target=servidor_udp, daemon=True)
    thread_servidor.start()

    # Roda o cliente (na thread principal)
    cliente_udp()
