# Genere app.ico a partir du logo fourni (la tuile carree au "F").
# Windows a besoin de toutes les tailles de 16 a 256 dans le MEME fichier :
# sans le 16 et le 32, la barre des taches et l'explorateur redimensionnent
# le 256 a la volee et l'icone sort floue.
# Usage : python faire_icone.py [chemin_du_png]
import os
import sys

from PIL import Image, ImageDraw

SIZES = (16, 24, 32, 48, 64, 128, 256)
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    HERE, "logo fivem pack manager.png")
OUT = os.path.join(HERE, "app.ico")

# La tuile dans la banniere fournie. Le halo autour empeche une detection
# fiable par seuil : ces bornes sont relevees a la main sur le fichier source.
TILE = (372, 187, 688, 503)


def tile_from(path: str) -> Image.Image:
    im = Image.open(path).convert("RGBA")
    if im.width > im.height * 1.4:      # banniere large -> on decoupe la tuile
        im = im.crop(TILE)
    else:                               # deja carre -> on garde tel quel
        side = min(im.size)
        im = im.crop(((im.width - side) // 2, (im.height - side) // 2,
                      (im.width + side) // 2, (im.height + side) // 2))
    return im


def rounded(im: Image.Image, size: int) -> Image.Image:
    """Redimensionne et rend les coins transparents. Sans ca, les coins
    gardent le fond de la banniere et l'icone montre un carre gris sur un
    theme clair."""
    big = size * 4                       # anticrenelage par sur-echantillonnage
    src = im.resize((big, big), Image.LANCZOS)
    mask = Image.new("L", (big, big), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, big - 1, big - 1),
                                           radius=int(big * 0.22), fill=255)
    src.putalpha(mask)
    return src.resize((size, size), Image.LANCZOS)


tile = tile_from(SRC)
print(f"source : {os.path.basename(SRC)} — tuile {tile.size[0]}x{tile.size[1]}")
frames = [rounded(tile, s) for s in SIZES]
frames[-1].save(OUT, format="ICO",
                sizes=[(s, s) for s in SIZES], append_images=frames[:-1])
print(f"app.ico ecrit : {os.path.getsize(OUT)} octets, "
      f"{len(SIZES)} tailles ({', '.join(str(s) for s in SIZES)})")

# apercu pour verification a l'oeil
prev = os.path.join(HERE, "app_icon_preview.png")
rounded(tile, 256).save(prev)
print("apercu :", os.path.basename(prev))
