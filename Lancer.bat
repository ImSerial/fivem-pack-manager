@echo off
cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 (
    echo Python introuvable. Installe-le depuis https://www.python.org/downloads/
    echo puis coche "Add Python to PATH" pendant l'installation.
    pause
    exit /b 1
)

rem Installe les dependances seulement si elles manquent
python -c "import webview, cryptography" >nul 2>nul
if errorlevel 1 (
    echo Premiere utilisation : installation des dependances...
    python -m pip install -r requirements.txt
)

start "" pythonw pack_manager.py
