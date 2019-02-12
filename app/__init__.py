# -*- coding: iso-8859-1 -*-
from flask import Flask
<<<<<<< HEAD
from flask_admin import Admin, AdminIndexView, expose, BaseView
from flask_admin.contrib.sqla import ModelView
=======
>>>>>>> models

app = Flask(__name__)
admin = Admin(app, name="administrador", template_mode='bootstrap3')

<<<<<<< HEAD
from app.models import db

from app.models.papel import Papel
from app.models.usuario import Usuario
from app.models.laboratorio import Laboratorio
from app.models.equipamento import Equipamento
from app.controllers import routes


=======
from app.controllers import routes
from app.models import admin

admin.cria_views_admin()
>>>>>>> models
