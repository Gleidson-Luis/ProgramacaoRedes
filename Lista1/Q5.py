# Verificação de portas abertas
while True:
    porta = int(input("Digite um número de porta: "))
    if porta == 80:
        print("A porta 80 é usada para HTTP.")
    elif porta == 443:
        print("A porta 443 é usada para HTTPS.")
    elif porta == 21:
        print("A porta 21 é usada para FTP.")
    elif porta == 22:
        print("A porta 22 é usada para SSH.")
    else:
        print("Porta desconhecida ou não convencional.")
