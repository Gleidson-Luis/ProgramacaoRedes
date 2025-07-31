# Criar endpoint /latencia no Flask que recebe via POST um JSON  com o tempo de latência e retorne se está boa, média ou ruim

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/latencia', methods=['POST'])
def verificar_latencia():
    dados = request.get_json()
    latencia = dados.get('latencia')

    if latencia is None:
        return jsonify({'erro': 'Campo latencia não enviado'}), 400

    if latencia < 50:
        status = 'Boa'
    elif latencia < 150:
        status = 'Média'
    else:
        status = 'Ruim'

    return jsonify({'status': status})

if __name__ == '__main__':
    app.run(debug=True)
