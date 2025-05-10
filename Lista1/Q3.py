# Se o número IP pertence a rede 192.168.1.0/24
while True:
    ip = input("Digite o número IP: ")
    ip_inicial = "192.168.1.1"
    ip_final = "192.168.1.254"
    if ip_inicial <= ip <= ip_final:
        print("O IP pertence a rede!")
        break
    else:
        print("O IP não pertence a rede!")