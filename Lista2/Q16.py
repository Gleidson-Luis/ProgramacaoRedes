# Perguntar ao usuário um intervalo de portas

import socket

# Função para verificar se uma porta está aberta
def porta_aberta(porta):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Cria um socket TCP
        s.settimeout(0.5)  # tempo de espera (meio segundo)
        resultado = s.connect_ex(('127.0.0.1', porta))
        return resultado == 0  # retorna True se a porta estiver aberta

# Entrada do usuário
entrada = input("Informe o intervalo de portas (ex: 20 a 100): ")
inicio, fim = map(int, entrada.replace('a', ' ').split())

# Verificação das portas
print(f"\nPortas abertas no localhost entre {inicio} e {fim}:\n")
for porta in range(inicio, fim + 1):
    if porta_aberta(porta):
        print(f"Porta {porta} está aberta")