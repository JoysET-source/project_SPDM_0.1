from PIL import Image

MAX_WIDTH = 800
MAX_HEIGHT = 600


def ridimensiona_immagine(image_path):
    """Ridimensiona l'immagine prima di salvarla"""
    try:
        img = Image.open(image_path)
        img.thumbnail((MAX_WIDTH, MAX_HEIGHT))
        img.save(image_path, optimize=True, quality=85)
    except Exception as e:
        print(f"Errore nel ridimensionamento: {e}")