# -*- coding: iso-8859-1 -*-
from app import app
from sqlalchemy import create_engine, MetaData
# from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy.orm import 
# from sqlalchemy.ext.declarative import declarative_base
from app.models import *

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/brlab_base'
app.config['SECRET_KEY'] = 'super-secret-key'
app.config['SECURITY_PASSWORD_SALT'] = 'super-secret-random-salt'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True
db = SQLAlchemy(app)
url = app.config['SQLALCHEMY_DATABASE_URI']
engine = create_engine(url, echo=True)
# from app.controllers import default
# db.create_all()
