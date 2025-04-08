from sqlalchemy import func

from import_bridge import db


# Creazione della tabella Ricetta
class Ricetta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_ricetta = db.Column(db.String(100), unique=True, nullable=False)
    ingredienti = db.Column(db.Text, nullable=True)
    kcal = db.Column(db.Integer, nullable=True)
    # Aggiungi questo campo per memorizzare l'URL(il percorso) dell'immagine che sta su static
    immagine = db.Column(db.String(100), nullable=True)
    categoria = db.Column(db.String(100), nullable=False)
    titolo = db.Column(db.String(100), nullable=True)
    descrizione = db.Column(db.String(5000), nullable=True)
    visibility = db.Column(db.Boolean, default=True)
    servings = db.Column(db.Integer, nullable=True)
    preparation_time = db.Column(db.Integer, nullable=True)
    cooking_time = db.Column(db.Integer, nullable=True)
    total_time = db.Column(db.Integer, nullable=True)
    steps = db.Column(db.Text, nullable=True)
    difficulty_level = db.Column(db.String(100), nullable=False)
    cousine_type = db.Column(db.String(100), nullable=True)
    autore = db.Column(db.String(100), nullable=True)
    rating = db.Column(db.Integer, nullable=True)
    tags = db.Column(db.String(100), nullable=True)
    prezzo = db.Column(db.Integer, nullable=True)
    valuta = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, nullable=True, default=func.now()) # Assegna la data automatica alla creazione
    updated_at = db.Column(db.DateTime, nullable=True, default=func.now(), onupdate=func.now()) # Aggiorna ogni volta che viene modificato
    access_logs = db.relationship('AccessLog', back_populates='ricetta') # collegamento a AccessLog model






