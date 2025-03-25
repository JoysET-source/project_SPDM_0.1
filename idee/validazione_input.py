# import  os
#
# def get_categorie():
#     """Legge dinamicamente le ricette dalla cartella static/ricette"""
#     categorie_path = os.path.join("static", "ricette")
#     if not os.path.exists(categorie_path):
#         return []
#     return [nome for nome in os.listdir(categorie_path) if os.path.isdir(os.path.join(categorie_path, nome))]
#
# def valida_categoria(categoria):
#     """Verifica se la categoria inserita è tra quelle valide"""
#     categorie_valide = get_categorie()  # Ora ottiene l'elenco corretto
#     return categoria in categorie_valide
