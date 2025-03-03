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
#         categorie=categorie_valide  # Passa le categorie al template
#     )
# il return e' dentro if di post
# return render_template("dashboard/admin_dashboard.html", categorie=categorie_valide)
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
#     """Legge dinamicamente le categorie dalla cartella static/ricette"""
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