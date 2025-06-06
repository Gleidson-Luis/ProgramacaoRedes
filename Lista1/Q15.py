# Leia um arquivo CSV e conte quantas linhas ele possui (sem considerar o cabeçalho)

import csv

arquivo_csv = "C:\PastaTeste\people-100.csv"

with open(arquivo_csv) as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)  # Ignora o cabeçalho
    contador = sum(1 for _ in leitor)

print(f"O arquivo contém {contador} linhas (sem contar o cabeçalho).")