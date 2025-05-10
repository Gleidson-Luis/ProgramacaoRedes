#Velocidade de Download
while True:
    velocidade = int(input("Digite a velocidade em Mbps: "))
    if velocidade < 10:
        print("Conexão Lenta!")
    elif velocidade >= 10 and velocidade <= 100:
        print("Conexão Normal!")
    else:
        print("Conexão Rápida!")