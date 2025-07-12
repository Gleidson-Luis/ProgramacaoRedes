from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de alunos (simulando um banco de dados)
alunos = [
    {"id": 1, "nome": "Joao", "idade": 20, "curso": "Engenharia"},
    {"id": 2, "nome": "Gabriel", "idade": 19, "curso": "Medicina"}
]

# Contador para gerar IDs únicos
proximo_id = 3

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Seja bem-vindo à API de Gerenciamento de Alunos!",
        "endpoints": {
            "GET /": "Pagina inicial",
            "GET /alunos": "Listar todos os alunos",
            "GET /alunos/<id>": "Buscar aluno por ID",
            "POST /alunos": "Criar novo aluno",
            "PUT /alunos/<id>": "Atualizar aluno",
            "DELETE /alunos/<id>": "Deletar aluno"
        }
    })

@app.route("/alunos", methods=["GET"])
def get_alunos():
    """Retorna todos os alunos"""
    return jsonify({
        "success": True,
        "data": alunos,
        "total": len(alunos)
    })

@app.route("/alunos/<int:id>", methods=["GET"])
def get_aluno(id):
    """Retorna um aluno específico por ID"""
    aluno = next((a for a in alunos if a["id"] == id), None)
    
    if aluno:
        return jsonify({
            "success": True,
            "data": aluno
        })
    else:
        return jsonify({
            "success": False,
            "error": "Aluno não encontrado"
        }), 404

@app.route("/alunos", methods=["POST"])
def criar_aluno():
    """Cria um novo aluno"""
    global proximo_id
    
    try:
        dados = request.get_json()
        
        # Validação dos dados obrigatórios
        if not dados or 'nome' not in dados:
            return jsonify({
                "success": False,
                "error": "Nome é obrigatório"
            }), 400
        
        # Criar novo aluno
        novo_aluno = {
            "id": proximo_id,
            "nome": dados["nome"],
            "idade": dados.get("idade", None),
            "curso": dados.get("curso", None)
        }
        
        alunos.append(novo_aluno)
        proximo_id += 1
        
        return jsonify({
            "success": True,
            "message": "Aluno criado com sucesso",
            "data": novo_aluno
        }), 201
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/alunos/<int:id>", methods=["PUT"])
def atualizar_aluno(id):
    """Atualiza um aluno existente"""
    try:
        dados = request.get_json()
        
        # Encontrar o aluno
        aluno = next((a for a in alunos if a["id"] == id), None)
        
        if not aluno:
            return jsonify({
                "success": False,
                "error": "Aluno não encontrado"
            }), 404
        
        # Atualizar dados
        if "nome" in dados:
            aluno["nome"] = dados["nome"]
        if "idade" in dados:
            aluno["idade"] = dados["idade"]
        if "curso" in dados:
            aluno["curso"] = dados["curso"]
        
        return jsonify({
            "success": True,
            "message": "Aluno atualizado com sucesso",
            "data": aluno
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/alunos/<int:id>", methods=["DELETE"])
def deletar_aluno(id):
    """Deleta um aluno"""
    global alunos
    
    # Encontrar o aluno
    aluno = next((a for a in alunos if a["id"] == id), None)
    
    if not aluno:
        return jsonify({
            "success": False,
            "error": "Aluno não encontrado"
        }), 404
    
    # Remover aluno da lista
    alunos = [a for a in alunos if a["id"] != id]
    
    return jsonify({
        "success": True,
        "message": "Aluno deletado com sucesso",
        "data": aluno
    })

@app.route("/alunos/buscar", methods=["GET"])
def buscar_alunos():
    """Busca alunos por nome ou curso"""
    nome = request.args.get("nome", "").lower()
    curso = request.args.get("curso", "").lower()
    
    resultados = alunos
    
    if nome:
        resultados = [a for a in resultados if nome in a["nome"].lower()]
    
    if curso:
        resultados = [a for a in resultados if a.get("curso") and curso in a["curso"].lower()]
    
    return jsonify({
        "success": True,
        "data": resultados,
        "total": len(resultados),
        "filtros": {
            "nome": nome if nome else None,
            "curso": curso if curso else None
        }
    })

@app.errorhandler(404)
def nao_encontrado(error):
    return jsonify({
        "success": False,
        "error": "Endpoint não encontrado"
    }), 404

@app.errorhandler(500)
def erro_servidor(error):
    return jsonify({
        "success": False,
        "error": "Erro interno do servidor"
    }), 500

if __name__ == "__main__":
    print("🚀 Iniciando API Flask...")
    print("📍 Acesse: http://localhost:5000")
    print("📖 Documentação: http://localhost:5000/")
    app.run(debug=True, port=5000)