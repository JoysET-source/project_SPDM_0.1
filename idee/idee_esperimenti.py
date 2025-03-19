# @ricette_routes.route("/upload_ricetta", methods=["POST"])
# def upload_ricetta():
#     categoria = request.form.get("categoria")  # Ottiene la categoria dal form
#     nome_ricetta = request.form.get("nome_ricetta")  # Nome della ricetta
#     descrizione = request.form.get("descrizione")  # Testo della ricetta
#     immagine = request.files.get("immagine")  # Immagine caricata
#
#     if not categoria or not nome_ricetta or not descrizione or not immagine:
#         return jsonify({"error": "Tutti i campi sono obbligatori!"}), 400
#
#     # Percorso della cartella categoria (es: static/Ricette/Pasta)
#     categoria_path = os.path.join("static/Ricette", categoria)
#     os.makedirs(categoria_path, exist_ok=True)  # Crea la cartella se non esiste
#
#     # Salva l'immagine nella cartella ricette/categoria
#     image_filename = f"{nome_ricetta}.jpg"
#     image_path = os.path.join(categoria_path, image_filename)
#     immagine.save(image_path)
#
#     # Salva il file di testo della ricetta nella cartella ricette/categoria
#     txt_filename = f"{nome_ricetta}.txt"
#     txt_path = os.path.join(categoria_path, txt_filename)
#     with open(txt_path, "w") as f:
#         f.write(descrizione)
#
#     return jsonify({"success": f"Ricetta '{nome_ricetta}' caricata in '{categoria}'!"}), 201
#
# ======================================================================================================================
# def ridimensiona_immagine(image_path):
#     """Ridimensiona l'immagine prima di salvarla"""
#     try:
#         img = Image.open(image_path)
#         img.thumbnail((MAX_WIDTH, MAX_HEIGHT))
#         img.save(image_path, optimize=True, quality=85)
#     except Exception as e:
#         print(f"Errore nel ridimensionamento: {e}")
# ======================================================================================================================
# @app.route("/ricette", methods=["GET"])
# def get_ricette():
#     ricette = Ricetta.query.all()
#     ricette_json = [
#         {
#             "id": r.id,
#             "nome": r.nome,
#             "categoria": r.categoria,
#             "descrizione": r.descrizione,
#             "immagine": r.immagine
#         }
#         for r in ricette
#     ]
#     return jsonify(ricette_json)
# ======================================================================================================================
# ======================================================================================================================
# Il mixin prende un argomento $padding-x con un valore predefinito di $container-padding-x
# Quando viene utilizzato, il mixin applica queste regole CSS all'elemento:
# praticamente crea un container con due bande di spazio a destra e a sinistra come cucchiaio dargento
#
# // Source mixin
# @mixin make-container($padding-x: $container-padding-x) {
#   width: 100%;
#   padding-right: $padding-x;
#   padding-left: $padding-x;
#   margin-right: auto;
#   margin-left: auto;
# }
#Quando usi il mixin così:
# // Usage
# .custom-container {
#   @include make-container(30px); <----$container-padding-x
# }
#Sass lo trasforma in CSS:
# .custom-container {
#   width: 100%;
#   padding-right: 30px;  /* Se $container-padding-x è 30px */
#   padding-left: 30px;
#   margin-right: auto;
#   margin-left: auto;
# }
# ======================================================================================================================
# ======================================================================================================================
# label a tendina con selection di base

# <!-- <select class="form-select form-select-sm" aria-label="Small select example">
#   <option selected>Scegli Categoria</option>
#   <option value="1">One</option>
#   <option value="2">Two</option>
#   <option value="3">Three</option>
# </select> -->
# ======================================================================================================================
# ======================================================================================================================
# gestione errore diretto sotto label gestito in backend
#
# dentro create_recipe:
# from test.validazione_input import valida_categoria, get_categorie
# categorie_valide = get_categorie()
# if not valida_categoria(categoria):
#     errore_categoria = f"Categoria non valida. Scegli tra: {', '.join(categorie_valide)}."
#     return render_template(
#         "dashboard/ricette/create_recipe.html",
#         messaggio="Aggiungi Ricetta",
#         errore_categoria=errore_categoria,
#         categoria=categoria,  # Mantiene il valore nel campo
#         ricette=categorie_valide  # Passa le ricette al template
#     )
# il return e' dentro if di post
# return render_template("dashboard/admin_dashboard.html", ricette=categorie_valide)
#
# questo nel suo  html
# <!-- <div class="container-fluid">
#     <div class="row">
#         <div class="col-md-3 col-sm-4">
#             <label>Categoria:</label>
#         </div>
#         <div class="col-md-6 col-sm-8">
#             <input type="text" name="categoria" required placeholder="Es. Pasta" class="form-control">
#             {% if errore_categoria %}
#             <p class="text-danger">{{ errore_categoria }}</p>
#             {% endif %}
#         </div>
#     </div>    -->
#
#  dentro il file validazione_input.py in test
# import  os
#
# def get_categorie():
#     """Legge dinamicamente le ricette dalla cartella static/ricette"""
#     categorie_path = os.path.join("static", "ricette")
#     if not os.path.exists(categorie_path):
#         return []
#     return [nome for nome in os.listdir(categorie_path) if os.path.isdir(os.path.join(categorie_path, nome))]
#
# def valida_categoria(categoria):
#     """Verifica se la categoria inserita è tra quelle valide"""
#     categorie_valide = get_categorie()  # Ora ottiene l'elenco corretto
#     return categoria in categorie_valide
#
# ======================================================================================================================
# ======================================================================================================================
# serve per vedere gli utenti loggati in tempo reale
# from flask import session
# from flask_login import current_user, login_user, logout_user
# from route_app import app
#
# logged_in_users = set()
#
# # Quando un utente fa il login, aggiungilo alla lista degli utenti loggati
# @app.before_request
# def before_request():
#     if current_user.is_authenticated:
#         logged_in_users.add(current_user.id)
#
# # Quando un utente fa il logout, rimuovilo dalla lista
# @app.teardown_request
# def teardown_request(exception=None):
#     if current_user.is_authenticated:
#         logged_in_users.discard(current_user.id)
#
# # Funzione per vedere gli utenti loggati
# @app.route("/utenti_loggati", methods=["GET"])
# def utenti_loggati():
#     return jsonify(list(logged_in_users))


# =====================================================================================================================
# # questa parte non la uso piu ma serviva per caricare le foto e le descrizioni tramite cartella
# # ora lo facciamo da interfaccia
# # carica le ricette in categoria.html per la visualizzazione grafica e restituisce json
# def load_ricette(categoria):
#     categoria_path = os.path.join(ricette_path, categoria)
#     ricette = []
#     if os.path.exists(categoria_path):
#         for filename in os.listdir(categoria_path):
#             if filename.endswith(".jpg"):
#                 image_path = f"Ricette/{categoria}/{filename}"  # Rimuovi "static" dal percorso
#                 recipe_txt = filename.replace(".jpg", ".txt")
#                 txt_path = os.path.join(categoria_path, recipe_txt)
#                 if os.path.exists(txt_path):
#                     with open(txt_path, "r") as f:
#                         description = f.read()
#                         ricette.append({"image": image_path, "description": description}) # restituzione json
#                         # questo serve per il debugging se non carica immagini e/o testo inserito
#                         # print(f"Immagine trovata: {image_path}")
#                         # print(f"Caricata ricetta: {filename}, descrizione: {description}") questi print aiutano il debug se non passano i dati richiesti
#     # else:
#         # print(f"Categoria '{categoria}' non trovata in {categoria_path}") come altro print
#     return ricette
# ======================================================================================================================
# from flask_login import current_user
# @app.route("/profile")
# def profile():
#     if current_user.is_authenticated:
#         return f"Benvenuto, {current_user.username}!"
#     else:
#         return "Devi essere loggato per vedere il tuo profilo."
# ======================================================================================================================