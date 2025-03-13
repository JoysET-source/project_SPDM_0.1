import os
import re

from flask import abort, request, jsonify
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required

from import_bridge import bcrypt, db
from models.login_model import LoginForm
from models.user_model import User
from models.ricetta_model import Ricetta
from models.login_model import password_complexity_check
from models.controllo_dimensione_immagini import ridimensiona_immagine
from routes.ricette import elenco_ricette

dashboard_routes = Blueprint("dashboard_routes", __name__)


@dashboard_routes.route("/admin_dashboard")
@login_required
def admin_dashboard():
    return render_template("dashboard/admin_dashboard.html", messaggio="Benvenuto Amministratore SPDM")


@dashboard_routes.route("/create_recipe", methods=["GET", "POST"])
@login_required
def create_recipe():
    # collegamento OS per iterazione sulle cartelle categorie
    cartella_base = "static/ricette/"
    elenco_categorie = [cartella_categoria for cartella_categoria in os.listdir(cartella_base)
                 if os.path.isdir(os.path.join(cartella_base, cartella_categoria))]

    # acquisisce i dati POST-ATI su html
    if request.method == "POST":
        nome_ricetta = request.form.get("nome_ricetta")
        ingredienti = request.form.get("ingredienti")
        kcal = request.form.get("kcal")
        immagine = request.files.get("immagine")
        categoria = request.form.get("categoria")
        titolo = request.form.get("titolo")
        descrizione = request.form.get("descrizione")
        servings = request.form.get("servings")
        preparation_time = request.form.get("preparation_time")
        cooking_time = request.form.get("cooking_time")
        steps = request.form.get("steps")
        difficulty_level = request.form.get("difficulty_level")
        cousine_type = request.form.get("cousine_type")
        autore = request.form.get("autore")
        rating = request.form.get("rating")
        tags = request.form.get("tags")
        prezzo = request.form.get("prezzo")
        valuta = request.form.get("valuta")

        # questo serve a rimandare il template gia compilato se abbiamo dimenticato il campo categoria
        if categoria is None or categoria == "Seleziona categoria":
            errore = "Inserisci una categoria"
            return render_template("dashboard/ricette/create_recipe.html",
                                   errore=errore,
                                   elenco_categorie=elenco_categorie,
                                   nome_ricetta=request.form.get("nome_ricetta"),
                                   ingredienti=request.form.get("ingredienti"),
                                   kcal=request.form.get("kcal"),
                                   immagine=request.files.get("immagine"),
                                   categoria=request.form.get("categoria"),
                                   titolo=request.form.get("titolo"),
                                   descrizione=request.form.get("descrizione"),
                                   servings=request.form.get("servings"),
                                   preparation_time=request.form.get("preparation_time"),
                                   cooking_time=request.form.get("cooking_time"),
                                   steps=request.form.get("steps"),
                                   difficulty_level=request.form.get("difficulty_level"),
                                   cousine_type=request.form.get("cousine_type"),
                                   autore=request.form.get("autore"),
                                   rating=request.form.get("rating"),
                                   tags=request.form.get("tags"),
                                   prezzo=request.form.get("prezzo"),
                                   valuta=request.form.get("valuta"),
                                   )


        # gestisce stoccaggio immagini caricate su html
        image_filename = None
        if immagine:
            categoria_path = os.path.join("static/ricette", categoria)
            os.makedirs(categoria_path, exist_ok=True)

            estensione = os.path.splitext(immagine.filename)[1]
            image_filename = f"{nome_ricetta}{estensione}"
            image_path = os.path.join(categoria_path, image_filename)
            immagine.save(image_path)

            # Ridimensionamento immagine
            ridimensiona_immagine(image_path)

            # Salva solo il percorso dell immagine nel database
            image_filename = f"static/ricette/{categoria}/{image_filename}"

        # calcoliamo il valore total_time prima dell inserimento nel DB
        total_time = int(preparation_time or 0) + int(cooking_time or 0)

        # crea la ricetta inserita e salva nel DB
        nuova_ricetta = Ricetta(
            categoria=categoria,
            nome_ricetta=nome_ricetta,
            ingredienti=ingredienti,
            kcal=kcal,
            immagine=image_filename,
            titolo=titolo,
            descrizione=descrizione,
            servings=servings,
            preparation_time=preparation_time,
            cooking_time=cooking_time,
            steps=steps,
            cousine_type=cousine_type,
            tags=tags,
            prezzo=prezzo,
            autore=autore,
            difficulty_level=difficulty_level,
            rating=rating,
            valuta=valuta,
            total_time=total_time
        )

        try:
            db.session.add(nuova_ricetta)
            db.session.commit()
            errore = None
        except Exception as error:
            db.session.rollback()
            success = None
            return render_template("dashboard/ricette/create_recipe.html",
                                   messaggio="Aggiungi Ricetta",
                                   elenco_categorie=elenco_categorie,
                                   errore=f"Salvataggio non riuscito, {error}",
                                   success=success
                                   )

        return render_template("dashboard/ricette/create_recipe.html",
                               messaggio="Aggiungi Ricetta",
                               success="Ricetta aggiunta al DB",
                               errore=errore
                               )

    return render_template("dashboard/ricette/create_recipe.html",
                           messaggio="Aggiungi Ricetta",
                           elenco_categorie=elenco_categorie,
                           )


@dashboard_routes.route("/aggiungi_categoria", methods=["POST"])
@login_required
def aggiungi_categoria():
    cartella_base = "static/ricette/"
    nome_categoria = request.form.get("nome_categoria", "").strip()

    # # Controllo che il nome sia valido (solo lettere e spazi, minimo 3 caratteri)
    # if not re.match(r"^[a-zA-ZÀ-ÿ\s]{3,}$", nome_categoria):
    #     return jsonify({"errore": "Categoria non accettata"}), 400

    new_categoria = os.path.join(cartella_base, nome_categoria)

    if not os.path.exists(new_categoria):
        os.makedirs(new_categoria)
        return jsonify({"alert": "Categoria Aggiunta"})
    else:
        return jsonify({"errore": "Categoria esistente"})


@dashboard_routes.route("/list_recipes", methods=["GET"])
@login_required
def list_recipes():
    # Ottieni tutte le ricette dal database
    lista_ricette = Ricetta.query.all()
    # Crea una lista di dizionari per ogni ricetta
    elenco_ricette = []
    for ricetta in lista_ricette:
        elenco_ricette.append({
            "id": ricetta.id,
            "nome_ricetta": ricetta.nome_ricetta,
            "ingredienti": ricetta.ingredienti,
            "total_time": ricetta.total_time,
            "categoria": ricetta.categoria,
            "prezzo": ricetta.prezzo
        })
    # Passa la lista di ricette al template
    return render_template("dashboard/ricette/list_recipes.html",
                           elenco_ricette=elenco_ricette,
                           messaggio="Lista Data Base Ricette"
                           )

@dashboard_routes.route("/read_recipe", methods=["GET"])
@login_required
def read_recipe():
    id = request.args.get("id")  # Ottieni il valore del parametro id da JS
    ricetta = Ricetta.query.filter_by(id=id).first()

    if ricetta is None:
        abort(404, description="non trovata")

    return render_template("dashboard/ricette/read_recipe.html", messaggio="Anteprima Ricetta", ricetta=ricetta)



# il valore del parametro id da JS lo passiamo diretto nella route
@dashboard_routes.route("/update_recipe/<int:id>", methods=["GET", "POST"])
@login_required
def update_recipe(id):

    # Ottieni dal DB tutti i parametri della ricetta in base a id richiesto
    db_ricetta = Ricetta.query.get(id)
    # Se la ricetta non esiste, reindirizza alla lista delle ricette
    if not db_ricetta:
        return redirect(url_for("dashboard_routes.list_recipes"))

    # Se la richiesta è GET, mostra il modulo con i dati esistenti
    if request.method == "GET":
        return render_template("dashboard/ricette/update_recipe.html", db_ricetta=db_ricetta)

    # Se la richiesta è POST, acquisisci i nuovi dati da html da mettere nel db
    if request.method == "POST":
        db_ricetta.nome_ricetta = request.form.get("nome_ricetta")
        db_ricetta.ingredienti = request.form.get("ingredienti")
        db_ricetta.kcal = request.form.get("kcal")
        db_ricetta.categoria = request.form.get("categoria")
        db_ricetta.titolo = request.form.get("titolo")
        db_ricetta.descrizione = request.form.get("descrizione")
        db_ricetta.servings = request.form.get("servings")
        db_ricetta.preparation_time = request.form.get("preparation_time")
        db_ricetta.cooking_time = request.form.get("cooking_time")
        db_ricetta.steps = request.form.get("steps")
        db_ricetta.difficulty_level = request.form.get("difficulty_level")
        db_ricetta.cousine_type = request.form.get("cousine_type")
        db_ricetta.autore = request.form.get("autore")
        db_ricetta.rating = request.form.get("rating")
        db_ricetta.tags = request.form.get("tags")
        db_ricetta.prezzo = request.form.get("prezzo")
        db_ricetta.valuta = request.form.get("valuta")

        # Gestisci l'immagine, se è stata aggiornata
        immagine = request.files.get("immagine")
        if immagine:
            # Elimina la vecchia immagine, se esiste
            if db_ricetta.immagine:
                os.remove(db_ricetta.immagine)

            # Salva la nuova immagine
            categoria = request.form.get("categoria")  # Assumendo che la categoria venga fornita dal form
            categoria_path = os.path.join("static/ricette", categoria)
            if not os.path.exists(categoria_path):
                os.makedirs(categoria_path)  # Crea la cartella se non esiste
            estensione = os.path.splitext(immagine.filename)[1]
            image_filename = f"{db_ricetta.nome_ricetta}{estensione}"
            image_path = os.path.join(categoria_path, image_filename)
            immagine.save(image_path)

            # Ridimensionamento immagine
            ridimensiona_immagine(image_path)

            # Salva il percorso dell'immagine nel database
            db_ricetta.immagine = f"static/ricette/{categoria}/{image_filename}"

        db_ricetta.total_time = int(db_ricetta.preparation_time) + int(db_ricetta.cooking_time)

        try:
            # Salva le modifiche nel database
            db.session.commit()
            return redirect(url_for("/templates\dashboard/ricette/list_recipes.html"))  # Redirect alla lista delle ricette
        except Exception as e:
            db.session.rollback()
            return render_template("dashboard/ricette/update_recipe.html", db_ricetta=db_ricetta,
                                   errore=f"Errore nell'aggiornamento: {e}")


@dashboard_routes.route("/delete_recipe", methods=["DELETE"])
@login_required
def delete_recipe():
    # Ottieni id dalla query string (in questo caso il pulsante)
    id = request.json.get("id")
    # ottieni dal DB la ricetta corrispondente a id
    ricetta = Ricetta.query.filter_by(id=id).first()

    if ricetta is None:
        abort(404, description="non trovata")

    db.session.delete(ricetta)
    db.session.commit()

    return jsonify({"messaggio": "Ricetta eliminata con successo"}), 200


@dashboard_routes.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth_routes.login"))