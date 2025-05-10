# Solicita a quantidade de switches
quantidade_switches = int(input("Quantos switches existem na rede? "))

# Variável para acumular o total de portas ocupadas
total_portas_ocupadas = 0

# Para cada switch, perguntar quantas portas estão ocupadas
for i in range(1, quantidade_switches + 1):
    portas_ocupadas = int(input(f"Quantas portas estão ocupadas no switch {i}? "))
    total_portas_ocupadas += portas_ocupadas

# Exibir o total de portas ocupadas
print(f"\nTotal de portas ocupadas na rede: {total_portas_ocupadas}")