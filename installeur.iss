; Installeur Modium (Inno Setup 6)
; Compilation : build.py s'en charge, ou ISCC.exe installeur.iss
; La version est injectee par build.py depuis APP_VERSION du source.

#ifndef AppVersion
  #define AppVersion "2.1.0"
#endif

#define AppName    "Modium"
#define AppExe     "Modium.exe"
#define AppPublisher "modium.xyz"
#define AppUrl     "https://modium.xyz"

[Setup]
AppId={{8E2F5A31-7C4D-4B9E-A6F3-1D0B2C5E7A94}
AppName={#AppName}
AppVersion={#AppVersion}
AppPublisher={#AppPublisher}
AppPublisherURL={#AppUrl}
AppSupportURL=https://github.com/ImSerial/modium
VersionInfoVersion={#AppVersion}

; Installation par utilisateur : aucun UAC, aucun droit administrateur.
; L'app ecrit dans FiveM.app et GTA V, pas besoin d'etre dans Program Files.
PrivilegesRequired=lowest
DefaultDirName={autopf}\{#AppName}
DisableProgramGroupPage=yes
DefaultGroupName={#AppName}

OutputDir=dist_installeur
OutputBaseFilename=Modium-Setup-{#AppVersion}
SetupIconFile=app.ico
UninstallDisplayIcon={app}\{#AppExe}
UninstallDisplayName={#AppName}

Compression=lzma2/max
SolidCompression=yes
WizardStyle=modern
ArchitecturesInstallIn64BitMode=x64compatible
ArchitecturesAllowed=x64compatible

; Refuse d'installer par-dessus une app en cours d'execution
CloseApplications=yes
RestartApplications=no

[Languages]
Name: "fr"; MessagesFile: "compiler:Languages\French.isl"

[Tasks]
Name: "desktopicon"; Description: "Créer un raccourci sur le Bureau"; \
  GroupDescription: "Raccourcis :"

[Files]
; Build --onedir : tout le dossier dist\Modium.
; Demarrage quasi instantane, contre plusieurs secondes en --onefile qui
; redecompressait 17 Mo dans le dossier temporaire a chaque lancement.
Source: "dist\Modium\*"; DestDir: "{app}"; \
  Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\{#AppName}"; Filename: "{app}\{#AppExe}"
Name: "{group}\Désinstaller {#AppName}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#AppName}"; Filename: "{app}\{#AppExe}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#AppExe}"; Description: "Lancer {#AppName}"; \
  Flags: nowait postinstall skipifsilent

[UninstallDelete]
; Le dossier de l'app seulement. Les donnees (cache des packs, sauvegardes
; des fichiers d'origine, reglages) vivent dans %LOCALAPPDATA%\Modium
; et sont traitees dans InitializeUninstall / CurUninstallStepChanged.
Type: filesandordirs; Name: "{app}"

[Code]
// Attention : une ligne qui COMMENCE par # est lue comme une directive du
// preprocesseur. Les sauts de ligne passent donc par cette constante.
const
  NL = #13#10;

function DataDir(): String;
begin
  Result := ExpandConstant('{localappdata}\Modium');
end;

// Refuse la desinstallation tant qu'un pack est installe dans le jeu.
// Sans ce garde-fou, supprimer les donnees emporterait les sauvegardes des
// fichiers d'origine : GTA V resterait modifie, sans aucun moyen de revenir
// en arriere. L'exe repond en code de sortie via --check-loaded.
function InitializeUninstall(): Boolean;
var
  Exe: String;
  Code: Integer;
begin
  Result := True;
  Exe := ExpandConstant('{app}\Modium.exe');
  if not FileExists(Exe) then
    Exit;
  if not Exec(Exe, '--check-loaded', '', SW_HIDE, ewWaitUntilTerminated, Code) then
    Exit;
  if Code = 1 then
  begin
    MsgBox('Des packs sont encore chargés dans FiveM ou GTA V.' + NL + NL +
           'Ouvre Modium et décharge-les avant de désinstaller.' +
           NL + NL +
           'Sinon les fichiers d''origine de ton jeu, sauvegardés par l''app, ' +
           'seraient perdus et le jeu resterait modifié définitivement.',
           mbCriticalError, MB_OK);
    Result := False;
  end;
end;

procedure CurUninstallStepChanged(CurUninstallStep: TUninstallStep);
begin
  if CurUninstallStep = usPostUninstall then
  begin
    if DirExists(DataDir()) then
      if MsgBox('Supprimer aussi les packs téléchargés et les réglages ?' +
                NL + NL + DataDir() + NL + NL +
                'Réponds Non pour les garder en vue d''une réinstallation.',
                mbConfirmation, MB_YESNO) = IDYES then
        DelTree(DataDir(), True, True, True);
  end;
end;
