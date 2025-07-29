# Percorrer arquivos de uma pasta e renomear

import os

# Pasta a ser percorrida
pasta = "C:\Trabalho_Lista2\quest5"

# Percorre todos os arquivos da pasta
for arquivo in os.listdir(pasta):
    if arquivo.endswith('.conf'):

# Renomeia: arquivo.conf em arquivo_old.conf
        nome_antigo = os.path.join(pasta, arquivo)
        nome_novo = os.path.join(pasta, arquivo.replace('.conf', '_old.conf'))
        os.rename(nome_antigo, nome_novo)
        print(f"Renomeado: {arquivo} → {arquivo.replace('.conf', '_old.conf')}")