#Lê um arquivo e conta quantos IPs estão listados

def contar_ips(arquivo="ips.txt"):
    try:
        with open(arquivo, 'r') as file:
            linhas = file.readlines()
# Remove linhas vazias
            ips = [linha.strip() for linha in linhas if linha.strip()]
            print(f"Total de IPs encontrados: {len(ips)}")
            
# Exibe os IPs encontrados
            if ips:
                print("\nIPs listados:")
                for i, ip in enumerate(ips, 1):
                    print(f"{i}. {ip}")
                    
    except FileNotFoundError:
        print(f"Arquivo '{arquivo}' não encontrado")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

# Executa o script
if __name__ == "__main__":
    contar_ips()