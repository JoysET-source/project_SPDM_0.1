



auth_routes = Blueprint('auth_routes', __name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first() # questo serve per controllare se user gia presente in db o no
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):# questo controlla che la password appartiene a user
                login_user(user) # e quindi ti logga dentro
                redirect(url_for("dashboard"))# e ti rimanda alla pagina dashboard in templates(struttura a pagamento per me)
    return render_template("login.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        new_user = User(username=form.username.data, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    redirect(url_for("login"))