# Solicitar ao usuário o endereço MAC de um dispositivo

mac = input("Digite o endereço MAC de um dispositivo (formato XX:XX:XX:XX:XX): ")

if mac.startswith("00:1A:2B"):
    print("O dispositivo pertece ao fabricante X")
else:
    print("O dispositivo pertence a outro fabricante")
    