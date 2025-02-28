# from app import app
# from import_bridge import bcrypt, db
# from models.user_model import User
#
# # inizializza il db
# with app.app_context():
#     db.create_all()
#
# # Crea un utente admin
# admin = User(username="admin", password=bcrypt.generate_password_hash("Adminadmin@").decode("utf-8"))
#
# # salva nel DB
# db.session.add(admin)
# db.session.commit()
#
# print("Admin creato con successo!")
