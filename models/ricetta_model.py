from sqlalchemy.sql import func
from import_bridge import db


# Creazione della tabella Ricetta
class Ricetta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_ricetta = db.Column(db.String(100), unique=True, nullable=False)
    ingredienti = db.Column(db.String, nullable=False)
    kcal = db.Column(db.Integer, nullable=False)
    # image_url = db.Column(db.String(500), nullable=True)  # Aggiungi questo campo per memorizzare l'URL(il percorso) dell'immagine che sta su static
    # category = db.Column(db.String, nullable=False)
    # title = db.Column(db.String, nullable=False)
    # description = db.Column(db.String, nullable=False)
    # visibility = db.Column(db.Boolean, nullable=False)
    # servings = db.Column(db.Integer, nullable=False)
    # preparation_time = db.Column(db.Integer, nullable=False)
    # coocking_time = db.Column(db.Integer, nullable=False)
    # total_time = db.Column(db.Integer, nullable=False)
    # steps = db.Column(db.String, nullable=False)
    # difficulty_level = db.Column(db.String, nullable=False)
    # cusine_type = db.Column(db.String, nullable=False)
    # author = db.Column(db.String, nullable=False)
    # rating = db.Column(db.Integer, nullable=False)
    # tags = db.Column(db.String, nullable=False)
    # price = db.Column(db.Integer, nullable=False)
    # created_at = db.Column(db.DateTime, nullable=False, default=func.now()) # Assegna la data automatica alla creazione
    # updated_at = db.Column(db.DateTime, nullable=False, default=func.now(), onupdate=func.now()) # Aggiorna ogni volta che viene modificato




