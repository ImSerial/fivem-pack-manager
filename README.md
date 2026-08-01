<div align="center">

<img src=".github/assets/banner.svg" alt="FiveM Pack Manager" width="100%">

<br>

![Windows](https://img.shields.io/badge/Windows-10%20%7C%2011-0a0a0a?style=for-the-badge&logo=windows11&logoColor=white&labelColor=000000)
![Python](https://img.shields.io/badge/Python-3.10+-0a0a0a?style=for-the-badge&logo=python&logoColor=white&labelColor=000000)
![Standalone](https://img.shields.io/badge/exe-100%25%20autonome-0a0a0a?style=for-the-badge&labelColor=000000)
![Setup](https://img.shields.io/badge/configuration-aucune-0a0a0a?style=for-the-badge&labelColor=000000)

**Installe et désinstalle tes packs graphiques FiveM en un clic.**
QuantV · NVE · ReShade · ENB · mods · plugins

<br>

<img src="https://github.com/user-attachments/assets/d551e536-6a45-416a-bb89-2f08a2e3f136" alt="Interface de FiveM Pack Manager" width="880">

</div>

<img src=".github/assets/divider.svg" alt="" width="100%">

## Le problème

Installer un pack graphique à la main, c'est ouvrir l'archive, deviner où va
chaque dossier, en copier une partie dans `FiveM.app`, l'autre dans le dossier
de GTA V, écraser des fichiers sans savoir lesquels — et prier pour pouvoir
revenir en arrière.

**Cette app fait tout ça pour toi, et sait défaire ce qu'elle a fait.**

<img src=".github/assets/divider.svg" alt="" width="100%">

## Installation

<table>
<tr>
<td width="50%" valign="top">

### ⚡ Prêt à l'emploi

Télécharge `FiveMPackManager.exe` depuis les [**Releases**](../../releases)
et double-clique.

Aucune installation, aucune configuration, aucune dépendance.
Les packs apparaissent tout seuls au lancement.

</td>
<td width="50%" valign="top">

### 🛠 Depuis le source

Nécessite [Python 3.10+](https://www.python.org/downloads/)
avec *Add Python to PATH* coché.

```bash
git clone https://github.com/ImSerial/fivem-pack-manager
cd fivem-pack-manager
Lancer.bat
```

</td>
</tr>
</table>

<img src=".github/assets/divider.svg" alt="" width="100%">

## Utilisation

| | Bouton | Ce qu'il fait |
|:--:|---|---|
| ⬇ | **Charger** | Télécharge le pack si besoin, l'extrait, l'installe. Sauvegarde tout fichier écrasé. |
| ↩ | **Décharger** | Retire exactement ce qui a été installé, restaure les originaux, nettoie les dossiers vides. |
| ▶ | **Preview** | Ouvre la vidéo de présentation du pack, quand il y en a une. |
| ✕ | **Annuler** | Stoppe un téléchargement en cours et nettoie derrière lui. |

La console en bas décrit chaque action en direct. La **taille du pack** est
affichée sur sa carte avant même de le télécharger.

> [!IMPORTANT]
> Ferme FiveM et GTA V avant de charger ou décharger. L'app refuse de continuer
> sinon — les fichiers seraient verrouillés et l'installation à moitié faite.

> [!NOTE]
> Les packs en `.rar` demandent **WinRAR ou 7-Zip** installé sur le PC.
> Les `.zip` fonctionnent partout.

<img src=".github/assets/divider.svg" alt="" width="100%">

## Ce qui se passe quand tu cliques sur Charger

```mermaid
flowchart LR
    A["🖱️ Charger"] --> B{"En cache ?"}
    B -- non --> C["⬇ Téléchargement<br/>Drive · Mega · Gofile · direct"]
    B -- oui --> E
    C --> D["📦 Extraction<br/>zip · rar · 7z · multi-volumes"]
    D --> E["🔍 Analyse de l'arbre"]
    E --> F["📁 FiveM.app<br/>citizen · mods · plugins"]
    E --> G["🎮 Dossier GTA V<br/>ENB · d3d11.dll · .asi"]
    E --> H["🗂️ mods/<br/>fichiers .rpf"]
    F --> I["💾 Sauvegarde des<br/>fichiers écrasés"]
    G --> I
    H --> I
    I --> J["✅ Installé"]
    I -. échec .-> K["⛔ Rollback complet"]
```

Chaque créateur range son pack à sa façon. L'app parcourt **tout** l'arbre et
répartit selon ce qu'elle trouve, quel que soit le niveau où c'est rangé.

<details>
<summary><b>Le détail du routage</b></summary>

<br>

| Dans le pack | Destination |
|---|---|
| `citizen/`, `mods/`, `plugins/`, `reshade-*` | `%LOCALAPPDATA%\FiveM\FiveM.app` |
| contenu de `GTAV/` ou `GTA5/` (ENB, `d3d11.dll`, `.asi`, `.ini`) | dossier d'installation de GTA V |
| fichiers `.rpf` | toujours `mods/`, au même sous-chemin que l'original |
| readme, screenshots, dossiers parasites | ignorés |

Cas particuliers gérés :

- pack ENB « nu », sans dossier wrapper `GTA5`
- `.asi` isolé, installé dans `plugins/` avec son `.ini` de config
- archives multi-volumes : `.part1.rar`, `.r00`/`.r01`, `.7z.001`
- archives imbriquées (`FIVEM.rar` + `GTA5.rar` dans le téléchargement)
- dossiers en majuscules laissés par une vieille install manuelle
- noms de dossiers exotiques : `GTA V Legacy`, `SinglePlayer`, `FIVEM FILES`…

Les deux dossiers de jeu sont détectés automatiquement (registre, `CitizenFX.ini`,
chemins connus dont les variantes *Legacy*). Réglables à la main dans
**Options → Avancé** si la détection se trompe.

</details>

<img src=".github/assets/divider.svg" alt="" width="100%">

## Sécurités

<table>
<tr>
<td width="33%" valign="top">

**🔒 Avant**

Refuse de travailler si FiveM ou GTA V tourne. Vérifie l'espace disque. Garde
anti double-chargement.

</td>
<td width="33%" valign="top">

**⚙️ Pendant**

Interdit toute écriture hors des dossiers cibles. **Rollback automatique** si
l'installation échoue en cours de route.

</td>
<td width="33%" valign="top">

**↩️ Après**

Le déchargement retire exactement ce qui a été posé et restaure les originaux.
Le jeu revient propre.

</td>
</tr>
</table>

Un dossier remplacé en entier (`enbseries`, `reshade-shaders`…) est mis de côté
complet, jamais mélangé avec l'ancien. `citizen`, `update`, `x64`, `dlcpacks` ne
sont jamais purgés : fusion classique, avec sauvegarde fichier par fichier.

<img src=".github/assets/divider.svg" alt="" width="100%">

## Ajouter tes propres packs

**Options → Mes packs**, colle un lien.

<table>
<tr>
<td align="center" width="25%"><b>Google Drive</b><br><sub>fichier ou dossier entier</sub></td>
<td align="center" width="25%"><b>Mega.nz</b><br><sub>déchiffrement AES client</sub></td>
<td align="center" width="25%"><b>Gofile</b><br><sub>résolution via API</sub></td>
<td align="center" width="25%"><b>Lien direct</b><br><sub>.rar · .zip · .7z</sub></td>
</tr>
</table>

Pour un **dossier** Google Drive, l'arbre est reconstruit et téléchargé fichier
par fichier ; les archives qu'il contient sont extraites automatiquement.

Champs image et preview YouTube optionnels. **Modifier** repréremplit le
formulaire ; la croix retire le pack **et** ses fichiers téléchargés, après
confirmation.

<img src=".github/assets/divider.svg" alt="" width="100%">

## Héberger ta propre liste

L'app pointe par défaut sur une liste publique. Pour servir la tienne, indique
l'URL de ton `packs.json` dans **Options → Avancé**, ou builde un exe avec ton
propre `embedded_config.json`.

<details>
<summary><b>Format du <code>packs.json</code></b></summary>

<br>

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

</details>

<details>
<summary><b>Config nginx</b></summary>

<br>

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

</details>

<details>
<summary><b>Builder l'exe</b></summary>

<br>

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

```
valeurs du code  →  embedded_config.json  →  config.json
```

</details>

<img src=".github/assets/divider.svg" alt="" width="100%">

## Dépannage

| Symptôme | Cause |
|---|---|
| « Aucun pack disponible » | serveur injoignable ou URL invalide → **Actualiser**, puis Options → Avancé |
| « FiveM est ouvert » | ferme le jeu **et** le launcher, ils verrouillent les fichiers |
| Extraction impossible sur un `.rar` | installe WinRAR ou 7-Zip |
| Le pack se télécharge mais n'installe rien | archive rangée d'une façon inconnue — la console détaille ce qui a été trouvé |
| Vignette pas à jour | l'image est mise en cache au premier téléchargement du pack |

<img src=".github/assets/divider.svg" alt="" width="100%">

## Sous le capot

<details>
<summary><b>Architecture</b></summary>

<br>

L'interface est du HTML/CSS/JS servi par un petit serveur HTTP local
(`127.0.0.1`, protégé par jeton), affiché dans une fenêtre
[pywebview](https://pywebview.flowrl.com/). Ce choix contourne un blocage du
pont natif pywebview une fois l'application compilée en exe.

Extraction : `zipfile` natif, puis UnRAR → WinRAR → 7-Zip → tar, chaque outil
installé étant essayé jusqu'au premier qui réussit.

| Fichier | Rôle |
|---|---|
| `pack_manager.py` | toute l'application |
| `Lancer.bat` | lance depuis le source, installe les dépendances au besoin |
| `requirements.txt` | dépendances Python |

Les données de travail (cache des packs, sauvegardes, réglages, image de fond)
vivent dans `%LOCALAPPDATA%\FiveMPackManager\` pour l'exe, et à côté du script
en mode développement.

</details>

<br>

<div align="center">
<sub>Fait pour la commu FiveM · <a href="https://uxqt.site">uxqt.site</a></sub>
</div>
