# -*- coding: iso-8859-1 -*-
from flask import Flask

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    SECRET_KEY='secret_xxx'
)

from app.controllers import routes
from app.models import admin



admin.cria_views_admin()

