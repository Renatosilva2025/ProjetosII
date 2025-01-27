from config import db

class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_paciente = db.Column(db.String(100), nullable=False)
    procedimento = db.Column(db.String(100), nullable=False)
    data_horario = db.Column(db.DateTime, nullable=False)

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_paciente = db.Column(db.String(100), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
