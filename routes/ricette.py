import os

from flask import Blueprint, render_template, request, jsonify, url_for
from flask_login import current_user, login_required
from sqlalchemy.sql.expression import func

from import_bridge import login_manager, db
from models.ricetta_model import Ricetta
from models.user_model import User
from routes.accessLog_routes import log_access


ricette_routes = Blueprint('ricette_routes', __name__)
# specifica il path contenente le ricette caricate
ricette_path = os.path.join("static", "Ricette")



#  questo chiama struttura come file per interfaccia home
@ricette_routes.route('/')
def home():
    # stabilisce la variabile per il 50% delle ricette
    percent_items_to_show = 0.5

    # conta tutte le ricette presenti nel DB
    total_items = Ricetta.query.count()

    # se non ci sono ricette nel DB restituisci la home vuota
    if total_items == 0:
        return render_template("struttura.html", ricette = [])

    # calcola la percentuale sul totale perche limit accetto solo integer
    items_to_show_count = int(total_items * percent_items_to_show)

    # filtra il 50% delle ricette visibili e le ordina casualmente
    ricette_giornaliere = Ricetta.query.filter_by(visibility=True).order_by(func.rand()).limit(items_to_show_count).all()

    # creiamo un set vuoto per evitare duplicati
    check_categorie = set()

    # creiamo una lista vuota per stoccare le ricette di categorie uniche
    ricette_categoria_unica = []

    # iteriamo e stocchiamo le ricette di categorie uniche
    for ricette in ricette_giornaliere:
        if ricette.categoria not in check_categorie:
            check_categorie.add(ricette.categoria)
            ricette_categoria_unica.append(ricette)

    log_access(
            action="visita_home",
            ricetta_vista=None,  # Non c'è una ricetta in questo caso
            ricetta_id=None
    )

    # Passiamo le ricette uniche al template
    return render_template("struttura.html", ricette_categoria_unica=ricette_categoria_unica)


# <categoria> è la parte dinamica dell'URL che identifica quale categoria è stata cliccata.
# e ne fornisce anche l`immagine di sfondo in diversi formati
@ricette_routes.route("/categoria/<categoria>")
def categoria(categoria):
    # Recuperiamo tutte le ricette appartenenti alla categoria scelta
    elenco_ricette = Ricetta.query.filter_by(categoria=categoria).all()

    # Percorso della cartella degli sfondi
    sfondi_dir = os.path.join("static", "sfondi")

    # Possibili estensioni
    estensioni = [".jpg", ".jpeg", ".png"]

    # Troviamo il file esistente
    sfondo_finale = None
    for estensione in estensioni:
        sfondo_file = f"{categoria}_sfondo{estensione}"
        if os.path.exists(os.path.join(sfondi_dir, sfondo_file)):
            sfondo_finale = sfondo_file
            break

    # Se non trova nessuna immagine, usa un'immagine di default
    if not sfondo_finale:
        sfondo_finale = "default.jpg"

    # Passiamo l'immagine scelta al template
    return render_template("categoria.html", categoria=categoria, elenco_ricette=elenco_ricette,
                           sfondo_finale=sfondo_finale)


# dettaglio e`la parte che gestisce il dettaglio delle singole ricette
@ricette_routes.route("/dettaglio_ricette/<categoria>/<nome_ricetta>")
def dettaglio_ricetta(categoria, nome_ricetta):

    # chiamiamo dal DB la ricetta in base a nome e categoria
    ricetta = Ricetta.query.filter_by(nome_ricetta=nome_ricetta, categoria=categoria).first()

    # Qui registri l'accesso al log
    log_access(
            action="visualizzazione_ricetta",  # Definisci l'azione, per esempio 'visualizzazione_ricetta'
            ricetta_vista=ricetta.nome_ricetta,  # Nome della ricetta che l'utente ha visualizzato
            ricetta_id=ricetta.id  # ID della ricetta
    )

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

    # Utente loggato, restituisci tutte le ricette
    elenco_ricette = Ricetta.query.order_by(Ricetta.visibility.desc()).all()


    return render_template("elenco_ricette_utente.html", elenco_ricette=elenco_ricette)

# esempio per visualizzazione parziale se non loggati
# from flask_login import current_user
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
    nome_ricetta = request.args.get("nome_ricetta").lower()
    # se non inserito il nome della ricetta o minore di 3 lettere
    if not nome_ricetta or len(nome_ricetta) < 3:
        return render_template("struttura.html", alert="Inserisci un nome valido")

    # cerca tutte le ricette che contengono il nome inserito anche se parziale
    elenco_ricette = Ricetta.query.filter(Ricetta.nome_ricetta.ilike(f"%{nome_ricetta}%")).all()

    if elenco_ricette:
        return render_template("elenco_ricette_utente.html", elenco_ricette=elenco_ricette)

    return render_template("struttura.html", errore="Ricetta non trovata")



# sessione per gestire ricerca ricette in base alle calorie
@ricette_routes.route("/trova_calorie", methods=["GET"])
def trova_calorie():
    calorie = request.args.get("kcal") # Ottieni il valore del parametro calorie da JS
    print(f"Calorie parameter: {calorie}")  # traccia il valore del parametro calorie quando apre la pagina

    # se quando carica la pagina il valore di calorie è None carica semplicemente la pagina
    if calorie is None:
        return render_template("kcal_searching.html")

    # se non inserito il valore delle calorie o non numerico
    if not calorie or not calorie.isdigit():
        return render_template("kcal_searching.html", alert="Inserisci un valore valido")

    # Converti il valore delle calorie in un intero
    calorie = int(calorie)

    elenco_calorie = Ricetta.query.filter_by(kcal=calorie).all()
    if elenco_calorie:
        return render_template("kcal_searching.html", calorie=calorie, elenco_calorie=elenco_calorie)

    return render_template("kcal_searching.html", alert="Ricette non trovate per calorie specificate")

# ======================================================================================================================
#  questa route dovrebbe essere per API con ajax e swagger
# @ricette_routes.route("/trova_calorie", methods=["GET"])
# def trova_calorie():
#     calorie = request.args.get("kcal")
#
#     # Se il valore non è valido
#     if not calorie or not calorie.isdigit():
#         return "<p class='alert alert-danger'>Inserisci un valore numerico valido</p>"
#
#     elenco_calorie = Ricetta.query.filter(Ricetta.kcal == int(calorie)).all()
#
#     # Se nessuna ricetta trovata
#     if not elenco_calorie:
#         return "<p class='alert alert-warning'>Nessuna ricetta trovata per queste calorie.</p>"
#
#     # Genera la lista HTML delle ricette trovate
#     results_html = ""
#     for ricetta in elenco_calorie:
#         results_html += f"""
#         <div class="container-top">
#             <div class="top-section-left">
#                 <a class="btn btn-primary" href="{url_for('ricette_routes.dettaglio_ricetta', categoria=ricetta.categoria, nome_ricetta=ricetta.nome_ricetta)}">
#                     <img src="{url_for('static', filename=ricetta.immagine[7:])}" alt="Immagine Ricetta">
#                 </a>
#             </div>
#             <div class="top-section-right">
#                 <ul class="dettagli-ricetta">
#                     <li>Calorie: <h3>{ricetta.kcal}</h3></li>
#                     <li>Cucina: <strong>{ricetta.cousine_type}</strong></li>
#                     <li>Nome: <strong>{ricetta.nome_ricetta}</strong></li>
#                     <li>Difficoltà: <strong>{ricetta.difficulty_level}</strong></li>
#                     <li>Tempo: <strong>{ricetta.total_time}</strong></li>
#                     <li>Prezzo: <strong>{ricetta.prezzo} {ricetta.valuta}</strong></li>
#                 </ul>
#             </div>
#         </div>
#         """
#
#     return results_html  # Restituisce solo i risultati (senza ricaricare la pagina)





