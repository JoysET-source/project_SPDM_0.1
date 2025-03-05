import os

from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from flask_login import login_user, logout_user, login_required

from import_bridge import bcrypt, db
from models.login_model import LoginForm
from models.user_model import User
from models.ricetta_model import Ricetta
from models.login_model import password_complexity_check
from models.controllo_dimensione_immagini import ridimensiona_immagine
from test.format_time_converter import total_time

dashboard_routes = Blueprint("dashboard_routes", __name__)


@dashboard_routes.route("/admin_dashboard")
@login_required
def admin_dashboard():
    messaggio =  "Benvenuto Amministratore SPDM"
    return render_template("dashboard/admin_dashboard.html", messaggio=messaggio)


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

        # gestisce stoccaggio immagini caricate su html
        image_filename = None
        if immagine:
            categoria_path = os.path.join("static/ricette", categoria)
            os.makedirs(categoria_path, exist_ok=True)

            image_filename = f"{nome_ricetta}.jpg"
            image_path = os.path.join(categoria_path, image_filename)
            immagine.save(image_path)

            # Ridimensionamento immagine
            ridimensiona_immagine(image_path)

            # Salva solo il percorso dell immagine nel database
            image_filename = f"static/ricette/{categoria}/{image_filename}"

        # calcoliamo il valore total_time prima dell inserimento nel DB
        total_time = preparation_time + cooking_time

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

        db.session.add(nuova_ricetta)
        db.session.commit()

        return render_template("dashboard/admin_dashboard.html")

    messaggio = "Aggiungi Ricetta"
    return render_template("dashboard/ricette/create_recipe.html",
                           messaggio=messaggio, elenco_categorie=elenco_categorie)



@dashboard_routes.route("/aggiungi_categoria", methods=["GET", "POST"])
def aggiungi_categoria():
    messaggio = "Crea Categoria"
    return render_template("dashboard/categorie/aggiungi_categoria.html", messaggio=messaggio)

@dashboard_routes.route("/read_recipe", methods=["GET"])
def read_recipe():
    return render_template("dashboard/ricette/read_recipe.html")

@dashboard_routes.route("/update_recipe", methods=["GET","POST"])
def update_recipe():
    return render_template("dashboard/ricette/update_recipe.html")

@dashboard_routes.route("/delete_recipe", methods=["GET", "POST"])
def delete_recipe():
    return render_template("dashboard/ricette/delete_recipe.html")

@dashboard_routes.route("/footer")
def footer():
    return render_template("dashboard/footer.html")

@dashboard_routes.route("/header")
def header():
    return render_template("dashboard/header.html")

@dashboard_routes.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth_routes.login"))