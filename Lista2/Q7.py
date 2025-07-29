# Ler uma lista de site em um arquivo e indicar se está online ou offline

import requests

# Lê a lista de sites do arquivo
with open('sites.txt', 'r', encoding='utf-8') as f:
    sites = [linha.strip() for linha in f.readlines()]

print("Verificando status dos sites...\n")

# Verifica cada site
for site in sites:
    try:
        response = requests.get(site, timeout=10)
        if response.status_code == 200:
            print(f"{site} - ONLINE")
        else:
            print(f"{site} - Status: {response.status_code}")
    except requests.exceptions.RequestException:
        print(f"{site} - OFFLINE")

print("\nVerificação concluída!")