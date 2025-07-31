# Monitorar a CPU do sistema e registrar em arquivo .txt

import psutil # biblioteca multiplataforma para recuperar informações sobre processos em execução e utilização do sistema (CPU, memória, discos, rede, sensores) em Python.
import time
from datetime import datetime

print("Monitorando CPU por 30 segundos (10 leituras a cada 3s)...")

# Abre o arquivo para escrita
with open('cpu_log.txt', 'w', encoding='utf-8') as f:
    f.write("=== Monitor de CPU ===\n")
    f.write("Data/Hora\t\tCPU (%)\n")
    f.write("-" * 35 + "\n")
    
    # 10 iterações a cada 3 segundos
    for i in range(10):
        # Obtém o uso de CPU
        cpu_percent = psutil.cpu_percent(interval=1)
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Registra no arquivo
        f.write(f"{timestamp}\t{cpu_percent:.1f}%\n")
        
        # Mostra na tela
        print(f"[{i+1}/10] {timestamp} - CPU: {cpu_percent:.1f}%")
        
        # Aguarda 3 segundos (menos 1s já usado no cpu_percent)
        if i < 9:  # Não espera na última iteração
            time.sleep(2)

# Imprime a conclusão do processo
print("\nMonitoramento concluído! Verifique o arquivo 'cpu_log.txt'")