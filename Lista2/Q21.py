# Monitorar a conectividade de uma API REST a cada minuto e registre em um arquivo de monitoramento.

import time
import requests
from datetime import datetime

# URL da API a ser monitorada
url_api = "https://jsonplaceholder.typicode.com/posts"  # substitua pela URL desejada

# Loop infinito com verificação a cada 60 segundos
while True:
    try:
        resposta = requests.get(url_api, timeout=5)
        status = "online" if resposta.status_code == 200 else "offline"
    except:
        status = "offline"

    # Marca de tempo
    agora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Registro no log
    with open("monitoramento_api.log", "a") as log:
        log.write(f"{agora} - {status}\n")

    print(f"{agora} - {status}")
    time.sleep(60)  # espera 1 minuto
