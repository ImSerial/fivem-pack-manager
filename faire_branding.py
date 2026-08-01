# Reconstruit l'identite Modium a partir du logo fourni.
#
# Le logo d'origine est une banniere d'agence : la tuile et le mot-symbole sont
# bons, mais le texte parle de "Next-gen Digital Solutions", "Web Apps",
# "Automation"... rien a voir avec un installeur de packs FiveM.
# On garde donc les deux elements graphiques tels quels, decoupes au pixel, et
# on repeint entierement le texte autour.
#
# Produit : app.ico (7 tailles) + .github/assets/banner.png + site/assets/*
# Usage   : python faire_branding.py
import os

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "logo modium.png")

# Zones relevees au pixel sur le fichier source (1672x941)
TUILE = (330, 174, 634, 478)
MOT = (690, 225, 1410, 410)

FONTS = os.path.join(os.environ.get("SystemRoot", r"C:\Windows"), "Fonts")
SANS = os.path.join(FONTS, "segoeuib.ttf")      # Segoe UI Bold
SANS_SB = os.path.join(FONTS, "seguisb.ttf")    # Segoe UI Semibold

NOIR = (6, 6, 7)
BLANC = (255, 255, 255)
GRIS = (150, 150, 156)
ROUGE = (216, 26, 26)       # releve sur le point du i et l'eclat du M

TAILLES_ICO = (16, 24, 32, 48, 64, 128, 256)


def tuile() -> Image.Image:
    return Image.open(SRC).convert("RGBA").crop(TUILE)


def icone(n: int) -> Image.Image:
    """Tuile redimensionnee, coins rendus transparents. Sans ca les coins
    gardent le fond de la banniere et l'icone montre un carre gris sur un
    theme clair."""
    big = n * 4
    src = tuile().resize((big, big), Image.LANCZOS)
    masque = Image.new("L", (big, big), 0)
    ImageDraw.Draw(masque).rounded_rectangle(
        (0, 0, big - 1, big - 1), radius=int(big * 0.225), fill=255)
    src.putalpha(masque)
    return src.resize((n, n), Image.LANCZOS)


def banniere(largeur=1400) -> Image.Image:
    W, H = largeur, 620
    im = Image.new("RGB", (W, H), NOIR)
    d = ImageDraw.Draw(im)

    pas = 46
    for x in range(0, W, pas):
        d.line([(x, 0), (x, H)], fill=(14, 14, 16))
    for y in range(0, H, pas):
        d.line([(0, y), (W, y)], fill=(14, 14, 16))

    # halo : blanc froid autour de la tuile, avec une pointe de rouge
    halo = Image.new("RGB", (W, H), (0, 0, 0))
    hd = ImageDraw.Draw(halo)
    hd.ellipse((70, 20, 560, 480), fill=(46, 46, 50))
    hd.ellipse((190, 150, 430, 350), fill=(70, 30, 32))
    im = Image.blend(im, halo.filter(ImageFilter.GaussianBlur(85)), 0.6)
    d = ImageDraw.Draw(im)

    # tuile : coins rendus transparents, sinon on voit le rectangle de decoupe
    t = icone(250)
    tx, ty = 120, 96
    im.paste(t, (tx, ty), t)

    # mot-symbole : detoure par un masque bati sur le canal MAXIMUM, pas sur la
    # luminance. Le point du i est rouge pur (216,26,26) : sa luminance est
    # faible et un masque luminance le rendrait a moitie transparent, alors que
    # son canal rouge vaut 216. Le fond quasi noir tombe a zero, le rectangle
    # de decoupe disparait.
    mot = Image.open(SRC).convert("RGB").crop(MOT)
    mw = 560
    mot = mot.resize((mw, round(mot.height * mw / mot.width)), Image.LANCZOS)
    r, v, bl = mot.split()
    canal_max = ImageChops.lighter(ImageChops.lighter(r, v), bl)
    masque = canal_max.point(lambda p: 0 if p < 16 else min(255, int((p - 16) * 2.2)))
    im.paste(mot, (tx + 300, ty + 34), masque)
    mx, my = tx + 300, ty + 34

    d.text((mx + 6, my + mot.height + 6),
           "Packs graphiques FiveM, installés en un clic",
           font=ImageFont.truetype(SANS_SB, 27), fill=GRIS)

    # pastilles : ce que fait vraiment l'app
    f = ImageFont.truetype(SANS_SB, 22)
    x, y = tx, ty + 292
    for mot_p in ("UN CLIC", "RÉVERSIBLE", "OPEN SOURCE", "GRATUIT"):
        w = d.textbbox((0, 0), mot_p, font=f)[2] + 76
        d.rounded_rectangle((x, y, x + w, y + 56), radius=28,
                            fill=(16, 16, 18), outline=(54, 54, 58))
        d.ellipse((x + 27, y + 23, x + 38, y + 34), fill=ROUGE)
        d.text((x + 52, y + 15), mot_p, font=f, fill=(226, 226, 231))
        x += w + 20

    # barre d'appel
    bx, by, bw, bh = tx + 92, y + 96, 760, 84
    d.rounded_rectangle((bx, by, bx + bw, by + bh), radius=20,
                        fill=(15, 15, 17), outline=(52, 52, 56))
    fb = ImageFont.truetype(SANS, 30)
    txt = "GÈRE TES PACKS COMME UN PRO"
    tw = d.textbbox((0, 0), txt, font=fb)[2]
    d.text((bx + (bw - tw) / 2 - 16, by + 24), txt, font=fb, fill=BLANC)
    d.text((bx + (bw + tw) / 2 + 8, by + 22), "›",
           font=ImageFont.truetype(SANS, 36), fill=ROUGE)
    return im


ico = os.path.join(HERE, "app.ico")
frames = [icone(s) for s in TAILLES_ICO]
frames[-1].save(ico, format="ICO", sizes=[(s, s) for s in TAILLES_ICO],
                append_images=frames[:-1])
print(f"app.ico          {os.path.getsize(ico):>8} o  ({len(TAILLES_ICO)} tailles)")

b = banniere()
for chemin in (os.path.join(HERE, ".github", "assets", "banner.png"),
               os.path.join(HERE, "site", "assets", "banner.png")):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    b.save(chemin, optimize=True)
    print(f"{os.path.relpath(chemin, HERE):<32} {os.path.getsize(chemin):>8} o")

for chemin in (os.path.join(HERE, "app_icon_preview.png"),
               os.path.join(HERE, ".github", "assets", "icon.png"),
               os.path.join(HERE, "site", "assets", "icon.png")):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    icone(256).save(chemin)
import shutil
shutil.copy(ico, os.path.join(HERE, "site", "assets", "favicon.ico"))
print("icones et favicon ecrits")
