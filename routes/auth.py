from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from flask_login import login_user, logout_user, login_required

from import_bridge import bcrypt, db
from models.login_model import LoginForm, RegisterForm
from models.user_model import User

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm() # stai creando un modulo con: campo username, password e tasto di invio

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first() # questo serve per controllare se user gia presente in db o no
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):# questo controlla che la password appartiene a user
                login_user(user) # e quindi ti logga dentro

                # controlla se login di admin
                if user.username == "admin":
                    return redirect(url_for("dashboard_routes.admin_dashboard"))
                else:
                    # e ti rimanda alla pagina dashboard in templates(struttura a pagamento per me)
                    # return "Login effettuato! <a href='/'>Torna alla home</a>"
                    return redirect(url_for("auth_routes.login_dashboard"))

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
            # return redirect(url_for("login"))
            return jsonify({"success":"Registrazione completata"}),200
        else:
            # Flask raccoglie gli errori del form e li restituisce come JSON
            errors = {field.name: field.errors for field in form if field.errors}
            return jsonify({"errors": errors}), 400

    return render_template("auth/register.html", form=form)

@auth_routes.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth_routes.login"))

@auth_routes.route("/login_dashboard")
def login_dashboard():
    return render_template("auth/login_dashboard.html")
