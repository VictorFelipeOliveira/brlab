# -*- coding: iso-8859-1 -*-

from flask import Flask
app = Flask(__name__)

from app.controllers import routes