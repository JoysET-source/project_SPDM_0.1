import os
from flask import Flask
from dotenv import load_dotenv
from import_bridge import db, bcrypt, login_manager

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ricette.db'
app.config['SQLALCHEMY_BINDS'] = {'users': 'sqlite:///users.db'}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv("SECRET_KEY")

# caricare le immagini inserite in HTML su flask nel percorso specificato
UPLOAD_FOLDER = "static/ricette"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "auth_routes.login"

with app.app_context():
    db.create_all()

from routes.auth import auth_routes
from routes.ricette import ricette_routes
from routes.manage_recipe import dashboard_routes

app.register_blueprint(auth_routes)
app.register_blueprint(ricette_routes)
app.register_blueprint(dashboard_routes)

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=5000) questo fa il sito raggiungibile da tutti i connessi in LAN

    # Ora, se il tuo computer è connesso alla rete,
    # altre persone sulla stessa rete locale possono accedere al tuo sito
    # usando l'indirizzo IP del tuo computer, ad esempio: http://<tuo-ip-locale>:5000.
