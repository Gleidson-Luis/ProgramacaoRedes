# Peça o nome de uma pasta, crie e dentro dela gere 3 arquivos txt

import os

# Solicita o nome da pasta ao usuário
nome_pasta = input("Digite o nome da nova pasta: ")

# Cria a pasta (se não existir)
if not os.path.exists(nome_pasta):
    os.makedirs(nome_pasta)
    print(f"Pasta '{nome_pasta}' criada com sucesso.")
else:
    print(f"Pasta '{nome_pasta}' já existe.")

# Lista de nomes de arquivos a serem criados
arquivos = ['ip_config.txt', 'latencia.txt', 'status_rede.txt']

# Cria cada arquivo dentro da pasta
for nome_arquivo in arquivos:
    caminho = os.path.join(nome_pasta, nome_arquivo)
    with open(caminho, 'w') as f:
        f.write("")  # Cria arquivo vazio

# Imprime a conclusão do processo
print("Arquivos criados com sucesso dentro da pasta.")
