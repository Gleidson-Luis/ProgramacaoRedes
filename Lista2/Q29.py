# Progrma que gera 15 endereços IPs aleatórios na faixa 172.16.0.0/16

import random

def gerar_ips():
    ips = []

    # Gera 15 IPs na faixa 172.16.0.0 a 172.16.255.255
    for _ in range(15):
        parte3 = random.randint(0, 255)
        parte4 = random.randint(0, 255)
        ip = f"172.16.{parte3}.{parte4}"
        ips.append(ip)

    # Salva no arquivo
    with open("ips_gerados.txt", "w") as arquivo:
        for ip in ips:
            arquivo.write(ip + "\n")

    print("Arquivo 'ips_gerados.txt' gerado com sucesso!")

# gera os ips
gerar_ips()