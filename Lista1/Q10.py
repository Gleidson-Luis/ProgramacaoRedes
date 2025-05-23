# Pergunte o nome de uma pasta e criar uma pasta no sistema, usando módulo os

import os

nome_pasta = input("Digite o nome da paste que deseja criar: ")

caminho_pasta = f"C:\PastaTeste\{nome_pasta}"

# Verifica se a pasta já existe e a cria se não existir
if not os.path.exists(caminho_pasta):
    os.makedirs(caminho_pasta)
    print(f"Pasta '{nome_pasta}' criada com sucesso em {caminho_pasta}")
else:
    print(f"A pasta '{nome_pasta}' já existe!")