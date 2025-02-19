from flask import Flask, jsonify, request
from flask_cors import CORS
import pymysql.cursors

app = Flask(__name__)
CORS(app)

# Configuração do banco de dados
db = pymysql.connect(
    host='localhost',
    user='root',
    password='sua_senha',
    database='clinica_estetica',
    cursorclass=pymysql.cursors.DictCursor
)

# Rotas para Clientes
@app.route('/clientes', methods=['GET'])
def listar_clientes():
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
    return jsonify(clientes)

@app.route('/clientes/<int:id>', methods=['GET'])
def obter_cliente(id):
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM clientes WHERE id = %s", (id,))
        cliente = cursor.fetchone()
    return jsonify(cliente)

@app.route('/clientes', methods=['POST'])
def criar_cliente():
    dados = request.json
    with db.cursor() as cursor:
        sql = "INSERT INTO clientes (nome, telefone, email) VALUES (%s, %s, %s)"
        cursor.execute(sql, (dados['nome'], dados['telefone'], dados['email']))
        db.commit()
    return jsonify({"mensagem": "Cliente criado com sucesso!"}), 201

@app.route('/clientes/<int:id>', methods=['PUT'])
def atualizar_cliente(id):
    dados = request.json
    with db.cursor() as cursor:
        sql = "UPDATE clientes SET nome = %s, telefone = %s, email = %s WHERE id = %s"
        cursor.execute(sql, (dados['nome'], dados['telefone'], dados['email'], id))
        db.commit()
    return jsonify({"mensagem": "Cliente atualizado com sucesso!"})

@app.route('/clientes/<int:id>', methods=['DELETE'])
def deletar_cliente(id):
    with db.cursor() as cursor:
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
        db.commit()
    return jsonify({"mensagem": "Cliente deletado com sucesso!"})

# Rotas para Profissionais (similares às de Clientes)
@app.route('/profissionais', methods=['GET'])
def listar_profissionais():
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM profissionais")
        profissionais = cursor.fetchall()
    return jsonify(profissionais)

@app.route('/profissionais/<int:id>', methods=['GET'])
def obter_profissional(id):
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM profissionais WHERE id = %s", (id,))
        profissional = cursor.fetchone()
    return jsonify(profissional)

@app.route('/profissionais', methods=['POST'])
def criar_profissional():
    dados = request.json
    with db.cursor() as cursor:
        sql = "INSERT INTO profissionais (nome, especialidade) VALUES (%s, %s)"
        cursor.execute(sql, (dados['nome'], dados['especialidade']))
        db.commit()
    return jsonify({"mensagem": "Profissional criado com sucesso!"}), 201

@app.route('/profissionais/<int:id>', methods=['PUT'])
def atualizar_profissional(id):
    dados = request.json
    with db.cursor() as cursor:
        sql = "UPDATE profissionais SET nome = %s, especialidade = %s WHERE id = %s"
        cursor.execute(sql, (dados['nome'], dados['especialidade'], id))
        db.commit()
    return jsonify({"mensagem": "Profissional atualizado com sucesso!"})

@app.route('/profissionais/<int:id>', methods=['DELETE'])
def deletar_profissional(id):
    with db.cursor() as cursor:
        cursor.execute("DELETE FROM profissionais WHERE id = %s", (id,))
        db.commit()
    return jsonify({"mensagem": "Profissional deletado com sucesso!"})

# Rotas para Serviços (similares às de Clientes)
@app.route('/servicos', methods=['GET'])
def listar_servicos():
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM servicos")
        servicos = cursor.fetchall()
    return jsonify(servicos)

@app.route('/servicos/<int:id>', methods=['GET'])
def obter_servico(id):
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM servicos WHERE id = %s", (id,))
        servico = cursor.fetchone()
    return jsonify(servico)

@app.route('/servicos', methods=['POST'])
def criar_servico():
    dados = request.json
    with db.cursor() as cursor:
        sql = "INSERT INTO servicos (nome_servico, descricao, preco) VALUES (%s, %s, %s)"
        cursor.execute(sql, (dados['nome_servico'], dados['descricao'], dados['preco']))
        db.commit()
    return jsonify({"mensagem": "Serviço criado com sucesso!"}), 201

@app.route('/servicos/<int:id>', methods=['PUT'])
def atualizar_servico(id):
    dados = request.json
    with db.cursor() as cursor:
        sql = "UPDATE servicos SET nome_servico = %s, descricao = %s, preco = %s WHERE id = %s"
        cursor.execute(sql, (dados['nome_servico'], dados['descricao'], dados['preco'], id))
        db.commit()
    return jsonify({"mensagem": "Serviço atualizado com sucesso!"})

@app.route('/servicos/<int:id>', methods=['DELETE'])
def deletar_servico(id):
    with db.cursor() as cursor:
        cursor.execute("DELETE FROM servicos WHERE id = %s", (id,))
        db.commit()
    return jsonify({"mensagem": "Serviço deletado com sucesso!"})

# Rotas para Agendamentos
@app.route('/agendamentos', methods=['GET'])
def listar_agendamentos():
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM agendamentos")
        agendamentos = cursor.fetchall()
    return jsonify(agendamentos)

@app.route('/agendamentos/<int:id>', methods=['GET'])
def obter_agendamento(id):
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM agendamentos WHERE id = %s", (id,))
        agendamento = cursor.fetchone()
    return jsonify(agendamento)

@app.route('/agendamentos', methods=['POST'])
def criar_agendamento():
    dados = request.json
    with db.cursor() as cursor:
        sql = """
        INSERT INTO agendamentos (cliente_id, servico_id, profissional_id, data_hora, status)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (
            dados['cliente_id'],
            dados['servico_id'],
            dados['profissional_id'],
            dados['data_hora'],
            dados.get('status', 'pendente')
        ))
        db.commit()
    return jsonify({"mensagem": "Agendamento criado com sucesso!"}), 201

@app.route('/agendamentos/<int:id>', methods=['PUT'])
def atualizar_agendamento(id):
    dados = request.json
    with db.cursor() as cursor:
        sql = """
        UPDATE agendamentos
        SET cliente_id = %s, servico_id = %s, profissional_id = %s, data_hora = %s, status = %s
        WHERE id = %s
        """
        cursor.execute(sql, (
            dados['cliente_id'],
            dados['servico_id'],
            dados['profissional_id'],
            dados['data_hora'],
            dados['status'],
            id
        ))
        db.commit()
    return jsonify({"mensagem": "Agendamento atualizado com sucesso!"})

@app.route('/agendamentos/<int:id>', methods=['DELETE'])
def deletar_agendamento(id):
    with db.cursor() as cursor:
        cursor.execute("DELETE FROM agendamentos WHERE id = %s", (id,))
        db.commit()
    return jsonify({"mensagem": "Agendamento deletado com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)