from app.models import db

class Laboratorio(db.Model):
    __tablename__ = 'laboratorios'
    sequencial = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True)
    descricao = db.Column(db.String(255))
    # url = db.Column()
    # uri =
    # criador = 
    # administrador_lab = 
    # data_criacao = 
    # modo_acesso = 
    # estado = 
    # dados_tecnicos =
    # requisitos=
    equipamentos = db.relationship('Equipamento', backref="laboratorio", lazy=True)
    

    def __init__(self):
        nome = self.nome
        descricao = self.descricao

    def __repr__(self):
        return ' Laboratório {0}: {1}'.format(self.nome, self.descricao)
