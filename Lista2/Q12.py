# Implementação de endpoint /adicionar_dispositivo do tipo POST

from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista em memória para armazenar os dispositivos
dispositivos = []

@app.route('/adicionar_dispositivo', methods=['POST'])
def adicionar_dispositivo():
    try:
        # Recebe o JSON da requisição
        dados = request.get_json()
        
        # Verifica se o JSON foi enviado
        if not dados:
            return jsonify({'erro': 'JSON não fornecido'}), 400
        
        # Verifica se o nome do dispositivo está presente
        if 'nome' not in dados:
            return jsonify({'erro': 'Campo "nome" é obrigatório'}), 400
        
        nome_dispositivo = dados['nome']
        
        # Verifica se o nome não está vazio
        if not nome_dispositivo or nome_dispositivo.strip() == '':
            return jsonify({'erro': 'Nome do dispositivo não pode estar vazio'}), 400
        
        # Adiciona o dispositivo à lista
        dispositivos.append(nome_dispositivo.strip())
        
        return jsonify({
            'mensagem': 'Dispositivo adicionado com sucesso',
            'dispositivo': nome_dispositivo.strip(),
            'total_dispositivos': len(dispositivos)
        }), 201
        
    except Exception as e:
        return jsonify({'erro': f'Erro interno: {str(e)}'}), 500

# Endpoint adicional para listar dispositivos (útil para testes)
@app.route('/listar_dispositivos', methods=['GET'])
def listar_dispositivos():
    return jsonify({
        'dispositivos': dispositivos,
        'total': len(dispositivos)
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)