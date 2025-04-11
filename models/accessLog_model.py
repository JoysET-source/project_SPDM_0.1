from datetime import datetime

from import_bridge import db
from models.user_model import User
from models.ricetta_model import Ricetta




# Creazione della tabella AccessLog
class AccessLog(db.Model):
    __tablename__ = 'access_log'
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    ip_address = db.Column(db.String(50), nullable=False)
    user_agent = db.Column(db.Text, nullable=False)
    action = db.Column(db.String(50), nullable=False)
    details = db.Column(db.Text, nullable=True)

    # collegamento con id specifico nella tabella user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    # Relationship with User model
    user = db.relationship('User', back_populates='access_logs')

    # questa la uso per vedere il nome della ricetta visitata
    ricetta_vista = db.Column(db.String(100), nullable=True)
    # collegamento con id specifico nella tabella ricetta
    ricetta_id = db.Column(db.Integer, db.ForeignKey('ricetta.id'), nullable=True)
    # Relationship with Ricetta model
    ricetta = db.relationship('Ricetta', back_populates='access_logs')


