# from app import debug
#
# class User(db.Model):
#     __tablename__ = "users"
#
#     id = db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.String(100), unique=True)
#     email = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(100))
#     name = db.Column(db.String(100))
#
#     def __init__(self, username, email, password, name):
#         self.username = username
#         self.email = email
#         self.password = password
#         self.name = name
#
#     def __repr__(self):
#         return "<User %r>" % self.username
#
# class Role(db.Model):
#     __tablename__ = "roles"
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(100), unique = True)
#     description = db.Column(db.String(200))
#
#     def __init__(self, name, description):
#         self.name = name
#         self.description = description
#
#
# roles_users = db.Table('roles_users',
#         db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#         db.Column('role_id', db.Integer, db.ForeignKey('role.id')))
