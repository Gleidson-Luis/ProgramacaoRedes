
import requests

lista_sites = ["http://www.g1.com.br", "http://www.ifrn.edu.br", "http://www.uol.com.br"]

for site in lista_sites:
    try:
        resposta = requests.get(site)
        if resposta.status_code ==200:
            print("Online")
        else:
            print("Offline")
    except:
        print("Erro")