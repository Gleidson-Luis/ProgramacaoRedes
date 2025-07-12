from flask import Flask, request, jsonify

app = Flask(__name__)

alunos = [{"id" : 1, "nome" : "Joao"}, {"id" : 2, "nome" : "Gabriel"}]

@app.route("/", methods=["GET"])
def home():
    return "Seja bem vindo."

@app.route("/buscar_aluno", methods=["GET"])
def buscarAluno():
    nome = request.args.get("nome")
    for aluno in alunos:
        if aluno.get("nome") == nome:
            return jsonify(aluno)
        return jsonify("{}}")
     
@app.route("/alunos", methods=["GET"])
def getAlunos():
    return jsonify(alunos)

@app.route("/alunos/<int:id>", methods=["GET"])
def getAluno(id):
    for aluno in alunos:
        if aluno.get("id") == id:
            return jsonify(aluno)
    return jsonify("{}")

@app.route("/alunos", methods=["POST"])
def salvarAluno(id):
    dados = request.get_json()
    alunos.append(dados)
    return jsonify("sucesso")

if __name__ == "__main__":
    app.run(debug = True, port = 5000)