from models.ricetta_model import Ricetta
from app import db

# convertitore minuti => HH:MM
def format_time(minutes):
    if minutes is None:
        return "00:00"
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours:02d}:{mins:02d}"

# calcola il tempo totale
def total_time():
    ricette = Ricetta.query.all()
    for ricetta in ricette:
        total_time = (ricetta.preparation_time or 0) + (ricetta.cooking_time or 0)
        ricetta.total_time = format_time(total_time)

    db.session.commit()






















