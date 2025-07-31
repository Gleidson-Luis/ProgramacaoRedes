# Gerar  senhas aleatórias de 8 dígitos para 5 roteadores e exiba as senhas na tela

import random # Biblioteca padrão para gerar números pseudoaleatórios

def gerar_senhas(qtd=5, tamanho=8): # Função para gerar senhas com dois parâmetros
    senhas = []
    for _ in range(qtd):
        senha = ''.join(random.choices('0123456789', k=tamanho)) # Gera uma senha de 8 dígitos numéricos aleatórios
        senhas.append(senha)
    return senhas

# Gerar e exibir as senhas
senhas_roteadores = gerar_senhas()
for i, senha in enumerate(senhas_roteadores, start=1):
    print(f"Roteador {i}: {senha}")