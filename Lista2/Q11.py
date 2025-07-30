# Adicionar um endpoint /dispositivo do tipo GET

from flask import Flask, jsonify

# Criar aplicação Flask
app = Flask(__name__)

# Endpoint /status
@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        "message": "API funcionando corretamente",
        "status": "ok"
    })

# Lista pré-definida de dispositivos conectados
dispositivos_conectados = ["roteador", "switch", "notebook", "smartphone", "impressora"]

# Endpoint /dispositivos
@app.route('/dispositivos', methods=['GET'])
def dispositivos():
    return jsonify({
        "dispositivos": dispositivos_conectados,
        "total": len(dispositivos_conectados)
    })

# Endpoint raiz (opcional)
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Bem-vindo à API REST",
        "endpoints": ["/status", "/dispositivos"]
    })

if __name__ == '__main__':
    # Executar servidor Flask
    print("Iniciando API REST...")
    print("Acesse: http://localhost:5000/status")
    print("       http://localhost:5000/dispositivos")
    app.run(
        host='0.0.0.0',  # Aceita conexões de qualquer IP
        port=5000,       # Porta padrão do Flask
        debug=True       # Modo debug (reinicia automaticamente)
    )