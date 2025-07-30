# Criar servidor TCP simples

import socket

# Configurações do servidor
HOST = 'localhost'  # Endereço do servidor
PORT = 8080         # Porta do servidor

# Criar socket TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Permitir reutilizar o endereço
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    # Vincular socket ao endereço e porta
    servidor.bind((HOST, PORT))
    
    # Começar a escutar conexões (máximo 5 na fila)
    servidor.listen(5)
    print(f"Servidor TCP rodando em {HOST}:{PORT}")
    print("Aguardando conexões...")
    
    while True:
        # Aceitar conexão
        cliente, endereco = servidor.accept()
        
        # Exibir mensagem com IP do cliente
        print(f"Conexão recebida de: {endereco[0]}")
        
        # Fechar conexão com o cliente
        cliente.close()
        
except KeyboardInterrupt:
    print("\nServidor interrompido pelo usuário")
except Exception as e:
    print(f"Erro: {e}")
finally:
    # Fechar socket do servidor
    servidor.close()
    print("Servidor fechado")