import flask
from flask import Blueprint, render_template, redirect, url_for, request, jsonify, flash
from flask_login import login_user, logout_user, login_required


from import_bridge import bcrypt, db
from models.login_model import LoginForm, RegisterForm
from models.user_model import User

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm() # stai creando un modulo con: campo username, password e tasto di invio

    if form.validate_on_submit():
        # questo serve per controllare se user gia presente in db o no
        user = User.query.filter_by(username=form.username.data).first()

        # verifica esistenza user nel DB
        if not user :
            flash("Utente non registrato", "danger")
            return redirect(url_for("auth_routes.login"))

        # verifica che la password appartiene a user
        if bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user) # e quindi ti logga dentro

            # controlla se login di admin
            if user.username == "admin":
                return redirect(url_for("dashboard_routes.admin_dashboard"))

            # se non admin, reindirizza alla home
            return redirect(url_for("ricette_routes.home"))

        # Se la password è sbagliata o l'utente non esiste
        return render_template("auth/login.html", form=form, alert="Credenziali errate!")

    return render_template("auth/login.html", form=form)


@auth_routes.route("/register", methods=["GET", "POST"])
def register():
    # crea un'istanza della classe RegisterForm, che è un form Flask-WTF.
    # Questa istanza viene poi passata al template HTML per essere utilizzata nel frontend.
    # comunica con class e con block su register.html
    form = RegisterForm()
    if request.method == "POST":
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
            new_user = User(username=form.username.data, password=hashed_password)

            db.session.add(new_user)
            db.session.commit()

            # gestione flash di successo registrazione
            flash("Registrazione completata!", "success")
            return redirect(url_for("auth_routes.login"))

        else:
            # Flask raccoglie gli errori del form e li restituisce come JSON
            errors = "User e password esistenti"
            return render_template("auth/register.html", form=form, errore=errors)

    return render_template("auth/register.html", form=form)

@auth_routes.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth_routes.login"))

@auth_routes.route("/login_dashboard")
def login_dashboard():
    return render_template("auth/login_dashboard.html")
