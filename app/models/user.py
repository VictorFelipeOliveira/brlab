from flask_security import Security, UserMixin
from app.models import db
# from SQLAlchemyUserDatastore
# user_datastore = SQLAlchemyUserDatastore(db, User, Role)
# security = Security(app, user_datastore)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users',lazy='dynamic'))

    def __init__(self, email, password, active):
        self.email = email
        self.password = password
        self.active = active

    def __repr__(self):
        return '<User %r>' % self.email
