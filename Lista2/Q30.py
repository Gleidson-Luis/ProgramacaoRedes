# Ler um arquivo .json e exibir suas chaves

import json

# Abre e lê o conteúdo do arquivo configs.json
with open("configs.json", "r") as arquivo:
    dados = json.load(arquivo)

# Percorre todas as chaves e valores do JSON
for chave, valor in dados.items():
    print(f"{chave}: {valor}")
