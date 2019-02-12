from app import app
from flask import redirect, url_for
from flask_admin import Admin, AdminIndexView, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from app.models import db
from app.models.usuario import Usuario
from app.models.papel import Papel
from app.models.laboratorio import Laboratorio
from app.models.equipamento import Equipamento

class HomeView(BaseView):
    @expose('/')
    def index(self):
        redirect(url_for('index'))

def cria_views_admin():
    admin = Admin(app, name="administrador", template_mode='bootstrap3')
    admin.add_view(ModelView(Usuario, db.session))
    admin.add_view(ModelView(Papel, db.session))
    admin.add_view(ModelView(Laboratorio, db.session))
    admin.add_view(ModelView(Equipamento, db.session))
    admin.add_view(HomeView(name="BrLab - site", endpoint='/'))
