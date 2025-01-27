from config import ma
from models import Agendamento, Contato, Usuario

class AgendamentoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Agendamento

class ContatoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Contato

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
