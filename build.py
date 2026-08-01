# Chaine de build complete : source lisible -> exe -> installeur.
#   python build.py            tout
#   python build.py --exe      s'arrete apres l'exe (pas d'installeur)
#   python build.py --iss      recompile juste l'installeur (exe deja construit)
#
# La version vient de APP_VERSION dans pack_manager.source.py : c'est la
# seule source de verite, version_info.txt et l'installeur en decoulent.
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
ONLY_EXE = "--exe" in sys.argv
ONLY_ISS = "--iss" in sys.argv

SOURCE = "pack_manager.source.py"
GENERATED = "pack_manager.py"
NAME = "Modium"


def run(cmd, label):
    print(f"\n>>> {label}")
    r = subprocess.run(cmd)
    if r.returncode != 0:
        sys.exit(f"ECHEC : {label} (code {r.returncode})")


def version() -> str:
    src = open(SOURCE, encoding="utf-8").read()
    m = re.search(r'^APP_VERSION\s*=\s*"([^"]+)"', src, re.M)
    if not m:
        sys.exit("APP_VERSION introuvable dans " + SOURCE)
    return m.group(1)


def write_version_info(v: str):
    """Metadonnees de Proprietes > Details. Un binaire sans editeur ni
    description parait anonyme et aggrave l'alerte SmartScreen."""
    parts = [int(n) for n in v.split(".")] + [0, 0, 0, 0]
    quad = ", ".join(str(n) for n in parts[:4])
    open("version_info.txt", "w", encoding="utf-8").write(f"""\
# Genere par build.py depuis APP_VERSION — ne pas editer a la main.
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=({quad}), prodvers=({quad}),
    mask=0x3f, flags=0x0, OS=0x40004, fileType=0x1, subtype=0x0, date=(0, 0)
  ),
  kids=[
    StringFileInfo([
      StringTable('040C04B0', [
        StringStruct('CompanyName', 'modium.xyz'),
        StringStruct('FileDescription', 'Modium'),
        StringStruct('FileVersion', '{v}'),
        StringStruct('InternalName', '{NAME}'),
        StringStruct('LegalCopyright', 'modium.xyz'),
        StringStruct('OriginalFilename', '{NAME}.exe'),
        StringStruct('ProductName', 'Modium'),
        StringStruct('ProductVersion', '{v}')])
    ]),
    VarFileInfo([VarStruct('Translation', [1036, 1200])])
  ]
)
""")


def find_iscc() -> str:
    # winget installe Inno par utilisateur (LOCALAPPDATA), l'installeur
    # classique dans Program Files : on regarde les deux
    local = os.environ.get("LOCALAPPDATA", "")
    for p in (os.path.join(local, "Programs", "Inno Setup 6", "ISCC.exe"),
              r"C:\Program Files (x86)\Inno Setup 6\ISCC.exe",
              r"C:\Program Files\Inno Setup 6\ISCC.exe"):
        if p and os.path.exists(p):
            return p
    found = shutil.which("ISCC")
    if found:
        return found
    sys.exit("Inno Setup introuvable. Installe-le : "
             "winget install JRSoftware.InnoSetup")


v = version()
print(f"Modium {v}")

if not ONLY_ISS:
    if not os.path.exists("app.ico"):
        run([sys.executable, "faire_icone.py"], "generation de l'icone")

    run([sys.executable, "-m", "python_minifier", SOURCE, "--rename-globals",
         "--remove-literal-statements", "--output", GENERATED],
        "obfuscation du source")

    write_version_info(v)

    # une instance qui tourne verrouille dist\ : PyInstaller echoue alors sur
    # un PermissionError peu parlant. On ferme avant de construire.
    subprocess.run(["taskkill", "/IM", f"{NAME}.exe", "/F"],
                   capture_output=True)

    # --onedir et non --onefile : en onefile, les 17 Mo sont redecompresses
    # dans le dossier temporaire A CHAQUE lancement, d'ou plusieurs secondes
    # d'attente avant l'ouverture de la fenetre. L'installeur pose un dossier,
    # le demarrage devient immediat.
    for d in ("build", "dist"):
        shutil.rmtree(d, ignore_errors=True)
    run([sys.executable, "-m", "PyInstaller", "--noconfirm", "--onedir",
         "--windowed", "--name", NAME, "--icon", "app.ico",
         "--version-file", "version_info.txt",
         "--collect-all", "webview", "--collect-all", "cryptography",
         GENERATED], "construction de l'exe")

    exe = os.path.join("dist", NAME, NAME + ".exe")
    if not os.path.exists(exe):
        sys.exit("exe introuvable apres le build : " + exe)
    taille = sum(os.path.getsize(os.path.join(r, f))
                 for r, _d, fs in os.walk(os.path.join("dist", NAME)) for f in fs)
    print(f"\nexe : {exe} — dossier complet {taille / 1048576:.0f} Mo")

if not ONLY_EXE:
    run([find_iscc(), f"/DAppVersion={v}", "installeur.iss"],
        "construction de l'installeur")
    out = os.path.join("dist_installeur", f"{NAME}-Setup-{v}.exe")
    if os.path.exists(out):
        # copie au nom fixe : le bouton du site pointe sur
        # releases/latest/download/Modium-Setup.exe, qui n'existe que si un
        # fichier porte EXACTEMENT ce nom dans la derniere release.
        stable = os.path.join("dist_installeur", f"{NAME}-Setup.exe")
        shutil.copyfile(out, stable)
        print(f"\nInstalleur : {out} — {os.path.getsize(out) / 1048576:.0f} Mo")
        print(f"Copie au nom fixe : {stable}")
        print("Publier les DEUX dans la release : le bouton du site pointe sur "
              "releases/latest/download/Modium-Setup.exe")
        print("\nNON SIGNE : Windows affichera « Windows a protege votre PC ».")
        print("L'utilisateur doit cliquer « Informations complementaires » "
              "puis « Executer quand meme ».")
