

#Portas válidas (conhecidas)
while True:
    porta = int(input("Digite uma porta TCP: "))
    if porta >= 1 and porta <= 1024:
        print("Porta Conhecida")
        print(porta, "É uma porta válida")
    else:
        print("Porta desconhecida")
