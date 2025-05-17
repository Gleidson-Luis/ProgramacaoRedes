# Solicitar ao usuário o endereço MAC de um dispositivo

mac = input("Digite o endereço MAC de um dispositivo: ")

if mac.startswith("00:1A:2B"):
    print("O dispositivo pertece ao fabricante X")
else:
    print("O dispositivo pertence a outro fabricante")
    