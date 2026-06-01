"""
╔══════════════════════════════════════════════════════════════╗
║           VERIFY INSTALL — Face Attendance System           ║
║  Checks all dependencies and files before first launch      ║
╚══════════════════════════════════════════════════════════════╝

Run this before starting the app for the first time:
    python verify_install.py
"""

import sys
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

PASS = "✅"
FAIL = "❌"
WARN = "⚠️ "

print("=" * 55)
print("  FaceTrack Pro — Installation Verifier")
print("=" * 55)

all_ok = True

# ── Python version ────────────────────────────────────────────
major, minor = sys.version_info[:2]
if major >= 3 and minor >= 9:
    print(f"{PASS} Python {major}.{minor} — OK")
else:
    print(f"{FAIL} Python {major}.{minor} — Need Python 3.9+")
    all_ok = False

# ── Required packages ─────────────────────────────────────────
packages = [
    ("cv2",              "opencv-python"),
    ("pkg_resources",    "setuptools<82"),
    ("face_recognition", "face-recognition"),
    ("customtkinter",    "customtkinter"),
    ("PIL",              "Pillow"),
    ("pandas",           "pandas"),
    ("numpy",            "numpy"),
    ("openpyxl",         "openpyxl"),
    ("matplotlib",       "matplotlib"),
    ("pygame",           "pygame"),
]

print("\n  Checking packages:")
for module, pip_name in packages:
    try:
        __import__(module)
        print(f"  {PASS} {pip_name}")
    except ImportError:
        print(f"  {FAIL} {pip_name}  →  run: pip install {pip_name}")
        all_ok = False

# ── Project files ─────────────────────────────────────────────
print("\n  Checking project files:")
required_files = [
    "main.py",
    "config.py",
    "requirements.txt",
    "database/db_manager.py",
    "face_recognition_engine/recognizer.py",
    "utils/helpers.py",
    "gui/splash_screen.py",
    "gui/sidebar.py",
    "gui/notification.py",
    "gui/admin_login.py",
    "gui/pages/dashboard.py",
    "gui/pages/attendance.py",
    "gui/pages/register.py",
    "gui/pages/records.py",
    "gui/pages/analytics.py",
    "gui/pages/settings.py",
]

for f in required_files:
    path = os.path.join(ROOT, f)
    if os.path.exists(path):
        print(f"  {PASS} {f}")
    else:
        print(f"  {FAIL} {f}  — FILE MISSING")
        all_ok = False

# ── Directories ───────────────────────────────────────────────
print("\n  Checking directories:")
required_dirs = ["data", "data/face_data", "data/backups", "exports", "logs"]
for d in required_dirs:
    path = os.path.join(ROOT, d)
    os.makedirs(path, exist_ok=True)
    print(f"  {PASS} {d}/")

# ── Camera ────────────────────────────────────────────────────
print("\n  Checking camera:")
try:
    import cv2
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        print(f"  {PASS} Camera at index 0 is accessible")
        cap.release()
    else:
        print(f"  {WARN} Camera at index 0 could not be opened")
        print(f"       (The app will still launch; check camera permissions)")
except Exception as e:
    print(f"  {WARN} Camera check failed: {e}")

# ── Database ──────────────────────────────────────────────────
print("\n  Checking database:")
try:
    from database.db_manager import DatabaseManager
    db = DatabaseManager()
    users = db.get_total_users()
    print(f"  {PASS} Database connected. Registered users: {users}")
except Exception as e:
    print(f"  {FAIL} Database error: {e}")
    all_ok = False

# ── Result ────────────────────────────────────────────────────
print("\n" + "=" * 55)
if all_ok:
    print(f"  {PASS} All checks passed! Run: python main.py")
else:
    print(f"  {FAIL} Some checks failed. Fix issues above, then retry.")
print("=" * 55 + "\n")
