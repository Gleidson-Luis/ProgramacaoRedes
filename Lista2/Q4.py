# Perguntar site e salvar em uma página .html

import requests

# Pergunta o site
url = input("Digite a URL do site: ")

# Adiciona https:// se não tiver
if not url.startswith('http'):
    url = 'https://' + url

# Baixa a página
response = requests.get(url)

# Salva em arquivo
with open('pagina.html', 'w', encoding='utf-8') as arquivo:
    arquivo.write(response.text)

print("Página salva em 'pagina.html'!")