from app.models import db


class Papel(db.Model):
    sequencial = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True)
    descricao = db.Column(db.String(255))

    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    def __repr__(self):
        return ' Papel {0}: {1}'.format(self.nome, self.descricao)
