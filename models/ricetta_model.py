from sqlalchemy import func

from import_bridge import db


# Creazione della tabella Ricetta
class Ricetta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_ricetta = db.Column(db.String(100), unique=True, nullable=False)
    ingredienti = db.Column(db.String, nullable=True)
    kcal = db.Column(db.Integer, nullable=True)
    immagine = db.Column(db.String(500), nullable=True)  # Aggiungi questo campo per memorizzare l'URL(il percorso) dell'immagine che sta su static
    categoria = db.Column(db.String, nullable=False)
    titolo = db.Column(db.String, nullable=True)
    descrizione = db.Column(db.String, nullable=True)
    visibility = db.Column(db.Boolean, nullable=True)
    servings = db.Column(db.Integer, nullable=True)
    preparation_time = db.Column(db.Integer, nullable=True)
    cooking_time = db.Column(db.Integer, nullable=True)
    total_time = db.Column(db.Integer, nullable=True)
    steps = db.Column(db.String, nullable=True)
    difficulty_level = db.Column(db.String, nullable=False)
    cousine_type = db.Column(db.String, nullable=True)
    autore = db.Column(db.String, nullable=True)
    rating = db.Column(db.Integer, nullable=True)
    tags = db.Column(db.String, nullable=True)
    prezzo = db.Column(db.Integer, nullable=True)
    valuta = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, nullable=True, default=func.now()) # Assegna la data automatica alla creazione
    updated_at = db.Column(db.DateTime, nullable=True, default=func.now(), onupdate=func.now()) # Aggiorna ogni volta che viene modificato






