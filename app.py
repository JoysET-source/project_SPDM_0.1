import os
import cloudinary
# import redis


from flask import Flask
from dotenv import load_dotenv
from import_bridge import db, migrate, bcrypt, login_manager
# from import_bridge import cache

# Importa i modelli per creare le tabelle nel database
from models.user_model import User
from models.ricetta_model import Ricetta
from models.accessLog_model import AccessLog



# Carica le variabili d'ambiente dal file .env
load_dotenv()

# print("CLOUD NAME:", os.getenv("CLOUDINARY_CLOUD_NAME"))
# print("API KEY:", os.getenv("CLOUDINARY_API_KEY"))
# print("API SECRET:", os.getenv("CLOUDINARY_API_SECRET"))

app = Flask(__name__)

#=============================================================
# creazione DB in locale
# collegamenti per creare DB in sql lite
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ricette.db'
# app.config['SQLALCHEMY_BINDS'] = {'users': 'sqlite:///users.db'}
# spostare db su mysql ma sembre locale
# collegamento per creare db in mysql
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'mysql+pymysql://root@localhost/spdm')
#=============================================================

# collegamento per creare db online in mysql con server remoto aiven
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

# collegamento per secret key
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv("SECRET_KEY")
#=============================================================
# Configura CLOUDINARY
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)
# debug cloudinary
# print("Cloudinary configurato con:", cloudinary.config().cloud_name)
# print("Cloudinary configurato con:", cloudinary.config().api_key)
# print("Cloudinary configurato con:", cloudinary.config().api_secret)

# result = upload("static/ricette/primi/test.jpg", folder="ricette/test/", public_id="prova_upload", overwrite=True)
# print(result["secure_url"])
#=============================================================

#=============================================================
# Configura Redis-cache Flask-Caching
# app.config["CACHE_TYPE"] = "RedisCache"
# app.config["CACHE_REDIS_URL"] = os.getenv("REDIS_URL")

# redis_port = os.getenv("REDIS_PORT", "6379")
# redis_client = redis.Redis(
#     host=os.getenv("REDIS_HOST"),
#     port=int(redis_port),
#     password=os.getenv("REDIS_PASSWORD"),
#     ssl=True,
#     socket_timeout=5,
#     socket_connect_timeout=5,
#     retry_on_timeout=True
# )

#=============================================================

# caricare le immagini inserite in HTML su flask nel percorso specificato
UPLOAD_FOLDER = "static/ricette"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# inizializza db, migrate, bcrypt, login, cache
db.init_app(app)
migrate.init_app(app, db)
bcrypt.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "auth_routes.login"
# cache.init_app(app)

# apre app e crea i db
with app.app_context():
    db.create_all()

from routes.auth import auth_routes
from routes.ricette import ricette_routes
from routes.manage_recipe import dashboard_routes
from routes.accessLog_routes import accessLog_routes

app.register_blueprint(auth_routes)
app.register_blueprint(ricette_routes)
app.register_blueprint(dashboard_routes)
app.register_blueprint(accessLog_routes)

if __name__ == '__main__':
    app.run(debug=False)
    # app.run(host='0.0.0.0', port=5000) questo fa il sito raggiungibile da tutti i connessi in LAN

    # Ora, se il tuo computer è connesso alla rete,
    # altre persone sulla stessa rete locale possono accedere al tuo sito
    # usando l'indirizzo IP del tuo computer, ad esempio: http://<tuo-ip-locale>:5000.
