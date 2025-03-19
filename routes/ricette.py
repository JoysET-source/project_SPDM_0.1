import os

from flask import Blueprint, render_template, request, jsonify

from import_bridge import login_manager, db
from models.ricetta_model import Ricetta
from models.user_model import User


ricette_routes = Blueprint('ricette_routes', __name__)
# specifica il path contenente le ricette caricate
ricette_path = os.path.join("static", "Ricette")



#  questo chiama struttura come file per interfaccia home
@ricette_routes.route('/')
def home():
    return render_template("struttura.html")

# <categoria> è la parte dinamica dell'URL che identifica quale categoria è stata cliccata.
@ricette_routes.route("/categoria/<categoria>")
def categoria(categoria):
    # recuperiamo tutte le ricette appartenenti alla categoria scelta
    elenco_ricette = Ricetta.query.filter_by(categoria=categoria).all()
    # restituiamo gli attributi a categoria html per visualizzarle
    return render_template("categoria.html", categoria=categoria, elenco_ricette=elenco_ricette)

# dettaglio e`la parte che gestisce il dettaglio delle singole ricette
@ricette_routes.route("/dettaglio_ricette/<categoria>/<nome_ricetta>")
def dettaglio_ricetta(categoria, nome_ricetta):
    # chiamiamo dal DB la ricetta in base a nome e categoria
    ricetta = Ricetta.query.filter_by(nome_ricetta=nome_ricetta, categoria=categoria).first()
    # passa i parametri specificati a dettaglio_ricetta.html
    return render_template("dettaglio_ricetta.html", categoria=categoria, ricetta=ricetta)


# la seguente gestisce utenticazione utente per le sessioni utente
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ======================================================================================================================
@ricette_routes.route("/run_script")
def run_script():
    # Esegui lo script Python quando il pulsante viene premuto
    # Esegui il tuo script Python qui
    # print("Il pulsante è stato premuto!")
    return 'Script eseguito!'
# ======================================================================================================================


# sessione che gestisce elenco delle ricette inserite visualizzabili da utente
@ricette_routes.route("/elenco_ricette", methods=["GET"])
def elenco_ricette():
    elenco_ricette = Ricetta.query.all()
    elenco = []
    for ricetta in elenco_ricette:
        elenco.append({
            "nome_ricetta": ricetta.nome_ricetta,
        })
    return jsonify(elenco)

# esempio per visualizzazione parziale se non loggati
from flask_login import current_user
# @ricette_routes.route("/elenco_ricette", methods=["GET"])
# def elenco_ricette():
#     if current_user.is_authenticated:
#         # Utente loggato, restituisci tutte le ricette
#         elenco_ricette = Ricetta.query.all()
#     else:
#         # Utente non loggato, restituisci solo alcune ricette
#         elenco_ricette = Ricetta.query.limit(5).all()
#     return render_template("elenco_ricette.html")


# sessione per la ricerca della ricetta desiderata tramite barra di ricerca
@ricette_routes.route("/trova_ricetta", methods=["GET"])
def trova_ricetta():
    nome_ricetta = request.args.get("nome_ricetta") # Ottieni il valore del parametro nome_ricetta da JS
    ricetta = Ricetta.query.filter_by(nome_ricetta=nome_ricetta).first()
    if ricetta is None:
        return jsonify({"detail": "Ricetta non trovata"}),404
    return jsonify({
            "nome_ricetta": ricetta.nome_ricetta,
            "ingredienti": ricetta.ingredienti,
            "kcal": ricetta.kcal
            })






