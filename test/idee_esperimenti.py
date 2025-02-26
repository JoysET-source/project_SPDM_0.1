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
