#!/bin/bash
echo "==========================================="
echo " FaceTrack Pro - macOS/Linux Auto Installer"
echo "==========================================="

echo "[1/4] Checking Python 3..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.9+ first."
    exit 1
fi

echo "[2/4] Checking for CMake (required for face_recognition)..."
if ! command -v cmake &> /dev/null; then
    echo "⚠️ CMake is not installed."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "Installing cmake via brew..."
        brew install cmake
    else
        echo "Please run: sudo apt install cmake"
        exit 1
    fi
fi

echo "[3/4] Creating virtual environment (optional but recommended)..."
python3 -m venv venv
source venv/bin/activate

echo "[4/4] Installing dependencies from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

echo "==========================================="
echo "✅ Installation Complete!"
echo "Run the application by executing: ./run.sh"
echo "==========================================="
