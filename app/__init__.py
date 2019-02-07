# -*- coding: iso-8859-1 -*-
from flask import Flask
from flask_admin import Admin, AdminIndexView, expose, BaseView
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
admin = Admin(app, name="administrador", template_mode='bootstrap3')

from app.models import db
# db.create_all()

from app.models.papel import Papel
from app.models.usuario import Usuario
from app.models.laboratorio import Laboratorio
from app.models.equipamento import Equipamento
from app.controllers import routes


