# Lê um arquivo .log
# Módulo para impressões regulares
import re

# Nome do arquivo de log
arquivo_log = "sistema.log"

# Lê o arquivo e conta as ocorrências
with open(arquivo_log, 'r', encoding='utf-8') as f:
    conteudo = f.read().lower()  # Converte para minúsculas para busca case-insensitive
    
    timeout_count = conteudo.count('timeout')
    connection_refused_count = conteudo.count('connection refused')

print(f"Arquivo: {arquivo_log}")
print(f"'timeout': {timeout_count} ocorrências")
print(f"'connection refused': {connection_refused_count} ocorrências")
print(f"Total: {timeout_count + connection_refused_count} ocorrências")