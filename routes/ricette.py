import os

from flask import Blueprint, render_template, request, jsonify

from import_bridge import login_manager, db
from models import Ricetta, User


ricette_routes = Blueprint('ricette_routes', __name__)
# specifica il path contenente le ricette caricate
ricette_path = os.path.join("static", "Ricette")

# carica le ricette in categoria.html per la visualizzazione grafica e restituisce json
def load_ricette(categoria):
    categoria_path = os.path.join(ricette_path, categoria)
    ricette = []
    if os.path.exists(categoria_path):
        for filename in os.listdir(categoria_path):
            if filename.endswith(".jpg"):
                image_path = f"Ricette/{categoria}/{filename}"  # Rimuovi "static" dal percorso
                recipe_txt = filename.replace(".jpg", ".txt")
                txt_path = os.path.join(categoria_path, recipe_txt)
                if os.path.exists(txt_path):
                    with open(txt_path, "r") as f:
                        description = f.read()
                        ricette.append({"image": image_path, "description": description}) # restituzione json
                        # questo serve per il debugging se non carica immagini e/o testo inserito
                        # print(f"Immagine trovata: {image_path}")
                        # print(f"Caricata ricetta: {filename}, descrizione: {description}") questi print aiutano il debug se non passano i dati richiesti
    # else:
        # print(f"Categoria '{categoria}' non trovata in {categoria_path}") come altro print
    return ricette

#  questo chiama struttura come file per interfaccia
@ricette_routes.route('/')
def home():
    return render_template("struttura.html")

# questo chiama categoria come interfaccia per le ricette uploadate
@ricette_routes.route("/categoria/<categoria>")
def categoria(categoria):
    ricette = load_ricette(categoria)
    return render_template("categoria.html", categoria=categoria, ricette=ricette)

@ricette_routes.route("/dettaglio_ricette/<categoria>/<nome_ricetta>")
def dettaglio_ricetta(categoria, nome_ricetta):
    image = request.args.get("image")  # Recupera il parametro dell'immagine
    ricetta = Ricetta.query.filter_by(nome_ricetta=nome_ricetta).first()
    # passa i parametri specificati a dettaglio_ricetta.html
    return render_template("dettaglio_ricetta.html", categoria=categoria, ricetta=ricetta, image=image)

# @app.route("/dettaglio_ricetta/<int:id>")
# def dettaglio_ricetta(id):
#     ricetta = Ricetta.query.get(id)  # Ottimizzato per ID
#     return render_template("dettaglio_ricetta.html", ricetta=ricetta)


# @app.route("/dashboard", methods=["GET", "POST"])
# @login_required
# def dashboard():
#     return render_template("dashboard.html")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@ricette_routes.route("/run_script")
def run_script():
    # Esegui lo script Python quando il pulsante viene premuto
    # Esegui il tuo script Python qui
    # print("Il pulsante è stato premuto!")
    return 'Script eseguito!'

@ricette_routes.route("/elenco_ricette", methods=["GET"])
def elenco_ricette():
    elenco_ricette = Ricetta.query.all()
    elenco = []
    for ricetta in elenco_ricette:
        elenco.append({
            "nome_ricetta": ricetta.nome_ricetta,
        })
    return jsonify(elenco)

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

@ricette_routes.route("/elimina_ricetta", methods=["GET"])
def elimina_ricetta():
    nome_ricetta = request.args.get("nome_ricetta")
    ricetta = Ricetta.query.filter_by(nome_ricetta=nome_ricetta).first()
    if ricetta is None:
        return jsonify({"detail": "La ricetta inserita non esiste"}), 404

    db.session.delete(ricetta)
    db.session.commit()
    return jsonify({"messaggio":"ricetta cancellata"}), 200


@ricette_routes.route("/utenti")
def lista_utenti():
    users = User.query.all()
    utenti = [{"id": user.id, "username": user.username} for user in users]
    return jsonify(utenti)



