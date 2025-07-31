# Desenvolvimento de endpoint que receba um lista de latências e retorne o maior valor

from flask import Flask, request, jsonify

app = Flask(__name__)  # Inicia a aplicação flask

@app.route('/maior_latencia', methods=['POST'])
def maior_latencia():
    dados = request.get_json()
    latencias = dados.get('latencias', [])
    
    if not latencias:
        return jsonify({'erro': 'Lista de latências vazia ou ausente'}), 400
    
    maior = max(latencias)
    return jsonify({'maior_latencia': maior})


# Executa o script
if __name__ == '__main__':
    app.run(debug=True)
