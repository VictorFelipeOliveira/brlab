from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://root:root@localhost/brlab-base'
db = SQLAlchemy(app)

from app.controllers import default
