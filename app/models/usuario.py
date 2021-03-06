from app.models import db
from flask_security import UserMixin

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    sequencial = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)
    last_login = db.Column(db.DateTime())
    last_logout = db.Column(db.DateTime())
    papel_id = db.Column(db.Integer, db.ForeignKey('papeis.sequencial'), nullable=False)
    papel = db.relationship('Papel', backref="usuario", lazy=True)
    
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.sequencial)

    def get(self):
        return self


    def __init__(self):
        # Usuario()
        username = self.username
        email = self.email
        password = self.password
        # self.active = active

    def __repr__(self):
        return self.username
