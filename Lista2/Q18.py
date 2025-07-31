
# Script que leia uma lista de IPs e gere um arquivo com regras
# Lê os IPs do arquivo de entrada
with open('ips_bloqueados.txt', 'r') as arquivo_entrada:
    ips = arquivo_entrada.readlines()

# Cria o arquivo de saída com regras de bloqueio
with open('firewall_rules.txt', 'w') as arquivo_saida:
    for ip in ips:
        ip_limpo = ip.strip()  # remove espaços e quebras de linha
        if ip_limpo:  # garante que a linha não está vazia
            regra = f"block ip {ip_limpo}\n"
            arquivo_saida.write(regra)

# Imprime o resultado da geração do arquivo
print("Regras de firewall geradas com sucesso em 'firewall_rules.txt'.")
