import platform  # Detecta o sistema operacional (Windows, Linux...)
import subprocess  # Permite executar comandos externos (como o ping) via Python
import re  # Permite executar comandos externos (como o ping) via Python

def ping_media(endereco='8.8.8.8', vezes=5):
    sistema = platform.system()

    if sistema == 'Windows':
        comando = ['ping', '-n', str(vezes), endereco]
    else:
        comando = ['ping', '-c', str(vezes), endereco]

    resultado = subprocess.run(comando, capture_output=True, text=True)

    # Exibe a saída bruta (opcional)
    # print(resultado.stdout)

    # Extrair o tempo médio da resposta
    if sistema == 'Windows':
        match = re.search(r'Média = (\d+)ms', resultado.stdout)
    else:
        match = re.search(r'avg[/=](\d+\.\d+)', resultado.stdout)

    if match:
        print(f"\nTempo médio de resposta: {match.group(1)} ms")
    else:
        print("\nNão foi possível obter o tempo médio de resposta.")

# Executar o ping
ping_media()
