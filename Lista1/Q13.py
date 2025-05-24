#Salvar site em html

import requests

site = input("Digite o endereço do site: ")
conteudo = requests.get(site)
arquivo = open("site.html", "w")
arquivo.write(conteudo.text)
print("O conteúdo HTML foi salvo com sucesso em 'site.html'.")
arquivo.close()