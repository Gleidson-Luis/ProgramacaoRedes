# Número de dispositivos conectados no WI-FI
while True:
    numero = int(input("Digite o número de dispositivos conectados no WI-FI: "))
    if numero > 10:
        print("Muitos dispositivos conectados!")
    else:
        print("Número de dispositivos suportados!")