# Criar uma API REST usando Flask

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

# Endpoint raiz (opcional)
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Bem-vindo à API REST",
        "endpoints": ["/status"]
    })

if __name__ == '__main__':
    # Executar servidor Flask
    print("Iniciando API REST...")
    print("Acesse: http://localhost:5000/status")
    app.run(
        host='0.0.0.0',  # Aceita conexões de qualquer IP
        port=5000,       # Porta padrão do Flask
        debug=True       # Modo debug (reinicia automaticamente)
    )