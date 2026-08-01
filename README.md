# FiveM Pack Manager

<img width="970" height="714" alt="FiveM Pack Manager" src="https://github.com/user-attachments/assets/d551e536-6a45-416a-bb89-2f08a2e3f136" />

**FiveMPackManager.exe est 100 % autonome** : URL du serveur et clé d'accès
embarquées dans le binaire. Pour distribuer, donne UNIQUEMENT le .exe.
Ses données (cache des packs, sauvegardes, réglages) vivent dans
`%LOCALAPPDATA%\FiveMPackManager\`.

L'app liste les packs graphiques hébergés sur ton site (uxqt.site), avec
image, 2 boutons par pack et une console qui décrit chaque action.

- **Charger** : télécharge le `.rar`/`.zip` depuis le site (si pas déjà en
  cache), l'extrait, détecte la structure et copie chaque dossier au bon
  endroit : citizen/mods/plugins → FiveM.app, contenu GTAV/GTA5 (ENB...) →
  dossier d'installation de GTA V. Les fichiers originaux écrasés sont
  sauvegardés automatiquement.
- **Décharger** : retire exactement ce qui a été installé (des deux côtés),
  restaure les originaux, nettoie les dossiers vides. Le jeu revient propre.

⚠ Ferme FiveM et GTA V avant de charger/décharger (bloqué sinon, c'est voulu).
⚠ Pour les `.rar`, le PC doit avoir WinRAR ou 7-Zip (les `.zip` marchent partout).

## Ajouter un pack

Les archives sont référencées par **liens** dans le `packs.json` hébergé sur le
VPS (`/var/www/packs/packs.json`). Deux formes d'entrée :

```json
{
  "packs": [
    { "name": "QuantV", "url": "https://exemple.com/lien-direct/quantv.rar", "version": "1" },
    { "name": "NVE", "file": "nve.rar", "version": "1" }
  ]
}
```

- `url` = lien externe direct vers le .rar/.zip (n'importe quel hébergeur,
  mais le lien doit pointer vers le fichier lui-même, pas une page de
  téléchargement).
- `file` = fichier posé dans `/var/www/packs/` sur le VPS (la clé d'accès est
  ajoutée automatiquement).
- `image` optionnel : lien externe ou fichier dans `/var/www/packs/`.
- Mise à jour : incrémente `version` → l'app re-télécharge au prochain chargement.

⚠ `admin-vps.json` contient les accès SSH du VPS — jamais le distribuer.

L'archive doit contenir directement la structure de FiveM.app :
`citizen/`, `mods/`, `plugins/`, fichiers racine (dxgi.dll...). Un dossier
racine unique dans l'archive est toléré (aplati automatiquement).

**Mise à jour d'un pack** : remplace le fichier + incrémente `version` dans
packs.json → l'app affiche « ⬆ mise à jour dispo » et re-télécharge au
prochain chargement.

## Fichiers du projet (dev uniquement — rien à distribuer)

- `pack_manager.py` — source. En dev, les données restent dans ce dossier ;
  en exe compilé, tout va dans `%LOCALAPPDATA%\FiveMPackManager\`
- `Lancer.bat` — lance l'app depuis le source (installe les dépendances
  manquantes au premier lancement, nécessite Python)
- `config.json` — surcharge locale de la config embarquée (optionnel)
- `admin-vps.json` — accès SSH du VPS (JAMAIS distribuer)
- `packs.reel.json` — copie de secours du `packs.json` du VPS (gitignoré)

## Recompiler l'exe

Crée `embedded_config.json` avec tes vraies valeurs (gitignoré, injecté dans
le binaire au build) :

```json
{
  "packs_url": "https://ton-site.example/chemin-secret/packs.json",
  "packs_key": "ta-cle-secrete-ou-vide"
}
```

```
python -m pip install -r requirements.txt
python -m PyInstaller --onefile --noconsole --name FiveMPackManager ^
  --collect-all webview --collect-all cryptography ^
  --add-data "embedded_config.json;." pack_manager.py
```

`.gitignore` couvre `embedded_config.json` et `admin-vps.json`. Le code source
ne contient aucun secret : publiable tel quel.

## Config serveur (nginx)

À inclure dans le bloc `server {}` du site (fichier typique :
`/etc/nginx/sites-available/tonsite`). Les fichiers vivent dans
`/var/www/packs/` (packs.json + éventuels .zip/.jpg posés sur le VPS).
Le chemin `/packs-x7k2m9/` est volontairement impossible à deviner et n'est
lié nulle part sur le site.

```nginx
location /packs-x7k2m9/ {
    alias /var/www/packs/;
    autoindex off;                 # personne ne peut lister le dossier

    # Protection par clé : la même clé se met dans l'app (embedded_config),
    # envoyée en ?key=...
    # if ($arg_key != "TA_CLE_SECRETE") {
    #     return 403;
    # }

    # gros zips : reprise de téléchargement supportée
    add_header Accept-Ranges bytes;
}
```
