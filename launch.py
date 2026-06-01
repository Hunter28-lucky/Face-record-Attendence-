#!/usr/bin/env python3
# Made by Harsh Bardhan Kumar and Team
"""
╔══════════════════════════════════════════════════════════════╗
║        UNIFIED LAUNCHER & BOOTSTRAPPER — FaceTrack Pro       ║
║  Auto-detects environment, installs dependencies, loads      ║
║  demo data, and runs the application seamlessly on any OS.   ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import sys
import subprocess
import platform
import shutil

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT_DIR)

PASS = "✅"
FAIL = "❌"
WARN = "⚠️"
INFO = "ℹ️"

print("=" * 60)
print("             FaceTrack Pro — Smart Boot Launcher")
print("=" * 60)

def get_venv_python():
    """Identify the virtual environment Python interpreter."""
    # Look for existing environments
    candidates = ["brew-venv", "venv", ".venv"]
    for cand in candidates:
        cand_path = os.path.join(ROOT_DIR, cand)
        if os.path.isdir(cand_path):
            if platform.system() == "Windows":
                py_path = os.path.join(cand_path, "Scripts", "python.exe")
            else:
                py_path = os.path.join(cand_path, "bin", "python")
            if os.path.exists(py_path):
                return py_path, cand
    return None, None

def create_venv():
    """Create a virtual environment if none exists."""
    print(f"\n{INFO} No virtual environment detected. Creating a fresh 'venv'...")
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print(f"{PASS} Virtual environment 'venv' successfully created!")
        
        # Resolve python path
        if platform.system() == "Windows":
            return os.path.join(ROOT_DIR, "venv", "Scripts", "python.exe"), "venv"
        else:
            return os.path.join(ROOT_DIR, "venv", "bin", "python"), "venv"
    except Exception as e:
        print(f"{FAIL} Failed to create virtual environment automatically: {e}")
        print(f"{WARN} Proceeding with system python interpreter...")
        return sys.executable, "system"

def verify_and_install_deps(python_bin, venv_name):
    """Ensure all required Python packages are installed inside the venv."""
    print(f"\n{INFO} Verifying dependencies in '{venv_name}'...")
    
    # Standard packages that are critical
    required_packages = {
        "cv2": "opencv-python",
        "pkg_resources": "setuptools<82",
        "face_recognition": "face-recognition",
        "customtkinter": "customtkinter",
        "PIL": "Pillow",
        "pandas": "pandas",
        "numpy": "numpy",
        "openpyxl": "openpyxl",
        "matplotlib": "matplotlib",
        "pygame": "pygame",
        "qrcode": "qrcode[pil]",
        "tqdm": "tqdm"
    }
    
    missing_packages = []
    for module_name, pip_name in required_packages.items():
        try:
            # Run check using the virtual env python binary
            subprocess.run(
                [python_bin, "-c", f"import {module_name}"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True
            )
        except subprocess.CalledProcessError:
            missing_packages.append(pip_name)

    if not missing_packages:
        print(f"{PASS} All libraries are already installed and up to date.")
        return True

    print(f"{WARN} Missing libraries detected: {', '.join(missing_packages)}")
    print(f"{INFO} Installing dependencies automatically...")
    
    # ── Handle system compiler warnings for dlib ─────────────────
    if "face-recognition" in missing_packages and not shutil.which("cmake"):
        print(f"\n{WARN} CMake is required to compile 'face-recognition'/'dlib' on your device.")
        if platform.system() == "Darwin":
            print(f"{INFO} Suggestion: Run 'brew install cmake' first.")
        elif platform.system() == "Windows":
            print(f"{INFO} Suggestion: Install CMake from https://cmake.org/download/ and check 'Add to Path'.")
        else:
            print(f"{INFO} Suggestion: Run 'sudo apt install cmake' first.")
        print("-" * 60)
        
    try:
        # Upgrade pip first
        subprocess.run([python_bin, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        # Install from requirements.txt
        req_file = os.path.join(ROOT_DIR, "requirements.txt")
        if os.path.exists(req_file):
            subprocess.run([python_bin, "-m", "pip", "install", "-r", req_file], check=True)
        else:
            # Install individual missing packages if requirements.txt doesn't exist
            subprocess.run([python_bin, "-m", "pip", "install"] + missing_packages, check=True)
        print(f"{PASS} All dependencies successfully installed!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"{FAIL} Dependency installation failed: {e}")
        print(f"{WARN} Attempting to proceed anyway...")
        return False

def seed_database_if_empty(python_bin):
    """Seed sample records if the database has zero registered users."""
    try:
        from database.db_manager import DatabaseManager
        db = DatabaseManager()
        if db.get_total_users() == 0:
            print(f"\n{INFO} Empty database detected. Loading demo data to populate analytics...")
            subprocess.run([python_bin, os.path.join(ROOT_DIR, "seed_demo_data.py")], check=True)
    except Exception:
        # Fallback if SQLite/import issues occur before main launch
        pass

def main():
    # 1. Resolve virtual environment Python interpreter
    python_bin, venv_name = get_venv_python()
    if not python_bin:
        python_bin, venv_name = create_venv()
        
    # 2. Check & auto-install dependencies
    verify_and_install_deps(python_bin, venv_name)
    
    # 3. Seed demo data is disabled to only keep real users
    # seed_database_if_empty(python_bin)
    
    # 4. Start the application
    print(f"\n{PASS} Bootstrapping completed! Starting FaceTrack Pro...")
    print("=" * 60)
    
    try:
        main_script = os.path.join(ROOT_DIR, "main.py")
        subprocess.run([python_bin, main_script])
    except KeyboardInterrupt:
        print(f"\n{INFO} Application terminated by user.")
    except Exception as e:
        print(f"{FAIL} Error launching application: {e}")

if __name__ == "__main__":
    main()
