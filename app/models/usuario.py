from app.models import db


class Usuario(db.Model):
    sequencial = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)
    # active = db.Column(db.Boolean())
    # last_login = db.Column(db.DateTime)

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
        return '<Usuario {0} -> {1}'.format(self.username, self.email)
