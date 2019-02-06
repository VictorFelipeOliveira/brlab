# -*- coding: iso-8859-1 -*-
from flask import Flask
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

from app.models import db
# db.create_all()

from app.models.usuario import Usuario
from app.models.papel import Papel
from app.models.laboratorio import Laboratorio
from app.models.equipamento import Equipamento

admin = Admin(app, name="administrador", template_mode='bootstrap3')
admin.add_view(ModelView(Papel, db.session))
admin.add_view(ModelView(Usuario, db.session))
admin.add_view(ModelView(Laboratorio, db.session))
admin.add_view(ModelView(Equipamento, db.session))
db.create_all()
from app.controllers import routes
