# Gerar 10 endereços IP aleatoriamente na faixa de 192.168.0.0/24

import random  # Biblioteca padrão para gerar números pseudoaleatórios

def gerar_ips():
    ips = set() # Garante que os IPs não se repitam
    while len(ips) < 10:
        ultimo_octeto = random.randint(1, 254) # Não gera .0 (rede) e .255 (broadcast)
        ip = f"192.168.0.{ultimo_octeto}"
        ips.add(ip)
    return list(ips)

# Gerar e imprimir os IPs
lista_ips = gerar_ips()
for ip in lista_ips:
    print(ip)