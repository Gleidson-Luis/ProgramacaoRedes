# Digite um endereço IP (ou 'fim' para terminar)
def validarIP(ip):
    ip_inicial = "192.168.1.1"
    ip_final = "192.168.1.254"
    if ip_inicial <= ip <= ip_final:
        return True
    else:
        return False

ips = []
while True:
    ip = input("Digite um endereço IP (ou 'fim' para terminar): ")
    if ip.lower() == "fim":
        break
    if validarIP(ip):
        ips.append(ip)
    
print("\nEndereços IP Válidos Cadastrados: ")
for ip in ips:
    print(ip)