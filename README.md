# FiveM Pack Manager

<img width="970" height="714" alt="FiveM Pack Manager" src="https://github.com/user-attachments/assets/d551e536-6a45-416a-bb89-2f08a2e3f136" />

Installe et désinstalle des **packs graphiques FiveM** en un clic — QuantV, NVE,
ReShade, ENB, mods, plugins. Plus besoin de glisser les fichiers à la main dans
cinq dossiers différents en croisant les doigts.

L'app télécharge le pack, détecte toute seule comment il est rangé, envoie chaque
partie au bon endroit, et **sauvegarde ce qu'elle écrase**. Un bouton pour
désinstaller, et le jeu revient exactement comme avant.

---

## Installation

**Le plus simple** — télécharge `FiveMPackManager.exe` depuis les
[Releases](../../releases) et double-clique. Rien à installer, rien à configurer,
les packs apparaissent tout seuls.

**Depuis le source** — nécessite [Python 3.10+](https://www.python.org/downloads/)
avec *Add Python to PATH* coché :

```bash
git clone https://github.com/ImSerial/fivem-pack-manager
cd fivem-pack-manager
Lancer.bat
```

`Lancer.bat` installe les dépendances au premier lancement, puis ouvre l'app.

---

## Utilisation

| Bouton | Ce qu'il fait |
|---|---|
| **Charger** | Télécharge le pack si besoin, l'extrait, l'installe. Sauvegarde tout fichier écrasé. |
| **Décharger** | Retire exactement ce qui a été installé, restaure les originaux, nettoie les dossiers vides. |
| **Preview** | Ouvre la vidéo de présentation du pack, quand il y en a une. |
| **annuler le téléchargement** | Stoppe un téléchargement en cours et nettoie derrière lui. |

La console en bas décrit chaque action en direct. La taille du pack est affichée
sur sa carte **avant** de le télécharger.

> [!IMPORTANT]
> Ferme FiveM et GTA V avant de charger ou décharger. L'app refuse de continuer
> sinon — les fichiers seraient verrouillés et l'installation à moitié faite.

> [!NOTE]
> Les packs en `.rar` demandent **WinRAR ou 7-Zip** installé sur le PC.
> Les `.zip` fonctionnent partout.

---

## Où vont les fichiers

Chaque créateur range son pack à sa façon. L'app parcourt tout l'arbre et
répartit selon ce qu'elle trouve, quel que soit le niveau où c'est rangé :

| Dans le pack | Destination |
|---|---|
| `citizen/`, `mods/`, `plugins/`, `reshade-*` | `%LOCALAPPDATA%\FiveM\FiveM.app` |
| contenu de `GTAV/` ou `GTA5/` (ENB, `d3d11.dll`, `.asi`, `.ini`) | dossier d'installation de GTA V |
| fichiers `.rpf` | toujours `mods/`, au même sous-chemin que l'original |
| readme, screenshots, dossiers parasites | ignorés |

Cas particuliers gérés : pack ENB « nu » sans dossier wrapper, `.asi` isolé avec
son `.ini`, archives multi-volumes (`.part1.rar`, `.r00`, `.7z.001`), archives
imbriquées, dossiers en majuscules d'une vieille install manuelle.

Les deux dossiers de jeu sont détectés automatiquement (registre, `CitizenFX.ini`,
chemins connus dont les variantes *Legacy*). Réglables à la main dans **Options →
Avancé** si la détection se trompe.

---

## Sécurités

- Refuse de travailler si FiveM ou GTA V tourne
- Vérifie l'espace disque avant de télécharger
- **Rollback automatique** si l'installation échoue en cours de route
- Interdit toute écriture en dehors des dossiers cibles
- Garde anti double-chargement du même pack
- Un dossier remplacé en entier (`enbseries`, `reshade-shaders`…) est mis de côté
  complet, jamais mélangé avec l'ancien. `citizen`, `update`, `x64`, `dlcpacks`
  ne sont jamais purgés : fusion classique, avec sauvegarde fichier par fichier.

---

## Ajouter tes propres packs

**Options → Mes packs**, colle un lien. Formats acceptés :

- **Google Drive** — fichier ou dossier entier (l'arbre est reconstruit et
  téléchargé fichier par fichier)
- **Mega.nz** — déchiffrement AES côté client
- **Gofile**
- n'importe quel **lien direct** `.rar` / `.zip` / `.7z`

Un champ image et un champ preview YouTube sont disponibles, tous deux optionnels.
Le bouton **Modifier** repréremplit le formulaire ; la croix retire le pack **et**
efface ses fichiers téléchargés, après confirmation.

---

## Héberger ta propre liste de packs

L'app pointe par défaut sur une liste publique. Pour servir la tienne, indique
l'URL de ton `packs.json` dans **Options → Avancé**, ou builde un exe avec ton
propre `embedded_config.json` (voir plus bas).

### Format du `packs.json`

```json
{
  "packs": [
    {
      "name": "QuantV",
      "url": "https://exemple.com/quantv.rar",
      "version": "2",
      "size": "4.1 Go",
      "image": "https://exemple.com/quantv.webp",
      "preview": "https://youtu.be/xxxxxxxxxxx"
    },
    { "name": "NVE", "file": "nve.rar", "version": "1" }
  ]
}
```

| Champ | Rôle |
|---|---|
| `name` | obligatoire, sert d'identifiant |
| `url` | lien externe direct vers l'archive |
| `file` | *alternative à `url`* : fichier posé à côté du `packs.json` |
| `version` | incrémente-la pour forcer le re-téléchargement |
| `size` | affiché sur la carte avant téléchargement |
| `image` | lien externe, ou fichier à côté du `packs.json` |
| `preview` | lien vidéo, affiche un bouton Preview |

### Config nginx

```nginx
location /mon-dossier-packs/ {
    alias /var/www/packs/;
    autoindex off;                 # le dossier n'est pas listable

    if ($arg_key != "MA_CLE") {    # clé envoyée par l'app en ?key=
        return 404;
    }

    add_header Accept-Ranges bytes;   # reprise de téléchargement
}
```

---

## Builder l'exe

```bash
python -m pip install -r requirements.txt

python -m PyInstaller --onefile --noconsole --name FiveMPackManager ^
  --collect-all webview --collect-all cryptography ^
  pack_manager.py
```

Pour pointer sur ton propre serveur, crée un `embedded_config.json` à côté du
script et ajoute `--add-data "embedded_config.json;."` à la commande :

```json
{
  "packs_url": "https://ton-site.fr/mon-dossier-packs/packs.json",
  "packs_key": "ma-cle-ou-vide"
}
```

Priorité de configuration, du plus faible au plus fort :
**valeurs du code** → `embedded_config.json` → `config.json` (données de l'app).

---

## Dépannage

| Symptôme | Cause |
|---|---|
| « Aucun pack disponible » | serveur injoignable ou URL invalide → **Actualiser**, puis Options → Avancé |
| « FiveM est ouvert » | ferme le jeu **et** le launcher, ils verrouillent les fichiers |
| Extraction impossible sur un `.rar` | installe WinRAR ou 7-Zip |
| Le pack se télécharge mais n'installe rien | archive rangée d'une façon inconnue — la console détaille ce qui a été trouvé |
| Vignette pas à jour | l'image est mise en cache au premier téléchargement du pack |

---

## Structure du projet

| Fichier | Rôle |
|---|---|
| `pack_manager.py` | toute l'application |
| `Lancer.bat` | lance depuis le source, installe les dépendances au besoin |
| `requirements.txt` | dépendances Python |

Les données de travail (cache des packs, sauvegardes, réglages, image de fond)
vivent dans `%LOCALAPPDATA%\FiveMPackManager\` pour l'exe, et à côté du script
en mode développement.

### Comment c'est fait

L'interface est du HTML/CSS/JS servi par un petit serveur HTTP local
(`127.0.0.1`, protégé par jeton), affiché dans une fenêtre
[pywebview](https://pywebview.flowrl.com/). Ce choix contourne un blocage du pont
natif pywebview une fois l'application compilée en exe.

Extraction : `zipfile` natif, puis UnRAR → WinRAR → 7-Zip → tar, chaque outil
installé étant essayé jusqu'au premier qui réussit.
