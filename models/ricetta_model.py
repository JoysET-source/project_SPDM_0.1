from import_bridge import db


# Creazione della tabella Ricetta
class Ricetta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_ricetta = db.Column(db.String(100), unique=True, nullable=False)
    ingredienti = db.Column(db.String, nullable=False)
    kcal = db.Column(db.Integer, nullable=False)
    # immagini = db.Column(db.String(500), nullable=True)  # Aggiungi questo campo per memorizzare l'URL(il percorso) dell'immagine che sta su static
    # categoria = db.Column(db.String, nullable=False)
    # titolo = db.Column(db.String, nullable=False)
    # descrizione = db.Column(db.String, nullable=False)
    # visibility = db.Column(db.Boolean, nullable=False)
    # servings = db.Column(db.Integer, nullable=False)
    # preparation_time = db.Column(db.Integer, nullable=False)
    # coocking_time = db.Column(db.Integer, nullable=False)
    # total_time = db.Column(db.Integer, nullable=False)
    # steps = db.Column(db.String, nullable=False)
    # difficulty_level = db.Column(db.String, nullable=False)
    # cousine_type = db.Column(db.String, nullable=False)
    # autore = db.Column(db.String, nullable=False)
    # rating = db.Column(db.Integer, nullable=False)
    # tags = db.Column(db.String, nullable=False)
    # prezzo = db.Column(db.Integer, nullable=False)
    # created_at = db.Column(db.DateTime, nullable=False, default=func.now()) # Assegna la data automatica alla creazione
    # updated_at = db.Column(db.DateTime, nullable=False, default=func.now(), onupdate=func.now()) # Aggiorna ogni volta che viene modificato




