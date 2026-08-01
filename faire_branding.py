# Genere une identite Modium PROVISOIRE, dans le langage graphique existant :
# tuile noire arrondie, monogramme blanc, les trois carres en bas, halo.
# Produit : app.ico (7 tailles) + .github/assets/banner.png
#
# A remplacer par le vrai logo quand il sera pret : depose-le et lance
#   python faire_icone.py mon_logo.png
# Usage : python faire_branding.py
import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(os.environ.get("SystemRoot", r"C:\Windows"), "Fonts")
MONO = os.path.join(FONTS, "consolab.ttf")      # Consolas Bold
SANS = os.path.join(FONTS, "bahnschrift.ttf")   # condensee, proche du logo

NOIR, BLANC, GRIS = (10, 10, 12), (255, 255, 255), (138, 138, 142)


def tuile(n: int) -> Image.Image:
    """La tuile de l'app : carre noir arrondi, M blanc, trois carres en bas."""
    S = n * 4  # on dessine 4x plus grand puis on reduit : bords propres
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, S - 1, S - 1), radius=int(S * 0.22), fill=NOIR)
    # lisere clair : c'est lui qui donne le relief du logo d'origine
    d.rounded_rectangle((0, 0, S - 1, S - 1), radius=int(S * 0.22),
                        outline=(70, 70, 74), width=max(1, S // 90))

    f = ImageFont.truetype(MONO, int(S * 0.52))
    box = d.textbbox((0, 0), "M", font=f)
    d.text(((S - (box[2] - box[0])) / 2 - box[0],
            S * 0.40 - (box[3] - box[1]) / 2 - box[1]), "M", font=f, fill=BLANC)

    # les trois carres, du plein au sombre, comme sur la banniere d'origine
    c, gap = S * 0.085, S * 0.045
    x0 = (S - (3 * c + 2 * gap)) / 2
    y0 = S * 0.70
    for i, col in enumerate((BLANC, (110, 110, 114), (70, 70, 74))):
        x = x0 + i * (c + gap)
        d.rounded_rectangle((x, y0, x + c, y0 + c), radius=c * 0.18, fill=col)
    return im.resize((n, n), Image.LANCZOS)


def banniere() -> Image.Image:
    W, H = 1200, 500
    im = Image.new("RGB", (W, H), (0, 0, 0))
    d = ImageDraw.Draw(im)
    for x in range(0, W, 34):      # grille tres discrete du fond d'origine
        d.line([(x, 0), (x, H)], fill=(16, 16, 18))
    for y in range(0, H, 34):
        d.line([(0, y), (W, y)], fill=(16, 16, 18))

    t = tuile(230)
    tx, ty = 120, (H - 230) // 2 - 30
    halo = Image.new("RGB", (W, H), (0, 0, 0))
    ImageDraw.Draw(halo).ellipse((tx - 90, ty - 90, tx + 320, ty + 320),
                                 fill=(48, 48, 52))
    im = Image.blend(im, halo.filter(ImageFilter.GaussianBlur(70)), 0.55)
    im.paste(t, (tx, ty), t)
    d = ImageDraw.Draw(im)

    d.text((tx + 300, ty + 30), "Modium",
           font=ImageFont.truetype(SANS, 110), fill=BLANC)
    d.text((tx + 306, ty + 160), "P A C K   M A N A G E R",
           font=ImageFont.truetype(MONO, 34), fill=(215, 215, 220))

    f = ImageFont.truetype(MONO, 22)
    x = tx
    for mot in ("RAPIDE", "SIMPLE", "SÉCURISÉ", "OPEN SOURCE"):
        w = d.textbbox((0, 0), mot, font=f)[2] + 74
        y = ty + 285
        d.rounded_rectangle((x, y, x + w, y + 52), radius=26,
                            fill=(18, 18, 20), outline=(60, 60, 64))
        d.ellipse((x + 26, y + 21, x + 36, y + 31), fill=BLANC)
        d.text((x + 50, y + 14), mot, font=f, fill=(205, 205, 210))
        x += w + 18
    return im


ico = os.path.join(HERE, "app.ico")
tailles = (16, 24, 32, 48, 64, 128, 256)
frames = [tuile(s) for s in tailles]
frames[-1].save(ico, format="ICO", sizes=[(s, s) for s in tailles],
                append_images=frames[:-1])
print(f"app.ico       {os.path.getsize(ico):>7} o  ({len(tailles)} tailles)")

os.makedirs(os.path.join(HERE, ".github", "assets"), exist_ok=True)
b = os.path.join(HERE, ".github", "assets", "banner.png")
banniere().save(b, optimize=True)
print(f"banner.png    {os.path.getsize(b):>7} o")

p = os.path.join(HERE, "app_icon_preview.png")
tuile(256).save(p)
print("apercu       ", os.path.basename(p))
