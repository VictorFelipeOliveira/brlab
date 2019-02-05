from app.models import db, engine
from sqlalchemy.orm import sessionmaker

class Laboratorio(db.Model):
    __tablename__ = 'laboratorios'
    # __bind_key__ = 'laboratorios'
    sequencial = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True)
    descricao = db.Column(db.String(255))
    equipamentos = db.relationship('Equipamento', backref="laboratorio", lazy=True)
    

    def __init__(self):
        nome = self.nome
        descricao = self.descricao

    def __repr__(self):
        return ' Laboratório {0}: {1}'.format(self.nome, self.descricao)

# db.create_all()
# Session = sessionmaker(bind=engine)