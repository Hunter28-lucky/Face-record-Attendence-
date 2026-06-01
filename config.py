# Made by Harsh Bardhan Kumar and Team
"""
╔══════════════════════════════════════════════════════════════╗
║            CONFIG — Face Attendance System                  ║
║  Central place for all tunable constants and app settings   ║
╚══════════════════════════════════════════════════════════════╝

Beginners: edit values in this file to customise the app
without hunting through the codebase.
"""

import os

# ── Paths ─────────────────────────────────────────────────────
BASE_DIR        = os.path.dirname(os.path.abspath(__file__))
DB_PATH         = os.path.join(BASE_DIR, "data", "attendance.db")
FACE_DATA_DIR   = os.path.join(BASE_DIR, "data", "face_data")
ENCODINGS_FILE  = os.path.join(BASE_DIR, "data", "face_encodings.pkl")
BACKUP_DIR      = os.path.join(BASE_DIR, "data", "backups")
EXPORT_DIR      = os.path.join(BASE_DIR, "exports")
LOG_DIR         = os.path.join(BASE_DIR, "logs")
ASSETS_DIR      = os.path.join(BASE_DIR, "assets")

# ── Face Recognition ─────────────────────────────────────────
# Number of sample images captured per new user
CAPTURE_SAMPLE_COUNT    = 30

# Face matching tolerance: 0.4 = very strict, 0.6 = lenient
RECOGNITION_TOLERANCE   = 0.50

# HOG is faster on CPU; CNN is more accurate but requires GPU / is slower
DETECTION_MODEL         = "hog"   # "hog" | "cnn"

# Frames-per-second target for live scanner
CAMERA_FPS_TARGET       = 30

# ── GUI ──────────────────────────────────────────────────────
APP_TITLE               = "FaceTrack Pro — Attendance System"
DEFAULT_WINDOW_SIZE     = "1200x720"
MIN_WINDOW_SIZE         = (960, 620)
DEFAULT_THEME           = "dark"   # "dark" | "light"

# ── Security ─────────────────────────────────────────────────
DEFAULT_ADMIN_PASSWORD  = "admin123"   # Change this before deployment!
MAX_LOGIN_ATTEMPTS      = 3

# ── Backup ───────────────────────────────────────────────────
AUTO_BACKUP_ENABLED     = True
AUTO_BACKUP_DELAY_SEC   = 30    # Seconds after app launch to trigger first backup

# ── Notifications ────────────────────────────────────────────
TOAST_DURATION_SEC      = 3.0   # How long toast notifications stay visible

# ── Sound ────────────────────────────────────────────────────
SOUND_ENABLED_DEFAULT   = True

# ── Version ──────────────────────────────────────────────────
APP_VERSION             = "2.0.0"
APP_BUILD               = "Professional Edition"
