from app.models import *
from app.models import db

def cria_tabelas():
    if db:
        db.create_all()
        print(db)
        return True
    return False
    