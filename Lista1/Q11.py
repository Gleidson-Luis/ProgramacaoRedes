#Listar arquivos com extensão .txt

import os

def lista_arquivos_txt(pasta):
    for arquivo in os.listdir(pasta):
        if os.path.isfile(os.path.join(pasta, arquivo)) and arquivo.endswith('.txt'):
            print(arquivo)

pasta = r"C:\Users\20241144030001\Documents"
lista_arquivos_txt(pasta)