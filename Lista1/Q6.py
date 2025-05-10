# Lista para armazenar os nomes dos dispositivos
nomes = []

# Solicita 5 nomes ao usuário
for i in range(5):
    nome = input("Digite o nome do dispositivo: ")
    nomes.append(nome)

# Imprime todos os nomes usando um for
print("\nDispositivos digitados:")
for nome in nomes:
    print(nome)
