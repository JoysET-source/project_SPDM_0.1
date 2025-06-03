import re

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Length, ValidationError, Regexp
from models.user_model import User


# verifica la complessita della password usando regex
def password_complexity_check(form, field):
    password = field.data
    if not re.search(r"[A-Z]", password):
        raise ValidationError("La password deve contenere almeno un carattere maiuscolo")
    if not re.search(r"[!@#$%^&*(),.?':{}|<>]", password):
        raise ValidationError("La password deve contenere almeno un carattere speciale")


# usando Flask-WTF serve per raccogliere i dati inseriti dall'utente in un modulo HTML.
class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=60),
                                       Regexp(r'^[\w.@+-]+$', message="Il nome utente contiene caratteri non validi")],
                           render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=60), password_complexity_check],
                             render_kw={"placeholder": "Password"})
    # questo e`il backend del pulsante login(tasto di invio) esplicitato nel front
    submit = SubmitField("Register")

    # assicurarsi che username non sia gia in uso
    # usa validate che WTF di default lo legge
    # FlaskForm gestisce già gli errori, quindi non serve restituire JSON qui.
    def validate_username(self, username):
        user_esistente = User.query.filter_by(username=username.data).first()
        if user_esistente:
            raise ValidationError("nome utente non disponibile, sceglierne un altro")


# usando Flask-WTF serve per raccogliere i dati inseriti dall'utente in un modulo HTML.
class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=60)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=60), password_complexity_check],
                             render_kw={"placeholder": "Password"})
    # questo e`il backend del pulsante login(tasto di invio) esplicitato nel front
    submit = SubmitField("Login")
