from flask_login import UserMixin
from main.import_bridge import db


# Creazione della tabella User
class User(db.Model, UserMixin):
    __bind_key__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # email = db.Column(db.String, nullable=True)
    username = db.Column(db.String(20), unique=True, nullable=True)
    password = db.Column(db.String(255), nullable=True)