@echo off
TITLE FaceTrack Pro - Windows Installer
echo ===========================================
echo  FaceTrack Pro - Windows Auto Installer
echo ===========================================

echo [1/3] Checking Python...
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo ERROR: Python is not installed or not in PATH.
    echo Please install Python 3.9+ from https://www.python.org/downloads/
    pause
    exit /b
)

echo [2/3] Upgrading pip...
python -m pip install --upgrade pip

echo [3/3] Installing dependencies...
pip install -r requirements.txt

echo ===========================================
echo  Installation Complete!
echo  Run the application using: run.bat
echo ===========================================
pause
