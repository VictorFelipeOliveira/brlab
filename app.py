from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from werkzeug.security import generate_password_hash, check_password_hash

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
db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin): #UserMixin
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users',lazy='dynamic'))

    def __init__(self, email, password, active):#,, active, confirmed_at
        self.email = email
        self.password = password
        self.active = active

    def __repr__(self):
        return '<User %r>' % self.email
#
# FLask Security
#
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# @app.before_first_request
# def create_user():
#     db.create_all()
#     user = User(email='root@root.com', password='root', active=1)
#     db.session.add(user)
#     db.session.commit()
    # user_datastore.create_user(email='admin@admin.com', password='admin')
    # db.session.commit()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/profile/<email>')
@login_required
def profile(email):
    user = User.query.filter_by(email = email).first()
    return render_template("profile.html", user=user)


@app.route('/begin')
def begin():
    return render_template("contact.html");

@app.route('/labs')
def labs():
    return render_template("about.html");

@app.route('/publications')
def publications():
    return render_template("about.html");

@app.route('/projects')
def projects():
    return render_template("about.html");

@app.route('/partners')
def partners():
    return render_template("about.html");

@app.route('/about')
def about():
    return render_template("about.html");

@app.route('/contact')
def contact():
    return render_template("contact.html");


@app.route('/post_user',methods=['POST'])
def post_user():
    user = User(request.form['username'], request.form['email'], request.form['password'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))

# @app.route('/post_role',methods=['POST'])
# def post_role():
#     role = Role(request.form['name'], request.form['description'])
#     db.session.add(role)
#     db.session.commit()
#     return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
