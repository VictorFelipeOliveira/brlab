from app.models import db

class Equipamento(db.Model):
    __tablename__ = 'equipamentos'
    sequencial = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True)
    descricao = db.Column(db.String(255))
    laboratorio_id = db.Column(db.Integer, db.ForeignKey('laboratorios.sequencial'), nullable=False)

    def __init__(self):
        nome = self.nome
        descricao = self.descricao

    def __repr__(self):
        return ' Equipamento {0}: {1}'.format(self.nome, self.descricao)
