# Ler a quantidade de uploads e downloads realizados na rede durante o dia e exiba o total de dados transferidos
# Solicita os dados ao usuário
uploads = float(input("Informe a quantidade de uploads (em MB): "))
downloads = float(input("Informe a quantidade de downloads (em MB): "))

# Calcula o total transferido
total = uploads + downloads

# Exibe o resultado
print(f"\nTotal de dados transferidos: {total:.2f} MB")
