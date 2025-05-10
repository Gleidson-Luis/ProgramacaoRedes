# Lista para armazenar as latências
latencias = []

print("Digite a latência (em ms) de cada servidor. Digite -1 para encerrar.")

# Loop para coletar latências
while True:
    entrada = float(input("Latência do servidor: "))
    if entrada == -1:
        break
    latencias.append(entrada)

# Verifica se houve entradas válidas
if latencias:
    menor_latencia = min(latencias)
    print(f"\nA menor latência registrada foi: {menor_latencia} ms")
else:
    print("\nNenhuma latência foi inserida.")