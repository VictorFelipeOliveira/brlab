from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://root:root@localhost/brlab-base'
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_PASSWORD_SALT'] = 'super-secret-random-salt'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True
db = SQLAlchemy(app)

#Define Models

roles_users = db.Table('roles_users',
db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin): #UserMixin
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users',lazy='dynamic'))

    def __init__(self, username, email, password):#,, active, confirmed_at
        self.username = username
        self.email = email
        self.password = encrypt_password(password)
        # self.active = active
        # self.confirmed_at = confirmed_at

    def __repr__(self):
        return '<User %r>' % self.username

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# @app.before_first_request
# def create_user():
#     db.create_all()
#     user_datastore.create_user(username='admin', email='admin@admin.com', password='admin')
#     db.session.commit()

@app.route('/')
def index():
    return render_template("add_user.html")
    myUser = User.query.all()
    oneItem = User.query.filter_by(email='admin').all()
    return render_template("add_user.html", myUser=myUser, oneItem=oneItem)

@app.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username = username).first()
    return render_template("profile.html", user=user)

@app.route('/post_user',methods=['POST'])
def post_user():
    user = User(request.form['username'], request.form['email'], request.form['password'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
