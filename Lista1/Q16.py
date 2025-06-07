#Salvar imagem de um site

import requests

site = input("Digite a URL da imagem: ")
nome_imagem = "imagem_baixada.jpg"
conteudo = requests.get(site)

with open("index.html","w", encoding = conteudo.apparent_encoding) as arquivo:
    arquivo.write(conteudo.text)
    print("O conteúdo HTML foi salvo com sucesso em 'site.html'.")
    arquivo.close()