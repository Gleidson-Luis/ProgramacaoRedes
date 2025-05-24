# Ler conteudo do arquivo e exiba quantas linhas possui

arquivo = open("Q5.py","r")
linhas = arquivo.readlines()
print(f"O arquivo {arquivo} possui {len(linhas)} linhas.")

arquivo.close()