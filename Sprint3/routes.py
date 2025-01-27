from flask import request, jsonify
from config import app, db
from models import Agendamento, Contato, Usuario
from schemas import AgendamentoSchema, ContatoSchema, UsuarioSchema

agendamento_schema = AgendamentoSchema()
agendamentos_schema = AgendamentoSchema(many=True)
contato_schema = ContatoSchema()
contatos_schema = ContatoSchema(many=True)
usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

# CRUD Agendamento
@app.route('/agendamentos', methods=['POST'])
def add_agendamento():
    nome_paciente = request.json['nome_paciente']
    procedimento = request.json['procedimento']
    data_horario = request.json['data_horario']
    new_agendamento = Agendamento(nome_paciente=nome_paciente, procedimento=procedimento, data_horario=data_horario)
    db.session.add(new_agendamento)
    db.session.commit()
    return agendamento_schema.jsonify(new_agendamento)

@app.route('/agendamentos', methods=['GET'])
def get_agendamentos():
    all_agendamentos = Agendamento.query.all()
    result = agendamentos_schema.dump(all_agendamentos)
    return jsonify(result)

@app.route('/agendamentos/<id>', methods=['GET'])
def get_agendamento(id):
    agendamento = Agendamento.query.get(id)
    return agendamento_schema.jsonify(agendamento)

@app.route('/agendamentos/<id>', methods=['PUT'])
def update_agendamento(id):
    agendamento = Agendamento.query.get(id)
    nome_paciente = request.json['nome_paciente']
    procedimento = request.json['procedimento']
    data_horario = request.json['data_horario']
    agendamento.nome_paciente = nome_paciente
    agendamento.procedimento = procedimento
    agendamento.data_horario = data_horario
    db.session.commit()
    return agendamento_schema.jsonify(agendamento)

@app.route('/agendamentos/<id>', methods=['DELETE'])
def delete_agendamento(id):
    agendamento = Agendamento.query.get(id)
    db.session.delete(agendamento)
    db.session.commit()
    return agendamento_schema.jsonify(agendamento)

# CRUD Contato
@app.route('/contatos', methods=['POST'])
def add_contato():
    nome_paciente = request.json['nome_paciente']
    mensagem = request.json['mensagem']
    new_contato = Contato(nome_paciente=nome_paciente, mensagem=mensagem)
    db.session.add(new_contato)
    db.session.commit()
    return contato_schema.jsonify(new_contato)

@app.route('/contatos', methods=['GET'])
def get_contatos():
    all_contatos = Contato.query.all()
    result = contatos_schema.dump(all_contatos)
    return jsonify(result)

@app.route('/contatos/<id>', methods=['GET'])
def get_contato(id):
    contato = Contato.query.get(id)
    return contato_schema.jsonify(contato)

@app.route('/contatos/<id>', methods=['PUT'])
def update_contato(id):
    contato = Contato.query.get(id)
    nome_paciente = request.json['nome_paciente']
    mensagem = request.json['mensagem']
    contato.nome_paciente = nome_paciente
    contacto.moriginalMessage: a
    db.session.commit()
    return contatos_schema.jsonify(contato)

@app.route('/contatos/<id>', methods=['DELETE'])
def delete_contato(id):
    contato = Contato.query.get(id)
    db.session.delete(contato)
    db.session.commit()
    return contato_schema.jsonify(contato)

# CRUD Usuário
@app.route('/usuarios', methods=['POST'])
def add_usuario():
    cpf = request.json['cpf']
    senha = request.json['senha']
    new_usuario = Usuario(cpf=cpf, senha=senha)
    db.session.add(new_usuario)
    db.session.commit()
    return usuario_schema.jsonify(new_usuario)

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    all_usuarios = Usuario.query.all()
    result = usuarios_schema.dump(all_usuarios)
    return jsonify(result)

@app.route('/usuarios/<id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuario.query.get(id)
    return usuario_schema.jsonify(usuario