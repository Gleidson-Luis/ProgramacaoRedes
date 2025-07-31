# Criar um endpoint /echo que receba via POST qualquer dado JSON e devolva o mesmo conteúdo como resposta

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/echo')
def get_echo():
    dados = {"erro": "Nenhum JSON recebido"}
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)
