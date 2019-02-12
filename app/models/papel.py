from app.models import db

class Papel(db.Model):
    __tablename__ = 'papeis'
    sequencial = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True)
    descricao = db.Column(db.String(255))
    usuarios = db.relationship('Usuario', backref="papel", lazy=True)

    def __init__(self):
        nome = self.nome
        descricao = self.descricao

    def __repr__(self):
<<<<<<< HEAD
        return ' Papel {0}: {1}'.format(self.nome, self.descricao)
=======
        return ' Usuario {0}: {1}'.format(self.nome, self.descricao)
>>>>>>> models
