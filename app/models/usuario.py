# from flask_security import UserMixin
from app.models import db
# from SQLAlchemyUserDatastore
# user_datastore = SQLAlchemyUserDatastore(db, User, Role)
# security = Security(app, user_datastore)


class Usuario(db.Model):
    sequencial = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True)
    senha = db.Column(db.String(255), nullable=False)
    # active = db.Column(db.Boolean())
    # confirmed_at = db.Column(db.DateTime())

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        # self.active = active

    def __repr__(self):
        return '<User %r>' % self.email
