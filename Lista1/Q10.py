import os

nome_pasta = input("Digite o nome da paste que deseja criar: ")
# Obtém o caminho completo onde a pasta será criada (no diretório atual)
caminho_pasta = os.path.join(os.getcwd(), nome_pasta)

# Verifica se a pasta já existe e a cria se não existir
if not os.path.exists(caminho_pasta):
    os.makedirs(caminho_pasta)
    print(f"Pasta '{nome_pasta}' criada com sucesso em {caminho_pasta}")
else:
    print(f"A pasta '{nome_pasta}' já existe!")