# Percorrer arquivos de um diretorio e exibir somente arquivos com extensão .log

import os

caminho_diretorio = "C:\Pastas_Lista2\quest2"
# Lista os arquivos .log no diretorio

try:
    arquivos = os.listdir(caminho_diretorio)
    arquivos_log = [arquivo for arquivo in arquivos if arquivo.endswith('.log')]
    # Imprime mensagem se houver ou não arquivos .log no diretório
    if arquivos_log:
        print(f"Arquivos .log encontrados em '{caminho_diretorio}': ")
        for arquivo in arquivos_log:
            print(f" {arquivo}")
    else:
        print("Nenhum arquivo .log encontrato")
# Imprime mensagem se não encontrar o diretório
except FileNotFoundError:
        print(f"Diretório '{caminho_diretorio}' não encontrado")