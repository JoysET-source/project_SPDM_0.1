import os

from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from flask_login import login_user, logout_user, login_required

from import_bridge import bcrypt, db
from models.login_model import LoginForm
from models.user_model import User
from models.ricetta_model import Ricetta
from models.login_model import password_complexity_check
from models.controllo_dimensione_immagini import ridimensiona_immagine


dashboard_routes = Blueprint("dashboard_routes", __name__)


@dashboard_routes.route("/admin_dashboard")
@login_required
def admin_dashboard():
    messaggio =  "Benvenuto Amministratore SPDM"
    return render_template("dashboard/admin_dashboard.html", messaggio=messaggio)

@dashboard_routes.route("/create_recipe", methods=["GET", "POST"])
@login_required
def create_recipe():
    messaggio = "Aggiungi Ricetta"
    if request.method == "GET":
        return render_template("dashboard/ricette/create_recipe.html", messaggio=messaggio)
    else:
        categoria = request.form.get("categoria")
        nome_ricetta = request.form.get("nome_ricetta")
        ingredienti = request.form.get("ingredienti")
        kcal = request.form.get("kcal")
        immagine = request.files.get("immagine")
        titolo = request.form.get("titolo")
        descrizione = request.form.get("descrizione")
        servings = request.form.get("servings")
        preparation_time = request.form.get("preparation_time")
        coocking_time = request.form.get("coocking_time")
        steps = request.form.get("steps")
        cousine_type = request.form.get("cousine_type")
        tags = request.form.get("tags")
        prezzo = request.form.get("prezzo")
        autore = request.form.get("autore")

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

        nuova_ricetta = Ricetta(
            categoria=categoria,
            nome=nome_ricetta,
            ingredienti=ingredienti,
            kcal=kcal,
            immagine=image_filename,
            titolo=titolo,
            descrizione=descrizione,
            servings=servings,
            preparation_time=preparation_time,
            coocking_time=coocking_time,
            steps=steps,
            cousine_type=cousine_type,
            tags=tags,
            prezzo=prezzo,
            autore=autore

        )
        db.session.add(nuova_ricetta)
        db.session.commit()

    return render_template("dashboard/ricette/create_recipe.html")

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