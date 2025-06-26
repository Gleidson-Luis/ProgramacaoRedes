# Verificar se processo está rodando

import psutil

# Nome do processo que você quer verificar
nome_processo = input("Digite o nome do processo: ")
processo_ativo = False
for processo in psutil.process_iter(["name"]):
    if processo.info["name"] == nome_processo:
        processo_ativo = True 

if processo_ativo:
    print(f"O processo '{nome_processo}' está em execução.")
else:
    print(f"O processo '{nome_processo}' NÃO está em execução.")
