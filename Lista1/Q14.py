# Escreva um script que renomeie todos os arquivos de uma pasta,
import os

diretorio = r"C:\PastaTeste"

for nome_arquivo in os.listdir(diretorio):
    caminho_antigo = os.path.join(diretorio, nome_arquivo)
    
    # Verifica se é um arquivo (evita renomear pastas)
    if os.path.isfile(caminho_antigo):
        novo_nome = "novo_" + nome_arquivo
        caminho_novo = os.path.join(diretorio, novo_nome)
        
        os.rename(caminho_antigo, caminho_novo)

print("Renomeação concluída!")