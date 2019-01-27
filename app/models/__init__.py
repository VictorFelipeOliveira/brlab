# -*- coding: iso-8859-1 -*-
from app import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/brlab_base'
app.config['SECRET_KEY'] = 'super-secret-key'
app.config['SECURITY_PASSWORD_SALT'] = 'super-secret-random-salt'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True
db = SQLAlchemy(app)
# db.create_all()

#from app.controllers import default
