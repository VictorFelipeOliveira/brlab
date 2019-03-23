# -*- coding: iso-8859-1 -*-
from flask import Flask

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    SECRET_KEY='secret_xxx'
)

# jinja_options = app.jinja_options.copy()
# jinja_options.update(dict(
#     block_start_string='{*',
#     block_end_string='*}',
#     variable_start_string='(%',
#     variable_end_string='%)',
#     comment_start_string='<#',
#     comment_end_string='#>'
# ))
# app.jinja_options = jinja_options

from app.controllers import routes
from app.models import admin



admin.cria_views_admin()
