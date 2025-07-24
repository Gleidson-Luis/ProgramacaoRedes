# Criar script que solicite o nome de um diretório e crie três subpastas chamadas "config", "logs" e 'backup.

import os

# Pedir o nome do diretório
nome_diretorio = input("Digite o nome do diretorio: ")

# Listar as subpastas
subpastas = ["config","logs","backup"]

# Cria o diretório principal
os.makedirs(nome_diretorio, exist_ok=True)
print(f"Diretorio '{nome_diretorio}' criado")

# Cria as subpastas  
for subpasta in subpastas:
    caminho = os.path.join(nome_diretorio,subpasta)
    os.makedirs(caminho,exist_ok=True)
    print(f"Subpasta '{subpasta}' criada")
          
print("Concluido")