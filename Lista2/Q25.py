# Adicionar endpoint /Ips no Flask que permita adicionar IPs ia POST e listar via GET

from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista para armazenar os IPs recebidos
lista_ips = []

@app.route('/ips', methods=['POST', 'GET'])
def gerenciar_ips():
    if request.method == 'POST':
        dados = request.get_json()
        ip = dados.get('ip')

        if not ip:
            return jsonify({'erro': 'Campo "ip" é obrigatório'}), 400

        lista_ips.append(ip)
        return jsonify({'mensagem': f'IP {ip} adicionado com sucesso'})

    elif request.method == 'GET':
        return jsonify({'ips': lista_ips})

# Executa o script
if __name__ == '__main__':
    app.run(debug=True)
