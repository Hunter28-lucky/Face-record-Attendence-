

# ============================================================
# File: ./config.py
# ============================================================

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
APP_TITLE               = "FaceTrack Pro — AI Attendance System"
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


# ============================================================
# File: ./test_cam.py
# ============================================================

import cv2
import sys

backends = [
    ("CAP_ANY", cv2.CAP_ANY),
    ("CAP_AVFOUNDATION", cv2.CAP_AVFOUNDATION),
    ("CAP_DSHOW", cv2.CAP_DSHOW) if hasattr(cv2, 'CAP_DSHOW') else ("CAP_DSHOW", -1)
]

for name, backend in backends:
    if backend == -1: continue
    print(f"Testing {name}...")
    cap = cv2.VideoCapture(0, backend)
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            print(f"  SUCCESS! Read frame {frame.shape}")
        else:
            print("  FAILED to read frame.")
        cap.release()
    else:
        print("  FAILED to open.")


# ============================================================
# File: ./requirements.txt
# ============================================================

# ============================================================
# Face Recognition Attendance System - Requirements
# ============================================================
# Install with: pip install -r requirements.txt

# Core computer vision
opencv-python>=4.8.0
opencv-contrib-python>=4.8.0

# Face recognition (requires cmake & dlib)
face-recognition>=1.3.0
dlib>=19.24.0

# Modern GUI
customtkinter>=5.2.0
Pillow>=10.0.0

# Data management
pandas>=2.0.0
numpy>=1.24.0
openpyxl>=3.1.0

# Database
# sqlite3 is built-in to Python

# Plotting / Analytics
matplotlib>=3.7.0

# Sound playback
pygame>=2.5.0

# Utilities
python-dateutil>=2.8.2
requests>=2.31.0

# QR code generation (bonus)
qrcode[pil]>=7.4.2

# Email support (bonus)
secure-smtplib

# Progress bar
tqdm>=4.65.0


# ============================================================
# File: ./debug_ui_cam.py
# ============================================================

import customtkinter as ctk
import cv2
import PIL.Image, PIL.ImageTk
import sys

app = ctk.CTk()
app.geometry("800x600")

lbl = ctk.CTkLabel(app, text="Waiting...")
lbl.pack(fill="both", expand=True)

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
#cap = cv2.VideoCapture(0)

def update():
    ret, frame = cap.read()
    if ret:
        print(f"Read frame! {frame.shape}")
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = PIL.Image.fromarray(rgb).resize((400, 300))
        imgtk = PIL.ImageTk.PhotoImage(image=img)
        lbl.imgtk = imgtk
        lbl.configure(image=imgtk, text="")
    else:
        print("Failed to read frame")
    app.after(50, update)

update()
app.after(3000, app.destroy)
app.mainloop()


# ============================================================
# File: ./README.md
# ============================================================

# 👁 FaceTrack Pro — AI-Powered Attendance System

> **Production-grade** face recognition attendance system built with Python, OpenCV, and CustomTkinter.  
> Beautiful dark/light UI · SQLite database · CSV/Excel export · One-command launch

---

## 📸 Features at a Glance

| Feature | Details |
|---|---|
| **Live Face Recognition** | Real-time webcam scanning with HOG model |
| **Auto Attendance** | Marks once per day, prevents duplicates |
| **User Registration** | Captures 30 face samples, trains instantly |
| **Dashboard** | Today's count, registered users, recent scans |
| **Analytics** | 7-day trend chart + department pie chart |
| **Records** | Filter by date range, export CSV / Excel |
| **Settings** | Camera selector, tolerance slider, backup |
| **Notifications** | Animated toast popups with sound effects |
| **Admin Login** | Password-protected admin gate |
| **Dark / Light Mode** | Toggle from Settings page |

---

## 🚀 Quick Start (macOS / Linux)

### Step 1 — Prerequisites

**Install CMake** (required for the `face_recognition` library):

```bash
# macOS
brew install cmake

# Ubuntu / Debian
sudo apt install cmake build-essential
```

### Step 2 — Install Dependencies

```bash
cd "face detection"
pip install -r requirements.txt
```

> 💡 Using a virtual environment is recommended:
> ```bash
> python3 -m venv venv && source venv/bin/activate
> pip install -r requirements.txt
> ```

### Step 3 — Verify Installation

```bash
python3 verify_install.py
```

All items should show ✅. Fix any ❌ before proceeding.

### Step 4 — (Optional) Load Demo Data

```bash
python3 seed_demo_data.py
```

Seeds 10 users and 14 days of sample attendance so the Dashboard looks populated immediately.

### Step 5 — Launch

```bash
python3 main.py
```

Or use the one-click script:

```bash
chmod +x run.sh && ./run.sh
```

---

## 🪟 Quick Start (Windows)

```bat
REM Install dependencies
install.bat

REM Verify
python verify_install.py

REM Seed demo data (optional)
python seed_demo_data.py

REM Launch
run.bat
```

---

## 📁 Project Structure

```
face detection/
│
├── main.py                      ← Entry point
├── config.py                    ← All tunable constants
├── requirements.txt
├── verify_install.py            ← Pre-launch checker
├── seed_demo_data.py            ← Demo data loader
├── install.sh / install.bat     ← Auto-installers
├── run.sh / run.bat             ← One-click launchers
│
├── database/
│   └── db_manager.py            ← SQLite: schema, CRUD, export
│
├── face_recognition_engine/
│   └── recognizer.py            ← Capture, train, recognize
│
├── gui/
│   ├── splash_screen.py         ← Animated startup screen
│   ├── sidebar.py               ← Left navigation panel
│   ├── notification.py          ← Toast popup notifications
│   ├── admin_login.py           ← Password dialog
│   └── pages/
│       ├── dashboard.py         ← Home stats & recent logs
│       ├── attendance.py        ← Live webcam scanner
│       ├── register.py          ← New user + face capture
│       ├── records.py           ← Attendance table + export
│       ├── analytics.py         ← Charts (trend + dept)
│       └── settings.py          ← Config & backup
│
├── utils/
│   └── helpers.py               ← Sound, theme, validation
│
├── data/
│   ├── attendance.db            ← SQLite database (auto-created)
│   ├── face_encodings.pkl       ← Trained face model (auto-created)
│   ├── face_data/               ← Raw captured images per user
│   └── backups/                 ← Auto timestamped DB backups
│
├── exports/                     ← CSV / Excel exports saved here
└── logs/                        ← app.log written here
```

---

## 🗃️ Database Schema

### `users` table
| Column | Type | Description |
|---|---|---|
| id | INTEGER PK | Auto-increment |
| name | TEXT | Full name |
| roll_number | TEXT UNIQUE | Employee / student ID |
| department | TEXT | Department or class |
| email | TEXT | Optional contact |
| phone | TEXT | Optional contact |
| photo_path | TEXT | Path to profile image |
| registered_at | TEXT | ISO timestamp |
| is_active | INTEGER | 1 = active, 0 = deleted |

### `attendance` table
| Column | Type | Description |
|---|---|---|
| id | INTEGER PK | Auto-increment |
| user_id | INTEGER FK | References `users.id` |
| date | TEXT | YYYY-MM-DD |
| time | TEXT | HH:MM:SS |
| status | TEXT | Present / Absent |
| marked_by | TEXT | "Face Recognition" |

> **Unique constraint on `(user_id, date)`** prevents duplicate entries per day.

### `settings` table
Key-value store for all app preferences (theme, camera, tolerance, etc.)

### `audit_log` table
Every important action (user added, attendance marked, backup created) is logged here for traceability.

---

## ⚙️ Configuration

Edit `config.py` to tune the system without touching core code:

```python
RECOGNITION_TOLERANCE = 0.50   # Lower = stricter (0.4–0.6)
CAPTURE_SAMPLE_COUNT  = 30     # Images captured per user
DETECTION_MODEL       = "hog"  # "hog" (CPU) or "cnn" (GPU)
DEFAULT_ADMIN_PASSWORD = "admin123"  # Change before deployment!
```

---

## 🎯 How Face Recognition Works

1. **Registration** — The system captures 30 images of a user's face from the webcam.
2. **Training** — Each image is encoded into a 128-dimension vector using `face_recognition`. All vectors for a user are averaged into a single representative encoding.
3. **Recognition** — During live scanning, each detected face is encoded and its distance to all known encodings is computed. If the closest distance is ≤ `RECOGNITION_TOLERANCE`, the user is identified.
4. **Attendance** — On a successful match, the system checks the `attendance` table. If no entry exists for today, it inserts one and plays a success sound.

---

## 🔧 Troubleshooting

| Problem | Fix |
|---|---|
| `dlib` fails to install | Install CMake first, then retry |
| Camera not opening | Check OS camera permissions; try index 1 or 2 in Settings |
| Slow recognition | Reduce frame size in `recognizer.py` (line `fx=0.25`) |
| Unknown faces | Lower `RECOGNITION_TOLERANCE` in `config.py` |
| App crashes on start | Run `python verify_install.py` and fix all ❌ items |
| No sound | Run `pip install pygame`; toggle sound in Settings |

---

## 📜 License

MIT License — Free for educational and commercial use.

---

*Built with ❤️ using Python · OpenCV · face_recognition · CustomTkinter*


# ============================================================
# File: ./full.py
# ============================================================

# -*- coding: utf-8 -*-
"""
Self-Extracting Single-File Distribution for:
AI-Powered Face Detection Attendance Management System

This file contains the complete source code, directory structures, configurations, 
and readmes for the entire project. 

When you run this script:
1. It will recreate the full directory structure and extract all files locally.
2. It will then automatically execute the main entry point (main.py).
"""

import os
import base64
import sys

# Files dictionary: relative_path -> base64_encoded_content
FILES = {'config.py': 'IiIiCuKVlOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVlwrilZEgICAgICAgICAgICBDT05GSUcg4oCUIEZhY2UgQXR0ZW5kYW5jZSBTeXN0ZW0gICAgICAgICAgICAgICAgICDilZEK4pWRICBDZW50cmFsIHBsYWNlIGZvciBhbGwgdHVuYWJsZSBjb25zdGFudHMgYW5kIGFwcCBzZXR0aW5ncyAgIOKVkQrilZrilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZ0KCkJlZ2lubmVyczogZWRpdCB2YWx1ZXMgaW4gdGhpcyBmaWxlIHRvIGN1c3RvbWlzZSB0aGUgYXBwCndpdGhvdXQgaHVudGluZyB0aHJvdWdoIHRoZSBjb2RlYmFzZS4KIiIiCgppbXBvcnQgb3MKCiMg4pSA4pSAIFBhdGhzIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgApCQVNFX0RJUiAgICAgICAgPSBvcy5wYXRoLmRpcm5hbWUob3MucGF0aC5hYnNwYXRoKF9fZmlsZV9fKSkKREJfUEFUSCAgICAgICAgID0gb3MucGF0aC5qb2luKEJBU0VfRElSLCAiZGF0YSIsICJhdHRlbmRhbmNlLmRiIikKRkFDRV9EQVRBX0RJUiAgID0gb3MucGF0aC5qb2luKEJBU0VfRElSLCAiZGF0YSIsICJmYWNlX2RhdGEiKQpFTkNPRElOR1NfRklMRSAgPSBvcy5wYXRoLmpvaW4oQkFTRV9ESVIsICJkYXRhIiwgImZhY2VfZW5jb2RpbmdzLnBrbCIpCkJBQ0tVUF9ESVIgICAgICA9IG9zLnBhdGguam9pbihCQVNFX0RJUiwgImRhdGEiLCAiYmFja3VwcyIpCkVYUE9SVF9ESVIgICAgICA9IG9zLnBhdGguam9pbihCQVNFX0RJUiwgImV4cG9ydHMiKQpMT0dfRElSICAgICAgICAgPSBvcy5wYXRoLmpvaW4oQkFTRV9ESVIsICJsb2dzIikKQVNTRVRTX0RJUiAgICAgID0gb3MucGF0aC5qb2luKEJBU0VfRElSLCAiYXNzZXRzIikKCiMg4pSA4pSAIEZhY2UgUmVjb2duaXRpb24g4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACiMgTnVtYmVyIG9mIHNhbXBsZSBpbWFnZXMgY2FwdHVyZWQgcGVyIG5ldyB1c2VyCkNBUFRVUkVfU0FNUExFX0NPVU5UICAgID0gMzAKCiMgRmFjZSBtYXRjaGluZyB0b2xlcmFuY2U6IDAuNCA9IHZlcnkgc3RyaWN0LCAwLjYgPSBsZW5pZW50ClJFQ09HTklUSU9OX1RPTEVSQU5DRSAgID0gMC41MAoKIyBIT0cgaXMgZmFzdGVyIG9uIENQVTsgQ05OIGlzIG1vcmUgYWNjdXJhdGUgYnV0IHJlcXVpcmVzIEdQVSAvIGlzIHNsb3dlcgpERVRFQ1RJT05fTU9ERUwgICAgICAgICA9ICJob2ciICAgIyAiaG9nIiB8ICJjbm4iCgojIEZyYW1lcy1wZXItc2Vjb25kIHRhcmdldCBmb3IgbGl2ZSBzY2FubmVyCkNBTUVSQV9GUFNfVEFSR0VUICAgICAgID0gMzAKCiMg4pSA4pSAIEdVSSDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIAKQVBQX1RJVExFICAgICAgICAgICAgICAgPSAiRmFjZVRyYWNrIFBybyDigJQgQUkgQXR0ZW5kYW5jZSBTeXN0ZW0iCkRFRkFVTFRfV0lORE9XX1NJWkUgICAgID0gIjEyMDB4NzIwIgpNSU5fV0lORE9XX1NJWkUgICAgICAgICA9ICg5NjAsIDYyMCkKREVGQVVMVF9USEVNRSAgICAgICAgICAgPSAiZGFyayIgICAjICJkYXJrIiB8ICJsaWdodCIKCiMg4pSA4pSAIFNlY3VyaXR5IOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgApERUZBVUxUX0FETUlOX1BBU1NXT1JEICA9ICJhZG1pbjEyMyIgICAjIENoYW5nZSB0aGlzIGJlZm9yZSBkZXBsb3ltZW50IQpNQVhfTE9HSU5fQVRURU1QVFMgICAgICA9IDMKCiMg4pSA4pSAIEJhY2t1cCDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIAKQVVUT19CQUNLVVBfRU5BQkxFRCAgICAgPSBUcnVlCkFVVE9fQkFDS1VQX0RFTEFZX1NFQyAgID0gMzAgICAgIyBTZWNvbmRzIGFmdGVyIGFwcCBsYXVuY2ggdG8gdHJpZ2dlciBmaXJzdCBiYWNrdXAKCiMg4pSA4pSAIE5vdGlmaWNhdGlvbnMg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSAClRPQVNUX0RVUkFUSU9OX1NFQyAgICAgID0gMy4wICAgIyBIb3cgbG9uZyB0b2FzdCBub3RpZmljYXRpb25zIHN0YXkgdmlzaWJsZQoKIyDilIDilIAgU291bmQg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSAClNPVU5EX0VOQUJMRURfREVGQVVMVCAgID0gVHJ1ZQoKIyDilIDilIAgVmVyc2lvbiDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIAKQVBQX1ZFUlNJT04gICAgICAgICAgICAgPSAiMi4wLjAiCkFQUF9CVUlMRCAgICAgICAgICAgICAgID0gIlByb2Zlc3Npb25hbCBFZGl0aW9uIgo=', 'test_cam.py': 'aW1wb3J0IGN2MgppbXBvcnQgc3lzCgpiYWNrZW5kcyA9IFsKICAgICgiQ0FQX0FOWSIsIGN2Mi5DQVBfQU5ZKSwKICAgICgiQ0FQX0FWRk9VTkRBVElPTiIsIGN2Mi5DQVBfQVZGT1VOREFUSU9OKSwKICAgICgiQ0FQX0RTSE9XIiwgY3YyLkNBUF9EU0hPVykgaWYgaGFzYXR0cihjdjIsICdDQVBfRFNIT1cnKSBlbHNlICgiQ0FQX0RTSE9XIiwgLTEpCl0KCmZvciBuYW1lLCBiYWNrZW5kIGluIGJhY2tlbmRzOgogICAgaWYgYmFja2VuZCA9PSAtMTogY29udGludWUKICAgIHByaW50KGYiVGVzdGluZyB7bmFtZX0uLi4iKQogICAgY2FwID0gY3YyLlZpZGVvQ2FwdHVyZSgwLCBiYWNrZW5kKQogICAgaWYgY2FwLmlzT3BlbmVkKCk6CiAgICAgICAgcmV0LCBmcmFtZSA9IGNhcC5yZWFkKCkKICAgICAgICBpZiByZXQ6CiAgICAgICAgICAgIHByaW50KGYiICBTVUNDRVNTISBSZWFkIGZyYW1lIHtmcmFtZS5zaGFwZX0iKQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIHByaW50KCIgIEZBSUxFRCB0byByZWFkIGZyYW1lLiIpCiAgICAgICAgY2FwLnJlbGVhc2UoKQogICAgZWxzZToKICAgICAgICBwcmludCgiICBGQUlMRUQgdG8gb3Blbi4iKQo=', 'requirements.txt': 'IyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0KIyBGYWNlIFJlY29nbml0aW9uIEF0dGVuZGFuY2UgU3lzdGVtIC0gUmVxdWlyZW1lbnRzCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09CiMgSW5zdGFsbCB3aXRoOiBwaXAgaW5zdGFsbCAtciByZXF1aXJlbWVudHMudHh0CgojIENvcmUgY29tcHV0ZXIgdmlzaW9uCm9wZW5jdi1weXRob24+PTQuOC4wCm9wZW5jdi1jb250cmliLXB5dGhvbj49NC44LjAKCiMgRmFjZSByZWNvZ25pdGlvbiAocmVxdWlyZXMgY21ha2UgJiBkbGliKQpmYWNlLXJlY29nbml0aW9uPj0xLjMuMApkbGliPj0xOS4yNC4wCgojIE1vZGVybiBHVUkKY3VzdG9tdGtpbnRlcj49NS4yLjAKUGlsbG93Pj0xMC4wLjAKCiMgRGF0YSBtYW5hZ2VtZW50CnBhbmRhcz49Mi4wLjAKbnVtcHk+PTEuMjQuMApvcGVucHl4bD49My4xLjAKCiMgRGF0YWJhc2UKIyBzcWxpdGUzIGlzIGJ1aWx0LWluIHRvIFB5dGhvbgoKIyBQbG90dGluZyAvIEFuYWx5dGljcwptYXRwbG90bGliPj0zLjcuMAoKIyBTb3VuZCBwbGF5YmFjawpweWdhbWU+PTIuNS4wCgojIFV0aWxpdGllcwpweXRob24tZGF0ZXV0aWw+PTIuOC4yCnJlcXVlc3RzPj0yLjMxLjAKCiMgUVIgY29kZSBnZW5lcmF0aW9uIChib251cykKcXJjb2RlW3BpbF0+PTcuNC4yCgojIEVtYWlsIHN1cHBvcnQgKGJvbnVzKQpzZWN1cmUtc210cGxpYgoKIyBQcm9ncmVzcyBiYXIKdHFkbT49NC42NS4wCg==', 'run.bat': 'QGVjaG8gb2ZmClRJVExFIEZhY2VUcmFjayBQcm8KcHl0aG9uIG1haW4ucHkKcGF1c2UK', 'install.sh': 'IyEvYmluL2Jhc2gKZWNobyAiPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PSIKZWNobyAiIEZhY2VUcmFjayBQcm8gLSBtYWNPUy9MaW51eCBBdXRvIEluc3RhbGxlciIKZWNobyAiPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PSIKCmVjaG8gIlsxLzRdIENoZWNraW5nIFB5dGhvbiAzLi4uIgppZiAhIGNvbW1hbmQgLXYgcHl0aG9uMyAmPiAvZGV2L251bGw7IHRoZW4KICAgIGVjaG8gIuKdjCBQeXRob24gMyBpcyBub3QgaW5zdGFsbGVkLiBQbGVhc2UgaW5zdGFsbCBQeXRob24gMy45KyBmaXJzdC4iCiAgICBleGl0IDEKZmkKCmVjaG8gIlsyLzRdIENoZWNraW5nIGZvciBDTWFrZSAocmVxdWlyZWQgZm9yIGZhY2VfcmVjb2duaXRpb24pLi4uIgppZiAhIGNvbW1hbmQgLXYgY21ha2UgJj4gL2Rldi9udWxsOyB0aGVuCiAgICBlY2hvICLimqDvuI8gQ01ha2UgaXMgbm90IGluc3RhbGxlZC4iCiAgICBpZiBbWyAiJE9TVFlQRSIgPT0gImRhcndpbiIqIF1dOyB0aGVuCiAgICAgICAgZWNobyAiSW5zdGFsbGluZyBjbWFrZSB2aWEgYnJldy4uLiIKICAgICAgICBicmV3IGluc3RhbGwgY21ha2UKICAgIGVsc2UKICAgICAgICBlY2hvICJQbGVhc2UgcnVuOiBzdWRvIGFwdCBpbnN0YWxsIGNtYWtlIgogICAgICAgIGV4aXQgMQogICAgZmkKZmkKCmVjaG8gIlszLzRdIENyZWF0aW5nIHZpcnR1YWwgZW52aXJvbm1lbnQgKG9wdGlvbmFsIGJ1dCByZWNvbW1lbmRlZCkuLi4iCnB5dGhvbjMgLW0gdmVudiB2ZW52CnNvdXJjZSB2ZW52L2Jpbi9hY3RpdmF0ZQoKZWNobyAiWzQvNF0gSW5zdGFsbGluZyBkZXBlbmRlbmNpZXMgZnJvbSByZXF1aXJlbWVudHMudHh0Li4uIgpwaXAgaW5zdGFsbCAtLXVwZ3JhZGUgcGlwCnBpcCBpbnN0YWxsIC1yIHJlcXVpcmVtZW50cy50eHQKCmVjaG8gIj09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0iCmVjaG8gIuKchSBJbnN0YWxsYXRpb24gQ29tcGxldGUhIgplY2hvICJSdW4gdGhlIGFwcGxpY2F0aW9uIGJ5IGV4ZWN1dGluZzogLi9ydW4uc2giCmVjaG8gIj09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0iCg==', 'error.log': 'SU5GTzpkYXRhYmFzZS5kYl9tYW5hZ2VyOkRhdGFiYXNlIGNvbm5lY3RlZDogL1VzZXJzL2tyaXNoeW9naS9EZXNrdG9wL2ZhY2UgZGV0ZWN0aW9uL2RhdGEvYXR0ZW5kYW5jZS5kYgpvYmpjWzk2MzQ0XTogQ2xhc3MgU0RMQXBwbGljYXRpb24gaXMgaW1wbGVtZW50ZWQgaW4gYm90aCAvVXNlcnMva3Jpc2h5b2dpLy5weWVudi92ZXJzaW9ucy8zLjEwLjEzL2xpYi9weXRob24zLjEwL3NpdGUtcGFja2FnZXMvcHlnYW1lLy5keWxpYnMvbGliU0RMMi0yLjAuMC5keWxpYiAoMHgxMGM1YTUyYzgpIGFuZCAvVXNlcnMva3Jpc2h5b2dpLy5weWVudi92ZXJzaW9ucy8zLjEwLjEzL2xpYi9weXRob24zLjEwL3NpdGUtcGFja2FnZXMvY3YyLy5keWxpYnMvbGliU0RMMi0yLjAuMC5keWxpYiAoMHgxMjY4MmM4OTApLiBUaGlzIG1heSBjYXVzZSBzcHVyaW91cyBjYXN0aW5nIGZhaWx1cmVzIGFuZCBteXN0ZXJpb3VzIGNyYXNoZXMuIE9uZSBvZiB0aGUgZHVwbGljYXRlcyBtdXN0IGJlIHJlbW92ZWQgb3IgcmVuYW1lZC4Kb2JqY1s5NjM0NF06IENsYXNzIFNETEFwcERlbGVnYXRlIGlzIGltcGxlbWVudGVkIGluIGJvdGggL1VzZXJzL2tyaXNoeW9naS8ucHllbnYvdmVyc2lvbnMvMy4xMC4xMy9saWIvcHl0aG9uMy4xMC9zaXRlLXBhY2thZ2VzL3B5Z2FtZS8uZHlsaWJzL2xpYlNETDItMi4wLjAuZHlsaWIgKDB4MTBjNWE1MzE4KSBhbmQgL1VzZXJzL2tyaXNoeW9naS8ucHllbnYvdmVyc2lvbnMvMy4xMC4xMy9saWIvcHl0aG9uMy4xMC9zaXRlLXBhY2thZ2VzL2N2Mi8uZHlsaWJzL2xpYlNETDItMi4wLjAuZHlsaWIgKDB4MTI2ODJjOGUwKS4gVGhpcyBtYXkgY2F1c2Ugc3B1cmlvdXMgY2FzdGluZyBmYWlsdXJlcyBhbmQgbXlzdGVyaW91cyBjcmFzaGVzLiBPbmUgb2YgdGhlIGR1cGxpY2F0ZXMgbXVzdCBiZSByZW1vdmVkIG9yIHJlbmFtZWQuCm9iamNbOTYzNDRdOiBDbGFzcyBTRExUcmFuc2xhdG9yUmVzcG9uZGVyIGlzIGltcGxlbWVudGVkIGluIGJvdGggL1VzZXJzL2tyaXNoeW9naS8ucHllbnYvdmVyc2lvbnMvMy4xMC4xMy9saWIvcHl0aG9uMy4xMC9zaXRlLXBhY2thZ2VzL3B5Z2FtZS8uZHlsaWJzL2xpYlNETDItMi4wLjAuZHlsaWIgKDB4MTBjNWE1MzkwKSBhbmQgL1VzZXJzL2tyaXNoeW9naS8ucHllbnYvdmVyc2lvbnMvMy4xMC4xMy9saWIvcHl0aG9uMy4xMC9zaXRlLXBhY2thZ2VzL2N2Mi8uZHlsaWJzL2xpYlNETDItMi4wLjAuZHlsaWIgKDB4MTI2ODJjOTU4KS4gVGhpcyBtYXkgY2F1c2Ugc3B1cmlvdXMgY2FzdGluZyBmYWlsdXJlcyBhbmQgbXlzdGVyaW91cyBjcmFzaGVzLiBPbmUgb2YgdGhlIGR1cGxpY2F0ZXMgbXVzdCBiZSByZW1vdmVkIG9yIHJlbmFtZWQuCm9iamNbOTYzNDRdOiBDbGFzcyBTRExNZXNzYWdlQm94UHJlc2VudGVyIGlzIGltcGxlbWVudGVkIGluIGJvdGggL1VzZXJzL2tyaXNoeW9naS8ucHllbnYvdmVyc2lvbnMvMy4xMC4xMy9saWIvcHl0aG9uMy4xMC9zaXRlLXBhY2thZ2VzL3B5Z2FtZS8uZHlsaWJzL2xpYlNETDItMi4wLjAuZHlsaWIgKDB4MTBjNWE1M2I4KSBhbmQgL1VzZXJzL2tyaXNoeW9naS8ucHllbnYvdmVyc2lvbnMvMy4xMC4xMy9saWIvcHl0aG9uMy4xMC9zaXRlLXBhY2thZ2VzL2N2Mi8uZHlsaWJzL2xpYlNETDItMi4wLjAuZHlsaWIgKDB4MTI2ODJjOTgwKS4gVGhpcyBtYXkgY2F1c2Ugc3B1cmlvdXMgY2FzdGluZyBmYWlsdXJlcyBhbmQgbXlzdGVyaW91cyBjcmFzaGVzLiBPbmUgb2YgdGhlIGR1cGxpY2F0ZXMgbXVzdCBiZSByZW1vdmVkIG9yIHJlbmFtZWQuCm9iamNbOTYzNDRdOiBDbGFzcyBTRExfY29jb2FtZXRhbHZpZXcgaXMgaW1wbGVtZW50ZWQgaW4gYm90aCAvVXNlcnMva3Jpc2h5b2dpLy5weWVudi92ZXJzaW9ucy8zLjEwLjEzL2xpYi9weXRob24zLjEwL3NpdGUtcGFja2FnZXMvcHlnYW1lLy5keWxpYnMvbGliU0RMMi0yLjAuMC5keWxpYiAoMHgxMGM1YTU0MDgpIGFuZCAvVXNlcnMva3Jpc2h5b2dpLy5weWVudi92ZXJzaW9ucy8zLjEwLjEzL2xpYi9weXRob24zLjEwL3NpdGUtcGFja2FnZXMvY3YyLy5keWxpYnMvbGliU0RMMi0yLjAuMC5keWxpYiAoMHgxMjY4MmM5ZDApLiBUaGlzIG1heSBjYXVzZSBzcHVyaW91cyBjYXN0aW5nIGZhaWx1cmVzIGFuZCBteXN0ZXJpb3VzIGNyYXNoZXMuIE9uZSBvZiB0aGUgZHVwbGljYXRlcyBtdXN0IGJlIHJlbW92ZWQgb3IgcmVuYW1lZC4Kb2JqY1s5NjM0NF06IENsYXNzIFNETE9wZW5HTENvbnRleHQgaXMgaW1wbGVtZW50ZWQgaW4gYm90aCAvVXNlcnMva3Jpc2h5b2dpLy5weWVudi92ZXJzaW9ucy8zLjEwLjEzL2xpYi9weXRob24zLjEwL3NpdGUtcGFja2FnZXMvcHlnYW1lLy5keWxpYnMvbGliU0RMMi0yLjAuMC5keWxpYiAoMHgxMGM1YTU0NTgpIGFuZCAvVXNlcnMva3Jpc2h5b2dpLy5weWVudi92ZXJzaW9ucy8zLjEwLjEzL2xpYi9weXRob24zLjEwL3NpdGUtcGFja2FnZXMvY3YyLy5keWxpYnMvbGliU0RMMi0yLjAuMC5keWxpYiAoMHgxMjY4MmNhMjApLiBUaGlzIG1heSBjYXVzZSBzcHVyaW91cyBjYXN0aW5nIGZhaWx1cmVzIGFuZCBteXN0ZXJpb3VzIGNyYXNoZXMuIE9uZSBvZiB0aGUgZHVwbGljYXRlcyBtdXN0IGJlIHJlbW92ZWQgb3IgcmVuYW1lZC4Kb2JqY1s5NjM0NF06IENsYXNzIFNETF9TaGFwZURhdGEgaXMgaW1wbGVtZW50ZWQgaW4gYm90aCAvVXNlcnMva3Jpc2h5b2dpLy5weWVudi92ZXJzaW9ucy8zLjEwLjEzL2xpYi9weXRob24zLjEwL3NpdGUtcGFja2FnZXMvcHlnYW1lLy5keWxpYnMvbGliU0RMMi0yLjAuMC5keWxpYiAoMHgxMGM1YTU0ZDApIGFuZCAvVXNlcnMva3Jpc2h5b2dpLy5weWVudi92ZXJzaW9ucy8zLjEwLjEzL2xpYi9weXRob24zLjEwL3NpdGUtcGFja2FnZXMvY3YyLy5keWxpYnMvbGliU0RMMi0yLjAuMC5keWxpYiAoMHgxMjY4MmNhOTgpLiBUaGlzIG1heSBjYXVzZSBzcHVyaW91cyBjYXN0aW5nIGZhaWx1cmVzIGFuZCBteXN0ZXJpb3VzIGNyYXNoZXMuIE9uZSBvZiB0aGUgZHVwbGljYXRlcyBtdXN0IGJlIHJlbW92ZWQgb3IgcmVuYW1lZC4Kb2JqY1s5NjM0NF06IENsYXNzIFNETF9Db2NvYUNsb3N1cmUgaXMgaW1wbGVtZW50ZWQgaW4gYm90aCAvVXNlcnMva3Jpc2h5b2dpLy5weWVudi92ZXJzaW9ucy8zLjEwLjEzL2xpYi9weXRob24zLjEwL3NpdGUtcGFja2FnZXMvcHlnYW1lLy5keWxpYnMvbGliU0RMMi0yLjAuMC5keWxpYiAoMHgxMGM1YTU1MjApIGFuZCAvVXNlcnMva3Jpc2h5b2dpLy5weWVudi92ZXJzaW9ucy8zLjEwLjEzL2xpYi9weXRob24zLjEwL3NpdGUtcGFja2FnZXMvY3YyLy5keWxpYnMvbGliU0RMMi0yLjAuMC5keWxpYiAoMHgxMjY4MmNhZTgpLiBUaGlzIG1heSBjYXVzZSBzcHVyaW91cyBjYXN0aW5nIGZhaWx1cmVzIGFuZCBteXN0ZXJpb3VzIGNyYXNoZXMuIE9uZSBvZiB0aGUgZHVwbGljYXRlcyBtdXN0IGJlIHJlbW92ZWQgb3IgcmVuYW1lZC4Kb2JqY1s5NjM0NF06IENsYXNzIFNETF9WaWRlb0RhdGEgaXMgaW1wbGVtZW50ZWQgaW4gYm90aCAvVXNlcnMva3Jpc2h5b2dpLy5weWVudi92ZXJzaW9ucy8zLjEwLjEzL2xpYi9weXRob24zLjEwL3NpdGUtcGFja2FnZXMvcHlnYW1lLy5keWxpYnMvbGliU0RMMi0yLjAuMC5keWxpYiAoMHgxMGM1YTU1NzApIGFuZCAvVXNlcnMva3Jpc2h5b2dpLy5weWVudi92ZXJzaW9ucy8zLjEwLjEzL2xpYi9weXRob24zLjEwL3NpdGUtcGFja2FnZXMvY3YyLy5keWxpYnMvbGliU0RMMi0yLjAuMC5keWxpYiAoMHgxMjY4MmNiMzgpLiBUaGlzIG1heSBjYXVzZSBzcHVyaW91cyBjYXN0aW5nIGZhaWx1cmVzIGFuZCBteXN0ZXJpb3VzIGNyYXNoZXMuIE9uZSBvZiB0aGUgZHVwbGljYXRlcyBtdXN0IGJlIHJlbW92ZWQgb3IgcmVuYW1lZC4Kb2JqY1s5NjM0NF06IENsYXNzIFNETF9XaW5kb3dEYXRhIGlzIGltcGxlbWVudGVkIGluIGJvdGggL1VzZXJzL2tyaXNoeW9naS8ucHllbnYvdmVyc2lvbnMvMy4xMC4xMy9saWIvcHl0aG9uMy4xMC9zaXRlLXBhY2thZ2VzL3B5Z2FtZS8uZHlsaWJzL2xpYlNETDItMi4wLjAuZHlsaWIgKDB4MTBjNWE1NWMwKSBhbmQgL1VzZXJzL2tyaXNoeW9naS8ucHllbnYvdmVyc2lvbnMvMy4xMC4xMy9saWIvcHl0aG9uMy4xMC9zaXRlLXBhY2thZ2VzL2N2Mi8uZHlsaWJzL2xpYlNETDItMi4wLjAuZHlsaWIgKDB4MTI2ODJjYjg4KS4gVGhpcyBtYXkgY2F1c2Ugc3B1cmlvdXMgY2FzdGluZyBmYWlsdXJlcyBhbmQgbXlzdGVyaW91cyBjcmFzaGVzLiBPbmUgb2YgdGhlIGR1cGxpY2F0ZXMgbXVzdCBiZSByZW1vdmVkIG9yIHJlbmFtZWQuCm9iamNbOTYzNDRdOiBDbGFzcyBTRExXaW5kb3cgaXMgaW1wbGVtZW50ZWQgaW4gYm90aCAvVXNlcnMva3Jpc2h5b2dpLy5weWVudi92ZXJzaW9ucy8zLjEwLjEzL2xpYi9weXRob24zLjEwL3NpdGUtcGFja2FnZXMvcHlnYW1lLy5keWxpYnMvbGliU0RMMi0yLjAuMC5keWxpYiAoMHgxMGM1YTU1ZTgpIGFuZCAvVXNlcnMva3Jpc2h5b2dpLy5weWVudi92ZXJzaW9ucy8zLjEwLjEzL2xpYi9weXRob24zLjEwL3NpdGUtcGFja2FnZXMvY3YyLy5keWxpYnMvbGliU0RMMi0yLjAuMC5keWxpYiAoMHgxMjY4MmNiYjApLiBUaGlzIG1heSBjYXVzZSBzcHVyaW91cyBjYXN0aW5nIGZhaWx1cmVzIGFuZCBteXN0ZXJpb3VzIGNyYXNoZXMuIE9uZSBvZiB0aGUgZHVwbGljYXRlcyBtdXN0IGJlIHJlbW92ZWQgb3IgcmVuYW1lZC4Kb2JqY1s5NjM0NF06IENsYXNzIENvY29hX1dpbmRvd0xpc3RlbmVyIGlzIGltcGxlbWVudGVkIGluIGJvdGggL1VzZXJzL2tyaXNoeW9naS8ucHllbnYvdmVyc2lvbnMvMy4xMC4xMy9saWIvcHl0aG9uMy4xMC9zaXRlLXBhY2thZ2VzL3B5Z2FtZS8uZHlsaWJzL2xpYlNETDItMi4wLjAuZHlsaWIgKDB4MTBjNWE1NjEwKSBhbmQgL1VzZXJzL2tyaXNoeW9naS8ucHllbnYvdmVyc2lvbnMvMy4xMC4xMy9saWIvcHl0aG9uMy4xMC9zaXRlLXBhY2thZ2VzL2N2Mi8uZHlsaWJzL2xpYlNETDItMi4wLjAuZHlsaWIgKDB4MTI2ODJjYmQ4KS4gVGhpcyBtYXkgY2F1c2Ugc3B1cmlvdXMgY2FzdGluZyBmYWlsdXJlcyBhbmQgbXlzdGVyaW91cyBjcmFzaGVzLiBPbmUgb2YgdGhlIGR1cGxpY2F0ZXMgbXVzdCBiZSByZW1vdmVkIG9yIHJlbmFtZWQuCm9iamNbOTYzNDRdOiBDbGFzcyBTRExWaWV3IGlzIGltcGxlbWVudGVkIGluIGJvdGggL1VzZXJzL2tyaXNoeW9naS8ucHllbnYvdmVyc2lvbnMvMy4xMC4xMy9saWIvcHl0aG9uMy4xMC9zaXRlLXBhY2thZ2VzL3B5Z2FtZS8uZHlsaWJzL2xpYlNETDItMi4wLjAuZHlsaWIgKDB4MTBjNWE1Njg4KSBhbmQgL1VzZXJzL2tyaXNoeW9naS8ucHllbnYvdmVyc2lvbnMvMy4xMC4xMy9saWIvcHl0aG9uMy4xMC9zaXRlLXBhY2thZ2VzL2N2Mi8uZHlsaWJzL2xpYlNETDItMi4wLjAuZHlsaWIgKDB4MTI2ODJjYzUwKS4gVGhpcyBtYXkgY2F1c2Ugc3B1cmlvdXMgY2FzdGluZyBmYWlsdXJlcyBhbmQgbXlzdGVyaW91cyBjcmFzaGVzLiBPbmUgb2YgdGhlIGR1cGxpY2F0ZXMgbXVzdCBiZSByZW1vdmVkIG9yIHJlbmFtZWQuCm9iamNbOTYzNDRdOiBDbGFzcyBNRVRBTF9SZW5kZXJEYXRhIGlzIGltcGxlbWVudGVkIGluIGJvdGggL1VzZXJzL2tyaXNoeW9naS8ucHllbnYvdmVyc2lvbnMvMy4xMC4xMy9saWIvcHl0aG9uMy4xMC9zaXRlLXBhY2thZ2VzL3B5Z2FtZS8uZHlsaWJzL2xpYlNETDItMi4wLjAuZHlsaWIgKDB4MTBjNWE1NzAwKSBhbmQgL1VzZXJzL2tyaXNoeW9naS8ucHllbnYvdmVyc2lvbnMvMy4xMC4xMy9saWIvcHl0aG9uMy4xMC9zaXRlLXBhY2thZ2VzL2N2Mi8uZHlsaWJzL2xpYlNETDItMi4wLjAuZHlsaWIgKDB4MTI2ODJjY2M4KS4gVGhpcyBtYXkgY2F1c2Ugc3B1cmlvdXMgY2FzdGluZyBmYWlsdXJlcyBhbmQgbXlzdGVyaW91cyBjcmFzaGVzLiBPbmUgb2YgdGhlIGR1cGxpY2F0ZXMgbXVzdCBiZSByZW1vdmVkIG9yIHJlbmFtZWQuCm9iamNbOTYzNDRdOiBDbGFzcyBNRVRBTF9UZXh0dXJlRGF0YSBpcyBpbXBsZW1lbnRlZCBpbiBib3RoIC9Vc2Vycy9rcmlzaHlvZ2kvLnB5ZW52L3ZlcnNpb25zLzMuMTAuMTMvbGliL3B5dGhvbjMuMTAvc2l0ZS1wYWNrYWdlcy9weWdhbWUvLmR5bGlicy9saWJTREwyLTIuMC4wLmR5bGliICgweDEwYzVhNTc1MCkgYW5kIC9Vc2Vycy9rcmlzaHlvZ2kvLnB5ZW52L3ZlcnNpb25zLzMuMTAuMTMvbGliL3B5dGhvbjMuMTAvc2l0ZS1wYWNrYWdlcy9jdjIvLmR5bGlicy9saWJTREwyLTIuMC4wLmR5bGliICgweDEyNjgyY2QxOCkuIFRoaXMgbWF5IGNhdXNlIHNwdXJpb3VzIGNhc3RpbmcgZmFpbHVyZXMgYW5kIG15c3RlcmlvdXMgY3Jhc2hlcy4gT25lIG9mIHRoZSBkdXBsaWNhdGVzIG11c3QgYmUgcmVtb3ZlZCBvciByZW5hbWVkLgpvYmpjWzk2MzQ0XTogQ2xhc3MgU0RMX1J1bWJsZU1vdG9yIGlzIGltcGxlbWVudGVkIGluIGJvdGggL1VzZXJzL2tyaXNoeW9naS8ucHllbnYvdmVyc2lvbnMvMy4xMC4xMy9saWIvcHl0aG9uMy4xMC9zaXRlLXBhY2thZ2VzL3B5Z2FtZS8uZHlsaWJzL2xpYlNETDItMi4wLjAuZHlsaWIgKDB4MTBjNWE1Nzc4KSBhbmQgL1VzZXJzL2tyaXNoeW9naS8ucHllbnYvdmVyc2lvbnMvMy4xMC4xMy9saWIvcHl0aG9uMy4xMC9zaXRlLXBhY2thZ2VzL2N2Mi8uZHlsaWJzL2xpYlNETDItMi4wLjAuZHlsaWIgKDB4MTI2ODJjZDQwKS4gVGhpcyBtYXkgY2F1c2Ugc3B1cmlvdXMgY2FzdGluZyBmYWlsdXJlcyBhbmQgbXlzdGVyaW91cyBjcmFzaGVzLiBPbmUgb2YgdGhlIGR1cGxpY2F0ZXMgbXVzdCBiZSByZW1vdmVkIG9yIHJlbmFtZWQuCm9iamNbOTYzNDRdOiBDbGFzcyBTRExfUnVtYmxlQ29udGV4dCBpcyBpbXBsZW1lbnRlZCBpbiBib3RoIC9Vc2Vycy9rcmlzaHlvZ2kvLnB5ZW52L3ZlcnNpb25zLzMuMTAuMTMvbGliL3B5dGhvbjMuMTAvc2l0ZS1wYWNrYWdlcy9weWdhbWUvLmR5bGlicy9saWJTREwyLTIuMC4wLmR5bGliICgweDEwYzVhNTdjOCkgYW5kIC9Vc2Vycy9rcmlzaHlvZ2kvLnB5ZW52L3ZlcnNpb25zLzMuMTAuMTMvbGliL3B5dGhvbjMuMTAvc2l0ZS1wYWNrYWdlcy9jdjIvLmR5bGlicy9saWJTREwyLTIuMC4wLmR5bGliICgweDEyNjgyY2Q5MCkuIFRoaXMgbWF5IGNhdXNlIHNwdXJpb3VzIGNhc3RpbmcgZmFpbHVyZXMgYW5kIG15c3RlcmlvdXMgY3Jhc2hlcy4gT25lIG9mIHRoZSBkdXBsaWNhdGVzIG11c3QgYmUgcmVtb3ZlZCBvciByZW5hbWVkLgpJTkZPOmZhY2VfcmVjb2duaXRpb25fZW5naW5lLnJlY29nbml6ZXI6Tm8gZW5jb2RpbmcgZmlsZSBmb3VuZC4gU3RhcnRpbmcgZnJlc2guCklORk86ZmFjZV9yZWNvZ25pdGlvbl9lbmdpbmUucmVjb2duaXplcjpGYWNlUmVjb2duaXRpb25FbmdpbmUgaW5pdGlhbGl6ZWQuCklORk86X19tYWluX186QXBwbGljYXRpb24gc3RhcnRpbmcg4oCUIHNob3dpbmcgc3BsYXNoIHNjcmVlbi4KT3BlbkNWOiBvdXQgZGV2aWNlIG9mIGJvdW5kICgwLTApOiAxCk9wZW5DVjogY2FtZXJhIGZhaWxlZCB0byBwcm9wZXJseSBpbml0aWFsaXplIQpbIFdBUk46MEA4LjQ4MF0gZ2xvYmFsIGNhcF9mZm1wZWdfaW1wbC5ocHA6MTIxNyBvcGVuIFZJREVPSU8vRkZNUEVHOiBGYWlsZWQgbGlzdCBkZXZpY2VzIGZvciBiYWNrZW5kIGF2Zm91bmRhdGlvbgpPcGVuQ1Y6IG91dCBkZXZpY2Ugb2YgYm91bmQgKDAtMCk6IDIKT3BlbkNWOiBjYW1lcmEgZmFpbGVkIHRvIHByb3Blcmx5IGluaXRpYWxpemUhCk9wZW5DVjogb3V0IGRldmljZSBvZiBib3VuZCAoMC0wKTogMwpPcGVuQ1Y6IGNhbWVyYSBmYWlsZWQgdG8gcHJvcGVybHkgaW5pdGlhbGl6ZSEKT3BlbkNWOiBvdXQgZGV2aWNlIG9mIGJvdW5kICgwLTApOiA0Ck9wZW5DVjogY2FtZXJhIGZhaWxlZCB0byBwcm9wZXJseSBpbml0aWFsaXplIQpJTkZPOl9fbWFpbl9fOk5hdmlnYXRlZCB0bzogZGFzaGJvYXJkCklORk86X19tYWluX186TWFpbiB3aW5kb3cgcmVhZHkuCklORk86ZGF0YWJhc2UuZGJfbWFuYWdlcjpEYXRhYmFzZSBiYWNrZWQgdXA6IC9Vc2Vycy9rcmlzaHlvZ2kvRGVza3RvcC9mYWNlIGRldGVjdGlvbi9kYXRhL2JhY2t1cHMvYXR0ZW5kYW5jZV9iYWNrdXBfMjAyNjA1MThfMTMwOTUwLmRiCklORk86X19tYWluX186QXV0by1iYWNrdXAgY29tcGxldGVkOiAvVXNlcnMva3Jpc2h5b2dpL0Rlc2t0b3AvZmFjZSBkZXRlY3Rpb24vZGF0YS9iYWNrdXBzL2F0dGVuZGFuY2VfYmFja3VwXzIwMjYwNTE4XzEzMDk1MC5kYgpUcmFjZWJhY2sgKG1vc3QgcmVjZW50IGNhbGwgbGFzdCk6CiAgRmlsZSAiL1VzZXJzL2tyaXNoeW9naS9EZXNrdG9wL2ZhY2UgZGV0ZWN0aW9uL21haW4ucHkiLCBsaW5lIDE4OSwgaW4gPG1vZHVsZT4KICAgIGFwcC5tYWlubG9vcCgpCiAgRmlsZSAiL1VzZXJzL2tyaXNoeW9naS8ucHllbnYvdmVyc2lvbnMvMy4xMC4xMy9saWIvcHl0aG9uMy4xMC9zaXRlLXBhY2thZ2VzL2N1c3RvbXRraW50ZXIvd2luZG93cy9jdGtfdGsucHkiLCBsaW5lIDE2NSwgaW4gbWFpbmxvb3AKICAgIHN1cGVyKCkubWFpbmxvb3AoKmFyZ3MsICoqa3dhcmdzKQogIEZpbGUgIi9Vc2Vycy9rcmlzaHlvZ2kvLnB5ZW52L3ZlcnNpb25zLzMuMTAuMTMvbGliL3B5dGhvbjMuMTAvdGtpbnRlci9fX2luaXRfXy5weSIsIGxpbmUgMTQ1OCwgaW4gbWFpbmxvb3AKICAgIHNlbGYudGsubWFpbmxvb3AobikKS2V5Ym9hcmRJbnRlcnJ1cHQK', 'debug_ui_cam.py': 'aW1wb3J0IGN1c3RvbXRraW50ZXIgYXMgY3RrCmltcG9ydCBjdjIKaW1wb3J0IFBJTC5JbWFnZSwgUElMLkltYWdlVGsKaW1wb3J0IHN5cwoKYXBwID0gY3RrLkNUaygpCmFwcC5nZW9tZXRyeSgiODAweDYwMCIpCgpsYmwgPSBjdGsuQ1RrTGFiZWwoYXBwLCB0ZXh0PSJXYWl0aW5nLi4uIikKbGJsLnBhY2soZmlsbD0iYm90aCIsIGV4cGFuZD1UcnVlKQoKY2FwID0gY3YyLlZpZGVvQ2FwdHVyZSgwLCBjdjIuQ0FQX0FWRk9VTkRBVElPTikKI2NhcCA9IGN2Mi5WaWRlb0NhcHR1cmUoMCkKCmRlZiB1cGRhdGUoKToKICAgIHJldCwgZnJhbWUgPSBjYXAucmVhZCgpCiAgICBpZiByZXQ6CiAgICAgICAgcHJpbnQoZiJSZWFkIGZyYW1lISB7ZnJhbWUuc2hhcGV9IikKICAgICAgICByZ2IgPSBjdjIuY3Z0Q29sb3IoZnJhbWUsIGN2Mi5DT0xPUl9CR1IyUkdCKQogICAgICAgIGltZyA9IFBJTC5JbWFnZS5mcm9tYXJyYXkocmdiKS5yZXNpemUoKDQwMCwgMzAwKSkKICAgICAgICBpbWd0ayA9IFBJTC5JbWFnZVRrLlBob3RvSW1hZ2UoaW1hZ2U9aW1nKQogICAgICAgIGxibC5pbWd0ayA9IGltZ3RrCiAgICAgICAgbGJsLmNvbmZpZ3VyZShpbWFnZT1pbWd0aywgdGV4dD0iIikKICAgIGVsc2U6CiAgICAgICAgcHJpbnQoIkZhaWxlZCB0byByZWFkIGZyYW1lIikKICAgIGFwcC5hZnRlcig1MCwgdXBkYXRlKQoKdXBkYXRlKCkKYXBwLmFmdGVyKDMwMDAsIGFwcC5kZXN0cm95KQphcHAubWFpbmxvb3AoKQo=', 'run.sh': 'IyEvYmluL2Jhc2gKIyBTaW1wbGUgc2NyaXB0IHRvIHJ1biB0aGUgYXBwbGljYXRpb24KCiMgQWN0aXZhdGUgdmlydHVhbCBlbnZpcm9ubWVudCBpZiBpdCBleGlzdHMKaWYgWyAtZCAiYnJldy12ZW52IiBdOyB0aGVuCiAgICBzb3VyY2UgYnJldy12ZW52L2Jpbi9hY3RpdmF0ZQplbGlmIFsgLWQgInZlbnYiIF07IHRoZW4KICAgIHNvdXJjZSB2ZW52L2Jpbi9hY3RpdmF0ZQpmaQoKIyBSdW4gdGhlIGFwcApweXRob24zIG1haW4ucHkK', 'README.md': 'IyDwn5GBIEZhY2VUcmFjayBQcm8g4oCUIEFJLVBvd2VyZWQgQXR0ZW5kYW5jZSBTeXN0ZW0KCj4gKipQcm9kdWN0aW9uLWdyYWRlKiogZmFjZSByZWNvZ25pdGlvbiBhdHRlbmRhbmNlIHN5c3RlbSBidWlsdCB3aXRoIFB5dGhvbiwgT3BlbkNWLCBhbmQgQ3VzdG9tVGtpbnRlci4gIAo+IEJlYXV0aWZ1bCBkYXJrL2xpZ2h0IFVJIMK3IFNRTGl0ZSBkYXRhYmFzZSDCtyBDU1YvRXhjZWwgZXhwb3J0IMK3IE9uZS1jb21tYW5kIGxhdW5jaAoKLS0tCgojIyDwn5O4IEZlYXR1cmVzIGF0IGEgR2xhbmNlCgp8IEZlYXR1cmUgfCBEZXRhaWxzIHwKfC0tLXwtLS18CnwgKipMaXZlIEZhY2UgUmVjb2duaXRpb24qKiB8IFJlYWwtdGltZSB3ZWJjYW0gc2Nhbm5pbmcgd2l0aCBIT0cgbW9kZWwgfAp8ICoqQXV0byBBdHRlbmRhbmNlKiogfCBNYXJrcyBvbmNlIHBlciBkYXksIHByZXZlbnRzIGR1cGxpY2F0ZXMgfAp8ICoqVXNlciBSZWdpc3RyYXRpb24qKiB8IENhcHR1cmVzIDMwIGZhY2Ugc2FtcGxlcywgdHJhaW5zIGluc3RhbnRseSB8CnwgKipEYXNoYm9hcmQqKiB8IFRvZGF5J3MgY291bnQsIHJlZ2lzdGVyZWQgdXNlcnMsIHJlY2VudCBzY2FucyB8CnwgKipBbmFseXRpY3MqKiB8IDctZGF5IHRyZW5kIGNoYXJ0ICsgZGVwYXJ0bWVudCBwaWUgY2hhcnQgfAp8ICoqUmVjb3JkcyoqIHwgRmlsdGVyIGJ5IGRhdGUgcmFuZ2UsIGV4cG9ydCBDU1YgLyBFeGNlbCB8CnwgKipTZXR0aW5ncyoqIHwgQ2FtZXJhIHNlbGVjdG9yLCB0b2xlcmFuY2Ugc2xpZGVyLCBiYWNrdXAgfAp8ICoqTm90aWZpY2F0aW9ucyoqIHwgQW5pbWF0ZWQgdG9hc3QgcG9wdXBzIHdpdGggc291bmQgZWZmZWN0cyB8CnwgKipBZG1pbiBMb2dpbioqIHwgUGFzc3dvcmQtcHJvdGVjdGVkIGFkbWluIGdhdGUgfAp8ICoqRGFyayAvIExpZ2h0IE1vZGUqKiB8IFRvZ2dsZSBmcm9tIFNldHRpbmdzIHBhZ2UgfAoKLS0tCgojIyDwn5qAIFF1aWNrIFN0YXJ0IChtYWNPUyAvIExpbnV4KQoKIyMjIFN0ZXAgMSDigJQgUHJlcmVxdWlzaXRlcwoKKipJbnN0YWxsIENNYWtlKiogKHJlcXVpcmVkIGZvciB0aGUgYGZhY2VfcmVjb2duaXRpb25gIGxpYnJhcnkpOgoKYGBgYmFzaAojIG1hY09TCmJyZXcgaW5zdGFsbCBjbWFrZQoKIyBVYnVudHUgLyBEZWJpYW4Kc3VkbyBhcHQgaW5zdGFsbCBjbWFrZSBidWlsZC1lc3NlbnRpYWwKYGBgCgojIyMgU3RlcCAyIOKAlCBJbnN0YWxsIERlcGVuZGVuY2llcwoKYGBgYmFzaApjZCAiZmFjZSBkZXRlY3Rpb24iCnBpcCBpbnN0YWxsIC1yIHJlcXVpcmVtZW50cy50eHQKYGBgCgo+IPCfkqEgVXNpbmcgYSB2aXJ0dWFsIGVudmlyb25tZW50IGlzIHJlY29tbWVuZGVkOgo+IGBgYGJhc2gKPiBweXRob24zIC1tIHZlbnYgdmVudiAmJiBzb3VyY2UgdmVudi9iaW4vYWN0aXZhdGUKPiBwaXAgaW5zdGFsbCAtciByZXF1aXJlbWVudHMudHh0Cj4gYGBgCgojIyMgU3RlcCAzIOKAlCBWZXJpZnkgSW5zdGFsbGF0aW9uCgpgYGBiYXNoCnB5dGhvbjMgdmVyaWZ5X2luc3RhbGwucHkKYGBgCgpBbGwgaXRlbXMgc2hvdWxkIHNob3cg4pyFLiBGaXggYW55IOKdjCBiZWZvcmUgcHJvY2VlZGluZy4KCiMjIyBTdGVwIDQg4oCUIChPcHRpb25hbCkgTG9hZCBEZW1vIERhdGEKCmBgYGJhc2gKcHl0aG9uMyBzZWVkX2RlbW9fZGF0YS5weQpgYGAKClNlZWRzIDEwIHVzZXJzIGFuZCAxNCBkYXlzIG9mIHNhbXBsZSBhdHRlbmRhbmNlIHNvIHRoZSBEYXNoYm9hcmQgbG9va3MgcG9wdWxhdGVkIGltbWVkaWF0ZWx5LgoKIyMjIFN0ZXAgNSDigJQgTGF1bmNoCgpgYGBiYXNoCnB5dGhvbjMgbWFpbi5weQpgYGAKCk9yIHVzZSB0aGUgb25lLWNsaWNrIHNjcmlwdDoKCmBgYGJhc2gKY2htb2QgK3ggcnVuLnNoICYmIC4vcnVuLnNoCmBgYAoKLS0tCgojIyDwn6qfIFF1aWNrIFN0YXJ0IChXaW5kb3dzKQoKYGBgYmF0ClJFTSBJbnN0YWxsIGRlcGVuZGVuY2llcwppbnN0YWxsLmJhdAoKUkVNIFZlcmlmeQpweXRob24gdmVyaWZ5X2luc3RhbGwucHkKClJFTSBTZWVkIGRlbW8gZGF0YSAob3B0aW9uYWwpCnB5dGhvbiBzZWVkX2RlbW9fZGF0YS5weQoKUkVNIExhdW5jaApydW4uYmF0CmBgYAoKLS0tCgojIyDwn5OBIFByb2plY3QgU3RydWN0dXJlCgpgYGAKZmFjZSBkZXRlY3Rpb24vCuKUggrilJzilIDilIAgbWFpbi5weSAgICAgICAgICAgICAgICAgICAgICDihpAgRW50cnkgcG9pbnQK4pSc4pSA4pSAIGNvbmZpZy5weSAgICAgICAgICAgICAgICAgICAg4oaQIEFsbCB0dW5hYmxlIGNvbnN0YW50cwrilJzilIDilIAgcmVxdWlyZW1lbnRzLnR4dArilJzilIDilIAgdmVyaWZ5X2luc3RhbGwucHkgICAgICAgICAgICDihpAgUHJlLWxhdW5jaCBjaGVja2VyCuKUnOKUgOKUgCBzZWVkX2RlbW9fZGF0YS5weSAgICAgICAgICAgIOKGkCBEZW1vIGRhdGEgbG9hZGVyCuKUnOKUgOKUgCBpbnN0YWxsLnNoIC8gaW5zdGFsbC5iYXQgICAgIOKGkCBBdXRvLWluc3RhbGxlcnMK4pSc4pSA4pSAIHJ1bi5zaCAvIHJ1bi5iYXQgICAgICAgICAgICAg4oaQIE9uZS1jbGljayBsYXVuY2hlcnMK4pSCCuKUnOKUgOKUgCBkYXRhYmFzZS8K4pSCICAg4pSU4pSA4pSAIGRiX21hbmFnZXIucHkgICAgICAgICAgICDihpAgU1FMaXRlOiBzY2hlbWEsIENSVUQsIGV4cG9ydArilIIK4pSc4pSA4pSAIGZhY2VfcmVjb2duaXRpb25fZW5naW5lLwrilIIgICDilJTilIDilIAgcmVjb2duaXplci5weSAgICAgICAgICAgIOKGkCBDYXB0dXJlLCB0cmFpbiwgcmVjb2duaXplCuKUggrilJzilIDilIAgZ3VpLwrilIIgICDilJzilIDilIAgc3BsYXNoX3NjcmVlbi5weSAgICAgICAgIOKGkCBBbmltYXRlZCBzdGFydHVwIHNjcmVlbgrilIIgICDilJzilIDilIAgc2lkZWJhci5weSAgICAgICAgICAgICAgIOKGkCBMZWZ0IG5hdmlnYXRpb24gcGFuZWwK4pSCICAg4pSc4pSA4pSAIG5vdGlmaWNhdGlvbi5weSAgICAgICAgICDihpAgVG9hc3QgcG9wdXAgbm90aWZpY2F0aW9ucwrilIIgICDilJzilIDilIAgYWRtaW5fbG9naW4ucHkgICAgICAgICAgIOKGkCBQYXNzd29yZCBkaWFsb2cK4pSCICAg4pSU4pSA4pSAIHBhZ2VzLwrilIIgICAgICAg4pSc4pSA4pSAIGRhc2hib2FyZC5weSAgICAgICAgIOKGkCBIb21lIHN0YXRzICYgcmVjZW50IGxvZ3MK4pSCICAgICAgIOKUnOKUgOKUgCBhdHRlbmRhbmNlLnB5ICAgICAgICDihpAgTGl2ZSB3ZWJjYW0gc2Nhbm5lcgrilIIgICAgICAg4pSc4pSA4pSAIHJlZ2lzdGVyLnB5ICAgICAgICAgIOKGkCBOZXcgdXNlciArIGZhY2UgY2FwdHVyZQrilIIgICAgICAg4pSc4pSA4pSAIHJlY29yZHMucHkgICAgICAgICAgIOKGkCBBdHRlbmRhbmNlIHRhYmxlICsgZXhwb3J0CuKUgiAgICAgICDilJzilIDilIAgYW5hbHl0aWNzLnB5ICAgICAgICAg4oaQIENoYXJ0cyAodHJlbmQgKyBkZXB0KQrilIIgICAgICAg4pSU4pSA4pSAIHNldHRpbmdzLnB5ICAgICAgICAgIOKGkCBDb25maWcgJiBiYWNrdXAK4pSCCuKUnOKUgOKUgCB1dGlscy8K4pSCICAg4pSU4pSA4pSAIGhlbHBlcnMucHkgICAgICAgICAgICAgICDihpAgU291bmQsIHRoZW1lLCB2YWxpZGF0aW9uCuKUggrilJzilIDilIAgZGF0YS8K4pSCICAg4pSc4pSA4pSAIGF0dGVuZGFuY2UuZGIgICAgICAgICAgICDihpAgU1FMaXRlIGRhdGFiYXNlIChhdXRvLWNyZWF0ZWQpCuKUgiAgIOKUnOKUgOKUgCBmYWNlX2VuY29kaW5ncy5wa2wgICAgICAg4oaQIFRyYWluZWQgZmFjZSBtb2RlbCAoYXV0by1jcmVhdGVkKQrilIIgICDilJzilIDilIAgZmFjZV9kYXRhLyAgICAgICAgICAgICAgIOKGkCBSYXcgY2FwdHVyZWQgaW1hZ2VzIHBlciB1c2VyCuKUgiAgIOKUlOKUgOKUgCBiYWNrdXBzLyAgICAgICAgICAgICAgICAg4oaQIEF1dG8gdGltZXN0YW1wZWQgREIgYmFja3VwcwrilIIK4pSc4pSA4pSAIGV4cG9ydHMvICAgICAgICAgICAgICAgICAgICAg4oaQIENTViAvIEV4Y2VsIGV4cG9ydHMgc2F2ZWQgaGVyZQrilJTilIDilIAgbG9ncy8gICAgICAgICAgICAgICAgICAgICAgICDihpAgYXBwLmxvZyB3cml0dGVuIGhlcmUKYGBgCgotLS0KCiMjIPCfl4PvuI8gRGF0YWJhc2UgU2NoZW1hCgojIyMgYHVzZXJzYCB0YWJsZQp8IENvbHVtbiB8IFR5cGUgfCBEZXNjcmlwdGlvbiB8CnwtLS18LS0tfC0tLXwKfCBpZCB8IElOVEVHRVIgUEsgfCBBdXRvLWluY3JlbWVudCB8CnwgbmFtZSB8IFRFWFQgfCBGdWxsIG5hbWUgfAp8IHJvbGxfbnVtYmVyIHwgVEVYVCBVTklRVUUgfCBFbXBsb3llZSAvIHN0dWRlbnQgSUQgfAp8IGRlcGFydG1lbnQgfCBURVhUIHwgRGVwYXJ0bWVudCBvciBjbGFzcyB8CnwgZW1haWwgfCBURVhUIHwgT3B0aW9uYWwgY29udGFjdCB8CnwgcGhvbmUgfCBURVhUIHwgT3B0aW9uYWwgY29udGFjdCB8CnwgcGhvdG9fcGF0aCB8IFRFWFQgfCBQYXRoIHRvIHByb2ZpbGUgaW1hZ2UgfAp8IHJlZ2lzdGVyZWRfYXQgfCBURVhUIHwgSVNPIHRpbWVzdGFtcCB8CnwgaXNfYWN0aXZlIHwgSU5URUdFUiB8IDEgPSBhY3RpdmUsIDAgPSBkZWxldGVkIHwKCiMjIyBgYXR0ZW5kYW5jZWAgdGFibGUKfCBDb2x1bW4gfCBUeXBlIHwgRGVzY3JpcHRpb24gfAp8LS0tfC0tLXwtLS18CnwgaWQgfCBJTlRFR0VSIFBLIHwgQXV0by1pbmNyZW1lbnQgfAp8IHVzZXJfaWQgfCBJTlRFR0VSIEZLIHwgUmVmZXJlbmNlcyBgdXNlcnMuaWRgIHwKfCBkYXRlIHwgVEVYVCB8IFlZWVktTU0tREQgfAp8IHRpbWUgfCBURVhUIHwgSEg6TU06U1MgfAp8IHN0YXR1cyB8IFRFWFQgfCBQcmVzZW50IC8gQWJzZW50IHwKfCBtYXJrZWRfYnkgfCBURVhUIHwgIkZhY2UgUmVjb2duaXRpb24iIHwKCj4gKipVbmlxdWUgY29uc3RyYWludCBvbiBgKHVzZXJfaWQsIGRhdGUpYCoqIHByZXZlbnRzIGR1cGxpY2F0ZSBlbnRyaWVzIHBlciBkYXkuCgojIyMgYHNldHRpbmdzYCB0YWJsZQpLZXktdmFsdWUgc3RvcmUgZm9yIGFsbCBhcHAgcHJlZmVyZW5jZXMgKHRoZW1lLCBjYW1lcmEsIHRvbGVyYW5jZSwgZXRjLikKCiMjIyBgYXVkaXRfbG9nYCB0YWJsZQpFdmVyeSBpbXBvcnRhbnQgYWN0aW9uICh1c2VyIGFkZGVkLCBhdHRlbmRhbmNlIG1hcmtlZCwgYmFja3VwIGNyZWF0ZWQpIGlzIGxvZ2dlZCBoZXJlIGZvciB0cmFjZWFiaWxpdHkuCgotLS0KCiMjIOKame+4jyBDb25maWd1cmF0aW9uCgpFZGl0IGBjb25maWcucHlgIHRvIHR1bmUgdGhlIHN5c3RlbSB3aXRob3V0IHRvdWNoaW5nIGNvcmUgY29kZToKCmBgYHB5dGhvbgpSRUNPR05JVElPTl9UT0xFUkFOQ0UgPSAwLjUwICAgIyBMb3dlciA9IHN0cmljdGVyICgwLjTigJMwLjYpCkNBUFRVUkVfU0FNUExFX0NPVU5UICA9IDMwICAgICAjIEltYWdlcyBjYXB0dXJlZCBwZXIgdXNlcgpERVRFQ1RJT05fTU9ERUwgICAgICAgPSAiaG9nIiAgIyAiaG9nIiAoQ1BVKSBvciAiY25uIiAoR1BVKQpERUZBVUxUX0FETUlOX1BBU1NXT1JEID0gImFkbWluMTIzIiAgIyBDaGFuZ2UgYmVmb3JlIGRlcGxveW1lbnQhCmBgYAoKLS0tCgojIyDwn46vIEhvdyBGYWNlIFJlY29nbml0aW9uIFdvcmtzCgoxLiAqKlJlZ2lzdHJhdGlvbioqIOKAlCBUaGUgc3lzdGVtIGNhcHR1cmVzIDMwIGltYWdlcyBvZiBhIHVzZXIncyBmYWNlIGZyb20gdGhlIHdlYmNhbS4KMi4gKipUcmFpbmluZyoqIOKAlCBFYWNoIGltYWdlIGlzIGVuY29kZWQgaW50byBhIDEyOC1kaW1lbnNpb24gdmVjdG9yIHVzaW5nIGBmYWNlX3JlY29nbml0aW9uYC4gQWxsIHZlY3RvcnMgZm9yIGEgdXNlciBhcmUgYXZlcmFnZWQgaW50byBhIHNpbmdsZSByZXByZXNlbnRhdGl2ZSBlbmNvZGluZy4KMy4gKipSZWNvZ25pdGlvbioqIOKAlCBEdXJpbmcgbGl2ZSBzY2FubmluZywgZWFjaCBkZXRlY3RlZCBmYWNlIGlzIGVuY29kZWQgYW5kIGl0cyBkaXN0YW5jZSB0byBhbGwga25vd24gZW5jb2RpbmdzIGlzIGNvbXB1dGVkLiBJZiB0aGUgY2xvc2VzdCBkaXN0YW5jZSBpcyDiiaQgYFJFQ09HTklUSU9OX1RPTEVSQU5DRWAsIHRoZSB1c2VyIGlzIGlkZW50aWZpZWQuCjQuICoqQXR0ZW5kYW5jZSoqIOKAlCBPbiBhIHN1Y2Nlc3NmdWwgbWF0Y2gsIHRoZSBzeXN0ZW0gY2hlY2tzIHRoZSBgYXR0ZW5kYW5jZWAgdGFibGUuIElmIG5vIGVudHJ5IGV4aXN0cyBmb3IgdG9kYXksIGl0IGluc2VydHMgb25lIGFuZCBwbGF5cyBhIHN1Y2Nlc3Mgc291bmQuCgotLS0KCiMjIPCflKcgVHJvdWJsZXNob290aW5nCgp8IFByb2JsZW0gfCBGaXggfAp8LS0tfC0tLXwKfCBgZGxpYmAgZmFpbHMgdG8gaW5zdGFsbCB8IEluc3RhbGwgQ01ha2UgZmlyc3QsIHRoZW4gcmV0cnkgfAp8IENhbWVyYSBub3Qgb3BlbmluZyB8IENoZWNrIE9TIGNhbWVyYSBwZXJtaXNzaW9uczsgdHJ5IGluZGV4IDEgb3IgMiBpbiBTZXR0aW5ncyB8CnwgU2xvdyByZWNvZ25pdGlvbiB8IFJlZHVjZSBmcmFtZSBzaXplIGluIGByZWNvZ25pemVyLnB5YCAobGluZSBgZng9MC4yNWApIHwKfCBVbmtub3duIGZhY2VzIHwgTG93ZXIgYFJFQ09HTklUSU9OX1RPTEVSQU5DRWAgaW4gYGNvbmZpZy5weWAgfAp8IEFwcCBjcmFzaGVzIG9uIHN0YXJ0IHwgUnVuIGBweXRob24gdmVyaWZ5X2luc3RhbGwucHlgIGFuZCBmaXggYWxsIOKdjCBpdGVtcyB8CnwgTm8gc291bmQgfCBSdW4gYHBpcCBpbnN0YWxsIHB5Z2FtZWA7IHRvZ2dsZSBzb3VuZCBpbiBTZXR0aW5ncyB8CgotLS0KCiMjIPCfk5wgTGljZW5zZQoKTUlUIExpY2Vuc2Ug4oCUIEZyZWUgZm9yIGVkdWNhdGlvbmFsIGFuZCBjb21tZXJjaWFsIHVzZS4KCi0tLQoKKkJ1aWx0IHdpdGgg4p2k77iPIHVzaW5nIFB5dGhvbiDCtyBPcGVuQ1YgwrcgZmFjZV9yZWNvZ25pdGlvbiDCtyBDdXN0b21Ua2ludGVyKgo=', 'install.bat': 'QGVjaG8gb2ZmClRJVExFIEZhY2VUcmFjayBQcm8gLSBXaW5kb3dzIEluc3RhbGxlcgplY2hvID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0KZWNobyAgRmFjZVRyYWNrIFBybyAtIFdpbmRvd3MgQXV0byBJbnN0YWxsZXIKZWNobyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09CgplY2hvIFsxLzNdIENoZWNraW5nIFB5dGhvbi4uLgpweXRob24gLS12ZXJzaW9uID5udWwgMj4mMQpJRiBFUlJPUkxFVkVMIDEgKAogICAgZWNobyBFUlJPUjogUHl0aG9uIGlzIG5vdCBpbnN0YWxsZWQgb3Igbm90IGluIFBBVEguCiAgICBlY2hvIFBsZWFzZSBpbnN0YWxsIFB5dGhvbiAzLjkrIGZyb20gaHR0cHM6Ly93d3cucHl0aG9uLm9yZy9kb3dubG9hZHMvCiAgICBwYXVzZQogICAgZXhpdCAvYgopCgplY2hvIFsyLzNdIFVwZ3JhZGluZyBwaXAuLi4KcHl0aG9uIC1tIHBpcCBpbnN0YWxsIC0tdXBncmFkZSBwaXAKCmVjaG8gWzMvM10gSW5zdGFsbGluZyBkZXBlbmRlbmNpZXMuLi4KcGlwIGluc3RhbGwgLXIgcmVxdWlyZW1lbnRzLnR4dAoKZWNobyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09CmVjaG8gIEluc3RhbGxhdGlvbiBDb21wbGV0ZSEKZWNobyAgUnVuIHRoZSBhcHBsaWNhdGlvbiB1c2luZzogcnVuLmJhdAplY2hvID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0KcGF1c2UK', 'seed_demo_data.py': 'IiIiCuKVlOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVlwrilZEgICAgICAgICBTRUVEIERFTU8gREFUQSDigJQgRmFjZSBBdHRlbmRhbmNlIFN5c3RlbSAgICAgICAgICAgICDilZEK4pWRICBQb3B1bGF0ZXMgdGhlIGRhdGFiYXNlIHdpdGggc2FtcGxlIHVzZXJzIGFuZCBhdHRlbmRhbmNlICAgIOKVkQrilZEgIHJlY29yZHMgc28geW91IGNhbiBleHBsb3JlIHRoZSBkYXNoYm9hcmQgaW1tZWRpYXRlbHkuICAgICAg4pWRCuKVmuKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVnQoKUnVuIHRoaXMgT05DRSB0byBwb3B1bGF0ZSB0aGUgZGF0YWJhc2Ugd2l0aCBzYW1wbGUgZGF0YToKICAgIHB5dGhvbiBzZWVkX2RlbW9fZGF0YS5weQoKV0FSTklORzogUnVubmluZyBhZ2FpbiB3aWxsIGF0dGVtcHQgZHVwbGljYXRlIGluc2VydHMgKHNhZmVseSBpZ25vcmVkKS4KIiIiCgppbXBvcnQgb3MKaW1wb3J0IHN5cwppbXBvcnQgcmFuZG9tCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGUsIHRpbWVkZWx0YQoKIyBBZGQgcHJvamVjdCByb290IHRvIHBhdGgKc3lzLnBhdGguaW5zZXJ0KDAsIG9zLnBhdGguZGlybmFtZShvcy5wYXRoLmFic3BhdGgoX19maWxlX18pKSkKCmZyb20gZGF0YWJhc2UuZGJfbWFuYWdlciBpbXBvcnQgRGF0YWJhc2VNYW5hZ2VyCgpwcmludCgiPSIgKiA1NSkKcHJpbnQoIiAgRmFjZVRyYWNrIFBybyDigJQgRGVtbyBEYXRhIFNlZWRlciIpCnByaW50KCI9IiAqIDU1KQoKZGIgPSBEYXRhYmFzZU1hbmFnZXIoKQoKIyDilIDilIAgU2FtcGxlIFVzZXJzIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgApERU1PX1VTRVJTID0gWwogICAgKCJBbGljZSBKb2huc29uIiwgICAiRU1QLTAwMSIsICJFbmdpbmVlcmluZyIsICAgImFsaWNlQGRlbW8uY29tIiwgICAiOTg3NjU0MzIxMCIpLAogICAgKCJCb2IgU21pdGgiLCAgICAgICAiRU1QLTAwMiIsICJIUiIsICAgICAgICAgICAgICJib2JAZGVtby5jb20iLCAgICAgIjk4NzY1NDMyMTEiKSwKICAgICgiQ2Fyb2wgV2lsbGlhbXMiLCAgIkVNUC0wMDMiLCAiRW5naW5lZXJpbmciLCAgICJjYXJvbEBkZW1vLmNvbSIsICAgIjk4NzY1NDMyMTIiKSwKICAgICgiRGF2aWQgQnJvd24iLCAgICAgIlNUVS0xMDEiLCAiQ29tcHV0ZXIgU2NpIiwgICJkYXZpZEBkZW1vLmNvbSIsICAgIjk4NzY1NDMyMTMiKSwKICAgICgiRXZhIE1hcnRpbmV6IiwgICAgIlNUVS0xMDIiLCAiQ29tcHV0ZXIgU2NpIiwgICJldmFAZGVtby5jb20iLCAgICAgIjk4NzY1NDMyMTQiKSwKICAgICgiRnJhbmsgTGVlIiwgICAgICAgIlNUVS0xMDMiLCAiRWxlY3Ryb25pY3MiLCAgICJmcmFua0BkZW1vLmNvbSIsICAgIjk4NzY1NDMyMTUiKSwKICAgICgiR3JhY2UgS2ltIiwgICAgICAgIkVNUC0wMDQiLCAiU2FsZXMiLCAgICAgICAgICAiZ3JhY2VAZGVtby5jb20iLCAgICI5ODc2NTQzMjE2IiksCiAgICAoIkhlbnJ5IERhdmlzIiwgICAgICJTVFUtMTA0IiwgIk1lY2hhbmljYWwiLCAgICAiaGVucnlAZGVtby5jb20iLCAgICI5ODc2NTQzMjE3IiksCiAgICAoIklzbGEgTW9vcmUiLCAgICAgICJFTVAtMDA1IiwgIkZpbmFuY2UiLCAgICAgICAgImlzbGFAZGVtby5jb20iLCAgICAiOTg3NjU0MzIxOCIpLAogICAgKCJKYWNrIFdpbHNvbiIsICAgICAiU1RVLTEwNSIsICJFbGVjdHJvbmljcyIsICAgImphY2tAZGVtby5jb20iLCAgICAiOTg3NjU0MzIxOSIpLApdCgpwcmludCgiXG5bMS8yXSBBZGRpbmcgZGVtbyB1c2Vycy4uLiIpCnVzZXJfaWRzID0gW10KZm9yIG5hbWUsIHJvbGwsIGRlcHQsIGVtYWlsLCBwaG9uZSBpbiBERU1PX1VTRVJTOgogICAgdWlkID0gZGIuYWRkX3VzZXIobmFtZT1uYW1lLCByb2xsX251bWJlcj1yb2xsLCBkZXBhcnRtZW50PWRlcHQsCiAgICAgICAgICAgICAgICAgICAgICBlbWFpbD1lbWFpbCwgcGhvbmU9cGhvbmUpCiAgICBpZiB1aWQgPiAwOgogICAgICAgIHVzZXJfaWRzLmFwcGVuZCh1aWQpCiAgICAgICAgcHJpbnQoZiIgICAgIOKchSAge25hbWV9ICh7cm9sbH0pIikKICAgIGVsc2U6CiAgICAgICAgIyBVc2VyIGFscmVhZHkgZXhpc3RzIOKAlCBmZXRjaCB0aGVpciBJRAogICAgICAgIGV4aXN0aW5nID0gZGIuZ2V0X3VzZXJfYnlfcm9sbChyb2xsKQogICAgICAgIGlmIGV4aXN0aW5nOgogICAgICAgICAgICB1c2VyX2lkcy5hcHBlbmQoZXhpc3RpbmdbImlkIl0pCiAgICAgICAgcHJpbnQoZiIgICAgIOKaoO+4jyAgIHtuYW1lfSAoe3JvbGx9KSDigJQgYWxyZWFkeSBleGlzdHMsIHNraXBwaW5nLiIpCgpwcmludChmIlxuICAgVG90YWwgYWN0aXZlIHVzZXJzOiB7ZGIuZ2V0X3RvdGFsX3VzZXJzKCl9IikKCiMg4pSA4pSAIFNhbXBsZSBBdHRlbmRhbmNlIChsYXN0IDE0IGRheXMpIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgApwcmludCgiXG5bMi8yXSBHZW5lcmF0aW5nIGF0dGVuZGFuY2UgZm9yIHRoZSBsYXN0IDE0IGRheXMuLi4iKQoKaW1wb3J0IHNxbGl0ZTMKCnRvZGF5ID0gZGF0ZS50b2RheSgpCnRvdGFsX2luc2VydGVkID0gMAoKZm9yIHVpZCBpbiB1c2VyX2lkczoKICAgICMgRWFjaCB1c2VyIGhhcyB+NzUlIGF0dGVuZGFuY2UgcHJvYmFiaWxpdHkgcGVyIGRheQogICAgZm9yIGRheXNfYmFjayBpbiByYW5nZSgxNCwgLTEsIC0xKToKICAgICAgICBhdHRlbmRhbmNlX2RhdGUgPSB0b2RheSAtIHRpbWVkZWx0YShkYXlzPWRheXNfYmFjaykKICAgICAgICBkYXRlX3N0ciA9IGF0dGVuZGFuY2VfZGF0ZS5zdHJmdGltZSgiJVktJW0tJWQiKQoKICAgICAgICAjIFNraXAgd2Vla2VuZHMgZm9yIHJlYWxpc20KICAgICAgICBpZiBhdHRlbmRhbmNlX2RhdGUud2Vla2RheSgpID49IDU6CiAgICAgICAgICAgIGNvbnRpbnVlCgogICAgICAgICMgUmFuZG9tIGF0dGVuZGFuY2UgKDc1JSBjaGFuY2UgcHJlc2VudCkKICAgICAgICBpZiByYW5kb20ucmFuZG9tKCkgPCAwLjc1OgogICAgICAgICAgICB0aW1lX3N0ciA9IGYie3JhbmRvbS5yYW5kaW50KDgsIDkpOjAyZH06e3JhbmRvbS5yYW5kaW50KDAsIDU5KTowMmR9OntyYW5kb20ucmFuZGludCgwLCA1OSk6MDJkfSIKICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgd2l0aCBkYi5fZ2V0X2Nvbm5lY3Rpb24oKSBhcyBjb25uOgogICAgICAgICAgICAgICAgICAgIGNvbm4uZXhlY3V0ZSgKICAgICAgICAgICAgICAgICAgICAgICAgIklOU0VSVCBPUiBJR05PUkUgSU5UTyBhdHRlbmRhbmNlICh1c2VyX2lkLCBkYXRlLCB0aW1lLCBzdGF0dXMpIFZBTFVFUyAoPywgPywgPywgPykiLAogICAgICAgICAgICAgICAgICAgICAgICAodWlkLCBkYXRlX3N0ciwgdGltZV9zdHIsICJQcmVzZW50IikKICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAgICAgY29ubi5jb21taXQoKQogICAgICAgICAgICAgICAgICAgIHRvdGFsX2luc2VydGVkICs9IDEKICAgICAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAgICAgICAgIHBhc3MKCnByaW50KGYiICAgICDinIUgIHt0b3RhbF9pbnNlcnRlZH0gYXR0ZW5kYW5jZSByZWNvcmRzIGluc2VydGVkLlxuIikKCnByaW50KCI9IiAqIDU1KQpwcmludChmIiAgVG9kYXkncyBhdHRlbmRhbmNlOiB7ZGIuZ2V0X3RvZGF5X2NvdW50KCl9IHJlY29yZHMiKQpwcmludChmIiAgVG90YWwgdXNlcnMgICAgICAgOiB7ZGIuZ2V0X3RvdGFsX3VzZXJzKCl9IikKcHJpbnQoZiIgIEF2ZyBhdHRlbmRhbmNlICUgIDoge2RiLmdldF9hdHRlbmRhbmNlX3BlcmNlbnRhZ2UoZGF5cz0xNCl9JSIpCnByaW50KCI9IiAqIDU1KQpwcmludCgiXG4gIOKchSBEZW1vIGRhdGEgcmVhZHkhIFJ1biBgcHl0aG9uIG1haW4ucHlgIHRvIGxhdW5jaC5cbiIpCg==', 'main.py': 'IiIiCuKVlOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVlwrilZEgICAgICAgICAgICBGQUNFIEFUVEVOREFOQ0UgU1lTVEVNIC0gTUFJTiBFTlRSWSBQT0lOVCAgICAgICAg4pWRCuKVkSAgSW5pdGlhbGl6ZXMgdGhlIEdVSSwgbWFuYWdlcyByb3V0aW5nIGJldHdlZW4gcGFnZXMsICAgICAgICDilZEK4pWRICBhbmQgc2NoZWR1bGVzIGJhY2tncm91bmQgdGFza3MgKGF1dG8tYmFja3VwLCByZWxvYWQpLiAgICAgIOKVkQrilZrilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZ0KIiIiCgppbXBvcnQgb3MKaW1wb3J0IHN5cwppbXBvcnQgdGhyZWFkaW5nCmltcG9ydCBsb2dnaW5nCgojIOKUgOKUgCBFbnN1cmUgcHJvamVjdCByb290IGlzIG9uIFBZVEhPTlBBVEgg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSAClJPT1QgPSBvcy5wYXRoLmRpcm5hbWUob3MucGF0aC5hYnNwYXRoKF9fZmlsZV9fKSkKc3lzLnBhdGguaW5zZXJ0KDAsIFJPT1QpCgppbXBvcnQgY3VzdG9tdGtpbnRlciBhcyBjdGsKZnJvbSB1dGlscy5oZWxwZXJzIGltcG9ydCB0aGVtZV9tYW5hZ2VyLCBzb3VuZF9tYW5hZ2VyCmZyb20gZGF0YWJhc2UuZGJfbWFuYWdlciBpbXBvcnQgZGIKCiMgR1VJIENvbXBvbmVudHMKZnJvbSBndWkuc3BsYXNoX3NjcmVlbiBpbXBvcnQgU3BsYXNoU2NyZWVuCmZyb20gZ3VpLnNpZGViYXIgaW1wb3J0IFNpZGViYXIKZnJvbSBndWkubm90aWZpY2F0aW9uIGltcG9ydCBUb2FzdE5vdGlmaWNhdGlvbgoKIyBQYWdlcwpmcm9tIGd1aS5wYWdlcy5kYXNoYm9hcmQgaW1wb3J0IERhc2hib2FyZFBhZ2UKZnJvbSBndWkucGFnZXMuYXR0ZW5kYW5jZSBpbXBvcnQgQXR0ZW5kYW5jZVBhZ2UKZnJvbSBndWkucGFnZXMucmVnaXN0ZXIgaW1wb3J0IFJlZ2lzdGVyUGFnZQpmcm9tIGd1aS5wYWdlcy5yZWNvcmRzIGltcG9ydCBSZWNvcmRzUGFnZQpmcm9tIGd1aS5wYWdlcy5hbmFseXRpY3MgaW1wb3J0IEFuYWx5dGljc1BhZ2UKZnJvbSBndWkucGFnZXMuc2V0dGluZ3MgaW1wb3J0IFNldHRpbmdzUGFnZQoKIyDilIDilIAgTG9nZ2luZyDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIAKbG9nZ2luZy5iYXNpY0NvbmZpZygKICAgIGxldmVsPWxvZ2dpbmcuSU5GTywKICAgIGZvcm1hdD0iJShhc2N0aW1lKXMgIFslKGxldmVsbmFtZSlzXSAgJShuYW1lKXMg4oCUICUobWVzc2FnZSlzIiwKICAgIGhhbmRsZXJzPVsKICAgICAgICBsb2dnaW5nLlN0cmVhbUhhbmRsZXIoKSwKICAgICAgICBsb2dnaW5nLkZpbGVIYW5kbGVyKG9zLnBhdGguam9pbihST09ULCAibG9ncyIsICJhcHAubG9nIiksIGVuY29kaW5nPSJ1dGYtOCIpLAogICAgXQopCm9zLm1ha2VkaXJzKG9zLnBhdGguam9pbihST09ULCAibG9ncyIpLCBleGlzdF9vaz1UcnVlKQpsb2dnZXIgPSBsb2dnaW5nLmdldExvZ2dlcihfX25hbWVfXykKCgojIOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkAojICBNYWluIEFwcGxpY2F0aW9uIFdpbmRvdwojIOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkApjbGFzcyBGYWNlQXR0ZW5kYW5jZUFwcChjdGsuQ1RrKToKICAgICIiIgogICAgVG9wLWxldmVsIGFwcGxpY2F0aW9uIHdpbmRvdy4KICAgIE1hbmFnZXMgdGhlIHNpZGViYXIgKyBwYWdlIGNvbnRhaW5lciBsYXlvdXQgYW5kIGFsbCBuYXZpZ2F0aW9uLgogICAgIiIiCgogICAgZGVmIF9faW5pdF9fKHNlbGYpOgogICAgICAgIHN1cGVyKCkuX19pbml0X18oKQoKICAgICAgICAjIOKUgOKUgCBBcHBseSBzYXZlZCB0aGVtZSDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIAKICAgICAgICBzYXZlZF90aGVtZSA9IGRiLmdldF9zZXR0aW5nKCJ0aGVtZSIsICJkYXJrIikKICAgICAgICBjdGsuc2V0X2FwcGVhcmFuY2VfbW9kZShzYXZlZF90aGVtZSkKICAgICAgICB0aGVtZV9tYW5hZ2VyLm1vZGUgICA9IHNhdmVkX3RoZW1lCiAgICAgICAgdGhlbWVfbWFuYWdlci5jb2xvcnMgPSAoCiAgICAgICAgICAgIHRoZW1lX21hbmFnZXIuREFSSyBpZiBzYXZlZF90aGVtZSA9PSAiZGFyayIgZWxzZSB0aGVtZV9tYW5hZ2VyLkxJR0hUCiAgICAgICAgKQoKICAgICAgICAjIOKUgOKUgCBXaW5kb3cgc2V0dXAg4pSA4pSA4pSA4pSA4pSA4pSACiAgICAgICAgIyBzZWxmLndpdGhkcmF3KCkgICMgRGlzYWJsZWQgdG8gZml4IG1hY09TIGJsYWNrIHNjcmVlbiBidWcKICAgICAgICBzZWxmLnRpdGxlKCJGYWNlVHJhY2sgUHJvIOKAlCBBSSBBdHRlbmRhbmNlIFN5c3RlbSIpCiAgICAgICAgc2VsZi5nZW9tZXRyeSgiMTIwMHg3MjAiKQogICAgICAgIHNlbGYubWluc2l6ZSg5NjAsIDYyMCkKICAgICAgICBzZWxmLmNvbmZpZ3VyZShmZ19jb2xvcj10aGVtZV9tYW5hZ2VyLmNvbG9yc1siYmdfcHJpbWFyeSJdKQoKICAgICAgICAjIFN0YXRlCiAgICAgICAgc2VsZi5wYWdlcyAgICAgICAgPSB7fQogICAgICAgIHNlbGYuY3VycmVudF9wYWdlID0gTm9uZQoKICAgICAgICBsb2dnZXIuaW5mbygiQXBwbGljYXRpb24gc3RhcnRpbmcg4oCUIGJ5cGFzc2luZyBzcGxhc2ggc2NyZWVuLiIpCiAgICAgICAgc2VsZi5fYnVpbGRfbWFpbl91aSgpCiAgICAgICAgIyBTY2hlZHVsZSBhdXRvLWJhY2t1cCBpbiBiYWNrZ3JvdW5kIChydW5zIDMwIHMgYWZ0ZXIgbGF1bmNoKQogICAgICAgIHRocmVhZGluZy5UaW1lcigzMCwgc2VsZi5fYXV0b19iYWNrdXApLnN0YXJ0KCkKCgogICAgIyDilIDilIAgTWFpbiBVSSDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIAKICAgIGRlZiBfYnVpbGRfbWFpbl91aShzZWxmKToKICAgICAgICAiIiJDb25zdHJ1Y3Qgc2lkZWJhciArIHBhZ2UgY29udGFpbmVyLiIiIgogICAgICAgIGMgPSB0aGVtZV9tYW5hZ2VyLmNvbG9ycwoKICAgICAgICAjIFJvb3QgZ3JpZAogICAgICAgIHNlbGYuZ3JpZF9yb3djb25maWd1cmUoMCwgd2VpZ2h0PTEpCiAgICAgICAgc2VsZi5ncmlkX2NvbHVtbmNvbmZpZ3VyZSgxLCB3ZWlnaHQ9MSkKCiAgICAgICAgIyBTaWRlYmFyCiAgICAgICAgc2VsZi5zaWRlYmFyID0gU2lkZWJhcihzZWxmLCBvbl9uYXZpZ2F0ZT1zZWxmLm5hdmlnYXRlKQogICAgICAgIHNlbGYuc2lkZWJhci5ncmlkKHJvdz0wLCBjb2x1bW49MCwgc3RpY2t5PSJuc2V3IikKCiAgICAgICAgIyBSaWdodC1zaWRlIGNvbnRhaW5lciAocGFnZXMgbGl2ZSBoZXJlKQogICAgICAgIHNlbGYuY29udGFpbmVyID0gY3RrLkNUa0ZyYW1lKAogICAgICAgICAgICBzZWxmLCBmZ19jb2xvcj1jWyJiZ19wcmltYXJ5Il0sIGNvcm5lcl9yYWRpdXM9MAogICAgICAgICkKICAgICAgICBzZWxmLmNvbnRhaW5lci5ncmlkKHJvdz0wLCBjb2x1bW49MSwgc3RpY2t5PSJuc2V3IikKCiAgICAgICAgIyBJbnN0YW50aWF0ZSBhbGwgcGFnZXMgKGxhenkgaWYgc2xvdykKICAgICAgICBzZWxmLnBhZ2VzWyJkYXNoYm9hcmQiXSAgPSBEYXNoYm9hcmRQYWdlKHNlbGYuY29udGFpbmVyKQogICAgICAgIHNlbGYucGFnZXNbImF0dGVuZGFuY2UiXSA9IEF0dGVuZGFuY2VQYWdlKHNlbGYuY29udGFpbmVyKQogICAgICAgIHNlbGYucGFnZXNbInJlZ2lzdGVyIl0gICA9IFJlZ2lzdGVyUGFnZShzZWxmLmNvbnRhaW5lcikKICAgICAgICBzZWxmLnBhZ2VzWyJyZWNvcmRzIl0gICAgPSBSZWNvcmRzUGFnZShzZWxmLmNvbnRhaW5lcikKICAgICAgICBzZWxmLnBhZ2VzWyJhbmFseXRpY3MiXSAgPSBBbmFseXRpY3NQYWdlKHNlbGYuY29udGFpbmVyKQogICAgICAgIHNlbGYucGFnZXNbInNldHRpbmdzIl0gICA9IFNldHRpbmdzUGFnZShzZWxmLmNvbnRhaW5lcikKCiAgICAgICAgIyBTdGFydCBvbiBkYXNoYm9hcmQKICAgICAgICBzZWxmLm5hdmlnYXRlKCJkYXNoYm9hcmQiKQoKICAgICMg4pSA4pSAIE5hdmlnYXRpb24g4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACiAgICBkZWYgbmF2aWdhdGUoc2VsZiwgcGFnZV9rZXk6IHN0cik6CiAgICAgICAgIiIiCiAgICAgICAgU3dpdGNoIHRoZSB2aXNpYmxlIHBhZ2UuCiAgICAgICAgLSBTdG9wcyB3ZWJjYW0gaWYgbGVhdmluZyBhdHRlbmRhbmNlIHBhZ2UuCiAgICAgICAgLSBDYWxscyByZWZyZXNoX2RhdGEoKSBvbiB0aGUgdGFyZ2V0IHBhZ2UgaWYgYXZhaWxhYmxlLgogICAgICAgICIiIgogICAgICAgICMgU3RvcCBjYW1lcmEgd2hlbiBsZWF2aW5nIGF0dGVuZGFuY2UgcGFnZQogICAgICAgIGlmIChzZWxmLmN1cnJlbnRfcGFnZSA9PSAiYXR0ZW5kYW5jZSIKICAgICAgICAgICAgICAgIGFuZCBwYWdlX2tleSAhPSAiYXR0ZW5kYW5jZSIKICAgICAgICAgICAgICAgIGFuZCAiYXR0ZW5kYW5jZSIgaW4gc2VsZi5wYWdlcyk6CiAgICAgICAgICAgIHNlbGYucGFnZXNbImF0dGVuZGFuY2UiXS5zdG9wKCkKCiAgICAgICAgIyBIaWRlIGN1cnJlbnQgcGFnZQogICAgICAgIGlmIHNlbGYuY3VycmVudF9wYWdlIGFuZCBzZWxmLmN1cnJlbnRfcGFnZSBpbiBzZWxmLnBhZ2VzOgogICAgICAgICAgICBzZWxmLnBhZ2VzW3NlbGYuY3VycmVudF9wYWdlXS5wYWNrX2ZvcmdldCgpCgogICAgICAgICMgU2hvdyB0YXJnZXQgcGFnZQogICAgICAgIHBhZ2UgPSBzZWxmLnBhZ2VzLmdldChwYWdlX2tleSkKICAgICAgICBpZiBwYWdlOgogICAgICAgICAgICBwYWdlLnBhY2soZmlsbD0iYm90aCIsIGV4cGFuZD1UcnVlKQogICAgICAgICAgICBzZWxmLmN1cnJlbnRfcGFnZSA9IHBhZ2Vfa2V5CgogICAgICAgICAgICAjIFJlZnJlc2ggZGF0YSAobm9uLWJsb2NraW5nKQogICAgICAgICAgICBpZiBoYXNhdHRyKHBhZ2UsICJyZWZyZXNoX2RhdGEiKToKICAgICAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgICAgICBwYWdlLnJlZnJlc2hfZGF0YSgpCiAgICAgICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgICAgICAgICAgICAgbG9nZ2VyLmVycm9yKGYicmVmcmVzaF9kYXRhIGVycm9yIG9uIHtwYWdlX2tleX06IHtlfSIpCgogICAgICAgICAgICBsb2dnZXIuaW5mbyhmIk5hdmlnYXRlZCB0bzoge3BhZ2Vfa2V5fSIpCgogICAgIyDilIDilIAgVG9hc3QgSGVscGVyIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgAogICAgZGVmIG5vdGlmeShzZWxmLCBtZXNzYWdlOiBzdHIsIHR5cGVfOiBzdHIgPSAiaW5mbyIpOgogICAgICAgICIiIlNob3cgYSB0b2FzdCBub3RpZmljYXRpb24gZnJvbSBhbnl3aGVyZSBpbiB0aGUgYXBwLiIiIgogICAgICAgIFRvYXN0Tm90aWZpY2F0aW9uKHNlbGYsIG1lc3NhZ2UsIHR5cGVfPXR5cGVfKQoKICAgICMg4pSA4pSAIEF1dG8gQmFja3VwIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgAogICAgZGVmIF9hdXRvX2JhY2t1cChzZWxmKToKICAgICAgICAiIiJTaWxlbnRseSBiYWNrdXAgdGhlIGRhdGFiYXNlIGlmIGF1dG8tYmFja3VwIGlzIGVuYWJsZWQuIiIiCiAgICAgICAgdHJ5OgogICAgICAgICAgICBpZiBkYi5nZXRfc2V0dGluZygiYXV0b19iYWNrdXAiLCAidHJ1ZSIpID09ICJ0cnVlIjoKICAgICAgICAgICAgICAgIHBhdGggPSBkYi5iYWNrdXBfZGF0YWJhc2UoKQogICAgICAgICAgICAgICAgbG9nZ2VyLmluZm8oZiJBdXRvLWJhY2t1cCBjb21wbGV0ZWQ6IHtwYXRofSIpCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgICAgICBsb2dnZXIuZXJyb3IoZiJBdXRvLWJhY2t1cCBmYWlsZWQ6IHtlfSIpCgogICAgIyDilIDilIAgQ2xlYW4gU2h1dGRvd24g4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACiAgICBkZWYgb25fY2xvc2Uoc2VsZik6CiAgICAgICAgIiIiR3JhY2VmdWxseSBzdG9wIGNhbWVyYSBhbmQgZXhpdC4iIiIKICAgICAgICBpZiAiYXR0ZW5kYW5jZSIgaW4gc2VsZi5wYWdlczoKICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgc2VsZi5wYWdlc1siYXR0ZW5kYW5jZSJdLnN0b3AoKQogICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgICAgICAgICAgcGFzcwogICAgICAgIGxvZ2dlci5pbmZvKCJBcHBsaWNhdGlvbiBjbG9zZWQuIikKICAgICAgICBzZWxmLmRlc3Ryb3koKQoKCiMg4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQCiMgIEVudHJ5IFBvaW50CiMg4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBhcHAgPSBGYWNlQXR0ZW5kYW5jZUFwcCgpCiAgICBhcHAucHJvdG9jb2woIldNX0RFTEVURV9XSU5ET1ciLCBhcHAub25fY2xvc2UpICAjIEhhbmRsZSB3aW5kb3ctY2xvc2UgY2xlYW5seQogICAgYXBwLm1haW5sb29wKCkK', 'test_ctk.py': 'aW1wb3J0IGN1c3RvbXRraW50ZXIgYXMgY3RrCmFwcCA9IGN0ay5DVGsoKQphcHAudGl0bGUoIlRlc3QiKQphcHAuZ2VvbWV0cnkoIjQwMHgzMDAiKQpjdGsuQ1RrTGFiZWwoYXBwLCB0ZXh0PSJDVGsgaXMgd29ya2luZyEiKS5wYWNrKGV4cGFuZD1UcnVlKQphcHAubWFpbmxvb3AoKQo=', 'verify_install.py': 'IiIiCuKVlOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVlwrilZEgICAgICAgICAgIFZFUklGWSBJTlNUQUxMIOKAlCBGYWNlIEF0dGVuZGFuY2UgU3lzdGVtICAgICAgICAgICDilZEK4pWRICBDaGVja3MgYWxsIGRlcGVuZGVuY2llcyBhbmQgZmlsZXMgYmVmb3JlIGZpcnN0IGxhdW5jaCAgICAgIOKVkQrilZrilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZ0KClJ1biB0aGlzIGJlZm9yZSBzdGFydGluZyB0aGUgYXBwIGZvciB0aGUgZmlyc3QgdGltZToKICAgIHB5dGhvbiB2ZXJpZnlfaW5zdGFsbC5weQoiIiIKCmltcG9ydCBzeXMKaW1wb3J0IG9zCgpST09UID0gb3MucGF0aC5kaXJuYW1lKG9zLnBhdGguYWJzcGF0aChfX2ZpbGVfXykpCnN5cy5wYXRoLmluc2VydCgwLCBST09UKQoKUEFTUyA9ICLinIUiCkZBSUwgPSAi4p2MIgpXQVJOID0gIuKaoO+4jyAiCgpwcmludCgiPSIgKiA1NSkKcHJpbnQoIiAgRmFjZVRyYWNrIFBybyDigJQgSW5zdGFsbGF0aW9uIFZlcmlmaWVyIikKcHJpbnQoIj0iICogNTUpCgphbGxfb2sgPSBUcnVlCgojIOKUgOKUgCBQeXRob24gdmVyc2lvbiDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIAKbWFqb3IsIG1pbm9yID0gc3lzLnZlcnNpb25faW5mb1s6Ml0KaWYgbWFqb3IgPj0gMyBhbmQgbWlub3IgPj0gOToKICAgIHByaW50KGYie1BBU1N9IFB5dGhvbiB7bWFqb3J9LnttaW5vcn0g4oCUIE9LIikKZWxzZToKICAgIHByaW50KGYie0ZBSUx9IFB5dGhvbiB7bWFqb3J9LnttaW5vcn0g4oCUIE5lZWQgUHl0aG9uIDMuOSsiKQogICAgYWxsX29rID0gRmFsc2UKCiMg4pSA4pSAIFJlcXVpcmVkIHBhY2thZ2VzIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgApwYWNrYWdlcyA9IFsKICAgICgiY3YyIiwgICAgICAgICAgICAgICJvcGVuY3YtcHl0aG9uIiksCiAgICAoImZhY2VfcmVjb2duaXRpb24iLCAiZmFjZS1yZWNvZ25pdGlvbiIpLAogICAgKCJjdXN0b210a2ludGVyIiwgICAgImN1c3RvbXRraW50ZXIiKSwKICAgICgiUElMIiwgICAgICAgICAgICAgICJQaWxsb3ciKSwKICAgICgicGFuZGFzIiwgICAgICAgICAgICJwYW5kYXMiKSwKICAgICgibnVtcHkiLCAgICAgICAgICAgICJudW1weSIpLAogICAgKCJvcGVucHl4bCIsICAgICAgICAgIm9wZW5weXhsIiksCiAgICAoIm1hdHBsb3RsaWIiLCAgICAgICAibWF0cGxvdGxpYiIpLAogICAgKCJweWdhbWUiLCAgICAgICAgICAgInB5Z2FtZSIpLApdCgpwcmludCgiXG4gIENoZWNraW5nIHBhY2thZ2VzOiIpCmZvciBtb2R1bGUsIHBpcF9uYW1lIGluIHBhY2thZ2VzOgogICAgdHJ5OgogICAgICAgIF9faW1wb3J0X18obW9kdWxlKQogICAgICAgIHByaW50KGYiICB7UEFTU30ge3BpcF9uYW1lfSIpCiAgICBleGNlcHQgSW1wb3J0RXJyb3I6CiAgICAgICAgcHJpbnQoZiIgIHtGQUlMfSB7cGlwX25hbWV9ICDihpIgIHJ1bjogcGlwIGluc3RhbGwge3BpcF9uYW1lfSIpCiAgICAgICAgYWxsX29rID0gRmFsc2UKCiMg4pSA4pSAIFByb2plY3QgZmlsZXMg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACnByaW50KCJcbiAgQ2hlY2tpbmcgcHJvamVjdCBmaWxlczoiKQpyZXF1aXJlZF9maWxlcyA9IFsKICAgICJtYWluLnB5IiwKICAgICJjb25maWcucHkiLAogICAgInJlcXVpcmVtZW50cy50eHQiLAogICAgImRhdGFiYXNlL2RiX21hbmFnZXIucHkiLAogICAgImZhY2VfcmVjb2duaXRpb25fZW5naW5lL3JlY29nbml6ZXIucHkiLAogICAgInV0aWxzL2hlbHBlcnMucHkiLAogICAgImd1aS9zcGxhc2hfc2NyZWVuLnB5IiwKICAgICJndWkvc2lkZWJhci5weSIsCiAgICAiZ3VpL25vdGlmaWNhdGlvbi5weSIsCiAgICAiZ3VpL2FkbWluX2xvZ2luLnB5IiwKICAgICJndWkvcGFnZXMvZGFzaGJvYXJkLnB5IiwKICAgICJndWkvcGFnZXMvYXR0ZW5kYW5jZS5weSIsCiAgICAiZ3VpL3BhZ2VzL3JlZ2lzdGVyLnB5IiwKICAgICJndWkvcGFnZXMvcmVjb3Jkcy5weSIsCiAgICAiZ3VpL3BhZ2VzL2FuYWx5dGljcy5weSIsCiAgICAiZ3VpL3BhZ2VzL3NldHRpbmdzLnB5IiwKXQoKZm9yIGYgaW4gcmVxdWlyZWRfZmlsZXM6CiAgICBwYXRoID0gb3MucGF0aC5qb2luKFJPT1QsIGYpCiAgICBpZiBvcy5wYXRoLmV4aXN0cyhwYXRoKToKICAgICAgICBwcmludChmIiAge1BBU1N9IHtmfSIpCiAgICBlbHNlOgogICAgICAgIHByaW50KGYiICB7RkFJTH0ge2Z9ICDigJQgRklMRSBNSVNTSU5HIikKICAgICAgICBhbGxfb2sgPSBGYWxzZQoKIyDilIDilIAgRGlyZWN0b3JpZXMg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACnByaW50KCJcbiAgQ2hlY2tpbmcgZGlyZWN0b3JpZXM6IikKcmVxdWlyZWRfZGlycyA9IFsiZGF0YSIsICJkYXRhL2ZhY2VfZGF0YSIsICJkYXRhL2JhY2t1cHMiLCAiZXhwb3J0cyIsICJsb2dzIl0KZm9yIGQgaW4gcmVxdWlyZWRfZGlyczoKICAgIHBhdGggPSBvcy5wYXRoLmpvaW4oUk9PVCwgZCkKICAgIG9zLm1ha2VkaXJzKHBhdGgsIGV4aXN0X29rPVRydWUpCiAgICBwcmludChmIiAge1BBU1N9IHtkfS8iKQoKIyDilIDilIAgQ2FtZXJhIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgApwcmludCgiXG4gIENoZWNraW5nIGNhbWVyYToiKQp0cnk6CiAgICBpbXBvcnQgY3YyCiAgICBjYXAgPSBjdjIuVmlkZW9DYXB0dXJlKDApCiAgICBpZiBjYXAuaXNPcGVuZWQoKToKICAgICAgICBwcmludChmIiAge1BBU1N9IENhbWVyYSBhdCBpbmRleCAwIGlzIGFjY2Vzc2libGUiKQogICAgICAgIGNhcC5yZWxlYXNlKCkKICAgIGVsc2U6CiAgICAgICAgcHJpbnQoZiIgIHtXQVJOfSBDYW1lcmEgYXQgaW5kZXggMCBjb3VsZCBub3QgYmUgb3BlbmVkIikKICAgICAgICBwcmludChmIiAgICAgICAoVGhlIGFwcCB3aWxsIHN0aWxsIGxhdW5jaDsgY2hlY2sgY2FtZXJhIHBlcm1pc3Npb25zKSIpCmV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgIHByaW50KGYiICB7V0FSTn0gQ2FtZXJhIGNoZWNrIGZhaWxlZDoge2V9IikKCiMg4pSA4pSAIERhdGFiYXNlIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgApwcmludCgiXG4gIENoZWNraW5nIGRhdGFiYXNlOiIpCnRyeToKICAgIGZyb20gZGF0YWJhc2UuZGJfbWFuYWdlciBpbXBvcnQgRGF0YWJhc2VNYW5hZ2VyCiAgICBkYiA9IERhdGFiYXNlTWFuYWdlcigpCiAgICB1c2VycyA9IGRiLmdldF90b3RhbF91c2VycygpCiAgICBwcmludChmIiAge1BBU1N9IERhdGFiYXNlIGNvbm5lY3RlZC4gUmVnaXN0ZXJlZCB1c2Vyczoge3VzZXJzfSIpCmV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgIHByaW50KGYiICB7RkFJTH0gRGF0YWJhc2UgZXJyb3I6IHtlfSIpCiAgICBhbGxfb2sgPSBGYWxzZQoKIyDilIDilIAgUmVzdWx0IOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgApwcmludCgiXG4iICsgIj0iICogNTUpCmlmIGFsbF9vazoKICAgIHByaW50KGYiICB7UEFTU30gQWxsIGNoZWNrcyBwYXNzZWQhIFJ1bjogcHl0aG9uIG1haW4ucHkiKQplbHNlOgogICAgcHJpbnQoZiIgIHtGQUlMfSBTb21lIGNoZWNrcyBmYWlsZWQuIEZpeCBpc3N1ZXMgYWJvdmUsIHRoZW4gcmV0cnkuIikKcHJpbnQoIj0iICogNTUgKyAiXG4iKQo=', 'database/db_manager.py': 'IiIiCuKVlOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVlwrilZEgICAgICAgICBEQVRBQkFTRSBNQU5BR0VSIOKAlCBGYWNlIEF0dGVuZGFuY2UgU3lzdGVtICAgICAgICAgICDilZEK4pWRICBIYW5kbGVzIGFsbCBTUUxpdGUgb3BlcmF0aW9uczogdXNlcnMsIGF0dGVuZGFuY2UsIHNldHRpbmdzIOKVkQrilZrilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZ0KClRoaXMgbW9kdWxlIGlzIHJlc3BvbnNpYmxlIGZvcjoKICAtIENyZWF0aW5nIC8gY29ubmVjdGluZyB0byB0aGUgU1FMaXRlIGRhdGFiYXNlCiAgLSBDcmVhdGluZyBhbGwgdGFibGVzICh1c2VycywgYXR0ZW5kYW5jZSwgc2V0dGluZ3MsIGF1ZGl0IGxvZykKICAtIENSVUQgb3BlcmF0aW9ucyAoQ3JlYXRlLCBSZWFkLCBVcGRhdGUsIERlbGV0ZSkKICAtIEV4cG9ydGluZyBhdHRlbmRhbmNlIHRvIENTViAvIEV4Y2VsCiAgLSBBbmFseXRpY3MgcXVlcmllcyAoYXR0ZW5kYW5jZSAlLCB0b3RhbHMsIHRyZW5kcykKIiIiCgppbXBvcnQgc3FsaXRlMwppbXBvcnQgb3MKaW1wb3J0IHNodXRpbAppbXBvcnQgcGFuZGFzIGFzIHBkCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCBkYXRlLCB0aW1lZGVsdGEKaW1wb3J0IGxvZ2dpbmcKCiMg4pSA4pSAIFBhdGhzIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgApCQVNFX0RJUiAgID0gb3MucGF0aC5kaXJuYW1lKG9zLnBhdGguZGlybmFtZShvcy5wYXRoLmFic3BhdGgoX19maWxlX18pKSkKREJfUEFUSCAgICA9IG9zLnBhdGguam9pbihCQVNFX0RJUiwgImRhdGEiLCAiYXR0ZW5kYW5jZS5kYiIpCkJBQ0tVUF9ESVIgPSBvcy5wYXRoLmpvaW4oQkFTRV9ESVIsICJkYXRhIiwgImJhY2t1cHMiKQpFWFBPUlRfRElSID0gb3MucGF0aC5qb2luKEJBU0VfRElSLCAiZXhwb3J0cyIpCgojIEVuc3VyZSByZXF1aXJlZCBkaXJlY3RvcmllcyBleGlzdApvcy5tYWtlZGlycyhvcy5wYXRoLmRpcm5hbWUoREJfUEFUSCksIGV4aXN0X29rPVRydWUpCm9zLm1ha2VkaXJzKEJBQ0tVUF9ESVIsIGV4aXN0X29rPVRydWUpCm9zLm1ha2VkaXJzKEVYUE9SVF9ESVIsIGV4aXN0X29rPVRydWUpCgojIOKUgOKUgCBMb2dnaW5nIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgApsb2dnaW5nLmJhc2ljQ29uZmlnKGxldmVsPWxvZ2dpbmcuSU5GTykKbG9nZ2VyID0gbG9nZ2luZy5nZXRMb2dnZXIoX19uYW1lX18pCgoKIyDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZAKIyAgRGF0YWJhc2VNYW5hZ2VyIENsYXNzCiMg4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQCmNsYXNzIERhdGFiYXNlTWFuYWdlcjoKICAgICIiIkNlbnRyYWwgZGF0YWJhc2UgbWFuYWdlciBmb3IgdGhlIGF0dGVuZGFuY2Ugc3lzdGVtLiIiIgoKICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkYl9wYXRoOiBzdHIgPSBEQl9QQVRIKToKICAgICAgICBzZWxmLmRiX3BhdGggPSBkYl9wYXRoCiAgICAgICAgc2VsZi5fY3JlYXRlX3RhYmxlcygpCiAgICAgICAgbG9nZ2VyLmluZm8oZiJEYXRhYmFzZSBjb25uZWN0ZWQ6IHtzZWxmLmRiX3BhdGh9IikKCiAgICAjIOKUgOKUgCBDb25uZWN0aW9uIGhlbHBlciDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIAKICAgIGRlZiBfZ2V0X2Nvbm5lY3Rpb24oc2VsZik6CiAgICAgICAgIiIiUmV0dXJuIGEgbmV3IFNRTGl0ZSBjb25uZWN0aW9uIHdpdGggcm93X2ZhY3RvcnkgZm9yIGRpY3QtbGlrZSByb3dzLiIiIgogICAgICAgIGNvbm4gPSBzcWxpdGUzLmNvbm5lY3Qoc2VsZi5kYl9wYXRoLCB0aW1lb3V0PTEwKQogICAgICAgIGNvbm4ucm93X2ZhY3RvcnkgPSBzcWxpdGUzLlJvdyAgICAgICAgICAjIHJvd3MgYWNjZXNzaWJsZSBhcyBkaWN0cwogICAgICAgIGNvbm4uZXhlY3V0ZSgiUFJBR01BIGpvdXJuYWxfbW9kZT1XQUwiKSAgIyBiZXR0ZXIgY29uY3VycmVuY3kKICAgICAgICBjb25uLmV4ZWN1dGUoIlBSQUdNQSBmb3JlaWduX2tleXM9T04iKSAgICMgZW5mb3JjZSBGSyBjb25zdHJhaW50cwogICAgICAgIHJldHVybiBjb25uCgogICAgIyDilIDilIAgVGFibGUgQ3JlYXRpb24g4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACiAgICBkZWYgX2NyZWF0ZV90YWJsZXMoc2VsZik6CiAgICAgICAgIiIiQ3JlYXRlIGFsbCBkYXRhYmFzZSB0YWJsZXMgaWYgdGhleSBkb24ndCBhbHJlYWR5IGV4aXN0LiIiIgogICAgICAgIHdpdGggc2VsZi5fZ2V0X2Nvbm5lY3Rpb24oKSBhcyBjb25uOgogICAgICAgICAgICBjdXJzb3IgPSBjb25uLmN1cnNvcigpCgogICAgICAgICAgICAjIOKUgOKUgCB1c2VycyB0YWJsZSDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIAKICAgICAgICAgICAgY3Vyc29yLmV4ZWN1dGUoIiIiCiAgICAgICAgICAgICAgICBDUkVBVEUgVEFCTEUgSUYgTk9UIEVYSVNUUyB1c2VycyAoCiAgICAgICAgICAgICAgICAgICAgaWQgICAgICAgICAgSU5URUdFUiBQUklNQVJZIEtFWSBBVVRPSU5DUkVNRU5ULAogICAgICAgICAgICAgICAgICAgIG5hbWUgICAgICAgIFRFWFQgICAgTk9UIE5VTEwsCiAgICAgICAgICAgICAgICAgICAgcm9sbF9udW1iZXIgVEVYVCAgICBVTklRVUUgTk9UIE5VTEwsCiAgICAgICAgICAgICAgICAgICAgZGVwYXJ0bWVudCAgVEVYVCAgICBOT1QgTlVMTCwKICAgICAgICAgICAgICAgICAgICBlbWFpbCAgICAgICBURVhULAogICAgICAgICAgICAgICAgICAgIHBob25lICAgICAgIFRFWFQsCiAgICAgICAgICAgICAgICAgICAgcGhvdG9fcGF0aCAgVEVYVCwKICAgICAgICAgICAgICAgICAgICByZWdpc3RlcmVkX2F0IFRFWFQgIERFRkFVTFQgKGRhdGV0aW1lKCdub3cnLCdsb2NhbHRpbWUnKSksCiAgICAgICAgICAgICAgICAgICAgaXNfYWN0aXZlICAgSU5URUdFUiBERUZBVUxUIDEKICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgIiIiKQoKICAgICAgICAgICAgIyDilIDilIAgYXR0ZW5kYW5jZSB0YWJsZSDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIAKICAgICAgICAgICAgY3Vyc29yLmV4ZWN1dGUoIiIiCiAgICAgICAgICAgICAgICBDUkVBVEUgVEFCTEUgSUYgTk9UIEVYSVNUUyBhdHRlbmRhbmNlICgKICAgICAgICAgICAgICAgICAgICBpZCAgICAgICAgICBJTlRFR0VSIFBSSU1BUlkgS0VZIEFVVE9JTkNSRU1FTlQsCiAgICAgICAgICAgICAgICAgICAgdXNlcl9pZCAgICAgSU5URUdFUiBOT1QgTlVMTCwKICAgICAgICAgICAgICAgICAgICBkYXRlICAgICAgICBURVhUICAgIE5PVCBOVUxMLAogICAgICAgICAgICAgICAgICAgIHRpbWUgICAgICAgIFRFWFQgICAgTk9UIE5VTEwsCiAgICAgICAgICAgICAgICAgICAgc3RhdHVzICAgICAgVEVYVCAgICBERUZBVUxUICdQcmVzZW50JywKICAgICAgICAgICAgICAgICAgICBtYXJrZWRfYnkgICBURVhUICAgIERFRkFVTFQgJ0ZhY2UgUmVjb2duaXRpb24nLAogICAgICAgICAgICAgICAgICAgIEZPUkVJR04gS0VZICh1c2VyX2lkKSBSRUZFUkVOQ0VTIHVzZXJzKGlkKSwKICAgICAgICAgICAgICAgICAgICBVTklRVUUodXNlcl9pZCwgZGF0ZSkgICAgICAgICAgIC0tIG9uZSBlbnRyeSBwZXIgcGVyc29uIHBlciBkYXkKICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgIiIiKQoKICAgICAgICAgICAgIyDilIDilIAgc2V0dGluZ3MgdGFibGUg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACiAgICAgICAgICAgIGN1cnNvci5leGVjdXRlKCIiIgogICAgICAgICAgICAgICAgQ1JFQVRFIFRBQkxFIElGIE5PVCBFWElTVFMgc2V0dGluZ3MgKAogICAgICAgICAgICAgICAgICAgIGtleSAgICAgICAgIFRFWFQgUFJJTUFSWSBLRVksCiAgICAgICAgICAgICAgICAgICAgdmFsdWUgICAgICAgVEVYVCBOT1QgTlVMTCwKICAgICAgICAgICAgICAgICAgICB1cGRhdGVkX2F0ICBURVhUIERFRkFVTFQgKGRhdGV0aW1lKCdub3cnLCdsb2NhbHRpbWUnKSkKICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgIiIiKQoKICAgICAgICAgICAgIyDilIDilIAgYXVkaXRfbG9nIHRhYmxlIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgAogICAgICAgICAgICBjdXJzb3IuZXhlY3V0ZSgiIiIKICAgICAgICAgICAgICAgIENSRUFURSBUQUJMRSBJRiBOT1QgRVhJU1RTIGF1ZGl0X2xvZyAoCiAgICAgICAgICAgICAgICAgICAgaWQgICAgICAgICAgSU5URUdFUiBQUklNQVJZIEtFWSBBVVRPSU5DUkVNRU5ULAogICAgICAgICAgICAgICAgICAgIGFjdGlvbiAgICAgIFRFWFQgICAgTk9UIE5VTEwsCiAgICAgICAgICAgICAgICAgICAgZGV0YWlscyAgICAgVEVYVCwKICAgICAgICAgICAgICAgICAgICB0aW1lc3RhbXAgICBURVhUICAgIERFRkFVTFQgKGRhdGV0aW1lKCdub3cnLCdsb2NhbHRpbWUnKSkKICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgIiIiKQoKICAgICAgICAgICAgY29ubi5jb21taXQoKQoKICAgICAgICAgICAgIyBJbnNlcnQgZGVmYXVsdCBzZXR0aW5ncwogICAgICAgICAgICBzZWxmLl9pbnNlcnRfZGVmYXVsdF9zZXR0aW5ncyhjdXJzb3IsIGNvbm4pCgogICAgZGVmIF9pbnNlcnRfZGVmYXVsdF9zZXR0aW5ncyhzZWxmLCBjdXJzb3IsIGNvbm4pOgogICAgICAgICIiIkluc2VydCBkZWZhdWx0IGFwcCBzZXR0aW5ncyBpZiB0aGV5IGRvbid0IGV4aXN0LiIiIgogICAgICAgIGRlZmF1bHRzID0gewogICAgICAgICAgICAidGhlbWUiOiAgICAgICAgICAgICAgImRhcmsiLAogICAgICAgICAgICAiY29uZmlkZW5jZV90aHJlc2hvbGQiOiAiMC41NSIsCiAgICAgICAgICAgICJjYW1lcmFfaW5kZXgiOiAgICAgICAiMCIsCiAgICAgICAgICAgICJhdXRvX2JhY2t1cCI6ICAgICAgICAidHJ1ZSIsCiAgICAgICAgICAgICJzb3VuZF9lbmFibGVkIjogICAgICAidHJ1ZSIsCiAgICAgICAgICAgICJiYWNrdXBfaW50ZXJ2YWxfZGF5cyI6ICI3IiwKICAgICAgICAgICAgImFkbWluX3Bhc3N3b3JkIjogICAgICJhZG1pbjEyMyIsCiAgICAgICAgfQogICAgICAgIGZvciBrZXksIHZhbHVlIGluIGRlZmF1bHRzLml0ZW1zKCk6CiAgICAgICAgICAgIGN1cnNvci5leGVjdXRlKAogICAgICAgICAgICAgICAgIklOU0VSVCBPUiBJR05PUkUgSU5UTyBzZXR0aW5ncyAoa2V5LCB2YWx1ZSkgVkFMVUVTICg/LCA/KSIsCiAgICAgICAgICAgICAgICAoa2V5LCB2YWx1ZSkKICAgICAgICAgICAgKQogICAgICAgIGNvbm4uY29tbWl0KCkKCiAgICAjIOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkAogICAgIyAgVVNFUiBPUEVSQVRJT05TCiAgICAjIOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkAoKICAgIGRlZiBhZGRfdXNlcihzZWxmLCBuYW1lOiBzdHIsIHJvbGxfbnVtYmVyOiBzdHIsIGRlcGFydG1lbnQ6IHN0ciwKICAgICAgICAgICAgICAgICBlbWFpbDogc3RyID0gIiIsIHBob25lOiBzdHIgPSAiIiwgcGhvdG9fcGF0aDogc3RyID0gIiIpIC0+IGludDoKICAgICAgICAiIiIKICAgICAgICBSZWdpc3RlciBhIG5ldyB1c2VyLgogICAgICAgIFJldHVybnMgdGhlIG5ldyB1c2VyJ3MgSUQsIG9yIC0xIG9uIGZhaWx1cmUuCiAgICAgICAgIiIiCiAgICAgICAgdHJ5OgogICAgICAgICAgICB3aXRoIHNlbGYuX2dldF9jb25uZWN0aW9uKCkgYXMgY29ubjoKICAgICAgICAgICAgICAgIGN1cnNvciA9IGNvbm4uY3Vyc29yKCkKICAgICAgICAgICAgICAgIGN1cnNvci5leGVjdXRlKCIiIgogICAgICAgICAgICAgICAgICAgIElOU0VSVCBJTlRPIHVzZXJzIChuYW1lLCByb2xsX251bWJlciwgZGVwYXJ0bWVudCwgZW1haWwsIHBob25lLCBwaG90b19wYXRoKQogICAgICAgICAgICAgICAgICAgIFZBTFVFUyAoPywgPywgPywgPywgPywgPykKICAgICAgICAgICAgICAgICIiIiwgKG5hbWUuc3RyaXAoKSwgcm9sbF9udW1iZXIuc3RyaXAoKSwgZGVwYXJ0bWVudC5zdHJpcCgpLAogICAgICAgICAgICAgICAgICAgICAgZW1haWwuc3RyaXAoKSwgcGhvbmUuc3RyaXAoKSwgcGhvdG9fcGF0aCkpCiAgICAgICAgICAgICAgICBjb25uLmNvbW1pdCgpCiAgICAgICAgICAgICAgICB1aWQgPSBjdXJzb3IubGFzdHJvd2lkCiAgICAgICAgICAgICAgICBzZWxmLl9sb2dfYWN0aW9uKCJVU0VSX0FEREVEIiwgZiJOYW1lPXtuYW1lfSwgUm9sbD17cm9sbF9udW1iZXJ9LCBEZXB0PXtkZXBhcnRtZW50fSIpCiAgICAgICAgICAgICAgICBsb2dnZXIuaW5mbyhmIlVzZXIgYWRkZWQ6IHtuYW1lfSAoSUQ9e3VpZH0pIikKICAgICAgICAgICAgICAgIHJldHVybiB1aWQKICAgICAgICBleGNlcHQgc3FsaXRlMy5JbnRlZ3JpdHlFcnJvcjoKICAgICAgICAgICAgbG9nZ2VyLndhcm5pbmcoZiJVc2VyIHdpdGggcm9sbCBudW1iZXIgJ3tyb2xsX251bWJlcn0nIGFscmVhZHkgZXhpc3RzLiIpCiAgICAgICAgICAgIHJldHVybiAtMQogICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICAgICAgbG9nZ2VyLmVycm9yKGYiRXJyb3IgYWRkaW5nIHVzZXI6IHtlfSIpCiAgICAgICAgICAgIHJldHVybiAtMQoKICAgIGRlZiBnZXRfYWxsX3VzZXJzKHNlbGYsIGFjdGl2ZV9vbmx5OiBib29sID0gVHJ1ZSkgLT4gbGlzdDoKICAgICAgICAiIiJSZXR1cm4gYSBsaXN0IG9mIGFsbCB1c2VycyAoZGljdHMpLiIiIgogICAgICAgIHdpdGggc2VsZi5fZ2V0X2Nvbm5lY3Rpb24oKSBhcyBjb25uOgogICAgICAgICAgICBxdWVyeSA9ICJTRUxFQ1QgKiBGUk9NIHVzZXJzIgogICAgICAgICAgICBpZiBhY3RpdmVfb25seToKICAgICAgICAgICAgICAgIHF1ZXJ5ICs9ICIgV0hFUkUgaXNfYWN0aXZlID0gMSIKICAgICAgICAgICAgcXVlcnkgKz0gIiBPUkRFUiBCWSBuYW1lIgogICAgICAgICAgICByb3dzID0gY29ubi5leGVjdXRlKHF1ZXJ5KS5mZXRjaGFsbCgpCiAgICAgICAgICAgIHJldHVybiBbZGljdChyKSBmb3IgciBpbiByb3dzXQoKICAgIGRlZiBnZXRfdXNlcl9ieV9pZChzZWxmLCB1c2VyX2lkOiBpbnQpIC0+IGRpY3QgfCBOb25lOgogICAgICAgICIiIlJldHVybiBhIHNpbmdsZSB1c2VyIGRpY3QsIG9yIE5vbmUgaWYgbm90IGZvdW5kLiIiIgogICAgICAgIHdpdGggc2VsZi5fZ2V0X2Nvbm5lY3Rpb24oKSBhcyBjb25uOgogICAgICAgICAgICByb3cgPSBjb25uLmV4ZWN1dGUoCiAgICAgICAgICAgICAgICAiU0VMRUNUICogRlJPTSB1c2VycyBXSEVSRSBpZCA9ID8iLCAodXNlcl9pZCwpCiAgICAgICAgICAgICkuZmV0Y2hvbmUoKQogICAgICAgICAgICByZXR1cm4gZGljdChyb3cpIGlmIHJvdyBlbHNlIE5vbmUKCiAgICBkZWYgZ2V0X3VzZXJfYnlfcm9sbChzZWxmLCByb2xsX251bWJlcjogc3RyKSAtPiBkaWN0IHwgTm9uZToKICAgICAgICAiIiJSZXR1cm4gdXNlciBieSByb2xsIG51bWJlci4iIiIKICAgICAgICB3aXRoIHNlbGYuX2dldF9jb25uZWN0aW9uKCkgYXMgY29ubjoKICAgICAgICAgICAgcm93ID0gY29ubi5leGVjdXRlKAogICAgICAgICAgICAgICAgIlNFTEVDVCAqIEZST00gdXNlcnMgV0hFUkUgcm9sbF9udW1iZXIgPSA/IiwgKHJvbGxfbnVtYmVyLCkKICAgICAgICAgICAgKS5mZXRjaG9uZSgpCiAgICAgICAgICAgIHJldHVybiBkaWN0KHJvdykgaWYgcm93IGVsc2UgTm9uZQoKICAgIGRlZiB1cGRhdGVfdXNlcihzZWxmLCB1c2VyX2lkOiBpbnQsICoqa3dhcmdzKSAtPiBib29sOgogICAgICAgICIiIlVwZGF0ZSB1c2VyIGZpZWxkcy4gUGFzcyBrZXl3b3JkIGFyZ3VtZW50cyBtYXRjaGluZyBjb2x1bW4gbmFtZXMuIiIiCiAgICAgICAgYWxsb3dlZCA9IHsibmFtZSIsICJkZXBhcnRtZW50IiwgImVtYWlsIiwgInBob25lIiwgInBob3RvX3BhdGgiLCAiaXNfYWN0aXZlIn0KICAgICAgICBmaWVsZHMgID0ge2s6IHYgZm9yIGssIHYgaW4ga3dhcmdzLml0ZW1zKCkgaWYgayBpbiBhbGxvd2VkfQogICAgICAgIGlmIG5vdCBmaWVsZHM6CiAgICAgICAgICAgIHJldHVybiBGYWxzZQogICAgICAgIHNldF9jbGF1c2UgPSAiLCAiLmpvaW4oZiJ7a30gPSA/IiBmb3IgayBpbiBmaWVsZHMpCiAgICAgICAgdmFsdWVzICAgICA9IGxpc3QoZmllbGRzLnZhbHVlcygpKSArIFt1c2VyX2lkXQogICAgICAgIHRyeToKICAgICAgICAgICAgd2l0aCBzZWxmLl9nZXRfY29ubmVjdGlvbigpIGFzIGNvbm46CiAgICAgICAgICAgICAgICBjb25uLmV4ZWN1dGUoZiJVUERBVEUgdXNlcnMgU0VUIHtzZXRfY2xhdXNlfSBXSEVSRSBpZCA9ID8iLCB2YWx1ZXMpCiAgICAgICAgICAgICAgICBjb25uLmNvbW1pdCgpCiAgICAgICAgICAgIHJldHVybiBUcnVlCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgICAgICBsb2dnZXIuZXJyb3IoZiJFcnJvciB1cGRhdGluZyB1c2VyIHt1c2VyX2lkfToge2V9IikKICAgICAgICAgICAgcmV0dXJuIEZhbHNlCgogICAgZGVmIGRlbGV0ZV91c2VyKHNlbGYsIHVzZXJfaWQ6IGludCkgLT4gYm9vbDoKICAgICAgICAiIiJTb2Z0LWRlbGV0ZSBhIHVzZXIgKG1hcmsgaW5hY3RpdmUpLiIiIgogICAgICAgIHJldHVybiBzZWxmLnVwZGF0ZV91c2VyKHVzZXJfaWQsIGlzX2FjdGl2ZT0wKQoKICAgIGRlZiBnZXRfdG90YWxfdXNlcnMoc2VsZikgLT4gaW50OgogICAgICAgIHdpdGggc2VsZi5fZ2V0X2Nvbm5lY3Rpb24oKSBhcyBjb25uOgogICAgICAgICAgICByZXR1cm4gY29ubi5leGVjdXRlKAogICAgICAgICAgICAgICAgIlNFTEVDVCBDT1VOVCgqKSBGUk9NIHVzZXJzIFdIRVJFIGlzX2FjdGl2ZSA9IDEiCiAgICAgICAgICAgICkuZmV0Y2hvbmUoKVswXQoKICAgICMg4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQCiAgICAjICBBVFRFTkRBTkNFIE9QRVJBVElPTlMKICAgICMg4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQCgogICAgZGVmIG1hcmtfYXR0ZW5kYW5jZShzZWxmLCB1c2VyX2lkOiBpbnQsIHN0YXR1czogc3RyID0gIlByZXNlbnQiKSAtPiBkaWN0OgogICAgICAgICIiIgogICAgICAgIE1hcmsgYXR0ZW5kYW5jZSBmb3IgYSB1c2VyIGZvciB0b2RheS4KICAgICAgICBSZXR1cm5zOiB7InN1Y2Nlc3MiOiBib29sLCAibWVzc2FnZSI6IHN0ciwgImFscmVhZHlfbWFya2VkIjogYm9vbH0KICAgICAgICAiIiIKICAgICAgICB0b2RheSAgICAgPSBkYXRlLnRvZGF5KCkuc3RyZnRpbWUoIiVZLSVtLSVkIikKICAgICAgICBub3dfdGltZSAgPSBkYXRldGltZS5ub3coKS5zdHJmdGltZSgiJUg6JU06JVMiKQogICAgICAgIHRyeToKICAgICAgICAgICAgd2l0aCBzZWxmLl9nZXRfY29ubmVjdGlvbigpIGFzIGNvbm46CiAgICAgICAgICAgICAgICBjb25uLmV4ZWN1dGUoIiIiCiAgICAgICAgICAgICAgICAgICAgSU5TRVJUIElOVE8gYXR0ZW5kYW5jZSAodXNlcl9pZCwgZGF0ZSwgdGltZSwgc3RhdHVzKQogICAgICAgICAgICAgICAgICAgIFZBTFVFUyAoPywgPywgPywgPykKICAgICAgICAgICAgICAgICIiIiwgKHVzZXJfaWQsIHRvZGF5LCBub3dfdGltZSwgc3RhdHVzKSkKICAgICAgICAgICAgICAgIGNvbm4uY29tbWl0KCkKICAgICAgICAgICAgICAgIHNlbGYuX2xvZ19hY3Rpb24oIkFUVEVOREFOQ0VfTUFSS0VEIiwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZiJVc2VySUQ9e3VzZXJfaWR9LCBEYXRlPXt0b2RheX0sIFRpbWU9e25vd190aW1lfSIpCiAgICAgICAgICAgICAgICByZXR1cm4geyJzdWNjZXNzIjogVHJ1ZSwgIm1lc3NhZ2UiOiAiQXR0ZW5kYW5jZSBtYXJrZWQgc3VjY2Vzc2Z1bGx5ISIsCiAgICAgICAgICAgICAgICAgICAgICAgICJhbHJlYWR5X21hcmtlZCI6IEZhbHNlfQogICAgICAgIGV4Y2VwdCBzcWxpdGUzLkludGVncml0eUVycm9yOgogICAgICAgICAgICAjIFVOSVFVRSBjb25zdHJhaW50OiBhbHJlYWR5IG1hcmtlZCB0b2RheQogICAgICAgICAgICByZXR1cm4geyJzdWNjZXNzIjogRmFsc2UsCiAgICAgICAgICAgICAgICAgICAgIm1lc3NhZ2UiOiAiQXR0ZW5kYW5jZSBhbHJlYWR5IG1hcmtlZCBmb3IgdG9kYXkuIiwKICAgICAgICAgICAgICAgICAgICAiYWxyZWFkeV9tYXJrZWQiOiBUcnVlfQogICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICAgICAgbG9nZ2VyLmVycm9yKGYiRXJyb3IgbWFya2luZyBhdHRlbmRhbmNlOiB7ZX0iKQogICAgICAgICAgICByZXR1cm4geyJzdWNjZXNzIjogRmFsc2UsICJtZXNzYWdlIjogc3RyKGUpLCAiYWxyZWFkeV9tYXJrZWQiOiBGYWxzZX0KCiAgICBkZWYgaXNfYXR0ZW5kYW5jZV9tYXJrZWRfdG9kYXkoc2VsZiwgdXNlcl9pZDogaW50KSAtPiBib29sOgogICAgICAgICIiIkNoZWNrIGlmIGF0dGVuZGFuY2UgaXMgYWxyZWFkeSBtYXJrZWQgZm9yIHRvZGF5LiIiIgogICAgICAgIHRvZGF5ID0gZGF0ZS50b2RheSgpLnN0cmZ0aW1lKCIlWS0lbS0lZCIpCiAgICAgICAgd2l0aCBzZWxmLl9nZXRfY29ubmVjdGlvbigpIGFzIGNvbm46CiAgICAgICAgICAgIHJvdyA9IGNvbm4uZXhlY3V0ZSgKICAgICAgICAgICAgICAgICJTRUxFQ1QgaWQgRlJPTSBhdHRlbmRhbmNlIFdIRVJFIHVzZXJfaWQgPSA/IEFORCBkYXRlID0gPyIsCiAgICAgICAgICAgICAgICAodXNlcl9pZCwgdG9kYXkpCiAgICAgICAgICAgICkuZmV0Y2hvbmUoKQogICAgICAgICAgICByZXR1cm4gcm93IGlzIG5vdCBOb25lCgogICAgZGVmIGdldF9hdHRlbmRhbmNlX3JlY29yZHMoc2VsZiwgc3RhcnRfZGF0ZTogc3RyID0gTm9uZSwgZW5kX2RhdGU6IHN0ciA9IE5vbmUsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB1c2VyX2lkOiBpbnQgPSBOb25lLCBkZXBhcnRtZW50OiBzdHIgPSBOb25lKSAtPiBsaXN0OgogICAgICAgICIiIgogICAgICAgIEZldGNoIGF0dGVuZGFuY2UgcmVjb3JkcyB3aXRoIG9wdGlvbmFsIGZpbHRlcnMuCiAgICAgICAgUmV0dXJucyBsaXN0IG9mIGRpY3RzIHdpdGggdXNlciBpbmZvIGpvaW5lZC4KICAgICAgICAiIiIKICAgICAgICBxdWVyeSA9ICIiIgogICAgICAgICAgICBTRUxFQ1QgYS5pZCwgYS51c2VyX2lkLCB1Lm5hbWUsIHUucm9sbF9udW1iZXIsIHUuZGVwYXJ0bWVudCwKICAgICAgICAgICAgICAgICAgIGEuZGF0ZSwgYS50aW1lLCBhLnN0YXR1cywgYS5tYXJrZWRfYnkKICAgICAgICAgICAgRlJPTSBhdHRlbmRhbmNlIGEKICAgICAgICAgICAgSk9JTiB1c2VycyB1IE9OIGEudXNlcl9pZCA9IHUuaWQKICAgICAgICAgICAgV0hFUkUgMT0xCiAgICAgICAgIiIiCiAgICAgICAgcGFyYW1zID0gW10KICAgICAgICBpZiBzdGFydF9kYXRlOgogICAgICAgICAgICBxdWVyeSArPSAiIEFORCBhLmRhdGUgPj0gPyIKICAgICAgICAgICAgcGFyYW1zLmFwcGVuZChzdGFydF9kYXRlKQogICAgICAgIGlmIGVuZF9kYXRlOgogICAgICAgICAgICBxdWVyeSArPSAiIEFORCBhLmRhdGUgPD0gPyIKICAgICAgICAgICAgcGFyYW1zLmFwcGVuZChlbmRfZGF0ZSkKICAgICAgICBpZiB1c2VyX2lkOgogICAgICAgICAgICBxdWVyeSArPSAiIEFORCBhLnVzZXJfaWQgPSA/IgogICAgICAgICAgICBwYXJhbXMuYXBwZW5kKHVzZXJfaWQpCiAgICAgICAgaWYgZGVwYXJ0bWVudDoKICAgICAgICAgICAgcXVlcnkgKz0gIiBBTkQgdS5kZXBhcnRtZW50ID0gPyIKICAgICAgICAgICAgcGFyYW1zLmFwcGVuZChkZXBhcnRtZW50KQogICAgICAgIHF1ZXJ5ICs9ICIgT1JERVIgQlkgYS5kYXRlIERFU0MsIGEudGltZSBERVNDIgoKICAgICAgICB3aXRoIHNlbGYuX2dldF9jb25uZWN0aW9uKCkgYXMgY29ubjoKICAgICAgICAgICAgcm93cyA9IGNvbm4uZXhlY3V0ZShxdWVyeSwgcGFyYW1zKS5mZXRjaGFsbCgpCiAgICAgICAgICAgIHJldHVybiBbZGljdChyKSBmb3IgciBpbiByb3dzXQoKICAgIGRlZiBnZXRfdG9kYXlfYXR0ZW5kYW5jZShzZWxmKSAtPiBsaXN0OgogICAgICAgICIiIlJldHVybiB0b2RheSdzIGF0dGVuZGFuY2UgcmVjb3Jkcy4iIiIKICAgICAgICB0b2RheSA9IGRhdGUudG9kYXkoKS5zdHJmdGltZSgiJVktJW0tJWQiKQogICAgICAgIHJldHVybiBzZWxmLmdldF9hdHRlbmRhbmNlX3JlY29yZHMoc3RhcnRfZGF0ZT10b2RheSwgZW5kX2RhdGU9dG9kYXkpCgogICAgZGVmIGdldF90b2RheV9jb3VudChzZWxmKSAtPiBpbnQ6CiAgICAgICAgIiIiUmV0dXJuIGNvdW50IG9mIHN0dWRlbnRzIG1hcmtlZCBwcmVzZW50IHRvZGF5LiIiIgogICAgICAgIHJldHVybiBsZW4oc2VsZi5nZXRfdG9kYXlfYXR0ZW5kYW5jZSgpKQoKICAgIGRlZiBnZXRfYXR0ZW5kYW5jZV9wZXJjZW50YWdlKHNlbGYsIHVzZXJfaWQ6IGludCA9IE5vbmUsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBkYXlzOiBpbnQgPSAzMCkgLT4gZmxvYXQ6CiAgICAgICAgIiIiCiAgICAgICAgQ2FsY3VsYXRlIGF0dGVuZGFuY2UgcGVyY2VudGFnZSBvdmVyIHRoZSBsYXN0IE4gZGF5cy4KICAgICAgICBJZiB1c2VyX2lkIGlzIGdpdmVuLCBjYWxjdWxhdGVzIGZvciB0aGF0IHVzZXI7IG90aGVyd2lzZSBvdmVyYWxsLgogICAgICAgICIiIgogICAgICAgIHN0YXJ0ID0gKGRhdGUudG9kYXkoKSAtIHRpbWVkZWx0YShkYXlzPWRheXMpKS5zdHJmdGltZSgiJVktJW0tJWQiKQogICAgICAgIGVuZCAgID0gZGF0ZS50b2RheSgpLnN0cmZ0aW1lKCIlWS0lbS0lZCIpCiAgICAgICAgcmVjb3JkcyA9IHNlbGYuZ2V0X2F0dGVuZGFuY2VfcmVjb3JkcyhzdGFydF9kYXRlPXN0YXJ0LCBlbmRfZGF0ZT1lbmQsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB1c2VyX2lkPXVzZXJfaWQpCiAgICAgICAgaWYgbm90IHJlY29yZHM6CiAgICAgICAgICAgIHJldHVybiAwLjAKICAgICAgICBpZiB1c2VyX2lkOgogICAgICAgICAgICByZXR1cm4gbWluKDEwMC4wLCByb3VuZChsZW4ocmVjb3JkcykgLyBkYXlzICogMTAwLCAxKSkKICAgICAgICAjIE92ZXJhbGw6IHVuaXF1ZSBkYXlzIC8gdG90YWxfZGF5cwogICAgICAgIHVuaXF1ZV9kYXlzID0gbGVuKHNldChyWyJkYXRlIl0gZm9yIHIgaW4gcmVjb3JkcykpCiAgICAgICAgcmV0dXJuIHJvdW5kKHVuaXF1ZV9kYXlzIC8gZGF5cyAqIDEwMCwgMSkKCiAgICBkZWYgZ2V0X2F0dGVuZGFuY2VfdHJlbmQoc2VsZiwgZGF5czogaW50ID0gNykgLT4gbGlzdDoKICAgICAgICAiIiJSZXR1cm4gZGFpbHkgYXR0ZW5kYW5jZSBjb3VudHMgZm9yIHRoZSBsYXN0IE4gZGF5cyAoZm9yIGNoYXJ0cykuIiIiCiAgICAgICAgcmVzdWx0ID0gW10KICAgICAgICBmb3IgaSBpbiByYW5nZShkYXlzIC0gMSwgLTEsIC0xKToKICAgICAgICAgICAgZCA9IChkYXRlLnRvZGF5KCkgLSB0aW1lZGVsdGEoZGF5cz1pKSkuc3RyZnRpbWUoIiVZLSVtLSVkIikKICAgICAgICAgICAgY291bnQgPSBsZW4oc2VsZi5nZXRfYXR0ZW5kYW5jZV9yZWNvcmRzKHN0YXJ0X2RhdGU9ZCwgZW5kX2RhdGU9ZCkpCiAgICAgICAgICAgIHJlc3VsdC5hcHBlbmQoeyJkYXRlIjogZCwgImNvdW50IjogY291bnR9KQogICAgICAgIHJldHVybiByZXN1bHQKCiAgICAjIOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkAogICAgIyAgRVhQT1JUIE9QRVJBVElPTlMKICAgICMg4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQCgogICAgZGVmIGV4cG9ydF90b19jc3Yoc2VsZiwgcmVjb3JkczogbGlzdCA9IE5vbmUsIGZpbGVuYW1lOiBzdHIgPSBOb25lKSAtPiBzdHI6CiAgICAgICAgIiIiRXhwb3J0IGF0dGVuZGFuY2UgcmVjb3JkcyB0byBDU1YuIFJldHVybnMgZmlsZSBwYXRoLiIiIgogICAgICAgIGlmIHJlY29yZHMgaXMgTm9uZToKICAgICAgICAgICAgcmVjb3JkcyA9IHNlbGYuZ2V0X2F0dGVuZGFuY2VfcmVjb3JkcygpCiAgICAgICAgaWYgbm90IHJlY29yZHM6CiAgICAgICAgICAgIHJldHVybiAiIgogICAgICAgIGRmID0gcGQuRGF0YUZyYW1lKHJlY29yZHMpCiAgICAgICAgaWYgZmlsZW5hbWUgaXMgTm9uZToKICAgICAgICAgICAgZmlsZW5hbWUgPSBmImF0dGVuZGFuY2Vfe2RhdGV0aW1lLm5vdygpLnN0cmZ0aW1lKCclWSVtJWRfJUglTSVTJyl9LmNzdiIKICAgICAgICBwYXRoID0gb3MucGF0aC5qb2luKEVYUE9SVF9ESVIsIGZpbGVuYW1lKQogICAgICAgIGRmLnRvX2NzdihwYXRoLCBpbmRleD1GYWxzZSkKICAgICAgICBsb2dnZXIuaW5mbyhmIkV4cG9ydGVkIENTVjoge3BhdGh9IikKICAgICAgICByZXR1cm4gcGF0aAoKICAgIGRlZiBleHBvcnRfdG9fZXhjZWwoc2VsZiwgcmVjb3JkczogbGlzdCA9IE5vbmUsIGZpbGVuYW1lOiBzdHIgPSBOb25lKSAtPiBzdHI6CiAgICAgICAgIiIiRXhwb3J0IGF0dGVuZGFuY2UgcmVjb3JkcyB0byBFeGNlbC4gUmV0dXJucyBmaWxlIHBhdGguIiIiCiAgICAgICAgaWYgcmVjb3JkcyBpcyBOb25lOgogICAgICAgICAgICByZWNvcmRzID0gc2VsZi5nZXRfYXR0ZW5kYW5jZV9yZWNvcmRzKCkKICAgICAgICBpZiBub3QgcmVjb3JkczoKICAgICAgICAgICAgcmV0dXJuICIiCiAgICAgICAgZGYgPSBwZC5EYXRhRnJhbWUocmVjb3JkcykKICAgICAgICBpZiBmaWxlbmFtZSBpcyBOb25lOgogICAgICAgICAgICBmaWxlbmFtZSA9IGYiYXR0ZW5kYW5jZV97ZGF0ZXRpbWUubm93KCkuc3RyZnRpbWUoJyVZJW0lZF8lSCVNJVMnKX0ueGxzeCIKICAgICAgICBwYXRoID0gb3MucGF0aC5qb2luKEVYUE9SVF9ESVIsIGZpbGVuYW1lKQogICAgICAgIHdpdGggcGQuRXhjZWxXcml0ZXIocGF0aCwgZW5naW5lPSJvcGVucHl4bCIpIGFzIHdyaXRlcjoKICAgICAgICAgICAgZGYudG9fZXhjZWwod3JpdGVyLCBzaGVldF9uYW1lPSJBdHRlbmRhbmNlIiwgaW5kZXg9RmFsc2UpCiAgICAgICAgICAgICMgQXV0by1zaXplIGNvbHVtbnMKICAgICAgICAgICAgd29ya3NoZWV0ID0gd3JpdGVyLnNoZWV0c1siQXR0ZW5kYW5jZSJdCiAgICAgICAgICAgIGZvciBjb2wgaW4gd29ya3NoZWV0LmNvbHVtbnM6CiAgICAgICAgICAgICAgICBtYXhfbGVuID0gbWF4KGxlbihzdHIoY2VsbC52YWx1ZSBvciAiIikpIGZvciBjZWxsIGluIGNvbCkgKyAyCiAgICAgICAgICAgICAgICB3b3Jrc2hlZXQuY29sdW1uX2RpbWVuc2lvbnNbY29sWzBdLmNvbHVtbl9sZXR0ZXJdLndpZHRoID0gbWF4X2xlbgogICAgICAgIGxvZ2dlci5pbmZvKGYiRXhwb3J0ZWQgRXhjZWw6IHtwYXRofSIpCiAgICAgICAgcmV0dXJuIHBhdGgKCiAgICAjIOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkAogICAgIyAgU0VUVElOR1MgT1BFUkFUSU9OUwogICAgIyDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZAKCiAgICBkZWYgZ2V0X3NldHRpbmcoc2VsZiwga2V5OiBzdHIsIGRlZmF1bHQ6IHN0ciA9ICIiKSAtPiBzdHI6CiAgICAgICAgIiIiUmV0cmlldmUgYSBzZXR0aW5nIHZhbHVlIGJ5IGtleS4iIiIKICAgICAgICB3aXRoIHNlbGYuX2dldF9jb25uZWN0aW9uKCkgYXMgY29ubjoKICAgICAgICAgICAgcm93ID0gY29ubi5leGVjdXRlKAogICAgICAgICAgICAgICAgIlNFTEVDVCB2YWx1ZSBGUk9NIHNldHRpbmdzIFdIRVJFIGtleSA9ID8iLCAoa2V5LCkKICAgICAgICAgICAgKS5mZXRjaG9uZSgpCiAgICAgICAgICAgIHJldHVybiByb3dbMF0gaWYgcm93IGVsc2UgZGVmYXVsdAoKICAgIGRlZiBzZXRfc2V0dGluZyhzZWxmLCBrZXk6IHN0ciwgdmFsdWU6IHN0cik6CiAgICAgICAgIiIiSW5zZXJ0IG9yIHVwZGF0ZSBhIHNldHRpbmcuIiIiCiAgICAgICAgd2l0aCBzZWxmLl9nZXRfY29ubmVjdGlvbigpIGFzIGNvbm46CiAgICAgICAgICAgIGNvbm4uZXhlY3V0ZSgiIiIKICAgICAgICAgICAgICAgIElOU0VSVCBJTlRPIHNldHRpbmdzIChrZXksIHZhbHVlLCB1cGRhdGVkX2F0KQogICAgICAgICAgICAgICAgVkFMVUVTICg/LCA/LCBkYXRldGltZSgnbm93JywnbG9jYWx0aW1lJykpCiAgICAgICAgICAgICAgICBPTiBDT05GTElDVChrZXkpIERPIFVQREFURSBTRVQKICAgICAgICAgICAgICAgICAgICB2YWx1ZSA9IGV4Y2x1ZGVkLnZhbHVlLAogICAgICAgICAgICAgICAgICAgIHVwZGF0ZWRfYXQgPSBleGNsdWRlZC51cGRhdGVkX2F0CiAgICAgICAgICAgICIiIiwgKGtleSwgdmFsdWUpKQogICAgICAgICAgICBjb25uLmNvbW1pdCgpCgogICAgZGVmIGdldF9hbGxfc2V0dGluZ3Moc2VsZikgLT4gZGljdDoKICAgICAgICAiIiJSZXR1cm4gYWxsIHNldHRpbmdzIGFzIGEgZGljdC4iIiIKICAgICAgICB3aXRoIHNlbGYuX2dldF9jb25uZWN0aW9uKCkgYXMgY29ubjoKICAgICAgICAgICAgcm93cyA9IGNvbm4uZXhlY3V0ZSgiU0VMRUNUIGtleSwgdmFsdWUgRlJPTSBzZXR0aW5ncyIpLmZldGNoYWxsKCkKICAgICAgICAgICAgcmV0dXJuIHtyWzBdOiByWzFdIGZvciByIGluIHJvd3N9CgogICAgIyDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZAKICAgICMgIEJBQ0tVUCBPUEVSQVRJT05TCiAgICAjIOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkAoKICAgIGRlZiBiYWNrdXBfZGF0YWJhc2Uoc2VsZikgLT4gc3RyOgogICAgICAgICIiIkNyZWF0ZSBhIHRpbWVzdGFtcGVkIGJhY2t1cCBvZiB0aGUgZGF0YWJhc2UuIFJldHVybnMgYmFja3VwIHBhdGguIiIiCiAgICAgICAgdGltZXN0YW1wID0gZGF0ZXRpbWUubm93KCkuc3RyZnRpbWUoIiVZJW0lZF8lSCVNJVMiKQogICAgICAgIGJhY2t1cF9wYXRoID0gb3MucGF0aC5qb2luKEJBQ0tVUF9ESVIsIGYiYXR0ZW5kYW5jZV9iYWNrdXBfe3RpbWVzdGFtcH0uZGIiKQogICAgICAgIHNodXRpbC5jb3B5MihzZWxmLmRiX3BhdGgsIGJhY2t1cF9wYXRoKQogICAgICAgIHNlbGYuX2xvZ19hY3Rpb24oIkJBQ0tVUF9DUkVBVEVEIiwgZiJQYXRoPXtiYWNrdXBfcGF0aH0iKQogICAgICAgIGxvZ2dlci5pbmZvKGYiRGF0YWJhc2UgYmFja2VkIHVwOiB7YmFja3VwX3BhdGh9IikKICAgICAgICByZXR1cm4gYmFja3VwX3BhdGgKCiAgICBkZWYgZ2V0X2RlcGFydG1lbnRzKHNlbGYpIC0+IGxpc3Q6CiAgICAgICAgIiIiUmV0dXJuIGxpc3Qgb2YgdW5pcXVlIGRlcGFydG1lbnRzLiIiIgogICAgICAgIHdpdGggc2VsZi5fZ2V0X2Nvbm5lY3Rpb24oKSBhcyBjb25uOgogICAgICAgICAgICByb3dzID0gY29ubi5leGVjdXRlKAogICAgICAgICAgICAgICAgIlNFTEVDVCBESVNUSU5DVCBkZXBhcnRtZW50IEZST00gdXNlcnMgV0hFUkUgaXNfYWN0aXZlPTEgT1JERVIgQlkgZGVwYXJ0bWVudCIKICAgICAgICAgICAgKS5mZXRjaGFsbCgpCiAgICAgICAgICAgIHJldHVybiBbclswXSBmb3IgciBpbiByb3dzXQoKICAgICMg4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQCiAgICAjICBBVURJVCBMT0cKICAgICMg4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQCgogICAgZGVmIF9sb2dfYWN0aW9uKHNlbGYsIGFjdGlvbjogc3RyLCBkZXRhaWxzOiBzdHIgPSAiIik6CiAgICAgICAgIiIiV3JpdGUgdG8gYXVkaXQgbG9nLiIiIgogICAgICAgIHRyeToKICAgICAgICAgICAgd2l0aCBzZWxmLl9nZXRfY29ubmVjdGlvbigpIGFzIGNvbm46CiAgICAgICAgICAgICAgICBjb25uLmV4ZWN1dGUoCiAgICAgICAgICAgICAgICAgICAgIklOU0VSVCBJTlRPIGF1ZGl0X2xvZyAoYWN0aW9uLCBkZXRhaWxzKSBWQUxVRVMgKD8sID8pIiwKICAgICAgICAgICAgICAgICAgICAoYWN0aW9uLCBkZXRhaWxzKQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgY29ubi5jb21taXQoKQogICAgICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgICAgIHBhc3MgICMgQXVkaXQgbG9nIGZhaWx1cmVzIHNob3VsZCBub3QgY3Jhc2ggdGhlIGFwcAoKICAgIGRlZiBnZXRfYXVkaXRfbG9nKHNlbGYsIGxpbWl0OiBpbnQgPSAxMDApIC0+IGxpc3Q6CiAgICAgICAgIiIiUmV0dXJuIHJlY2VudCBhdWRpdCBsb2cgZW50cmllcy4iIiIKICAgICAgICB3aXRoIHNlbGYuX2dldF9jb25uZWN0aW9uKCkgYXMgY29ubjoKICAgICAgICAgICAgcm93cyA9IGNvbm4uZXhlY3V0ZSgKICAgICAgICAgICAgICAgICJTRUxFQ1QgKiBGUk9NIGF1ZGl0X2xvZyBPUkRFUiBCWSB0aW1lc3RhbXAgREVTQyBMSU1JVCA/IiwKICAgICAgICAgICAgICAgIChsaW1pdCwpCiAgICAgICAgICAgICkuZmV0Y2hhbGwoKQogICAgICAgICAgICByZXR1cm4gW2RpY3QocikgZm9yIHIgaW4gcm93c10KCgojIOKUgOKUgCBTaW5nbGV0b24gaW5zdGFuY2UgKGltcG9ydCBhbmQgdXNlIGRpcmVjdGx5KSDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIAKZGIgPSBEYXRhYmFzZU1hbmFnZXIoKQo=', 'database/__init__.py': 'IyBEYXRhYmFzZSBwYWNrYWdlCg==', 'utils/__init__.py': 'IyBVdGlsaXRpZXMgcGFja2FnZQo=', 'utils/helpers.py': 'IiIiCuKVlOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVlwrilZEgICAgICAgICAgICAgVVRJTElUSUVTIOKAlCBGYWNlIEF0dGVuZGFuY2UgU3lzdGVtICAgICAgICAgICAgICDilZEK4pWRICBTaGFyZWQgaGVscGVyczogc291bmQsIHRoZW1lLCB0aW1lLCBub3RpZmljYXRpb25zLCBjYW1lcmEgIOKVkQrilZrilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZ0KIiIiCgppbXBvcnQgb3MKaW1wb3J0IHN5cwppbXBvcnQgdGhyZWFkaW5nCmltcG9ydCBwbGF0Zm9ybQppbXBvcnQgbG9nZ2luZwpmcm9tIGRhdGV0aW1lIGltcG9ydCBkYXRldGltZQoKbG9nZ2VyID0gbG9nZ2luZy5nZXRMb2dnZXIoX19uYW1lX18pCgpCQVNFX0RJUiA9IG9zLnBhdGguZGlybmFtZShvcy5wYXRoLmRpcm5hbWUob3MucGF0aC5hYnNwYXRoKF9fZmlsZV9fKSkpCgoKIyDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZAKIyAgU09VTkQgTUFOQUdFUgojIOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkApjbGFzcyBTb3VuZE1hbmFnZXI6CiAgICAiIiIKICAgIFBsYXkgc291bmQgZWZmZWN0cyB1c2luZyBweWdhbWUubWl4ZXIuCiAgICBGYWxscyBiYWNrIHNpbGVudGx5IGlmIHB5Z2FtZSBpcyB1bmF2YWlsYWJsZS4KICAgICIiIgoKICAgIGRlZiBfX2luaXRfXyhzZWxmKToKICAgICAgICBzZWxmLl9hdmFpbGFibGUgPSBGYWxzZQogICAgICAgIHRyeToKICAgICAgICAgICAgaW1wb3J0IHB5Z2FtZQogICAgICAgICAgICBweWdhbWUubWl4ZXIuaW5pdChmcmVxdWVuY3k9NDQxMDAsIHNpemU9LTE2LCBjaGFubmVscz0yLCBidWZmZXI9NTEyKQogICAgICAgICAgICBzZWxmLl9weWdhbWUgPSBweWdhbWUKICAgICAgICAgICAgc2VsZi5fYXZhaWxhYmxlID0gVHJ1ZQogICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICAgICAgbG9nZ2VyLndhcm5pbmcoZiJTb3VuZCB1bmF2YWlsYWJsZToge2V9IikKCiAgICBkZWYgcGxheV9zdWNjZXNzKHNlbGYpOgogICAgICAgICIiIlBsYXkgYSBzdWNjZXNzIHRvbmUgKGF0dGVuZGFuY2UgbWFya2VkKS4iIiIKICAgICAgICBzZWxmLl9iZWVwKGZyZXF1ZW5jeT04ODAsIGR1cmF0aW9uPTAuMTUpCgogICAgZGVmIHBsYXlfZXJyb3Ioc2VsZik6CiAgICAgICAgIiIiUGxheSBhbiBlcnJvciB0b25lIChhbHJlYWR5IG1hcmtlZCAvIHVua25vd24pLiIiIgogICAgICAgIHNlbGYuX2JlZXAoZnJlcXVlbmN5PTMwMCwgZHVyYXRpb249MC4yKQoKICAgIGRlZiBwbGF5X25vdGlmaWNhdGlvbihzZWxmKToKICAgICAgICAiIiJQbGF5IGEgc29mdCBub3RpZmljYXRpb24gc291bmQuIiIiCiAgICAgICAgc2VsZi5fYmVlcChmcmVxdWVuY3k9NjYwLCBkdXJhdGlvbj0wLjEpCgogICAgZGVmIF9iZWVwKHNlbGYsIGZyZXF1ZW5jeTogaW50LCBkdXJhdGlvbjogZmxvYXQpOgogICAgICAgICIiIkdlbmVyYXRlIGFuZCBwbGF5IGEgc2luZS13YXZlIGJlZXAgaW4gYSBiYWNrZ3JvdW5kIHRocmVhZC4iIiIKICAgICAgICBpZiBub3Qgc2VsZi5fYXZhaWxhYmxlOgogICAgICAgICAgICByZXR1cm4KICAgICAgICB0aHJlYWRpbmcuVGhyZWFkKAogICAgICAgICAgICB0YXJnZXQ9c2VsZi5fcGxheV9iZWVwX3RocmVhZCwKICAgICAgICAgICAgYXJncz0oZnJlcXVlbmN5LCBkdXJhdGlvbiksCiAgICAgICAgICAgIGRhZW1vbj1UcnVlCiAgICAgICAgKS5zdGFydCgpCgogICAgZGVmIF9wbGF5X2JlZXBfdGhyZWFkKHNlbGYsIGZyZXF1ZW5jeTogaW50LCBkdXJhdGlvbjogZmxvYXQpOgogICAgICAgIHRyeToKICAgICAgICAgICAgaW1wb3J0IG51bXB5IGFzIG5wCiAgICAgICAgICAgIGltcG9ydCBweWdhbWUKICAgICAgICAgICAgc2FtcGxlX3JhdGUgPSA0NDEwMAogICAgICAgICAgICBzYW1wbGVzICAgICA9IGludChzYW1wbGVfcmF0ZSAqIGR1cmF0aW9uKQogICAgICAgICAgICB0ICAgICAgICAgICA9IG5wLmxpbnNwYWNlKDAsIGR1cmF0aW9uLCBzYW1wbGVzLCBGYWxzZSkKICAgICAgICAgICAgd2F2ZSAgICAgICAgPSAobnAuc2luKDIgKiBucC5waSAqIGZyZXF1ZW5jeSAqIHQpICogMzI3NjcpLmFzdHlwZShucC5pbnQxNikKICAgICAgICAgICAgc3RlcmVvICAgICAgPSBucC5jb2x1bW5fc3RhY2soW3dhdmUsIHdhdmVdKQogICAgICAgICAgICBzb3VuZCAgICAgICA9IHB5Z2FtZS5zbmRhcnJheS5tYWtlX3NvdW5kKHN0ZXJlbykKICAgICAgICAgICAgc291bmQucGxheSgpCiAgICAgICAgICAgIHB5Z2FtZS50aW1lLndhaXQoaW50KGR1cmF0aW9uICogMTAwMCkgKyA1MCkKICAgICAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgICAgICBwYXNzCgoKIyDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZAKIyAgVEhFTUUgTUFOQUdFUgojIOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkApjbGFzcyBUaGVtZU1hbmFnZXI6CiAgICAiIiIKICAgIENlbnRyYWxpemVkIGNvbG9yIHBhbGV0dGUgYW5kIGZvbnQgZGVmaW5pdGlvbnMuCiAgICBTdXBwb3J0cyBEYXJrIChkZWZhdWx0KSBhbmQgTGlnaHQgbW9kZXMuCiAgICAiIiIKCiAgICBEQVJLID0gewogICAgICAgICJiZ19wcmltYXJ5IjogICAgICAiIzBEMTExNyIsCiAgICAgICAgImJnX3NlY29uZGFyeSI6ICAgICIjMTYxQjIyIiwKICAgICAgICAiYmdfY2FyZCI6ICAgICAgICAgIiMxQzIzMzMiLAogICAgICAgICJiZ19zaWRlYmFyIjogICAgICAiIzBEMTExNyIsCiAgICAgICAgImJnX2hvdmVyIjogICAgICAgICIjMjEyNjJEIiwKICAgICAgICAiYWNjZW50IjogICAgICAgICAgIiMyMTg4RkYiLAogICAgICAgICJhY2NlbnRfaG92ZXIiOiAgICAiIzFGNzhFOCIsCiAgICAgICAgImFjY2VudF9ncmVlbiI6ICAgICIjM0ZCOTUwIiwKICAgICAgICAiYWNjZW50X3JlZCI6ICAgICAgIiNGODUxNDkiLAogICAgICAgICJhY2NlbnRfeWVsbG93IjogICAiI0QyOTkyMiIsCiAgICAgICAgImFjY2VudF9wdXJwbGUiOiAgICIjQkM4Q0ZGIiwKICAgICAgICAidGV4dF9wcmltYXJ5IjogICAgIiNFNkVERjMiLAogICAgICAgICJ0ZXh0X3NlY29uZGFyeSI6ICAiIzhCOTQ5RSIsCiAgICAgICAgInRleHRfbXV0ZWQiOiAgICAgICIjNDg0RjU4IiwKICAgICAgICAiYm9yZGVyIjogICAgICAgICAgIiMzMDM2M0QiLAogICAgICAgICJib3JkZXJfYWN0aXZlIjogICAiIzIxODhGRiIsCiAgICAgICAgInN1Y2Nlc3MiOiAgICAgICAgICIjM0ZCOTUwIiwKICAgICAgICAid2FybmluZyI6ICAgICAgICAgIiNEMjk5MjIiLAogICAgICAgICJlcnJvciI6ICAgICAgICAgICAiI0Y4NTE0OSIsCiAgICAgICAgInRhYmxlX2hlYWRlciI6ICAgICIjMUMyMzMzIiwKICAgICAgICAidGFibGVfcm93IjogICAgICAgIiMxNjFCMjIiLAogICAgICAgICJ0YWJsZV9yb3dfYWx0IjogICAiIzFDMjMzMyIsCiAgICAgICAgInNjcm9sbGJhciI6ICAgICAgICIjMjEyNjJEIiwKICAgICAgICAiYnV0dG9uX3RleHQiOiAgICAgIiNGRkZGRkYiLAogICAgICAgICJzaWRlYmFyX2FjdGl2ZSI6ICAiIzIxMjYyRCIsCiAgICAgICAgImNoYXJ0X2NvbG9ycyI6ICAgWyIjMjE4OEZGIiwgIiMzRkI5NTAiLCAiI0JDOENGRiIsICIjRDI5OTIyIiwgIiNGODUxNDkiXSwKICAgIH0KCiAgICBMSUdIVCA9IHsKICAgICAgICAiYmdfcHJpbWFyeSI6ICAgICAgIiNGNkY4RkEiLAogICAgICAgICJiZ19zZWNvbmRhcnkiOiAgICAiI0ZGRkZGRiIsCiAgICAgICAgImJnX2NhcmQiOiAgICAgICAgICIjRkZGRkZGIiwKICAgICAgICAiYmdfc2lkZWJhciI6ICAgICAgIiNGNkY4RkEiLAogICAgICAgICJiZ19ob3ZlciI6ICAgICAgICAiI0VGRjJGNSIsCiAgICAgICAgImFjY2VudCI6ICAgICAgICAgICIjMDk2OURBIiwKICAgICAgICAiYWNjZW50X2hvdmVyIjogICAgIiMwODYwQ0EiLAogICAgICAgICJhY2NlbnRfZ3JlZW4iOiAgICAiIzFBN0YzNyIsCiAgICAgICAgImFjY2VudF9yZWQiOiAgICAgICIjQ0YyMjJFIiwKICAgICAgICAiYWNjZW50X3llbGxvdyI6ICAgIiM5QTY3MDAiLAogICAgICAgICJhY2NlbnRfcHVycGxlIjogICAiIzgyNTBERiIsCiAgICAgICAgInRleHRfcHJpbWFyeSI6ICAgICIjMUYyMzI4IiwKICAgICAgICAidGV4dF9zZWNvbmRhcnkiOiAgIiM1NzYwNkEiLAogICAgICAgICJ0ZXh0X211dGVkIjogICAgICAiIzhDOTU5RiIsCiAgICAgICAgImJvcmRlciI6ICAgICAgICAgICIjRDBEN0RFIiwKICAgICAgICAiYm9yZGVyX2FjdGl2ZSI6ICAgIiMwOTY5REEiLAogICAgICAgICJzdWNjZXNzIjogICAgICAgICAiIzFBN0YzNyIsCiAgICAgICAgIndhcm5pbmciOiAgICAgICAgICIjOUE2NzAwIiwKICAgICAgICAiZXJyb3IiOiAgICAgICAgICAgIiNDRjIyMkUiLAogICAgICAgICJ0YWJsZV9oZWFkZXIiOiAgICAiI0Y2RjhGQSIsCiAgICAgICAgInRhYmxlX3JvdyI6ICAgICAgICIjRkZGRkZGIiwKICAgICAgICAidGFibGVfcm93X2FsdCI6ICAgIiNGNkY4RkEiLAogICAgICAgICJzY3JvbGxiYXIiOiAgICAgICAiI0QwRDdERSIsCiAgICAgICAgImJ1dHRvbl90ZXh0IjogICAgICIjRkZGRkZGIiwKICAgICAgICAic2lkZWJhcl9hY3RpdmUiOiAgIiNFRkYyRjUiLAogICAgICAgICJjaGFydF9jb2xvcnMiOiAgIFsiIzA5NjlEQSIsICIjMUE3RjM3IiwgIiM4MjUwREYiLCAiIzlBNjcwMCIsICIjQ0YyMjJFIl0sCiAgICB9CgogICAgRk9OVFMgPSB7CiAgICAgICAgImhlYWRpbmdfeGwiOiAgKCJIZWx2ZXRpY2EgTmV1ZSIsIDI4LCAiYm9sZCIpLAogICAgICAgICJoZWFkaW5nX2xnIjogICgiSGVsdmV0aWNhIE5ldWUiLCAyMiwgImJvbGQiKSwKICAgICAgICAiaGVhZGluZ19tZCI6ICAoIkhlbHZldGljYSBOZXVlIiwgMTgsICJib2xkIiksCiAgICAgICAgImhlYWRpbmdfc20iOiAgKCJIZWx2ZXRpY2EgTmV1ZSIsIDE1LCAiYm9sZCIpLAogICAgICAgICJib2R5X2xnIjogICAgICgiSGVsdmV0aWNhIE5ldWUiLCAxNCwgIm5vcm1hbCIpLAogICAgICAgICJib2R5X21kIjogICAgICgiSGVsdmV0aWNhIE5ldWUiLCAxMywgIm5vcm1hbCIpLAogICAgICAgICJib2R5X3NtIjogICAgICgiSGVsdmV0aWNhIE5ldWUiLCAxMiwgIm5vcm1hbCIpLAogICAgICAgICJjYXB0aW9uIjogICAgICgiSGVsdmV0aWNhIE5ldWUiLCAxMSwgIm5vcm1hbCIpLAogICAgICAgICJtb25vIjogICAgICAgICgiQ291cmllciBOZXciLCAgICAxMiwgIm5vcm1hbCIpLAogICAgICAgICJidXR0b24iOiAgICAgICgiSGVsdmV0aWNhIE5ldWUiLCAxMywgImJvbGQiKSwKICAgICAgICAiYmFkZ2UiOiAgICAgICAoIkhlbHZldGljYSBOZXVlIiwgMTAsICJib2xkIiksCiAgICB9CgogICAgZGVmIF9faW5pdF9fKHNlbGYsIG1vZGU6IHN0ciA9ICJkYXJrIik6CiAgICAgICAgc2VsZi5tb2RlID0gbW9kZQogICAgICAgIHNlbGYuY29sb3JzID0gc2VsZi5EQVJLIGlmIG1vZGUgPT0gImRhcmsiIGVsc2Ugc2VsZi5MSUdIVAoKICAgIGRlZiB0b2dnbGUoc2VsZik6CiAgICAgICAgc2VsZi5tb2RlICAgPSAibGlnaHQiIGlmIHNlbGYubW9kZSA9PSAiZGFyayIgZWxzZSAiZGFyayIKICAgICAgICBzZWxmLmNvbG9ycyA9IHNlbGYuREFSSyBpZiBzZWxmLm1vZGUgPT0gImRhcmsiIGVsc2Ugc2VsZi5MSUdIVAogICAgICAgIHJldHVybiBzZWxmLm1vZGUKCiAgICBkZWYgZ2V0KHNlbGYsIGtleTogc3RyKSAtPiBzdHI6CiAgICAgICAgcmV0dXJuIHNlbGYuY29sb3JzLmdldChrZXksICIjRkZGRkZGIikKCiAgICBkZWYgZm9udChzZWxmLCBrZXk6IHN0cikgLT4gdHVwbGU6CiAgICAgICAgcmV0dXJuIHNlbGYuRk9OVFMuZ2V0KGtleSwgKCJIZWx2ZXRpY2EgTmV1ZSIsIDEzLCAibm9ybWFsIikpCgoKIyDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZAKIyAgVElNRSBVVElMSVRJRVMKIyDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZAKZGVmIGdldF9jdXJyZW50X3RpbWVfc3RyKCkgLT4gc3RyOgogICAgIiIiUmV0dXJuIGZvcm1hdHRlZCBjdXJyZW50IHRpbWU6IEhIOk1NOlNTIiIiCiAgICByZXR1cm4gZGF0ZXRpbWUubm93KCkuc3RyZnRpbWUoIiVIOiVNOiVTIikKCgpkZWYgZ2V0X2N1cnJlbnRfZGF0ZV9zdHIoKSAtPiBzdHI6CiAgICAiIiJSZXR1cm4gZm9ybWF0dGVkIGN1cnJlbnQgZGF0ZTogRGF5LCBERCBNb250aCBZWVlZIiIiCiAgICByZXR1cm4gZGF0ZXRpbWUubm93KCkuc3RyZnRpbWUoIiVBLCAlZCAlQiAlWSIpCgoKZGVmIGdldF90aW1lc3RhbXAoKSAtPiBzdHI6CiAgICAiIiJSZXR1cm4gZnVsbCB0aW1lc3RhbXAgc3RyaW5nLiIiIgogICAgcmV0dXJuIGRhdGV0aW1lLm5vdygpLnN0cmZ0aW1lKCIlWS0lbS0lZCAlSDolTTolUyIpCgoKZGVmIGZvcm1hdF9kYXRlKGRhdGVfc3RyOiBzdHIpIC0+IHN0cjoKICAgICIiIkNvbnZlcnQgWVlZWS1NTS1ERCB0byByZWFkYWJsZSBERCBNb24gWVlZWS4iIiIKICAgIHRyeToKICAgICAgICBkdCA9IGRhdGV0aW1lLnN0cnB0aW1lKGRhdGVfc3RyLCAiJVktJW0tJWQiKQogICAgICAgIHJldHVybiBkdC5zdHJmdGltZSgiJWQgJWIgJVkiKQogICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICByZXR1cm4gZGF0ZV9zdHIKCgojIOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkAojICBDQU1FUkEgVVRJTElUSUVTCiMg4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQCmRlZiBsaXN0X2F2YWlsYWJsZV9jYW1lcmFzKG1heF9jaGVjazogaW50ID0gNSkgLT4gbGlzdDoKICAgICIiIgogICAgRGV0ZWN0IGF2YWlsYWJsZSBjYW1lcmEgaW5kaWNlcy4KICAgIFJldHVybnMgYSBsaXN0IG9mIHZhbGlkIGludGVnZXIgaW5kaWNlcy4KICAgICIiIgogICAgaW1wb3J0IGN2MgogICAgYXZhaWxhYmxlID0gW10KICAgIGZvciBpIGluIHJhbmdlKG1heF9jaGVjayk6CiAgICAgICAgY2FwID0gY3YyLlZpZGVvQ2FwdHVyZShpKQogICAgICAgIGlmIGNhcC5pc09wZW5lZCgpOgogICAgICAgICAgICBhdmFpbGFibGUuYXBwZW5kKGkpCiAgICAgICAgICAgIGNhcC5yZWxlYXNlKCkKICAgIHJldHVybiBhdmFpbGFibGUgaWYgYXZhaWxhYmxlIGVsc2UgWzBdCgoKIyDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZAKIyAgVkFMSURBVElPTiBVVElMSVRJRVMKIyDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZAKZGVmIHZhbGlkYXRlX3VzZXJfaW5wdXQobmFtZTogc3RyLCByb2xsOiBzdHIsIGRlcHQ6IHN0cikgLT4gdHVwbGVbYm9vbCwgc3RyXToKICAgICIiIgogICAgVmFsaWRhdGUgcmVnaXN0cmF0aW9uIGZvcm0gaW5wdXRzLgogICAgUmV0dXJuczogKGlzX3ZhbGlkOiBib29sLCBlcnJvcl9tZXNzYWdlOiBzdHIpCiAgICAiIiIKICAgIGlmIG5vdCBuYW1lIG9yIGxlbihuYW1lLnN0cmlwKCkpIDwgMjoKICAgICAgICByZXR1cm4gRmFsc2UsICJOYW1lIG11c3QgYmUgYXQgbGVhc3QgMiBjaGFyYWN0ZXJzLiIKICAgIGlmIG5vdCByb2xsIG9yIGxlbihyb2xsLnN0cmlwKCkpIDwgMToKICAgICAgICByZXR1cm4gRmFsc2UsICJSb2xsIG51bWJlciAvIElEIGlzIHJlcXVpcmVkLiIKICAgIGlmIG5vdCBkZXB0IG9yIGxlbihkZXB0LnN0cmlwKCkpIDwgMToKICAgICAgICByZXR1cm4gRmFsc2UsICJEZXBhcnRtZW50IC8gQ2xhc3MgaXMgcmVxdWlyZWQuIgogICAgIyBSZWplY3Qgc3BlY2lhbCBjaGFyYWN0ZXJzIGluIHJvbGwgbnVtYmVyCiAgICBpbXBvcnQgcmUKICAgIGlmIG5vdCByZS5tYXRjaChyIl5bQS1aYS16MC05XC1fL10rJCIsIHJvbGwuc3RyaXAoKSk6CiAgICAgICAgcmV0dXJuIEZhbHNlLCAiUm9sbCBudW1iZXIgbWF5IG9ubHkgY29udGFpbiBsZXR0ZXJzLCBkaWdpdHMsIC0sIF8sIC8uIgogICAgcmV0dXJuIFRydWUsICIiCgoKZGVmIG9wZW5fZmlsZShwYXRoOiBzdHIpOgogICAgIiIiT3BlbiBhIGZpbGUgd2l0aCB0aGUgc3lzdGVtIGRlZmF1bHQgYXBwbGljYXRpb24uIiIiCiAgICB0cnk6CiAgICAgICAgaWYgcGxhdGZvcm0uc3lzdGVtKCkgPT0gIkRhcndpbiI6CiAgICAgICAgICAgIG9zLnN5c3RlbShmJ29wZW4gIntwYXRofSInKQogICAgICAgIGVsaWYgcGxhdGZvcm0uc3lzdGVtKCkgPT0gIldpbmRvd3MiOgogICAgICAgICAgICBvcy5zdGFydGZpbGUocGF0aCkKICAgICAgICBlbHNlOgogICAgICAgICAgICBvcy5zeXN0ZW0oZid4ZGctb3BlbiAie3BhdGh9IicpCiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgbG9nZ2VyLmVycm9yKGYiQ2Fubm90IG9wZW4gZmlsZToge2V9IikKCgojIOKUgOKUgCBTaW5nbGV0b25zIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgApzb3VuZF9tYW5hZ2VyID0gU291bmRNYW5hZ2VyKCkKdGhlbWVfbWFuYWdlciA9IFRoZW1lTWFuYWdlcihtb2RlPSJkYXJrIikK', 'exports/.gitkeep': 'IyBFeHBvcnRlZCBhdHRlbmRhbmNlIGZpbGVzIChDU1YgYW5kIEV4Y2VsKSBhcmUgc2F2ZWQgaGVyZSBhdXRvbWF0aWNhbGx5Lgo=', 'logs/.gitkeep': 'IyBBcHBsaWNhdGlvbiBsb2dzIGFyZSB3cml0dGVuIGhlcmUuIFJvdGF0ZWQgYXV0b21hdGljYWxseS4K', 'logs/app.log': '', 'face_recognition_engine/recognizer.py': 'IiIiCuKVlOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVlwrilZEgICAgICBGQUNFIFJFQ09HTklUSU9OIEVOR0lORSDigJQgRmFjZSBBdHRlbmRhbmNlIFN5c3RlbSAgICAgICDilZEK4pWRICBIYW5kbGVzIGZhY2UgZW5jb2RpbmcsIHRyYWluaW5nLCBhbmQgcmVhbC10aW1lIGRldGVjdGlvbiAgIOKVkQrilZrilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZ0KClRoaXMgbW9kdWxlIGhhbmRsZXM6CiAgLSBDYXB0dXJpbmcgZmFjZSBpbWFnZXMgZm9yIG5ldyB1c2VycwogIC0gRW5jb2RpbmcgZmFjZXMgYW5kIHNhdmluZyBlbmNvZGluZ3MgdG8gZGlzawogIC0gTG9hZGluZyBleGlzdGluZyBlbmNvZGluZ3MgZnJvbSBkaXNrCiAgLSBSZWFsLXRpbWUgZmFjZSByZWNvZ25pdGlvbiBmcm9tIHdlYmNhbSBmcmFtZXMKICAtIENvbmZpZGVuY2Ugc2NvcmluZyBhbmQgdW5rbm93biBmYWNlIGhhbmRsaW5nCiIiIgoKaW1wb3J0IGN2MgppbXBvcnQgZmFjZV9yZWNvZ25pdGlvbgppbXBvcnQgbnVtcHkgYXMgbnAKaW1wb3J0IG9zCmltcG9ydCBwaWNrbGUKaW1wb3J0IGxvZ2dpbmcKZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUKCiMg4pSA4pSAIFBhdGhzIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgApCQVNFX0RJUiAgICAgICA9IG9zLnBhdGguZGlybmFtZShvcy5wYXRoLmRpcm5hbWUob3MucGF0aC5hYnNwYXRoKF9fZmlsZV9fKSkpCkZBQ0VfREFUQV9ESVIgID0gb3MucGF0aC5qb2luKEJBU0VfRElSLCAiZGF0YSIsICJmYWNlX2RhdGEiKQpFTkNPRElOR1NfRklMRSA9IG9zLnBhdGguam9pbihCQVNFX0RJUiwgImRhdGEiLCAiZmFjZV9lbmNvZGluZ3MucGtsIikKCm9zLm1ha2VkaXJzKEZBQ0VfREFUQV9ESVIsIGV4aXN0X29rPVRydWUpCgojIOKUgOKUgCBMb2dnaW5nIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgApsb2dnZXIgPSBsb2dnaW5nLmdldExvZ2dlcihfX25hbWVfXykKCgojIOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkAojICBGYWNlUmVjb2duaXRpb25FbmdpbmUgQ2xhc3MKIyDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZAKY2xhc3MgRmFjZVJlY29nbml0aW9uRW5naW5lOgogICAgIiIiCiAgICBDb3JlIGZhY2UgcmVjb2duaXRpb24gZW5naW5lLgogICAgTWFuYWdlcyBlbmNvZGluZyBzdG9yYWdlLCBtb2RlbCB0cmFpbmluZywgYW5kIGxpdmUgcmVjb2duaXRpb24uCiAgICAiIiIKCiAgICBkZWYgX19pbml0X18oc2VsZik6CiAgICAgICAgIyBMb2FkZWQgZW5jb2RpbmdzOiB7ImVuY29kaW5ncyI6IFsuLi5dLCAiaWRzIjogWy4uLl0sICJuYW1lcyI6IFsuLi5dfQogICAgICAgIHNlbGYua25vd25fZW5jb2RpbmdzID0gW10KICAgICAgICBzZWxmLmtub3duX2lkcyAgICAgICA9IFtdCiAgICAgICAgc2VsZi5rbm93bl9uYW1lcyAgICAgPSBbXQoKICAgICAgICAjIFRvbGVyYW5jZTogbG93ZXIgPSBzdHJpY3RlciBtYXRjaGluZyAoMC40LTAuNiBpcyB0eXBpY2FsKQogICAgICAgIHNlbGYudG9sZXJhbmNlID0gMC41MAoKICAgICAgICAjIEhhYXIgY2FzY2FkZSBmb3IgZmFzdCBmYWNlIGRldGVjdGlvbiAocHJlLWNoZWNrIGJlZm9yZSBkZWVwIGVuY29kaW5nKQogICAgICAgIGNhc2NhZGVfcGF0aCA9IGN2Mi5kYXRhLmhhYXJjYXNjYWRlcyArICJoYWFyY2FzY2FkZV9mcm9udGFsZmFjZV9kZWZhdWx0LnhtbCIKICAgICAgICBzZWxmLmZhY2VfY2FzY2FkZSA9IGN2Mi5DYXNjYWRlQ2xhc3NpZmllcihjYXNjYWRlX3BhdGgpCgogICAgICAgICMgTG9hZCBleGlzdGluZyBlbmNvZGluZ3MgZnJvbSBkaXNrCiAgICAgICAgc2VsZi5sb2FkX2VuY29kaW5ncygpCiAgICAgICAgbG9nZ2VyLmluZm8oIkZhY2VSZWNvZ25pdGlvbkVuZ2luZSBpbml0aWFsaXplZC4iKQoKICAgICMg4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQCiAgICAjICBFTkNPRElORyBQRVJTSVNURU5DRQogICAgIyDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZAKCiAgICBkZWYgc2F2ZV9lbmNvZGluZ3Moc2VsZik6CiAgICAgICAgIiIiU2F2ZSBhbGwga25vd24gZW5jb2RpbmdzIHRvIGRpc2sgYXMgYSBwaWNrbGUgZmlsZS4iIiIKICAgICAgICBkYXRhID0gewogICAgICAgICAgICAiZW5jb2RpbmdzIjogc2VsZi5rbm93bl9lbmNvZGluZ3MsCiAgICAgICAgICAgICJpZHMiOiAgICAgICBzZWxmLmtub3duX2lkcywKICAgICAgICAgICAgIm5hbWVzIjogICAgIHNlbGYua25vd25fbmFtZXMsCiAgICAgICAgfQogICAgICAgIHdpdGggb3BlbihFTkNPRElOR1NfRklMRSwgIndiIikgYXMgZjoKICAgICAgICAgICAgcGlja2xlLmR1bXAoZGF0YSwgZikKICAgICAgICBsb2dnZXIuaW5mbyhmIkVuY29kaW5ncyBzYXZlZDoge2xlbihzZWxmLmtub3duX2VuY29kaW5ncyl9IGZhY2VzLiIpCgogICAgZGVmIGxvYWRfZW5jb2RpbmdzKHNlbGYpOgogICAgICAgICIiIkxvYWQgZW5jb2RpbmdzIGZyb20gZGlzayAoaWYgZmlsZSBleGlzdHMpLiIiIgogICAgICAgIGlmIG9zLnBhdGguZXhpc3RzKEVOQ09ESU5HU19GSUxFKToKICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgd2l0aCBvcGVuKEVOQ09ESU5HU19GSUxFLCAicmIiKSBhcyBmOgogICAgICAgICAgICAgICAgICAgIGRhdGEgPSBwaWNrbGUubG9hZChmKQogICAgICAgICAgICAgICAgc2VsZi5rbm93bl9lbmNvZGluZ3MgPSBkYXRhLmdldCgiZW5jb2RpbmdzIiwgW10pCiAgICAgICAgICAgICAgICBzZWxmLmtub3duX2lkcyAgICAgICA9IGRhdGEuZ2V0KCJpZHMiLCBbXSkKICAgICAgICAgICAgICAgIHNlbGYua25vd25fbmFtZXMgICAgID0gZGF0YS5nZXQoIm5hbWVzIiwgW10pCiAgICAgICAgICAgICAgICBsb2dnZXIuaW5mbyhmIkxvYWRlZCB7bGVuKHNlbGYua25vd25fZW5jb2RpbmdzKX0gZmFjZSBlbmNvZGluZ3MuIikKICAgICAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgICAgICAgICAgbG9nZ2VyLmVycm9yKGYiRXJyb3IgbG9hZGluZyBlbmNvZGluZ3M6IHtlfSIpCiAgICAgICAgICAgICAgICBzZWxmLmtub3duX2VuY29kaW5ncyA9IFtdCiAgICAgICAgICAgICAgICBzZWxmLmtub3duX2lkcyAgICAgICA9IFtdCiAgICAgICAgICAgICAgICBzZWxmLmtub3duX25hbWVzICAgICA9IFtdCiAgICAgICAgZWxzZToKICAgICAgICAgICAgbG9nZ2VyLmluZm8oIk5vIGVuY29kaW5nIGZpbGUgZm91bmQuIFN0YXJ0aW5nIGZyZXNoLiIpCgogICAgZGVmIHJlbG9hZF9lbmNvZGluZ3Moc2VsZik6CiAgICAgICAgIiIiUHVibGljIG1ldGhvZCB0byByZWxvYWQgZW5jb2RpbmdzIGZyb20gZGlzayAoY2FsbCBhZnRlciB0cmFpbmluZykuIiIiCiAgICAgICAgc2VsZi5sb2FkX2VuY29kaW5ncygpCgogICAgIyDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZAKICAgICMgIEZBQ0UgQ0FQVFVSRSAoUmVnaXN0cmF0aW9uKQogICAgIyDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZAKCiAgICBkZWYgY2FwdHVyZV9mYWNlX2ltYWdlcyhzZWxmLCB1c2VyX2lkOiBpbnQsIHVzZXJfbmFtZTogc3RyLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgbnVtX2ltYWdlczogaW50ID0gMzAsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBjYW1lcmFfaW5kZXg6IGludCA9IDAsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBwcm9ncmVzc19jYWxsYmFjaz1Ob25lLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgZnJhbWVfY2FsbGJhY2s9Tm9uZSkgLT4gYm9vbDoKICAgICAgICAiIiIKICAgICAgICBDYXB0dXJlIGBudW1faW1hZ2VzYCBmYWNlIGltYWdlcyBmcm9tIHdlYmNhbSBmb3IgYSBuZXcgdXNlci4KCiAgICAgICAgQXJnczoKICAgICAgICAgICAgdXNlcl9pZDogICAgICAgICAgIERhdGFiYXNlIElEIG9mIHRoZSB1c2VyCiAgICAgICAgICAgIHVzZXJfbmFtZTogICAgICAgICBEaXNwbGF5IG5hbWUgKGZvciBmb2xkZXIgbmFtaW5nKQogICAgICAgICAgICBudW1faW1hZ2VzOiAgICAgICAgTnVtYmVyIG9mIGZhY2UgaW1hZ2VzIHRvIGNhcHR1cmUKICAgICAgICAgICAgY2FtZXJhX2luZGV4OiAgICAgIFdlYmNhbSBpbmRleCAoMCA9IGRlZmF1bHQpCiAgICAgICAgICAgIHByb2dyZXNzX2NhbGxiYWNrOiBDYWxsZWQgd2l0aCAoY3VycmVudCwgdG90YWwpIGZvciBwcm9ncmVzcyBiYXIKICAgICAgICAgICAgZnJhbWVfY2FsbGJhY2s6ICAgIENhbGxlZCB3aXRoIGVhY2ggQkdSIGZyYW1lIGZvciBsaXZlIHByZXZpZXcKCiAgICAgICAgUmV0dXJuczoKICAgICAgICAgICAgVHJ1ZSBpZiBzdWNjZXNzZnVsLCBGYWxzZSBvdGhlcndpc2UuCiAgICAgICAgIiIiCiAgICAgICAgIyBDcmVhdGUgdXNlci1zcGVjaWZpYyBmb2xkZXIKICAgICAgICBzYWZlX25hbWUgICA9ICIiLmpvaW4oYyBmb3IgYyBpbiB1c2VyX25hbWUgaWYgYy5pc2FsbnVtKCkgb3IgYyBpbiAiXyAtIikKICAgICAgICB1c2VyX2ZvbGRlciA9IG9zLnBhdGguam9pbihGQUNFX0RBVEFfRElSLCBmInt1c2VyX2lkfV97c2FmZV9uYW1lfSIpCiAgICAgICAgb3MubWFrZWRpcnModXNlcl9mb2xkZXIsIGV4aXN0X29rPVRydWUpCgogICAgICAgIGNhcCA9IGN2Mi5WaWRlb0NhcHR1cmUoY2FtZXJhX2luZGV4KQogICAgICAgIGlmIG5vdCBjYXAuaXNPcGVuZWQoKToKICAgICAgICAgICAgbG9nZ2VyLmVycm9yKCJDYW5ub3Qgb3BlbiBjYW1lcmEgZm9yIGNhcHR1cmUuIikKICAgICAgICAgICAgcmV0dXJuIEZhbHNlCgogICAgICAgIGNhcC5zZXQoY3YyLkNBUF9QUk9QX0ZSQU1FX1dJRFRILCAgNjQwKQogICAgICAgIGNhcC5zZXQoY3YyLkNBUF9QUk9QX0ZSQU1FX0hFSUdIVCwgNDgwKQogICAgICAgIGNhcC5zZXQoY3YyLkNBUF9QUk9QX0ZQUywgICAgICAgICAgMzApCgogICAgICAgIGNhcHR1cmVkID0gMAogICAgICAgIGF0dGVtcHQgID0gMAogICAgICAgIG1heF9hdHRlbXB0cyA9IG51bV9pbWFnZXMgKiAxMCAgIyBhdm9pZCBpbmZpbml0ZSBsb29wCgogICAgICAgIGxvZ2dlci5pbmZvKGYiQ2FwdHVyaW5nIHtudW1faW1hZ2VzfSBpbWFnZXMgZm9yOiB7dXNlcl9uYW1lfSIpCgogICAgICAgIHdoaWxlIGNhcHR1cmVkIDwgbnVtX2ltYWdlcyBhbmQgYXR0ZW1wdCA8IG1heF9hdHRlbXB0czoKICAgICAgICAgICAgcmV0LCBmcmFtZSA9IGNhcC5yZWFkKCkKICAgICAgICAgICAgaWYgbm90IHJldDoKICAgICAgICAgICAgICAgIGF0dGVtcHQgKz0gMQogICAgICAgICAgICAgICAgY29udGludWUKCiAgICAgICAgICAgIGF0dGVtcHQgKz0gMQogICAgICAgICAgICByZ2JfZnJhbWUgPSBjdjIuY3Z0Q29sb3IoZnJhbWUsIGN2Mi5DT0xPUl9CR1IyUkdCKQoKICAgICAgICAgICAgIyBEZXRlY3QgZmFjZXMgdXNpbmcgZmFzdCBIT0cgbW9kZWwKICAgICAgICAgICAgZmFjZV9sb2NhdGlvbnMgPSBmYWNlX3JlY29nbml0aW9uLmZhY2VfbG9jYXRpb25zKHJnYl9mcmFtZSwgbW9kZWw9ImhvZyIpCgogICAgICAgICAgICBpZiBsZW4oZmFjZV9sb2NhdGlvbnMpID09IDE6ICAgIyBleGFjdGx5IG9uZSBmYWNlIOKAlCBpZGVhbAogICAgICAgICAgICAgICAgdG9wLCByaWdodCwgYm90dG9tLCBsZWZ0ID0gZmFjZV9sb2NhdGlvbnNbMF0KCiAgICAgICAgICAgICAgICAjIERyYXcgZ3JlZW4gcmVjdGFuZ2xlIGFyb3VuZCBmYWNlCiAgICAgICAgICAgICAgICBkaXNwbGF5ID0gZnJhbWUuY29weSgpCiAgICAgICAgICAgICAgICBjdjIucmVjdGFuZ2xlKGRpc3BsYXksIChsZWZ0LCB0b3ApLCAocmlnaHQsIGJvdHRvbSksICgwLCAyNTUsIDEwMCksIDIpCiAgICAgICAgICAgICAgICBjdjIucHV0VGV4dChkaXNwbGF5LCBmIkNhcHR1cmluZzoge2NhcHR1cmVkKzF9L3tudW1faW1hZ2VzfSIsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAoMTAsIDMwKSwgY3YyLkZPTlRfSEVSU0hFWV9TSU1QTEVYLCAwLjgsICgwLCAyNTUsIDEwMCksIDIpCgogICAgICAgICAgICAgICAgIyBTYXZlIGZhY2UgaW1hZ2UKICAgICAgICAgICAgICAgIGZhY2VfaW1nID0gZnJhbWVbdG9wOmJvdHRvbSwgbGVmdDpyaWdodF0KICAgICAgICAgICAgICAgIGltZ19wYXRoID0gb3MucGF0aC5qb2luKHVzZXJfZm9sZGVyLCBmIntjYXB0dXJlZDowNGR9LmpwZyIpCiAgICAgICAgICAgICAgICBjdjIuaW13cml0ZShpbWdfcGF0aCwgZmFjZV9pbWcpCiAgICAgICAgICAgICAgICBjYXB0dXJlZCArPSAxCgogICAgICAgICAgICAgICAgaWYgcHJvZ3Jlc3NfY2FsbGJhY2s6CiAgICAgICAgICAgICAgICAgICAgcHJvZ3Jlc3NfY2FsbGJhY2soY2FwdHVyZWQsIG51bV9pbWFnZXMpCiAgICAgICAgICAgICAgICBpZiBmcmFtZV9jYWxsYmFjazoKICAgICAgICAgICAgICAgICAgICBmcmFtZV9jYWxsYmFjayhkaXNwbGF5KQoKICAgICAgICAgICAgZWxpZiBsZW4oZmFjZV9sb2NhdGlvbnMpID09IDA6CiAgICAgICAgICAgICAgICAjIE5vIGZhY2UgZGV0ZWN0ZWQg4oCUIHNob3cgd2FybmluZyBvbiBmcmFtZQogICAgICAgICAgICAgICAgZGlzcGxheSA9IGZyYW1lLmNvcHkoKQogICAgICAgICAgICAgICAgY3YyLnB1dFRleHQoZGlzcGxheSwgIk5vIGZhY2UgZGV0ZWN0ZWQuIExvb2sgYXQgY2FtZXJhLiIsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAoMTAsIDMwKSwgY3YyLkZPTlRfSEVSU0hFWV9TSU1QTEVYLCAwLjcsICgwLCAxMDAsIDI1NSksIDIpCiAgICAgICAgICAgICAgICBpZiBmcmFtZV9jYWxsYmFjazoKICAgICAgICAgICAgICAgICAgICBmcmFtZV9jYWxsYmFjayhkaXNwbGF5KQogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgIyBNdWx0aXBsZSBmYWNlcyDigJQgYXNrIHVzZXIgdG8gYmUgYWxvbmUKICAgICAgICAgICAgICAgIGRpc3BsYXkgPSBmcmFtZS5jb3B5KCkKICAgICAgICAgICAgICAgIGN2Mi5wdXRUZXh0KGRpc3BsYXksICJNdWx0aXBsZSBmYWNlcyEgU3RheSBhbG9uZSBpbiBmcmFtZS4iLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgKDEwLCAzMCksIGN2Mi5GT05UX0hFUlNIRVlfU0lNUExFWCwgMC43LCAoMCwgNTAsIDI1NSksIDIpCiAgICAgICAgICAgICAgICBpZiBmcmFtZV9jYWxsYmFjazoKICAgICAgICAgICAgICAgICAgICBmcmFtZV9jYWxsYmFjayhkaXNwbGF5KQoKICAgICAgICBjYXAucmVsZWFzZSgpCgogICAgICAgIGlmIGNhcHR1cmVkID49IG51bV9pbWFnZXM6CiAgICAgICAgICAgIGxvZ2dlci5pbmZvKGYiQ2FwdHVyZWQge2NhcHR1cmVkfSBpbWFnZXMgZm9yIHt1c2VyX25hbWV9LiIpCiAgICAgICAgICAgIHJldHVybiBUcnVlCiAgICAgICAgZWxzZToKICAgICAgICAgICAgbG9nZ2VyLndhcm5pbmcoZiJPbmx5IGNhcHR1cmVkIHtjYXB0dXJlZH0ve251bV9pbWFnZXN9IGltYWdlcy4iKQogICAgICAgICAgICByZXR1cm4gY2FwdHVyZWQgPiA1ICAjIEFjY2VwdCBwYXJ0aWFsIGlmIGF0IGxlYXN0IDUgaW1hZ2VzCgogICAgIyDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZAKICAgICMgIFRSQUlOSU5HCiAgICAjIOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkAoKICAgIGRlZiB0cmFpbl9tb2RlbChzZWxmLCBwcm9ncmVzc19jYWxsYmFjaz1Ob25lKSAtPiBib29sOgogICAgICAgICIiIgogICAgICAgIFNjYW4gYWxsIGZhY2UgaW1hZ2UgZm9sZGVycywgZW5jb2RlIGVhY2ggZmFjZSwKICAgICAgICBhbmQgc2F2ZSBlbmNvZGluZ3MgdG8gZGlzay4KCiAgICAgICAgQXJnczoKICAgICAgICAgICAgcHJvZ3Jlc3NfY2FsbGJhY2s6IENhbGxlZCB3aXRoIChjdXJyZW50LCB0b3RhbCkgZHVyaW5nIHRyYWluaW5nCgogICAgICAgIFJldHVybnM6CiAgICAgICAgICAgIFRydWUgb24gc3VjY2VzcywgRmFsc2Ugb24gZmFpbHVyZS4KICAgICAgICAiIiIKICAgICAgICBsb2dnZXIuaW5mbygiU3RhcnRpbmcgbW9kZWwgdHJhaW5pbmcuLi4iKQoKICAgICAgICAjIERpc2NvdmVyIGFsbCB1c2VyIGZvbGRlcnMKICAgICAgICB1c2VyX2ZvbGRlcnMgPSBbCiAgICAgICAgICAgIGQgZm9yIGQgaW4gb3MubGlzdGRpcihGQUNFX0RBVEFfRElSKQogICAgICAgICAgICBpZiBvcy5wYXRoLmlzZGlyKG9zLnBhdGguam9pbihGQUNFX0RBVEFfRElSLCBkKSkKICAgICAgICBdCgogICAgICAgIGlmIG5vdCB1c2VyX2ZvbGRlcnM6CiAgICAgICAgICAgIGxvZ2dlci53YXJuaW5nKCJObyBmYWNlIGRhdGEgZm91bmQgdG8gdHJhaW4gb24uIikKICAgICAgICAgICAgcmV0dXJuIEZhbHNlCgogICAgICAgIG5ld19lbmNvZGluZ3MgPSBbXQogICAgICAgIG5ld19pZHMgICAgICAgPSBbXQogICAgICAgIG5ld19uYW1lcyAgICAgPSBbXQoKICAgICAgICB0b3RhbF9pbWFnZXMgPSBzdW0oCiAgICAgICAgICAgIGxlbihvcy5saXN0ZGlyKG9zLnBhdGguam9pbihGQUNFX0RBVEFfRElSLCBmKSkpCiAgICAgICAgICAgIGZvciBmIGluIHVzZXJfZm9sZGVycwogICAgICAgICkKICAgICAgICBwcm9jZXNzZWQgPSAwCgogICAgICAgIGZvciBmb2xkZXJfbmFtZSBpbiB1c2VyX2ZvbGRlcnM6CiAgICAgICAgICAgICMgRm9sZGVyIGZvcm1hdDogInVzZXJJRF91c2VyTmFtZSIKICAgICAgICAgICAgcGFydHMgICA9IGZvbGRlcl9uYW1lLnNwbGl0KCJfIiwgMSkKICAgICAgICAgICAgdXNlcl9pZCA9IGludChwYXJ0c1swXSkgaWYgcGFydHNbMF0uaXNkaWdpdCgpIGVsc2UgLTEKICAgICAgICAgICAgbmFtZSAgICA9IHBhcnRzWzFdIGlmIGxlbihwYXJ0cykgPiAxIGVsc2UgZm9sZGVyX25hbWUKCiAgICAgICAgICAgIGZvbGRlcl9wYXRoID0gb3MucGF0aC5qb2luKEZBQ0VfREFUQV9ESVIsIGZvbGRlcl9uYW1lKQogICAgICAgICAgICBpbWFnZV9maWxlcyA9IFsKICAgICAgICAgICAgICAgIGYgZm9yIGYgaW4gb3MubGlzdGRpcihmb2xkZXJfcGF0aCkKICAgICAgICAgICAgICAgIGlmIGYubG93ZXIoKS5lbmRzd2l0aCgoIi5qcGciLCAiLmpwZWciLCAiLnBuZyIpKQogICAgICAgICAgICBdCgogICAgICAgICAgICBlbmNvZGluZ3NfZm9yX3VzZXIgPSBbXQoKICAgICAgICAgICAgZm9yIGltZ19maWxlIGluIGltYWdlX2ZpbGVzOgogICAgICAgICAgICAgICAgaW1nX3BhdGggPSBvcy5wYXRoLmpvaW4oZm9sZGVyX3BhdGgsIGltZ19maWxlKQogICAgICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgICAgIGltYWdlICAgICA9IGZhY2VfcmVjb2duaXRpb24ubG9hZF9pbWFnZV9maWxlKGltZ19wYXRoKQogICAgICAgICAgICAgICAgICAgIGVuY29kaW5ncyA9IGZhY2VfcmVjb2duaXRpb24uZmFjZV9lbmNvZGluZ3MoaW1hZ2UpCgogICAgICAgICAgICAgICAgICAgIGlmIGVuY29kaW5nczoKICAgICAgICAgICAgICAgICAgICAgICAgZW5jb2RpbmdzX2Zvcl91c2VyLmFwcGVuZChlbmNvZGluZ3NbMF0pCiAgICAgICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgICAgICAgICAgICAgbG9nZ2VyLndhcm5pbmcoZiJDb3VsZCBub3QgZW5jb2RlIHtpbWdfcGF0aH06IHtlfSIpCgogICAgICAgICAgICAgICAgcHJvY2Vzc2VkICs9IDEKICAgICAgICAgICAgICAgIGlmIHByb2dyZXNzX2NhbGxiYWNrOgogICAgICAgICAgICAgICAgICAgIHByb2dyZXNzX2NhbGxiYWNrKHByb2Nlc3NlZCwgdG90YWxfaW1hZ2VzKQoKICAgICAgICAgICAgIyBVc2UgbWVhbiBlbmNvZGluZyBmb3IgYmV0dGVyIHJvYnVzdG5lc3MKICAgICAgICAgICAgaWYgZW5jb2RpbmdzX2Zvcl91c2VyOgogICAgICAgICAgICAgICAgbWVhbl9lbmNvZGluZyA9IG5wLm1lYW4oZW5jb2RpbmdzX2Zvcl91c2VyLCBheGlzPTApCiAgICAgICAgICAgICAgICBuZXdfZW5jb2RpbmdzLmFwcGVuZChtZWFuX2VuY29kaW5nKQogICAgICAgICAgICAgICAgbmV3X2lkcy5hcHBlbmQodXNlcl9pZCkKICAgICAgICAgICAgICAgIG5ld19uYW1lcy5hcHBlbmQobmFtZSkKICAgICAgICAgICAgICAgIGxvZ2dlci5pbmZvKGYiVHJhaW5lZDoge25hbWV9ICh7bGVuKGVuY29kaW5nc19mb3JfdXNlcil9IGltYWdlcykiKQoKICAgICAgICBpZiBuZXdfZW5jb2RpbmdzOgogICAgICAgICAgICBzZWxmLmtub3duX2VuY29kaW5ncyA9IG5ld19lbmNvZGluZ3MKICAgICAgICAgICAgc2VsZi5rbm93bl9pZHMgICAgICAgPSBuZXdfaWRzCiAgICAgICAgICAgIHNlbGYua25vd25fbmFtZXMgICAgID0gbmV3X25hbWVzCiAgICAgICAgICAgIHNlbGYuc2F2ZV9lbmNvZGluZ3MoKQogICAgICAgICAgICBsb2dnZXIuaW5mbyhmIlRyYWluaW5nIGNvbXBsZXRlLiB7bGVuKG5ld19lbmNvZGluZ3MpfSB1c2VycyB0cmFpbmVkLiIpCiAgICAgICAgICAgIHJldHVybiBUcnVlCiAgICAgICAgZWxzZToKICAgICAgICAgICAgbG9nZ2VyLmVycm9yKCJObyB2YWxpZCBlbmNvZGluZ3MgZm91bmQgZHVyaW5nIHRyYWluaW5nLiIpCiAgICAgICAgICAgIHJldHVybiBGYWxzZQoKICAgICMg4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQCiAgICAjICBSRUFMLVRJTUUgUkVDT0dOSVRJT04KICAgICMg4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQCgogICAgZGVmIHJlY29nbml6ZV9mYWNlcyhzZWxmLCBmcmFtZTogbnAubmRhcnJheSkgLT4gbGlzdDoKICAgICAgICAiIiIKICAgICAgICBSZWNvZ25pemUgZmFjZXMgaW4gYSBzaW5nbGUgQkdSIGZyYW1lLgoKICAgICAgICBBcmdzOgogICAgICAgICAgICBmcmFtZTogT3BlbkNWIEJHUiBpbWFnZSAobnVtcHkgYXJyYXkpCgogICAgICAgIFJldHVybnM6CiAgICAgICAgICAgIExpc3Qgb2YgZGljdHM6IFsKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgIm5hbWUiOiAgICAgICBzdHIsICAgICAgICAjIHJlY29nbml6ZWQgbmFtZSBvciAiVW5rbm93biIKICAgICAgICAgICAgICAgICAgInVzZXJfaWQiOiAgICBpbnQsICAgICAgICAjIERCIHVzZXIgSUQgb3IgLTEKICAgICAgICAgICAgICAgICAgImNvbmZpZGVuY2UiOiBmbG9hdCwgICAgICAjIDAuMCDigJMgMS4wIChoaWdoZXIgPSBtb3JlIGNvbmZpZGVudCkKICAgICAgICAgICAgICAgICAgImxvY2F0aW9uIjogICh0b3AsIHJpZ2h0LCBib3R0b20sIGxlZnQpCiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgIF0KICAgICAgICAiIiIKICAgICAgICBpZiBub3Qgc2VsZi5rbm93bl9lbmNvZGluZ3M6CiAgICAgICAgICAgIHJldHVybiBbXQoKICAgICAgICAjIFJlc2l6ZSBmcmFtZSB0byAxLzQgc2l6ZSBmb3IgZmFzdGVyIHByb2Nlc3NpbmcKICAgICAgICBzbWFsbF9mcmFtZSA9IGN2Mi5yZXNpemUoZnJhbWUsICgwLCAwKSwgZng9MC4yNSwgZnk9MC4yNSkKICAgICAgICByZ2Jfc21hbGwgICA9IGN2Mi5jdnRDb2xvcihzbWFsbF9mcmFtZSwgY3YyLkNPTE9SX0JHUjJSR0IpCgogICAgICAgICMgRGV0ZWN0IGZhY2UgbG9jYXRpb25zIChIT0cgaXMgZmFzdGVyIHRoYW4gQ05OIG9uIENQVSkKICAgICAgICBmYWNlX2xvY2F0aW9ucyA9IGZhY2VfcmVjb2duaXRpb24uZmFjZV9sb2NhdGlvbnMocmdiX3NtYWxsLCBtb2RlbD0iaG9nIikKCiAgICAgICAgaWYgbm90IGZhY2VfbG9jYXRpb25zOgogICAgICAgICAgICByZXR1cm4gW10KCiAgICAgICAgIyBDb21wdXRlIGVuY29kaW5ncyBmb3IgYWxsIGRldGVjdGVkIGZhY2VzCiAgICAgICAgZmFjZV9lbmNvZGluZ3MgPSBmYWNlX3JlY29nbml0aW9uLmZhY2VfZW5jb2RpbmdzKHJnYl9zbWFsbCwgZmFjZV9sb2NhdGlvbnMpCgogICAgICAgIHJlc3VsdHMgPSBbXQogICAgICAgIGZvciBlbmNvZGluZywgbG9jYXRpb24gaW4gemlwKGZhY2VfZW5jb2RpbmdzLCBmYWNlX2xvY2F0aW9ucyk6CiAgICAgICAgICAgICMgQ29tcGFyZSBhZ2FpbnN0IGFsbCBrbm93biBlbmNvZGluZ3MKICAgICAgICAgICAgZGlzdGFuY2VzID0gZmFjZV9yZWNvZ25pdGlvbi5mYWNlX2Rpc3RhbmNlKHNlbGYua25vd25fZW5jb2RpbmdzLCBlbmNvZGluZykKCiAgICAgICAgICAgIGJlc3RfbWF0Y2hfaWR4ICA9IG5wLmFyZ21pbihkaXN0YW5jZXMpCiAgICAgICAgICAgIGJlc3RfZGlzdGFuY2UgICA9IGRpc3RhbmNlc1tiZXN0X21hdGNoX2lkeF0KICAgICAgICAgICAgY29uZmlkZW5jZSAgICAgID0gMS4wIC0gYmVzdF9kaXN0YW5jZSAgICMgY2xvc2VyIHRvIDEgPSBtb3JlIGNvbmZpZGVudAoKICAgICAgICAgICAgIyBTY2FsZSBsb2NhdGlvbiBiYWNrIHRvIGZ1bGwgZnJhbWUgc2l6ZQogICAgICAgICAgICB0b3AsIHJpZ2h0LCBib3R0b20sIGxlZnQgPSBsb2NhdGlvbgogICAgICAgICAgICB0b3AgICAgKj0gNAogICAgICAgICAgICByaWdodCAgKj0gNAogICAgICAgICAgICBib3R0b20gKj0gNAogICAgICAgICAgICBsZWZ0ICAgKj0gNAoKICAgICAgICAgICAgaWYgYmVzdF9kaXN0YW5jZSA8PSBzZWxmLnRvbGVyYW5jZToKICAgICAgICAgICAgICAgIHJlc3VsdHMuYXBwZW5kKHsKICAgICAgICAgICAgICAgICAgICAibmFtZSI6ICAgICAgIHNlbGYua25vd25fbmFtZXNbYmVzdF9tYXRjaF9pZHhdLAogICAgICAgICAgICAgICAgICAgICJ1c2VyX2lkIjogICAgc2VsZi5rbm93bl9pZHNbYmVzdF9tYXRjaF9pZHhdLAogICAgICAgICAgICAgICAgICAgICJjb25maWRlbmNlIjogcm91bmQoY29uZmlkZW5jZSwgMyksCiAgICAgICAgICAgICAgICAgICAgImxvY2F0aW9uIjogICAodG9wLCByaWdodCwgYm90dG9tLCBsZWZ0KSwKICAgICAgICAgICAgICAgIH0pCiAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICByZXN1bHRzLmFwcGVuZCh7CiAgICAgICAgICAgICAgICAgICAgIm5hbWUiOiAgICAgICAiVW5rbm93biIsCiAgICAgICAgICAgICAgICAgICAgInVzZXJfaWQiOiAgICAtMSwKICAgICAgICAgICAgICAgICAgICAiY29uZmlkZW5jZSI6IHJvdW5kKGNvbmZpZGVuY2UsIDMpLAogICAgICAgICAgICAgICAgICAgICJsb2NhdGlvbiI6ICAgKHRvcCwgcmlnaHQsIGJvdHRvbSwgbGVmdCksCiAgICAgICAgICAgICAgICB9KQoKICAgICAgICByZXR1cm4gcmVzdWx0cwoKICAgIGRlZiBkcmF3X3JlY29nbml0aW9uX3Jlc3VsdHMoc2VsZiwgZnJhbWU6IG5wLm5kYXJyYXksCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHJlc3VsdHM6IGxpc3QsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG1hcmtlZF90b2RheTogc2V0ID0gTm9uZSkgLT4gbnAubmRhcnJheToKICAgICAgICAiIiIKICAgICAgICBEcmF3IGJvdW5kaW5nIGJveGVzIGFuZCBsYWJlbHMgb24gYSBmcmFtZS4KCiAgICAgICAgQXJnczoKICAgICAgICAgICAgZnJhbWU6ICAgICAgICBCR1IgZnJhbWUgdG8gZHJhdyBvbgogICAgICAgICAgICByZXN1bHRzOiAgICAgIE91dHB1dCBvZiByZWNvZ25pemVfZmFjZXMoKQogICAgICAgICAgICBtYXJrZWRfdG9kYXk6IFNldCBvZiB1c2VyX2lkcyBhbHJlYWR5IG1hcmtlZCB0b2RheQoKICAgICAgICBSZXR1cm5zOgogICAgICAgICAgICBBbm5vdGF0ZWQgQkdSIGZyYW1lCiAgICAgICAgIiIiCiAgICAgICAgbWFya2VkX3RvZGF5ID0gbWFya2VkX3RvZGF5IG9yIHNldCgpCiAgICAgICAgb3ZlcmxheSAgICAgID0gZnJhbWUuY29weSgpCgogICAgICAgIGZvciByIGluIHJlc3VsdHM6CiAgICAgICAgICAgIHRvcCwgcmlnaHQsIGJvdHRvbSwgbGVmdCA9IHJbImxvY2F0aW9uIl0KICAgICAgICAgICAgbmFtZSAgICAgICA9IHJbIm5hbWUiXQogICAgICAgICAgICBjb25maWRlbmNlID0gclsiY29uZmlkZW5jZSJdCiAgICAgICAgICAgIHVzZXJfaWQgICAgPSByWyJ1c2VyX2lkIl0KICAgICAgICAgICAgYWxyZWFkeSAgICA9IHVzZXJfaWQgaW4gbWFya2VkX3RvZGF5CgogICAgICAgICAgICAjIENvbG9yIGNvZGluZwogICAgICAgICAgICBpZiBuYW1lID09ICJVbmtub3duIjoKICAgICAgICAgICAgICAgIGNvbG9yID0gKDAsIDUwLCAyNTUpICAgICMgUmVkLWlzaAogICAgICAgICAgICAgICAgbGFiZWwgPSAiVW5rbm93biIKICAgICAgICAgICAgZWxpZiBhbHJlYWR5OgogICAgICAgICAgICAgICAgY29sb3IgPSAoMCwgMjAwLCAyNTUpICAgIyBBbWJlciDigJQgYWxyZWFkeSBtYXJrZWQKICAgICAgICAgICAgICAgIGxhYmVsID0gZiJ7bmFtZX0g4pyTIChBbHJlYWR5IE1hcmtlZCkiCiAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICBjb2xvciA9ICgwLCAyMjAsIDgwKSAgICAjIEdyZWVuIOKAlCByZWNvZ25pemVkLCBub3QgeWV0IG1hcmtlZAogICAgICAgICAgICAgICAgbGFiZWwgPSBmIntuYW1lfSAoe2ludChjb25maWRlbmNlICogMTAwKX0lKSIKCiAgICAgICAgICAgICMgRHJhdyBmaWxsZWQgcmVjdGFuZ2xlIGZvciBsYWJlbCBiYWNrZ3JvdW5kCiAgICAgICAgICAgIGN2Mi5yZWN0YW5nbGUob3ZlcmxheSwgKGxlZnQsIHRvcCksIChyaWdodCwgYm90dG9tKSwgY29sb3IsIDIpCiAgICAgICAgICAgIGN2Mi5yZWN0YW5nbGUob3ZlcmxheSwgKGxlZnQsIGJvdHRvbSAtIDMwKSwgKHJpZ2h0LCBib3R0b20pLCBjb2xvciwgY3YyLkZJTExFRCkKICAgICAgICAgICAgY3YyLnB1dFRleHQob3ZlcmxheSwgbGFiZWwsCiAgICAgICAgICAgICAgICAgICAgICAgIChsZWZ0ICsgNiwgYm90dG9tIC0gOCksCiAgICAgICAgICAgICAgICAgICAgICAgIGN2Mi5GT05UX0hFUlNIRVlfU0lNUExFWCwgMC41NSwgKDI1NSwgMjU1LCAyNTUpLCAxKQoKICAgICAgICAjIEJsZW5kIG92ZXJsYXkgZm9yIHNlbWktdHJhbnNwYXJlbmN5CiAgICAgICAgcmV0dXJuIGN2Mi5hZGRXZWlnaHRlZChvdmVybGF5LCAwLjg1LCBmcmFtZSwgMC4xNSwgMCkKCiAgICAjIOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkAogICAgIyAgVVRJTElUSUVTCiAgICAjIOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkAoKICAgIGRlZiBnZXRfcmVnaXN0ZXJlZF9jb3VudChzZWxmKSAtPiBpbnQ6CiAgICAgICAgIiIiTnVtYmVyIG9mIHVzZXJzIGN1cnJlbnRseSBsb2FkZWQgaW4gbWVtb3J5LiIiIgogICAgICAgIHJldHVybiBsZW4oc2VsZi5rbm93bl9lbmNvZGluZ3MpCgogICAgZGVmIHJlbW92ZV91c2VyX2VuY29kaW5ncyhzZWxmLCB1c2VyX2lkOiBpbnQpIC0+IGJvb2w6CiAgICAgICAgIiIiUmVtb3ZlIGVuY29kaW5ncyBmb3IgYSBzcGVjaWZpYyB1c2VyIGFuZCByZXRyYWluLiIiIgogICAgICAgIGluZGljZXNfdG9fcmVtb3ZlID0gWwogICAgICAgICAgICBpIGZvciBpLCB1aWQgaW4gZW51bWVyYXRlKHNlbGYua25vd25faWRzKSBpZiB1aWQgPT0gdXNlcl9pZAogICAgICAgIF0KICAgICAgICBpZiBub3QgaW5kaWNlc190b19yZW1vdmU6CiAgICAgICAgICAgIHJldHVybiBGYWxzZQogICAgICAgIGZvciBpIGluIHNvcnRlZChpbmRpY2VzX3RvX3JlbW92ZSwgcmV2ZXJzZT1UcnVlKToKICAgICAgICAgICAgc2VsZi5rbm93bl9lbmNvZGluZ3MucG9wKGkpCiAgICAgICAgICAgIHNlbGYua25vd25faWRzLnBvcChpKQogICAgICAgICAgICBzZWxmLmtub3duX25hbWVzLnBvcChpKQogICAgICAgIHNlbGYuc2F2ZV9lbmNvZGluZ3MoKQogICAgICAgIHJldHVybiBUcnVlCgogICAgZGVmIHNldF90b2xlcmFuY2Uoc2VsZiwgdmFsdWU6IGZsb2F0KToKICAgICAgICAiIiJBZGp1c3QgcmVjb2duaXRpb24gdG9sZXJhbmNlICgwLjQgPSBzdHJpY3QsIDAuNiA9IGxlbmllbnQpLiIiIgogICAgICAgIHNlbGYudG9sZXJhbmNlID0gbWF4KDAuMywgbWluKDAuNywgdmFsdWUpKQogICAgICAgIGxvZ2dlci5pbmZvKGYiVG9sZXJhbmNlIHNldCB0byB7c2VsZi50b2xlcmFuY2V9IikKCgojIOKUgOKUgCBTaW5nbGV0b24gaW5zdGFuY2Ug4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACmVuZ2luZSA9IEZhY2VSZWNvZ25pdGlvbkVuZ2luZSgpCg==', 'face_recognition_engine/__init__.py': 'IyBGYWNlIHJlY29nbml0aW9uIGVuZ2luZSBwYWNrYWdlCg==', 'gui/sidebar.py': 'IiIiCuKVlOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVlwrilZEgICAgICAgICAgICAgIFNJREVCQVIg4oCUIEZhY2UgQXR0ZW5kYW5jZSBTeXN0ZW0gICAgICAgICAgICAgICDilZEK4pWRICBMZWZ0IG5hdmlnYXRpb24gcGFuZWwgd2l0aCBhbmltYXRlZCBob3ZlciBlZmZlY3RzICAgICAgICAgIOKVkQrilZrilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZ0KIiIiCgppbXBvcnQgY3VzdG9tdGtpbnRlciBhcyBjdGsKZnJvbSB1dGlscy5oZWxwZXJzIGltcG9ydCB0aGVtZV9tYW5hZ2VyCgoKIyDilIDilIAgTmF2aWdhdGlvbiBpdGVtczogKGljb24sIGxhYmVsLCBwYWdlX2tleSkg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACk5BVl9JVEVNUyA9IFsKICAgICgi8J+PoCIsICJEYXNoYm9hcmQiLCAgICAgICAiZGFzaGJvYXJkIiksCiAgICAoIvCfk7ciLCAiQXR0ZW5kYW5jZSIsICAgICAgImF0dGVuZGFuY2UiKSwKICAgICgi8J+RpCIsICJSZWdpc3RlciBVc2VyIiwgICAicmVnaXN0ZXIiKSwKICAgICgi8J+TiyIsICJWaWV3IFJlY29yZHMiLCAgICAicmVjb3JkcyIpLAogICAgKCLwn5OKIiwgIkFuYWx5dGljcyIsICAgICAgICJhbmFseXRpY3MiKSwKICAgICgi4pqZ77iPIiwgICJTZXR0aW5ncyIsICAgICAgICAic2V0dGluZ3MiKSwKXQoKCmNsYXNzIFNpZGViYXIoY3RrLkNUa0ZyYW1lKToKICAgICIiIgogICAgTGVmdC1zaWRlIG5hdmlnYXRpb24gc2lkZWJhci4KICAgIENhbGxzIG9uX25hdmlnYXRlKHBhZ2Vfa2V5KSB3aGVuIGEgbmF2IGl0ZW0gaXMgY2xpY2tlZC4KICAgICIiIgoKICAgIGRlZiBfX2luaXRfXyhzZWxmLCBwYXJlbnQsIG9uX25hdmlnYXRlLCAqKmt3YXJncyk6CiAgICAgICAgYyA9IHRoZW1lX21hbmFnZXIuY29sb3JzCiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygKICAgICAgICAgICAgcGFyZW50LAogICAgICAgICAgICB3aWR0aD0yMjAsCiAgICAgICAgICAgIGNvcm5lcl9yYWRpdXM9MCwKICAgICAgICAgICAgZmdfY29sb3I9Y1siYmdfc2lkZWJhciJdLAogICAgICAgICAgICAqKmt3YXJncwogICAgICAgICkKICAgICAgICBzZWxmLm9uX25hdmlnYXRlICAgPSBvbl9uYXZpZ2F0ZQogICAgICAgIHNlbGYuYWN0aXZlX2tleSAgICA9ICJkYXNoYm9hcmQiCiAgICAgICAgc2VsZi5fYnV0dG9ucyAgICAgID0ge30KCiAgICAgICAgc2VsZi5wYWNrX3Byb3BhZ2F0ZShGYWxzZSkKICAgICAgICBzZWxmLl9idWlsZF91aSgpCgogICAgZGVmIF9idWlsZF91aShzZWxmKToKICAgICAgICBjID0gdGhlbWVfbWFuYWdlci5jb2xvcnMKCiAgICAgICAgIyDilIDilIAgTG9nbyAvIEFwcCBOYW1lIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgAogICAgICAgIGxvZ29fZnJhbWUgPSBjdGsuQ1RrRnJhbWUoc2VsZiwgZmdfY29sb3I9InRyYW5zcGFyZW50IiwgaGVpZ2h0PTgwKQogICAgICAgIGxvZ29fZnJhbWUucGFjayhmaWxsPSJ4IiwgcGFkeD0wLCBwYWR5PTApCiAgICAgICAgbG9nb19mcmFtZS5wYWNrX3Byb3BhZ2F0ZShGYWxzZSkKCiAgICAgICAgY3RrLkNUa0xhYmVsKAogICAgICAgICAgICBsb2dvX2ZyYW1lLCB0ZXh0PSLwn5GBIEZhY2VUcmFjayIsCiAgICAgICAgICAgIGZvbnQ9Y3RrLkNUa0ZvbnQoZmFtaWx5PSJIZWx2ZXRpY2EgTmV1ZSIsIHNpemU9MjAsIHdlaWdodD0iYm9sZCIpLAogICAgICAgICAgICB0ZXh0X2NvbG9yPWNbInRleHRfcHJpbWFyeSJdCiAgICAgICAgKS5wYWNrKHBhZHk9KDIyLCAwKSkKCiAgICAgICAgY3RrLkNUa0xhYmVsKAogICAgICAgICAgICBsb2dvX2ZyYW1lLCB0ZXh0PSJQcm8iLAogICAgICAgICAgICBmb250PWN0ay5DVGtGb250KHNpemU9MTEpLAogICAgICAgICAgICB0ZXh0X2NvbG9yPWNbImFjY2VudCJdCiAgICAgICAgKS5wYWNrKHBhZHk9KDAsIDEwKSkKCiAgICAgICAgIyDilIDilIAgRGl2aWRlciDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIAKICAgICAgICBjdGsuQ1RrRnJhbWUoc2VsZiwgaGVpZ2h0PTEsIGZnX2NvbG9yPWNbImJvcmRlciJdKS5wYWNrKGZpbGw9IngiLCBwYWR4PTE2KQoKICAgICAgICAjIOKUgOKUgCBOYXZpZ2F0aW9uIEJ1dHRvbnMg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACiAgICAgICAgbmF2X2ZyYW1lID0gY3RrLkNUa0ZyYW1lKHNlbGYsIGZnX2NvbG9yPSJ0cmFuc3BhcmVudCIpCiAgICAgICAgbmF2X2ZyYW1lLnBhY2soZmlsbD0iYm90aCIsIGV4cGFuZD1UcnVlLCBwYWR5PSgxMiwgMCkpCgogICAgICAgIGZvciBpY29uLCBsYWJlbCwga2V5IGluIE5BVl9JVEVNUzoKICAgICAgICAgICAgYnRuID0gc2VsZi5fY3JlYXRlX25hdl9idXR0b24obmF2X2ZyYW1lLCBpY29uLCBsYWJlbCwga2V5KQogICAgICAgICAgICBzZWxmLl9idXR0b25zW2tleV0gPSBidG4KCiAgICAgICAgIyDilIDilIAgQm90dG9tOiBWZXJzaW9uIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgAogICAgICAgIGN0ay5DVGtMYWJlbCgKICAgICAgICAgICAgc2VsZiwgdGV4dD0idjIuMC4wIFByb2Zlc3Npb25hbCIsCiAgICAgICAgICAgIGZvbnQ9Y3RrLkNUa0ZvbnQoc2l6ZT0xMCksCiAgICAgICAgICAgIHRleHRfY29sb3I9Y1sidGV4dF9tdXRlZCJdCiAgICAgICAgKS5wYWNrKHNpZGU9ImJvdHRvbSIsIHBhZHk9MTIpCgogICAgICAgICMgU2V0IGluaXRpYWwgYWN0aXZlIHN0YXRlCiAgICAgICAgc2VsZi5fc2V0X2FjdGl2ZSgiZGFzaGJvYXJkIikKCiAgICBkZWYgX2NyZWF0ZV9uYXZfYnV0dG9uKHNlbGYsIHBhcmVudCwgaWNvbjogc3RyLCBsYWJlbDogc3RyLCBrZXk6IHN0cik6CiAgICAgICAgIiIiQ3JlYXRlIGEgc2luZ2xlIG5hdmlnYXRpb24gYnV0dG9uIHdpdGggaG92ZXIgYW5pbWF0aW9uLiIiIgogICAgICAgIGMgICA9IHRoZW1lX21hbmFnZXIuY29sb3JzCiAgICAgICAgYnRuID0gY3RrLkNUa0J1dHRvbigKICAgICAgICAgICAgcGFyZW50LAogICAgICAgICAgICB0ZXh0PWYiICB7aWNvbn0gICB7bGFiZWx9IiwKICAgICAgICAgICAgZm9udD1jdGsuQ1RrRm9udChmYW1pbHk9IkhlbHZldGljYSBOZXVlIiwgc2l6ZT0xMywgd2VpZ2h0PSJib2xkIiksCiAgICAgICAgICAgIGZnX2NvbG9yPSJ0cmFuc3BhcmVudCIsCiAgICAgICAgICAgIHRleHRfY29sb3I9Y1sidGV4dF9zZWNvbmRhcnkiXSwKICAgICAgICAgICAgaG92ZXJfY29sb3I9Y1siYmdfaG92ZXIiXSwKICAgICAgICAgICAgYW5jaG9yPSJ3IiwKICAgICAgICAgICAgaGVpZ2h0PTQ0LAogICAgICAgICAgICBjb3JuZXJfcmFkaXVzPTgsCiAgICAgICAgICAgIGNvbW1hbmQ9bGFtYmRhIGs9a2V5OiBzZWxmLl9vbl9jbGljayhrKQogICAgICAgICkKICAgICAgICBidG4ucGFjayhmaWxsPSJ4IiwgcGFkeD0xMiwgcGFkeT0yKQogICAgICAgIHJldHVybiBidG4KCiAgICBkZWYgX29uX2NsaWNrKHNlbGYsIGtleTogc3RyKToKICAgICAgICBzZWxmLl9zZXRfYWN0aXZlKGtleSkKICAgICAgICBzZWxmLm9uX25hdmlnYXRlKGtleSkKCiAgICBkZWYgX3NldF9hY3RpdmUoc2VsZiwga2V5OiBzdHIpOgogICAgICAgICIiIkhpZ2hsaWdodCB0aGUgYWN0aXZlIG5hdmlnYXRpb24gaXRlbS4iIiIKICAgICAgICBjID0gdGhlbWVfbWFuYWdlci5jb2xvcnMKICAgICAgICAjIERlYWN0aXZhdGUgYWxsCiAgICAgICAgZm9yIGssIGJ0biBpbiBzZWxmLl9idXR0b25zLml0ZW1zKCk6CiAgICAgICAgICAgIGJ0bi5jb25maWd1cmUoCiAgICAgICAgICAgICAgICBmZ19jb2xvcj0idHJhbnNwYXJlbnQiLAogICAgICAgICAgICAgICAgdGV4dF9jb2xvcj1jWyJ0ZXh0X3NlY29uZGFyeSJdCiAgICAgICAgICAgICkKICAgICAgICAjIEFjdGl2YXRlIHNlbGVjdGVkCiAgICAgICAgaWYga2V5IGluIHNlbGYuX2J1dHRvbnM6CiAgICAgICAgICAgIHNlbGYuX2J1dHRvbnNba2V5XS5jb25maWd1cmUoCiAgICAgICAgICAgICAgICBmZ19jb2xvcj1jWyJzaWRlYmFyX2FjdGl2ZSJdLAogICAgICAgICAgICAgICAgdGV4dF9jb2xvcj1jWyJ0ZXh0X3ByaW1hcnkiXQogICAgICAgICAgICApCiAgICAgICAgICAgIHNlbGYuYWN0aXZlX2tleSA9IGtleQoKICAgIGRlZiByZWZyZXNoX3RoZW1lKHNlbGYpOgogICAgICAgICIiIlJlLWFwcGx5IHRoZW1lIGNvbG9ycyAoY2FsbGVkIG9uIHRoZW1lIHRvZ2dsZSkuIiIiCiAgICAgICAgYyA9IHRoZW1lX21hbmFnZXIuY29sb3JzCiAgICAgICAgc2VsZi5jb25maWd1cmUoZmdfY29sb3I9Y1siYmdfc2lkZWJhciJdKQogICAgICAgIHNlbGYuX3NldF9hY3RpdmUoc2VsZi5hY3RpdmVfa2V5KQo=', 'gui/notification.py': 'IiIiCuKVlOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVlwrilZEgICAgICAgICAgTk9USUZJQ0FUSU9OIOKAlCBGYWNlIEF0dGVuZGFuY2UgU3lzdGVtICAgICAgICAgICAgICDilZEK4pWRICBUb2FzdC1zdHlsZSBwb3B1cCBub3RpZmljYXRpb25zICAgICAgICAgICAgICAgICAgICAgICAgICAgIOKVkQrilZrilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZ0KIiIiCgppbXBvcnQgY3VzdG9tdGtpbnRlciBhcyBjdGsKaW1wb3J0IHRocmVhZGluZwppbXBvcnQgdGltZQoKY2xhc3MgVG9hc3ROb3RpZmljYXRpb246CiAgICAiIiIKICAgIERpc3BsYXlzIGEgZmxvYXRpbmcgdG9hc3Qtc3R5bGUgbm90aWZpY2F0aW9uIGluIHRoZSBib3R0b20tcmlnaHQgY29ybmVyLgogICAgQXV0by1kaXNtaXNzZXMgYWZ0ZXIgYSBzZXQgZHVyYXRpb24uCiAgICAKICAgIFVzYWdlOgogICAgICAgIFRvYXN0Tm90aWZpY2F0aW9uKHJvb3QsICJBdHRlbmRhbmNlIE1hcmtlZCEiLCB0eXBlXz0ic3VjY2VzcyIpCiAgICAiIiIKCiAgICBkZWYgX19pbml0X18oc2VsZiwgcGFyZW50LCBtZXNzYWdlOiBzdHIsIHR5cGVfOiBzdHIgPSAiaW5mbyIsIGR1cmF0aW9uOiBmbG9hdCA9IDMuMCk6CiAgICAgICAgIiIiCiAgICAgICAgQXJnczoKICAgICAgICAgICAgcGFyZW50OiAgIFRoZSByb290L3BhcmVudCBUa2ludGVyIHdpbmRvdy4KICAgICAgICAgICAgbWVzc2FnZTogIFRoZSB0ZXh0IHRvIGRpc3BsYXkuCiAgICAgICAgICAgIHR5cGVfOiAgICBPbmUgb2YgJ3N1Y2Nlc3MnLCAnZXJyb3InLCAnd2FybmluZycsICdpbmZvJy4KICAgICAgICAgICAgZHVyYXRpb246IFNlY29uZHMgYmVmb3JlIGF1dG8tZGlzbWlzcy4KICAgICAgICAiIiIKICAgICAgICBzZWxmLnBhcmVudCAgID0gcGFyZW50CiAgICAgICAgc2VsZi5tZXNzYWdlICA9IG1lc3NhZ2UKICAgICAgICBzZWxmLnR5cGVfICAgID0gdHlwZV8KICAgICAgICBzZWxmLmR1cmF0aW9uID0gZHVyYXRpb24KCiAgICAgICAgIyBDb2xvciBtYXBwaW5nCiAgICAgICAgY29sb3JzID0gewogICAgICAgICAgICAic3VjY2VzcyI6ICgiIzNGQjk1MCIsICLinIUiKSwKICAgICAgICAgICAgImVycm9yIjogICAoIiNGODUxNDkiLCAi4p2MIiksCiAgICAgICAgICAgICJ3YXJuaW5nIjogKCIjRDI5OTIyIiwgIuKaoO+4jyIpLAogICAgICAgICAgICAiaW5mbyI6ICAgICgiIzIxODhGRiIsICLihLnvuI8iKSwKICAgICAgICB9CiAgICAgICAgc2VsZi5jb2xvciwgc2VsZi5pY29uID0gY29sb3JzLmdldCh0eXBlXywgY29sb3JzWyJpbmZvIl0pCgogICAgICAgIHNlbGYuX2J1aWxkKCkKCiAgICBkZWYgX2J1aWxkKHNlbGYpOgogICAgICAgICMgQ3JlYXRlIGEgVG9wbGV2ZWwgd2luZG93IChubyB0aXRsZSBiYXIpCiAgICAgICAgc2VsZi50b2FzdCA9IGN0ay5DVGtUb3BsZXZlbChzZWxmLnBhcmVudCkKICAgICAgICBzZWxmLnRvYXN0Lm92ZXJyaWRlcmVkaXJlY3QoVHJ1ZSkKICAgICAgICBzZWxmLnRvYXN0LmF0dHJpYnV0ZXMoIi10b3Btb3N0IiwgVHJ1ZSkKICAgICAgICBzZWxmLnRvYXN0LmNvbmZpZ3VyZShmZ19jb2xvcj0iIzFDMjMzMyIpCiAgICAgICAgc2VsZi50b2FzdC5hdHRyaWJ1dGVzKCItYWxwaGEiLCAwLjApICAjIFN0YXJ0IGludmlzaWJsZQoKICAgICAgICAjIENvbnRlbnQKICAgICAgICBmcmFtZSA9IGN0ay5DVGtGcmFtZShzZWxmLnRvYXN0LCBmZ19jb2xvcj0iIzFDMjMzMyIsIGNvcm5lcl9yYWRpdXM9MTAsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGJvcmRlcl93aWR0aD0xLCBib3JkZXJfY29sb3I9c2VsZi5jb2xvcikKICAgICAgICBmcmFtZS5wYWNrKHBhZHg9MiwgcGFkeT0yKQoKICAgICAgICBjdGsuQ1RrTGFiZWwoZnJhbWUsIHRleHQ9c2VsZi5pY29uLCBmb250PWN0ay5DVGtGb250KHNpemU9MTgpKS5wYWNrKAogICAgICAgICAgICBzaWRlPSJsZWZ0IiwgcGFkeD0oMTUsIDUpLCBwYWR5PTEyCiAgICAgICAgKQogICAgICAgIGN0ay5DVGtMYWJlbCgKICAgICAgICAgICAgZnJhbWUsIHRleHQ9c2VsZi5tZXNzYWdlLAogICAgICAgICAgICBmb250PWN0ay5DVGtGb250KGZhbWlseT0iSGVsdmV0aWNhIE5ldWUiLCBzaXplPTEzKSwKICAgICAgICAgICAgdGV4dF9jb2xvcj0iI0U2RURGMyIsCiAgICAgICAgICAgIHdyYXBsZW5ndGg9MjYwCiAgICAgICAgKS5wYWNrKHNpZGU9ImxlZnQiLCBwYWR4PSgwLCAxNSksIHBhZHk9MTIpCgogICAgICAgIHNlbGYudG9hc3QudXBkYXRlX2lkbGV0YXNrcygpCiAgICAgICAgdyA9IHNlbGYudG9hc3Qud2luZm9fcmVxd2lkdGgoKQogICAgICAgIGggPSBzZWxmLnRvYXN0LndpbmZvX3JlcWhlaWdodCgpCiAgICAgICAgc3cgPSBzZWxmLnBhcmVudC53aW5mb19zY3JlZW53aWR0aCgpCiAgICAgICAgc2ggPSBzZWxmLnBhcmVudC53aW5mb19zY3JlZW5oZWlnaHQoKQoKICAgICAgICAjIFBvc2l0aW9uOiBib3R0b20tcmlnaHQKICAgICAgICB4ID0gc3cgLSB3IC0gMjAKICAgICAgICB5ID0gc2ggLSBoIC0gNjAKICAgICAgICBzZWxmLnRvYXN0Lmdlb21ldHJ5KGYiK3t4fSt7eX0iKQoKICAgICAgICAjIEZhZGUtaW4gdGhlbiBhdXRvLWRpc21pc3MKICAgICAgICB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1zZWxmLl9hbmltYXRlLCBkYWVtb249VHJ1ZSkuc3RhcnQoKQoKICAgIGRlZiBfYW5pbWF0ZShzZWxmKToKICAgICAgICAiIiJGYWRlIGluIOKGkiB3YWl0IOKGkiBmYWRlIG91dC4iIiIKICAgICAgICAjIEZhZGUgaW4KICAgICAgICBmb3IgaSBpbiByYW5nZSgxLCAxMSk6CiAgICAgICAgICAgIHNlbGYudG9hc3QuYWZ0ZXIoMCwgbGFtYmRhIHY9aS8xMDogc2VsZi50b2FzdC5hdHRyaWJ1dGVzKCItYWxwaGEiLCB2KSkKICAgICAgICAgICAgdGltZS5zbGVlcCgwLjAzKQoKICAgICAgICB0aW1lLnNsZWVwKHNlbGYuZHVyYXRpb24pCgogICAgICAgICMgRmFkZSBvdXQKICAgICAgICBmb3IgaSBpbiByYW5nZSgxMCwgMCwgLTEpOgogICAgICAgICAgICBzZWxmLnRvYXN0LmFmdGVyKDAsIGxhbWJkYSB2PWkvMTA6IHNlbGYudG9hc3QuYXR0cmlidXRlcygiLWFscGhhIiwgdikpCiAgICAgICAgICAgIHRpbWUuc2xlZXAoMC4wMykKCiAgICAgICAgc2VsZi50b2FzdC5hZnRlcigwLCBzZWxmLnRvYXN0LmRlc3Ryb3kpCg==', 'gui/__init__.py': 'IyBHVUkgcGFja2FnZQo=', 'gui/splash_screen.py': 'IiIiCuKVlOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVlwrilZEgICAgICAgICAgU1BMQVNIIFNDUkVFTiDigJQgRmFjZSBBdHRlbmRhbmNlIFN5c3RlbSAgICAgICAgICAgICDilZEK4pWRICBQcm9mZXNzaW9uYWwgc3RhcnR1cCBzY3JlZW4gd2l0aCBhbmltYXRlZCBwcm9ncmVzcyBiYXIgICAgIOKVkQrilZrilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZ0KIiIiCgppbXBvcnQgY3VzdG9tdGtpbnRlciBhcyBjdGsKaW1wb3J0IHRraW50ZXIgYXMgdGsKZnJvbSB0a2ludGVyIGltcG9ydCBmb250IGFzIHRrZm9udAppbXBvcnQgdGhyZWFkaW5nCmltcG9ydCB0aW1lCgoKY2xhc3MgU3BsYXNoU2NyZWVuKGN0ay5DVGtUb3BsZXZlbCk6CiAgICAiIiIKICAgIEFuaW1hdGVkIHNwbGFzaCBzY3JlZW4gc2hvd24gd2hpbGUgdGhlIGFwcCBsb2Fkcy4KICAgIEF1dG9tYXRpY2FsbHkgY2xvc2VzIGFuZCBjYWxscyBvbl9jb21wbGV0ZSB3aGVuIGxvYWRpbmcgZmluaXNoZXMuCiAgICAiIiIKCiAgICBkZWYgX19pbml0X18oc2VsZiwgcGFyZW50LCBvbl9jb21wbGV0ZSk6CiAgICAgICAgc3VwZXIoKS5fX2luaXRfXyhwYXJlbnQpCiAgICAgICAgc2VsZi5vbl9jb21wbGV0ZSA9IG9uX2NvbXBsZXRlCiAgICAgICAgc2VsZi5fcHJvZ3Jlc3MgICA9IDAuMAogICAgICAgIHNlbGYuX3Rhc2tzICAgICAgPSBbXQoKICAgICAgICBzZWxmLl9zZXR1cF93aW5kb3coKQogICAgICAgIHNlbGYuX2J1aWxkX3VpKCkKICAgICAgICBzZWxmLl9zdGFydF9sb2FkaW5nKCkKCiAgICBkZWYgX3NldHVwX3dpbmRvdyhzZWxmKToKICAgICAgICAiIiJDb25maWd1cmUgc3BsYXNoIHdpbmRvdzogbm8gdGl0bGUgYmFyLCBjZW50ZXJlZCwgYWx3YXlzIG9uIHRvcC4iIiIKICAgICAgICBzZWxmLm92ZXJyaWRlcmVkaXJlY3QoVHJ1ZSkgICAgICAgIyBObyB0aXRsZSBiYXIKICAgICAgICBzZWxmLmF0dHJpYnV0ZXMoIi10b3Btb3N0IiwgVHJ1ZSkKCiAgICAgICAgdywgaCA9IDUyMCwgMzQwCiAgICAgICAgc3cgICA9IHNlbGYud2luZm9fc2NyZWVud2lkdGgoKQogICAgICAgIHNoICAgPSBzZWxmLndpbmZvX3NjcmVlbmhlaWdodCgpCiAgICAgICAgeCAgICA9IChzdyAtIHcpIC8vIDIKICAgICAgICB5ICAgID0gKHNoIC0gaCkgLy8gMgogICAgICAgIHNlbGYuZ2VvbWV0cnkoZiJ7d314e2h9K3t4fSt7eX0iKQogICAgICAgIHNlbGYuY29uZmlndXJlKGZnX2NvbG9yPSIjMEQxMTE3IikKICAgICAgICBzZWxmLnJlc2l6YWJsZShGYWxzZSwgRmFsc2UpCgogICAgICAgICMgUm91bmRlZCBjb3JuZXJzIG9uIG1hY09TCiAgICAgICAgdHJ5OgogICAgICAgICAgICBzZWxmLmF0dHJpYnV0ZXMoIi10cmFuc3BhcmVudCIsIFRydWUpCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAgICAgcGFzcwoKICAgIGRlZiBfYnVpbGRfdWkoc2VsZik6CiAgICAgICAgIiIiQnVpbGQgYWxsIFVJIGVsZW1lbnRzLiIiIgogICAgICAgICMg4pSA4pSAIEJhY2tncm91bmQgZ3JhZGllbnQgZnJhbWUg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACiAgICAgICAgbWFpbiA9IGN0ay5DVGtGcmFtZShzZWxmLCBmZ19jb2xvcj0iIzBEMTExNyIsIGNvcm5lcl9yYWRpdXM9MTYpCiAgICAgICAgbWFpbi5wYWNrKGZpbGw9ImJvdGgiLCBleHBhbmQ9VHJ1ZSwgcGFkeD0yLCBwYWR5PTIpCgogICAgICAgICMg4pSA4pSAIEFjY2VudCB0b3AgYm9yZGVyIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgAogICAgICAgIGFjY2VudCA9IGN0ay5DVGtGcmFtZShtYWluLCBmZ19jb2xvcj0iIzIxODhGRiIsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBoZWlnaHQ9NCwgY29ybmVyX3JhZGl1cz0wKQogICAgICAgIGFjY2VudC5wYWNrKGZpbGw9IngiLCBzaWRlPSJ0b3AiKQoKICAgICAgICAjIOKUgOKUgCBMb2dvIC8gSWNvbiDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIAKICAgICAgICBjdGsuQ1RrTGFiZWwobWFpbiwgdGV4dD0i8J+RgSIsCiAgICAgICAgICAgICAgICAgICAgIGZvbnQ9Y3RrLkNUa0ZvbnQoc2l6ZT02NCkpLnBhY2socGFkeT0oMzAsIDApKQoKICAgICAgICAjIOKUgOKUgCBBcHAgVGl0bGUg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACiAgICAgICAgY3RrLkNUa0xhYmVsKG1haW4sIHRleHQ9IkZhY2VUcmFjayBQcm8iLAogICAgICAgICAgICAgICAgICAgICBmb250PWN0ay5DVGtGb250KGZhbWlseT0iSGVsdmV0aWNhIE5ldWUiLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHNpemU9MzIsIHdlaWdodD0iYm9sZCIpLAogICAgICAgICAgICAgICAgICAgICB0ZXh0X2NvbG9yPSIjRTZFREYzIikucGFjayhwYWR5PSg4LCAyKSkKCiAgICAgICAgIyDilIDilIAgU3VidGl0bGUg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACiAgICAgICAgY3RrLkNUa0xhYmVsKG1haW4sIHRleHQ9IkFJLVBvd2VyZWQgQXR0ZW5kYW5jZSBTeXN0ZW0iLAogICAgICAgICAgICAgICAgICAgICBmb250PWN0ay5DVGtGb250KHNpemU9MTQpLAogICAgICAgICAgICAgICAgICAgICB0ZXh0X2NvbG9yPSIjOEI5NDlFIikucGFjaygpCgogICAgICAgICMg4pSA4pSAIFZlcnNpb24g4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACiAgICAgICAgY3RrLkNUa0xhYmVsKG1haW4sIHRleHQ9InYyLjAuMCAg4oCiICBQcm9mZXNzaW9uYWwgRWRpdGlvbiIsCiAgICAgICAgICAgICAgICAgICAgIGZvbnQ9Y3RrLkNUa0ZvbnQoc2l6ZT0xMSksCiAgICAgICAgICAgICAgICAgICAgIHRleHRfY29sb3I9IiM0ODRGNTgiKS5wYWNrKHBhZHk9KDQsIDApKQoKICAgICAgICAjIOKUgOKUgCBQcm9ncmVzcyBCYXIg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACiAgICAgICAgcHJvZ3Jlc3NfZnJhbWUgPSBjdGsuQ1RrRnJhbWUobWFpbiwgZmdfY29sb3I9InRyYW5zcGFyZW50IikKICAgICAgICBwcm9ncmVzc19mcmFtZS5wYWNrKGZpbGw9IngiLCBwYWR4PTUwLCBwYWR5PSgzMCwgOCkpCgogICAgICAgIHNlbGYucHJvZ3Jlc3NfYmFyID0gY3RrLkNUa1Byb2dyZXNzQmFyKAogICAgICAgICAgICBwcm9ncmVzc19mcmFtZSwKICAgICAgICAgICAgbW9kZT0iZGV0ZXJtaW5hdGUiLAogICAgICAgICAgICBoZWlnaHQ9NiwKICAgICAgICAgICAgY29ybmVyX3JhZGl1cz0zLAogICAgICAgICAgICBmZ19jb2xvcj0iIzIxMjYyRCIsCiAgICAgICAgICAgIHByb2dyZXNzX2NvbG9yPSIjMjE4OEZGIiwKICAgICAgICApCiAgICAgICAgc2VsZi5wcm9ncmVzc19iYXIucGFjayhmaWxsPSJ4IikKICAgICAgICBzZWxmLnByb2dyZXNzX2Jhci5zZXQoMCkKCiAgICAgICAgIyDilIDilIAgU3RhdHVzIExhYmVsIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgAogICAgICAgIHNlbGYuc3RhdHVzX2xhYmVsID0gY3RrLkNUa0xhYmVsKAogICAgICAgICAgICBtYWluLAogICAgICAgICAgICB0ZXh0PSJJbml0aWFsaXppbmcuLi4iLAogICAgICAgICAgICBmb250PWN0ay5DVGtGb250KHNpemU9MTIpLAogICAgICAgICAgICB0ZXh0X2NvbG9yPSIjOEI5NDlFIgogICAgICAgICkKICAgICAgICBzZWxmLnN0YXR1c19sYWJlbC5wYWNrKCkKCiAgICAgICAgIyDilIDilIAgRm9vdGVyIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgAogICAgICAgIGN0ay5DVGtMYWJlbChtYWluLCB0ZXh0PSLCqSAyMDI0IEZhY2VUcmFjayBQcm8gIOKAoiAgQWxsIHJpZ2h0cyByZXNlcnZlZCIsCiAgICAgICAgICAgICAgICAgICAgIGZvbnQ9Y3RrLkNUa0ZvbnQoc2l6ZT0xMCksCiAgICAgICAgICAgICAgICAgICAgIHRleHRfY29sb3I9IiMyMTI2MkQiKS5wYWNrKHNpZGU9ImJvdHRvbSIsIHBhZHk9MTIpCgogICAgZGVmIF9zdGFydF9sb2FkaW5nKHNlbGYpOgogICAgICAgICIiIlJ1biBsb2FkaW5nIHRhc2tzIGluIGEgYmFja2dyb3VuZCB0aHJlYWQuIiIiCiAgICAgICAgc2VsZi5fdGFza3MgPSBbCiAgICAgICAgICAgICgwLjEwLCAiTG9hZGluZyBjb25maWd1cmF0aW9uLi4uIiksCiAgICAgICAgICAgICgwLjI1LCAiQ29ubmVjdGluZyB0byBkYXRhYmFzZS4uLiIpLAogICAgICAgICAgICAoMC40NSwgIkxvYWRpbmcgZmFjZSBlbmNvZGluZ3MuLi4iKSwKICAgICAgICAgICAgKDAuNjUsICJJbml0aWFsaXppbmcgY2FtZXJhLi4uIiksCiAgICAgICAgICAgICgwLjgwLCAiQnVpbGRpbmcgaW50ZXJmYWNlLi4uIiksCiAgICAgICAgICAgICgwLjk1LCAiQWxtb3N0IHJlYWR5Li4uIiksCiAgICAgICAgICAgICgxLjAwLCAiV2VsY29tZSB0byBGYWNlVHJhY2sgUHJvISIpLAogICAgICAgIF0KICAgICAgICB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1zZWxmLl9ydW5fdGFza3MsIGRhZW1vbj1UcnVlKS5zdGFydCgpCgogICAgZGVmIF9ydW5fdGFza3Moc2VsZik6CiAgICAgICAgIiIiU2ltdWxhdGUgbG9hZGluZyB0YXNrcyB3aXRoIHNtb290aCBwcm9ncmVzcyBhbmltYXRpb24uIiIiCiAgICAgICAgZm9yIHByb2dyZXNzLCBtZXNzYWdlIGluIHNlbGYuX3Rhc2tzOgogICAgICAgICAgICAjIEFuaW1hdGUgdG8gdGFyZ2V0IHByb2dyZXNzIHNtb290aGx5CiAgICAgICAgICAgIHN0ZXBzID0gMjAKICAgICAgICAgICAgc3RhcnQgPSBzZWxmLl9wcm9ncmVzcwogICAgICAgICAgICBkZWx0YSA9IChwcm9ncmVzcyAtIHN0YXJ0KSAvIHN0ZXBzCiAgICAgICAgICAgIGZvciBfIGluIHJhbmdlKHN0ZXBzKToKICAgICAgICAgICAgICAgIHNlbGYuX3Byb2dyZXNzICs9IGRlbHRhCiAgICAgICAgICAgICAgICBzZWxmLl91cGRhdGVfcHJvZ3Jlc3Moc2VsZi5fcHJvZ3Jlc3MsIG1lc3NhZ2UpCiAgICAgICAgICAgICAgICB0aW1lLnNsZWVwKDAuMDMpCgogICAgICAgIHRpbWUuc2xlZXAoMC40KQogICAgICAgIHNlbGYuX2ZpbmlzaCgpCgogICAgZGVmIF91cGRhdGVfcHJvZ3Jlc3Moc2VsZiwgdmFsdWU6IGZsb2F0LCBtZXNzYWdlOiBzdHIpOgogICAgICAgICIiIlRocmVhZC1zYWZlIFVJIHVwZGF0ZS4iIiIKICAgICAgICB0cnk6CiAgICAgICAgICAgIHNlbGYuYWZ0ZXIoMCwgbGFtYmRhOiBzZWxmLnByb2dyZXNzX2Jhci5zZXQodmFsdWUpKQogICAgICAgICAgICBzZWxmLmFmdGVyKDAsIGxhbWJkYTogc2VsZi5zdGF0dXNfbGFiZWwuY29uZmlndXJlKHRleHQ9bWVzc2FnZSkpCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAgICAgcGFzcwoKICAgIGRlZiBfZmluaXNoKHNlbGYpOgogICAgICAgICIiIkNsb3NlIHNwbGFzaCBhbmQgY2FsbCBvbl9jb21wbGV0ZSBjYWxsYmFjay4iIiIKICAgICAgICB0cnk6CiAgICAgICAgICAgIHNlbGYuYWZ0ZXIoMjAwLCBzZWxmLl9jbG9zZSkKICAgICAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgICAgICBwYXNzCgogICAgZGVmIF9jbG9zZShzZWxmKToKICAgICAgICB0cnk6CiAgICAgICAgICAgIHNlbGYub25fY29tcGxldGUoKQogICAgICAgICAgICBzZWxmLmRlc3Ryb3koKQogICAgICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgICAgIHBhc3MK', 'gui/admin_login.py': 'IiIiCuKVlOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVlwrilZEgICAgICAgICAgIEFETUlOIExPR0lOIERJQUxPRyDigJQgRmFjZSBBdHRlbmRhbmNlIFN5c3RlbSAgICAgICDilZEK4pWRICBTaW1wbGUgcGFzc3dvcmQtcHJvdGVjdGVkIGdhdGUgYmVmb3JlIGFkbWluIGFyZWFzICAgICAgICAgIOKVkQrilZrilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZ0KIiIiCgppbXBvcnQgY3VzdG9tdGtpbnRlciBhcyBjdGsKZnJvbSBkYXRhYmFzZS5kYl9tYW5hZ2VyIGltcG9ydCBkYgpmcm9tIHV0aWxzLmhlbHBlcnMgaW1wb3J0IHRoZW1lX21hbmFnZXIKCgpjbGFzcyBBZG1pbkxvZ2luRGlhbG9nKGN0ay5DVGtUb3BsZXZlbCk6CiAgICAiIiIKICAgIEEgbW9kYWwgYWRtaW4gbG9naW4gZGlhbG9nLgogICAgCiAgICBVc2FnZToKICAgICAgICBkaWFsb2cgPSBBZG1pbkxvZ2luRGlhbG9nKHBhcmVudCkKICAgICAgICBwYXJlbnQud2FpdF93aW5kb3coZGlhbG9nKQogICAgICAgIGlmIGRpYWxvZy5hdXRoZW50aWNhdGVkOgogICAgICAgICAgICAuLi4gIyBwcm9jZWVkCiAgICAiIiIKCiAgICBkZWYgX19pbml0X18oc2VsZiwgcGFyZW50KToKICAgICAgICBzdXBlcigpLl9faW5pdF9fKHBhcmVudCkKICAgICAgICBzZWxmLmF1dGhlbnRpY2F0ZWQgPSBGYWxzZQogICAgICAgIHNlbGYuX2F0dGVtcHRzICAgICA9IDAKICAgICAgICBzZWxmLl9tYXhfYXR0ZW1wdHMgPSAzCgogICAgICAgIHNlbGYuX3NldHVwX3dpbmRvdygpCiAgICAgICAgc2VsZi5fYnVpbGRfdWkoKQogICAgICAgIHNlbGYuZ3JhYl9zZXQoKSAgICAgICAgICAgIyBNYWtlIG1vZGFsCiAgICAgICAgc2VsZi5lbnRfcGFzc3dvcmQuZm9jdXMoKSAjIEZvY3VzIHBhc3N3b3JkIGZpZWxkCgogICAgZGVmIF9zZXR1cF93aW5kb3coc2VsZik6CiAgICAgICAgc2VsZi50aXRsZSgiQWRtaW4gQXV0aGVudGljYXRpb24iKQogICAgICAgIHNlbGYuZ2VvbWV0cnkoIjQwMHgzMDAiKQogICAgICAgIHNlbGYucmVzaXphYmxlKEZhbHNlLCBGYWxzZSkKICAgICAgICBjID0gdGhlbWVfbWFuYWdlci5jb2xvcnMKICAgICAgICBzZWxmLmNvbmZpZ3VyZShmZ19jb2xvcj1jWyJiZ19zZWNvbmRhcnkiXSkKICAgICAgICBzZWxmLmF0dHJpYnV0ZXMoIi10b3Btb3N0IiwgVHJ1ZSkKCiAgICAgICAgIyBDZW50ZXIgb24gcGFyZW50CiAgICAgICAgc2VsZi51cGRhdGVfaWRsZXRhc2tzKCkKICAgICAgICBwdywgcGggPSBzZWxmLndpbmZvX3JlcXdpZHRoKCksIHNlbGYud2luZm9fcmVxaGVpZ2h0KCkKICAgICAgICBweCA9IHNlbGYubWFzdGVyLndpbmZvX3Jvb3R4KCkgKyAoc2VsZi5tYXN0ZXIud2luZm9fd2lkdGgoKSAgLSBwdykgLy8gMgogICAgICAgIHB5ID0gc2VsZi5tYXN0ZXIud2luZm9fcm9vdHkoKSArIChzZWxmLm1hc3Rlci53aW5mb19oZWlnaHQoKSAtIHBoKSAvLyAyCiAgICAgICAgc2VsZi5nZW9tZXRyeShmIit7cHh9K3tweX0iKQoKICAgIGRlZiBfYnVpbGRfdWkoc2VsZik6CiAgICAgICAgYyA9IHRoZW1lX21hbmFnZXIuY29sb3JzCgogICAgICAgIGN0ay5DVGtMYWJlbCgKICAgICAgICAgICAgc2VsZiwgdGV4dD0i8J+UkCAgQWRtaW4gTG9naW4iLAogICAgICAgICAgICBmb250PXRoZW1lX21hbmFnZXIuZm9udCgiaGVhZGluZ19tZCIpLAogICAgICAgICAgICB0ZXh0X2NvbG9yPWNbInRleHRfcHJpbWFyeSJdCiAgICAgICAgKS5wYWNrKHBhZHk9KDM1LCA1KSkKCiAgICAgICAgY3RrLkNUa0xhYmVsKAogICAgICAgICAgICBzZWxmLCB0ZXh0PSJFbnRlciB0aGUgYWRtaW4gcGFzc3dvcmQgdG8gY29udGludWUuIiwKICAgICAgICAgICAgZm9udD10aGVtZV9tYW5hZ2VyLmZvbnQoImJvZHlfc20iKSwKICAgICAgICAgICAgdGV4dF9jb2xvcj1jWyJ0ZXh0X3NlY29uZGFyeSJdCiAgICAgICAgKS5wYWNrKHBhZHk9KDAsIDI1KSkKCiAgICAgICAgc2VsZi5lbnRfcGFzc3dvcmQgPSBjdGsuQ1RrRW50cnkoCiAgICAgICAgICAgIHNlbGYsIHBsYWNlaG9sZGVyX3RleHQ9IlBhc3N3b3JkIiwKICAgICAgICAgICAgc2hvdz0i4oCiIiwgaGVpZ2h0PTQyLCB3aWR0aD0yODAsCiAgICAgICAgICAgIGZvbnQ9dGhlbWVfbWFuYWdlci5mb250KCJib2R5X21kIikKICAgICAgICApCiAgICAgICAgc2VsZi5lbnRfcGFzc3dvcmQucGFjaygpCiAgICAgICAgc2VsZi5lbnRfcGFzc3dvcmQuYmluZCgiPFJldHVybj4iLCBsYW1iZGEgXzogc2VsZi5fdHJ5X2xvZ2luKCkpCgogICAgICAgIHNlbGYubGJsX2Vycm9yID0gY3RrLkNUa0xhYmVsKAogICAgICAgICAgICBzZWxmLCB0ZXh0PSIiLCB0ZXh0X2NvbG9yPWNbImVycm9yIl0sCiAgICAgICAgICAgIGZvbnQ9dGhlbWVfbWFuYWdlci5mb250KCJib2R5X3NtIikKICAgICAgICApCiAgICAgICAgc2VsZi5sYmxfZXJyb3IucGFjayhwYWR5PTgpCgogICAgICAgIGN0ay5DVGtCdXR0b24oCiAgICAgICAgICAgIHNlbGYsIHRleHQ9IkF1dGhlbnRpY2F0ZSIsIHdpZHRoPTI4MCwgaGVpZ2h0PTQyLAogICAgICAgICAgICBmb250PXRoZW1lX21hbmFnZXIuZm9udCgiYnV0dG9uIiksCiAgICAgICAgICAgIGZnX2NvbG9yPWNbImFjY2VudCJdLCBob3Zlcl9jb2xvcj1jWyJhY2NlbnRfaG92ZXIiXSwKICAgICAgICAgICAgY29tbWFuZD1zZWxmLl90cnlfbG9naW4KICAgICAgICApLnBhY2soKQoKICAgICAgICBjdGsuQ1RrQnV0dG9uKAogICAgICAgICAgICBzZWxmLCB0ZXh0PSJDYW5jZWwiLCB3aWR0aD0yODAsIGhlaWdodD0zNiwKICAgICAgICAgICAgZm9udD10aGVtZV9tYW5hZ2VyLmZvbnQoImJvZHlfc20iKSwKICAgICAgICAgICAgZmdfY29sb3I9InRyYW5zcGFyZW50IiwKICAgICAgICAgICAgdGV4dF9jb2xvcj1jWyJ0ZXh0X3NlY29uZGFyeSJdLAogICAgICAgICAgICBob3Zlcl9jb2xvcj1jWyJiZ19ob3ZlciJdLAogICAgICAgICAgICBjb21tYW5kPXNlbGYuZGVzdHJveQogICAgICAgICkucGFjayhwYWR5PSg4LCAwKSkKCiAgICBkZWYgX3RyeV9sb2dpbihzZWxmKToKICAgICAgICBwYXNzd29yZCA9IHNlbGYuZW50X3Bhc3N3b3JkLmdldCgpCiAgICAgICAgc3RvcmVkICAgPSBkYi5nZXRfc2V0dGluZygiYWRtaW5fcGFzc3dvcmQiLCAiYWRtaW4xMjMiKQoKICAgICAgICBpZiBwYXNzd29yZCA9PSBzdG9yZWQ6CiAgICAgICAgICAgIHNlbGYuYXV0aGVudGljYXRlZCA9IFRydWUKICAgICAgICAgICAgc2VsZi5kZXN0cm95KCkKICAgICAgICBlbHNlOgogICAgICAgICAgICBzZWxmLl9hdHRlbXB0cyArPSAxCiAgICAgICAgICAgIHJlbWFpbmluZyA9IHNlbGYuX21heF9hdHRlbXB0cyAtIHNlbGYuX2F0dGVtcHRzCiAgICAgICAgICAgIGlmIHJlbWFpbmluZyA8PSAwOgogICAgICAgICAgICAgICAgc2VsZi5sYmxfZXJyb3IuY29uZmlndXJlKHRleHQ9IlRvbyBtYW55IGZhaWxlZCBhdHRlbXB0cy4iKQogICAgICAgICAgICAgICAgc2VsZi5hZnRlcigxNTAwLCBzZWxmLmRlc3Ryb3kpCiAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICBzZWxmLmxibF9lcnJvci5jb25maWd1cmUoCiAgICAgICAgICAgICAgICAgICAgdGV4dD1mIkluY29ycmVjdCBwYXNzd29yZC4ge3JlbWFpbmluZ30gYXR0ZW1wdChzKSBsZWZ0LiIKICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIHNlbGYuZW50X3Bhc3N3b3JkLmRlbGV0ZSgwLCAiZW5kIikK', 'gui/pages/register.py': 'IiIiCuKVlOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVlwrilZEgICAgICAgICAgICAgIFJFR0lTVEVSIOKAlCBGYWNlIEF0dGVuZGFuY2UgU3lzdGVtICAgICAgICAgICAgICDilZEK4pWRICBBZGQgbmV3IHVzZXJzIGFuZCBjYXB0dXJlIHRyYWluaW5nIGZhY2UgaW1hZ2VzICAgICAgICAgICAgIOKVkQrilZrilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZ0KIiIiCgppbXBvcnQgY3VzdG9tdGtpbnRlciBhcyBjdGsKaW1wb3J0IGN2MgppbXBvcnQgUElMLkltYWdlLCBQSUwuSW1hZ2VUawppbXBvcnQgdGhyZWFkaW5nCmZyb20gZGF0YWJhc2UuZGJfbWFuYWdlciBpbXBvcnQgZGIKZnJvbSBmYWNlX3JlY29nbml0aW9uX2VuZ2luZS5yZWNvZ25pemVyIGltcG9ydCBlbmdpbmUKZnJvbSB1dGlscy5oZWxwZXJzIGltcG9ydCB0aGVtZV9tYW5hZ2VyLCB2YWxpZGF0ZV91c2VyX2lucHV0CgpjbGFzcyBSZWdpc3RlclBhZ2UoY3RrLkNUa0ZyYW1lKToKICAgIGRlZiBfX2luaXRfXyhzZWxmLCBwYXJlbnQpOgogICAgICAgIGMgPSB0aGVtZV9tYW5hZ2VyLmNvbG9ycwogICAgICAgIHN1cGVyKCkuX19pbml0X18ocGFyZW50LCBmZ19jb2xvcj1jWyJiZ19wcmltYXJ5Il0sIGNvcm5lcl9yYWRpdXM9MCkKICAgICAgICAKICAgICAgICBzZWxmLnBhY2tfcHJvcGFnYXRlKEZhbHNlKQogICAgICAgIHNlbGYuaXNfY2FwdHVyaW5nID0gRmFsc2UKICAgICAgICBzZWxmLl9idWlsZF91aSgpCgogICAgZGVmIF9idWlsZF91aShzZWxmKToKICAgICAgICBjID0gdGhlbWVfbWFuYWdlci5jb2xvcnMKICAgICAgICAKICAgICAgICBzZWxmLmdyaWRfY29sdW1uY29uZmlndXJlKDAsIHdlaWdodD00KQogICAgICAgIHNlbGYuZ3JpZF9jb2x1bW5jb25maWd1cmUoMSwgd2VpZ2h0PTYpCiAgICAgICAgc2VsZi5ncmlkX3Jvd2NvbmZpZ3VyZSgwLCB3ZWlnaHQ9MSkKICAgICAgICAKICAgICAgICAjIOKUgOKUgCBMZWZ0OiBGb3JtIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgAogICAgICAgIGZvcm1fcGFuZWwgPSBjdGsuQ1RrRnJhbWUoc2VsZiwgZmdfY29sb3I9Y1siYmdfY2FyZCJdLCBjb3JuZXJfcmFkaXVzPTEyKQogICAgICAgIGZvcm1fcGFuZWwuZ3JpZChyb3c9MCwgY29sdW1uPTAsIHN0aWNreT0ibnNldyIsIHBhZHg9KDMwLCAxNSksIHBhZHk9MzApCiAgICAgICAgZm9ybV9wYW5lbC5wYWNrX3Byb3BhZ2F0ZShGYWxzZSkKICAgICAgICAKICAgICAgICBjdGsuQ1RrTGFiZWwoCiAgICAgICAgICAgIGZvcm1fcGFuZWwsIHRleHQ9Ik5ldyBVc2VyIFJlZ2lzdHJhdGlvbiIsCiAgICAgICAgICAgIGZvbnQ9dGhlbWVfbWFuYWdlci5mb250KCJoZWFkaW5nX2xnIiksIHRleHRfY29sb3I9Y1sidGV4dF9wcmltYXJ5Il0KICAgICAgICApLnBhY2soYW5jaG9yPSJ3IiwgcGFkeD0yNSwgcGFkeT0oMjUsIDIwKSkKICAgICAgICAKICAgICAgICAjIElucHV0cwogICAgICAgIHNlbGYuZW50X25hbWUgPSBzZWxmLl9jcmVhdGVfaW5wdXQoZm9ybV9wYW5lbCwgIkZ1bGwgTmFtZSAqIiwgImUuZy4gSm9obiBEb2UiKQogICAgICAgIHNlbGYuZW50X3JvbGwgPSBzZWxmLl9jcmVhdGVfaW5wdXQoZm9ybV9wYW5lbCwgIklEIC8gUm9sbCBOdW1iZXIgKiIsICJlLmcuIEVNUC0xMDEiKQogICAgICAgIAogICAgICAgICMgRGVwYXJ0bWVudCBkcm9wZG93biAoZmV0Y2ggZXhpc3Rpbmcgb3IgYWxsb3cgbmV3KQogICAgICAgIGRlcHRfZnJhbWUgPSBjdGsuQ1RrRnJhbWUoZm9ybV9wYW5lbCwgZmdfY29sb3I9InRyYW5zcGFyZW50IikKICAgICAgICBkZXB0X2ZyYW1lLnBhY2soZmlsbD0ieCIsIHBhZHg9MjUsIHBhZHk9MTApCiAgICAgICAgY3RrLkNUa0xhYmVsKGRlcHRfZnJhbWUsIHRleHQ9IkRlcGFydG1lbnQgLyBDbGFzcyAqIiwgZm9udD10aGVtZV9tYW5hZ2VyLmZvbnQoImJ1dHRvbiIpLCB0ZXh0X2NvbG9yPWNbInRleHRfc2Vjb25kYXJ5Il0pLnBhY2soYW5jaG9yPSJ3IiwgcGFkeT0oMCwgNSkpCiAgICAgICAgCiAgICAgICAgZGVwdHMgPSBkYi5nZXRfZGVwYXJ0bWVudHMoKQogICAgICAgIGlmIG5vdCBkZXB0czogZGVwdHMgPSBbIklUIiwgIkhSIiwgIkVuZ2luZWVyaW5nIiwgIlNhbGVzIl0KICAgICAgICBzZWxmLmVudF9kZXB0ID0gY3RrLkNUa0NvbWJvQm94KGRlcHRfZnJhbWUsIHZhbHVlcz1kZXB0cywgaGVpZ2h0PTQwLCBmb250PXRoZW1lX21hbmFnZXIuZm9udCgiYm9keV9tZCIpKQogICAgICAgIHNlbGYuZW50X2RlcHQucGFjayhmaWxsPSJ4IikKICAgICAgICAKICAgICAgICBzZWxmLmVudF9lbWFpbCA9IHNlbGYuX2NyZWF0ZV9pbnB1dChmb3JtX3BhbmVsLCAiRW1haWwgQWRkcmVzcyIsICJPcHRpb25hbCIpCiAgICAgICAgc2VsZi5lbnRfcGhvbmUgPSBzZWxmLl9jcmVhdGVfaW5wdXQoZm9ybV9wYW5lbCwgIlBob25lIE51bWJlciIsICJPcHRpb25hbCIpCiAgICAgICAgCiAgICAgICAgIyBFcnJvciBMYWJlbAogICAgICAgIHNlbGYubGJsX2Vycm9yID0gY3RrLkNUa0xhYmVsKGZvcm1fcGFuZWwsIHRleHQ9IiIsIHRleHRfY29sb3I9Y1siZXJyb3IiXSwgZm9udD10aGVtZV9tYW5hZ2VyLmZvbnQoImJvZHlfc20iKSkKICAgICAgICBzZWxmLmxibF9lcnJvci5wYWNrKHBhZHk9MTApCiAgICAgICAgCiAgICAgICAgIyBCdXR0b25zCiAgICAgICAgc2VsZi5idG5fY2FwdHVyZSA9IGN0ay5DVGtCdXR0b24oCiAgICAgICAgICAgIGZvcm1fcGFuZWwsIHRleHQ9IlN0YXJ0IENhcHR1cmUgJiBUcmFpbiIsIGhlaWdodD00NSwKICAgICAgICAgICAgZm9udD10aGVtZV9tYW5hZ2VyLmZvbnQoImhlYWRpbmdfbWQiKSwgZmdfY29sb3I9Y1siYWNjZW50Il0sIGhvdmVyX2NvbG9yPWNbImFjY2VudF9ob3ZlciJdLAogICAgICAgICAgICBjb21tYW5kPXNlbGYuX3N0YXJ0X3JlZ2lzdHJhdGlvbgogICAgICAgICkKICAgICAgICBzZWxmLmJ0bl9jYXB0dXJlLnBhY2soZmlsbD0ieCIsIHBhZHg9MjUsIHBhZHk9KDEwLCAxMCkpCgogICAgICAgICMg4pSA4pSAIFJpZ2h0OiBQcmV2aWV3ICYgUHJvZ3Jlc3Mg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACiAgICAgICAgcHJldmlld19wYW5lbCA9IGN0ay5DVGtGcmFtZShzZWxmLCBmZ19jb2xvcj0idHJhbnNwYXJlbnQiKQogICAgICAgIHByZXZpZXdfcGFuZWwuZ3JpZChyb3c9MCwgY29sdW1uPTEsIHN0aWNreT0ibnNldyIsIHBhZHg9KDE1LCAzMCksIHBhZHk9MzApCiAgICAgICAgcHJldmlld19wYW5lbC5wYWNrX3Byb3BhZ2F0ZShGYWxzZSkKICAgICAgICAKICAgICAgICAjIENhbWVyYSBkaXNwbGF5IGxhYmVsCiAgICAgICAgc2VsZi5jYW1fZnJhbWUgPSBjdGsuQ1RrRnJhbWUocHJldmlld19wYW5lbCwgZmdfY29sb3I9IiMwMDAwMDAiLCBjb3JuZXJfcmFkaXVzPTEyKQogICAgICAgIHNlbGYuY2FtX2ZyYW1lLnBhY2soZmlsbD0iYm90aCIsIGV4cGFuZD1UcnVlLCBwYWR5PSgwLCAyMCkpCiAgICAgICAgc2VsZi5jYW1fZnJhbWUucGFja19wcm9wYWdhdGUoRmFsc2UpCiAgICAgICAgCiAgICAgICAgc2VsZi5sYmxfdmlkZW8gPSBjdGsuQ1RrTGFiZWwoc2VsZi5jYW1fZnJhbWUsIHRleHQ9IkNhbWVyYSBQcmV2aWV3IiwgdGV4dF9jb2xvcj0iIzU1NTU1NSIpCiAgICAgICAgc2VsZi5sYmxfdmlkZW8ucGFjayhleHBhbmQ9VHJ1ZSkKICAgICAgICAKICAgICAgICAjIFByb2dyZXNzIFVJCiAgICAgICAgc2VsZi5wcm9ncmVzc19mcmFtZSA9IGN0ay5DVGtGcmFtZShwcmV2aWV3X3BhbmVsLCBmZ19jb2xvcj1jWyJiZ19jYXJkIl0sIGNvcm5lcl9yYWRpdXM9MTIsIGhlaWdodD0xMjApCiAgICAgICAgc2VsZi5wcm9ncmVzc19mcmFtZS5wYWNrKGZpbGw9IngiKQogICAgICAgIHNlbGYucHJvZ3Jlc3NfZnJhbWUucGFja19wcm9wYWdhdGUoRmFsc2UpCiAgICAgICAgCiAgICAgICAgc2VsZi5sYmxfc3RhdHVzID0gY3RrLkNUa0xhYmVsKHNlbGYucHJvZ3Jlc3NfZnJhbWUsIHRleHQ9IlJlYWR5IiwgZm9udD10aGVtZV9tYW5hZ2VyLmZvbnQoImJvZHlfbGciKSwgdGV4dF9jb2xvcj1jWyJ0ZXh0X3ByaW1hcnkiXSkKICAgICAgICBzZWxmLmxibF9zdGF0dXMucGFjayhwYWR5PSgyMCwgMTApKQogICAgICAgIAogICAgICAgIHNlbGYucHJvZ3Jlc3NfYmFyID0gY3RrLkNUa1Byb2dyZXNzQmFyKHNlbGYucHJvZ3Jlc3NfZnJhbWUsIG1vZGU9ImRldGVybWluYXRlIiwgaGVpZ2h0PTgsIGZnX2NvbG9yPWNbImJnX3NlY29uZGFyeSJdLCBwcm9ncmVzc19jb2xvcj1jWyJhY2NlbnQiXSkKICAgICAgICBzZWxmLnByb2dyZXNzX2Jhci5wYWNrKGZpbGw9IngiLCBwYWR4PTMwKQogICAgICAgIHNlbGYucHJvZ3Jlc3NfYmFyLnNldCgwKQoKICAgIGRlZiBfY3JlYXRlX2lucHV0KHNlbGYsIHBhcmVudCwgbGFiZWwsIHBsYWNlaG9sZGVyKToKICAgICAgICBjID0gdGhlbWVfbWFuYWdlci5jb2xvcnMKICAgICAgICBmcmFtZSA9IGN0ay5DVGtGcmFtZShwYXJlbnQsIGZnX2NvbG9yPSJ0cmFuc3BhcmVudCIpCiAgICAgICAgZnJhbWUucGFjayhmaWxsPSJ4IiwgcGFkeD0yNSwgcGFkeT0xMCkKICAgICAgICAKICAgICAgICBjdGsuQ1RrTGFiZWwoZnJhbWUsIHRleHQ9bGFiZWwsIGZvbnQ9dGhlbWVfbWFuYWdlci5mb250KCJidXR0b24iKSwgdGV4dF9jb2xvcj1jWyJ0ZXh0X3NlY29uZGFyeSJdKS5wYWNrKGFuY2hvcj0idyIsIHBhZHk9KDAsIDUpKQogICAgICAgIGVudCA9IGN0ay5DVGtFbnRyeShmcmFtZSwgcGxhY2Vob2xkZXJfdGV4dD1wbGFjZWhvbGRlciwgaGVpZ2h0PTQwLCBmb250PXRoZW1lX21hbmFnZXIuZm9udCgiYm9keV9tZCIpKQogICAgICAgIGVudC5wYWNrKGZpbGw9IngiKQogICAgICAgIHJldHVybiBlbnQKCiAgICBkZWYgX3N0YXJ0X3JlZ2lzdHJhdGlvbihzZWxmKToKICAgICAgICBpZiBzZWxmLmlzX2NhcHR1cmluZzoKICAgICAgICAgICAgcmV0dXJuCiAgICAgICAgICAgIAogICAgICAgICMgMS4gVmFsaWRhdGUKICAgICAgICBuYW1lID0gc2VsZi5lbnRfbmFtZS5nZXQoKQogICAgICAgIHJvbGwgPSBzZWxmLmVudF9yb2xsLmdldCgpCiAgICAgICAgZGVwdCA9IHNlbGYuZW50X2RlcHQuZ2V0KCkKICAgICAgICAKICAgICAgICBpc192YWxpZCwgZXJyID0gdmFsaWRhdGVfdXNlcl9pbnB1dChuYW1lLCByb2xsLCBkZXB0KQogICAgICAgIGlmIG5vdCBpc192YWxpZDoKICAgICAgICAgICAgc2VsZi5sYmxfZXJyb3IuY29uZmlndXJlKHRleHQ9ZXJyKQogICAgICAgICAgICByZXR1cm4KICAgICAgICAgICAgCiAgICAgICAgc2VsZi5sYmxfZXJyb3IuY29uZmlndXJlKHRleHQ9IiIpCiAgICAgICAgCiAgICAgICAgIyAyLiBDaGVjayBpZiB1c2VyIGV4aXN0cwogICAgICAgIGlmIGRiLmdldF91c2VyX2J5X3JvbGwocm9sbCk6CiAgICAgICAgICAgIHNlbGYubGJsX2Vycm9yLmNvbmZpZ3VyZSh0ZXh0PSJVc2VyIHdpdGggdGhpcyBJRCBhbHJlYWR5IGV4aXN0cy4iKQogICAgICAgICAgICByZXR1cm4KCiAgICAgICAgIyAzLiBBZGQgdG8gREIKICAgICAgICB1aWQgPSBkYi5hZGRfdXNlcigKICAgICAgICAgICAgbmFtZT1uYW1lLCByb2xsX251bWJlcj1yb2xsLCBkZXBhcnRtZW50PWRlcHQsCiAgICAgICAgICAgIGVtYWlsPXNlbGYuZW50X2VtYWlsLmdldCgpLCBwaG9uZT1zZWxmLmVudF9waG9uZS5nZXQoKQogICAgICAgICkKICAgICAgICBpZiB1aWQgPT0gLTE6CiAgICAgICAgICAgIHNlbGYubGJsX2Vycm9yLmNvbmZpZ3VyZSh0ZXh0PSJEYXRhYmFzZSBlcnJvci4gQ2hlY2sgbG9ncy4iKQogICAgICAgICAgICByZXR1cm4KCiAgICAgICAgIyA0LiBTdGFydCBDYXB0dXJlICYgVHJhaW4gVGhyZWFkCiAgICAgICAgc2VsZi5pc19jYXB0dXJpbmcgPSBUcnVlCiAgICAgICAgc2VsZi5fc2V0X3VpX3N0YXRlKCJkaXNhYmxlZCIpCiAgICAgICAgc2VsZi5wcm9ncmVzc19iYXIuc2V0KDApCiAgICAgICAgc2VsZi5sYmxfc3RhdHVzLmNvbmZpZ3VyZSh0ZXh0PSJDYXB0dXJpbmcgZmFjZSBpbWFnZXMuLi4gUGxlYXNlIGxvb2sgYXQgdGhlIGNhbWVyYS4iKQogICAgICAgIAogICAgICAgIHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PXNlbGYuX2NhcHR1cmVfcHJvY2VzcywgYXJncz0odWlkLCBuYW1lKSwgZGFlbW9uPVRydWUpLnN0YXJ0KCkKCiAgICBkZWYgX2NhcHR1cmVfcHJvY2VzcyhzZWxmLCB1aWQsIG5hbWUpOgogICAgICAgIGNhbV9pZHggPSBpbnQoZGIuZ2V0X3NldHRpbmcoImNhbWVyYV9pbmRleCIsICIwIikpCiAgICAgICAgCiAgICAgICAgIyBDYXB0dXJlCiAgICAgICAgc3VjY2VzcyA9IGVuZ2luZS5jYXB0dXJlX2ZhY2VfaW1hZ2VzKAogICAgICAgICAgICB1c2VyX2lkPXVpZCwKICAgICAgICAgICAgdXNlcl9uYW1lPW5hbWUsCiAgICAgICAgICAgIG51bV9pbWFnZXM9MzAsCiAgICAgICAgICAgIGNhbWVyYV9pbmRleD1jYW1faWR4LAogICAgICAgICAgICBwcm9ncmVzc19jYWxsYmFjaz1zZWxmLl91cGRhdGVfcHJvZ3Jlc3MsCiAgICAgICAgICAgIGZyYW1lX2NhbGxiYWNrPXNlbGYuX3VwZGF0ZV9wcmV2aWV3CiAgICAgICAgKQogICAgICAgIAogICAgICAgIGlmIHN1Y2Nlc3M6CiAgICAgICAgICAgIHNlbGYuYWZ0ZXIoMCwgbGFtYmRhOiBzZWxmLmxibF9zdGF0dXMuY29uZmlndXJlKHRleHQ9IlRyYWluaW5nIG1vZGVsLi4uIFRoaXMgbWF5IHRha2UgYSBtaW51dGUuIikpCiAgICAgICAgICAgIHNlbGYuYWZ0ZXIoMCwgbGFtYmRhOiBzZWxmLnByb2dyZXNzX2Jhci5zZXQoMCkpCiAgICAgICAgICAgIAogICAgICAgICAgICAjIFRyYWluCiAgICAgICAgICAgIHRyYWluX3N1Y2Nlc3MgPSBlbmdpbmUudHJhaW5fbW9kZWwocHJvZ3Jlc3NfY2FsbGJhY2s9c2VsZi5fdXBkYXRlX3RyYWluX3Byb2dyZXNzKQogICAgICAgICAgICAKICAgICAgICAgICAgaWYgdHJhaW5fc3VjY2VzczoKICAgICAgICAgICAgICAgIHNlbGYuYWZ0ZXIoMCwgbGFtYmRhOiBzZWxmLl9yZWdpc3RyYXRpb25fY29tcGxldGUoVHJ1ZSwgIlJlZ2lzdHJhdGlvbiBhbmQgVHJhaW5pbmcgU3VjY2Vzc2Z1bCEiKSkKICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIHNlbGYuYWZ0ZXIoMCwgbGFtYmRhOiBzZWxmLl9yZWdpc3RyYXRpb25fY29tcGxldGUoRmFsc2UsICJUcmFpbmluZyBmYWlsZWQuIFBsZWFzZSB0cnkgYWdhaW4uIikpCiAgICAgICAgZWxzZToKICAgICAgICAgICAgc2VsZi5hZnRlcigwLCBsYW1iZGE6IHNlbGYuX3JlZ2lzdHJhdGlvbl9jb21wbGV0ZShGYWxzZSwgIkNhcHR1cmUgZmFpbGVkLiBObyBmYWNlcyBkZXRlY3RlZC4iKSkKCiAgICBkZWYgX3VwZGF0ZV9wcm9ncmVzcyhzZWxmLCBjdXJyZW50LCB0b3RhbCk6CiAgICAgICAgcGN0ID0gY3VycmVudCAvIHRvdGFsCiAgICAgICAgc2VsZi5hZnRlcigwLCBsYW1iZGE6IHNlbGYucHJvZ3Jlc3NfYmFyLnNldChwY3QpKQogICAgICAgIAogICAgZGVmIF91cGRhdGVfdHJhaW5fcHJvZ3Jlc3Moc2VsZiwgY3VycmVudCwgdG90YWwpOgogICAgICAgIHBjdCA9IGN1cnJlbnQgLyB0b3RhbCBpZiB0b3RhbCA+IDAgZWxzZSAwCiAgICAgICAgc2VsZi5hZnRlcigwLCBsYW1iZGE6IHNlbGYucHJvZ3Jlc3NfYmFyLnNldChwY3QpKQoKICAgIGRlZiBfdXBkYXRlX3ByZXZpZXcoc2VsZiwgZnJhbWUpOgogICAgICAgIHRyeToKICAgICAgICAgICAgcmdiID0gY3YyLmN2dENvbG9yKGZyYW1lLCBjdjIuQ09MT1JfQkdSMlJHQikKICAgICAgICAgICAgaW1nID0gUElMLkltYWdlLmZyb21hcnJheShyZ2IpCiAgICAgICAgICAgIHcsIGggPSBzZWxmLmNhbV9mcmFtZS53aW5mb193aWR0aCgpLCBzZWxmLmNhbV9mcmFtZS53aW5mb19oZWlnaHQoKQogICAgICAgICAgICBpZiB3ID4gMTAgYW5kIGggPiAxMDoKICAgICAgICAgICAgICAgIGltZyA9IGltZy5yZXNpemUoKHcsIGgpLCBQSUwuSW1hZ2UuUmVzYW1wbGluZy5MQU5DWk9TKQogICAgICAgICAgICBpbWd0ayA9IFBJTC5JbWFnZVRrLlBob3RvSW1hZ2UoaW1hZ2U9aW1nKQogICAgICAgICAgICAKICAgICAgICAgICAgc2VsZi5hZnRlcigwLCBzZWxmLl9zZXRfaW1hZ2UsIGltZ3RrKQogICAgICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgICAgIHBhc3MKICAgICAgICAgICAgCiAgICBkZWYgX3NldF9pbWFnZShzZWxmLCBpbWd0ayk6CiAgICAgICAgc2VsZi5sYmxfdmlkZW8uaW1ndGsgPSBpbWd0awogICAgICAgIHNlbGYubGJsX3ZpZGVvLmNvbmZpZ3VyZShpbWFnZT1pbWd0aykKCiAgICBkZWYgX3JlZ2lzdHJhdGlvbl9jb21wbGV0ZShzZWxmLCBzdWNjZXNzLCBtc2cpOgogICAgICAgIHNlbGYuaXNfY2FwdHVyaW5nID0gRmFsc2UKICAgICAgICBzZWxmLl9zZXRfdWlfc3RhdGUoIm5vcm1hbCIpCiAgICAgICAgYyA9IHRoZW1lX21hbmFnZXIuY29sb3JzCiAgICAgICAgCiAgICAgICAgaWYgc3VjY2VzczoKICAgICAgICAgICAgc2VsZi5sYmxfc3RhdHVzLmNvbmZpZ3VyZSh0ZXh0PW1zZywgdGV4dF9jb2xvcj1jWyJzdWNjZXNzIl0pCiAgICAgICAgICAgIHNlbGYucHJvZ3Jlc3NfYmFyLnNldCgxLjApCiAgICAgICAgICAgIHNlbGYuX2NsZWFyX2Zvcm0oKQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIHNlbGYubGJsX3N0YXR1cy5jb25maWd1cmUodGV4dD1tc2csIHRleHRfY29sb3I9Y1siZXJyb3IiXSkKICAgICAgICAgICAgCiAgICAgICAgc2VsZi5sYmxfdmlkZW8uY29uZmlndXJlKGltYWdlPU5vbmUsIHRleHQ9IkNhbWVyYSBQcmV2aWV3IikKCiAgICBkZWYgX3NldF91aV9zdGF0ZShzZWxmLCBzdGF0ZSk6CiAgICAgICAgc2VsZi5lbnRfbmFtZS5jb25maWd1cmUoc3RhdGU9c3RhdGUpCiAgICAgICAgc2VsZi5lbnRfcm9sbC5jb25maWd1cmUoc3RhdGU9c3RhdGUpCiAgICAgICAgc2VsZi5lbnRfZGVwdC5jb25maWd1cmUoc3RhdGU9c3RhdGUpCiAgICAgICAgc2VsZi5lbnRfZW1haWwuY29uZmlndXJlKHN0YXRlPXN0YXRlKQogICAgICAgIHNlbGYuZW50X3Bob25lLmNvbmZpZ3VyZShzdGF0ZT1zdGF0ZSkKICAgICAgICBzZWxmLmJ0bl9jYXB0dXJlLmNvbmZpZ3VyZShzdGF0ZT1zdGF0ZSkKCiAgICBkZWYgX2NsZWFyX2Zvcm0oc2VsZik6CiAgICAgICAgc2VsZi5lbnRfbmFtZS5kZWxldGUoMCwgJ2VuZCcpCiAgICAgICAgc2VsZi5lbnRfcm9sbC5kZWxldGUoMCwgJ2VuZCcpCiAgICAgICAgc2VsZi5lbnRfZW1haWwuZGVsZXRlKDAsICdlbmQnKQogICAgICAgIHNlbGYuZW50X3Bob25lLmRlbGV0ZSgwLCAnZW5kJykK', 'gui/pages/attendance.py': 'IiIiCuKVlOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVlwrilZEgICAgICAgICAgICAgQVRURU5EQU5DRSDigJQgRmFjZSBBdHRlbmRhbmNlIFN5c3RlbSAgICAgICAgICAgICDilZEK4pWRICBMaXZlIHdlYmNhbSBmZWVkIGFuZCByZWFsLXRpbWUgZmFjZSByZWNvZ25pdGlvbiBzY2FubmluZyAgIOKVkQrilZrilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZ0KIiIiCgppbXBvcnQgY3VzdG9tdGtpbnRlciBhcyBjdGsKaW1wb3J0IGN2MgppbXBvcnQgUElMLkltYWdlLCBQSUwuSW1hZ2VUawpmcm9tIGRhdGFiYXNlLmRiX21hbmFnZXIgaW1wb3J0IGRiCmZyb20gZmFjZV9yZWNvZ25pdGlvbl9lbmdpbmUucmVjb2duaXplciBpbXBvcnQgZW5naW5lCmZyb20gdXRpbHMuaGVscGVycyBpbXBvcnQgdGhlbWVfbWFuYWdlciwgc291bmRfbWFuYWdlciwgZ2V0X2N1cnJlbnRfdGltZV9zdHIKaW1wb3J0IHRocmVhZGluZwoKY2xhc3MgQXR0ZW5kYW5jZVBhZ2UoY3RrLkNUa0ZyYW1lKToKICAgIGRlZiBfX2luaXRfXyhzZWxmLCBwYXJlbnQpOgogICAgICAgIGMgPSB0aGVtZV9tYW5hZ2VyLmNvbG9ycwogICAgICAgIHN1cGVyKCkuX19pbml0X18ocGFyZW50LCBmZ19jb2xvcj1jWyJiZ19wcmltYXJ5Il0sIGNvcm5lcl9yYWRpdXM9MCkKICAgICAgICAKICAgICAgICBzZWxmLnBhY2tfcHJvcGFnYXRlKEZhbHNlKQogICAgICAgIHNlbGYuY2FtZXJhX2FjdGl2ZSA9IEZhbHNlCiAgICAgICAgc2VsZi5jYXAgPSBOb25lCiAgICAgICAgc2VsZi5tYXJrZWRfdG9kYXkgPSBzZXQoKSAgIyBDYWNoZSB0byBwcmV2ZW50IERCIHNwYW0KICAgICAgICBzZWxmLmxhc3RfcmVzdWx0cyA9IFtdCiAgICAgICAgCiAgICAgICAgc2VsZi5fYnVpbGRfdWkoKQoKICAgIGRlZiBfYnVpbGRfdWkoc2VsZik6CiAgICAgICAgYyA9IHRoZW1lX21hbmFnZXIuY29sb3JzCiAgICAgICAgCiAgICAgICAgIyDilIDilIAgTWFpbiBMYXlvdXQg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACiAgICAgICAgc2VsZi5ncmlkX2NvbHVtbmNvbmZpZ3VyZSgwLCB3ZWlnaHQ9NykKICAgICAgICBzZWxmLmdyaWRfY29sdW1uY29uZmlndXJlKDEsIHdlaWdodD0zKQogICAgICAgIHNlbGYuZ3JpZF9yb3djb25maWd1cmUoMCwgd2VpZ2h0PTEpCiAgICAgICAgCiAgICAgICAgIyDilIDilIAgTGVmdDogQ2FtZXJhIFZpZXcg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACiAgICAgICAgY2FtX2NvbnRhaW5lciA9IGN0ay5DVGtGcmFtZShzZWxmLCBmZ19jb2xvcj0idHJhbnNwYXJlbnQiKQogICAgICAgIGNhbV9jb250YWluZXIuZ3JpZChyb3c9MCwgY29sdW1uPTAsIHN0aWNreT0ibnNldyIsIHBhZHg9KDMwLCAxNSksIHBhZHk9MzApCiAgICAgICAgY2FtX2NvbnRhaW5lci5wYWNrX3Byb3BhZ2F0ZShGYWxzZSkKICAgICAgICAKICAgICAgICBoZWFkZXIgPSBjdGsuQ1RrRnJhbWUoY2FtX2NvbnRhaW5lciwgZmdfY29sb3I9InRyYW5zcGFyZW50IikKICAgICAgICBoZWFkZXIucGFjayhmaWxsPSJ4IiwgcGFkeT0oMCwgMTUpKQogICAgICAgIAogICAgICAgIGN0ay5DVGtMYWJlbCgKICAgICAgICAgICAgaGVhZGVyLCB0ZXh0PSJMaXZlIFNjYW5uZXIiLAogICAgICAgICAgICBmb250PXRoZW1lX21hbmFnZXIuZm9udCgiaGVhZGluZ19sZyIpLCB0ZXh0X2NvbG9yPWNbInRleHRfcHJpbWFyeSJdCiAgICAgICAgKS5wYWNrKHNpZGU9ImxlZnQiKQogICAgICAgIAogICAgICAgIHNlbGYuYnRuX3RvZ2dsZV9jYW0gPSBjdGsuQ1RrQnV0dG9uKAogICAgICAgICAgICBoZWFkZXIsIHRleHQ9IlN0YXJ0IENhbWVyYSIsCiAgICAgICAgICAgIGZvbnQ9dGhlbWVfbWFuYWdlci5mb250KCJidXR0b24iKSwKICAgICAgICAgICAgZmdfY29sb3I9Y1siYWNjZW50X2dyZWVuIl0sIGhvdmVyX2NvbG9yPWNbInN1Y2Nlc3MiXSwKICAgICAgICAgICAgY29tbWFuZD1zZWxmLnRvZ2dsZV9jYW1lcmEKICAgICAgICApCiAgICAgICAgc2VsZi5idG5fdG9nZ2xlX2NhbS5wYWNrKHNpZGU9InJpZ2h0IikKICAgICAgICAKICAgICAgICAjIENhbWVyYSBkaXNwbGF5IGxhYmVsCiAgICAgICAgc2VsZi5jYW1fZnJhbWUgPSBjdGsuQ1RrRnJhbWUoY2FtX2NvbnRhaW5lciwgZmdfY29sb3I9IiMwMDAwMDAiLCBjb3JuZXJfcmFkaXVzPTEyKQogICAgICAgIHNlbGYuY2FtX2ZyYW1lLnBhY2soZmlsbD0iYm90aCIsIGV4cGFuZD1UcnVlKQogICAgICAgIHNlbGYuY2FtX2ZyYW1lLnBhY2tfcHJvcGFnYXRlKEZhbHNlKQogICAgICAgIAogICAgICAgIHNlbGYubGJsX3ZpZGVvID0gY3RrLkNUa0xhYmVsKHNlbGYuY2FtX2ZyYW1lLCB0ZXh0PSJDYW1lcmEgT2ZmbGluZSIsIHRleHRfY29sb3I9IiM1NTU1NTUiKQogICAgICAgIHNlbGYubGJsX3ZpZGVvLnBhY2soZXhwYW5kPVRydWUpCiAgICAgICAgCiAgICAgICAgIyDilIDilIAgUmlnaHQ6IFN0YXR1cyAmIExvZ3Mg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACiAgICAgICAgc2lkZV9wYW5lbCA9IGN0ay5DVGtGcmFtZShzZWxmLCBmZ19jb2xvcj1jWyJiZ19jYXJkIl0sIGNvcm5lcl9yYWRpdXM9MTIpCiAgICAgICAgc2lkZV9wYW5lbC5ncmlkKHJvdz0wLCBjb2x1bW49MSwgc3RpY2t5PSJuc2V3IiwgcGFkeD0oMTUsIDMwKSwgcGFkeT0zMCkKICAgICAgICBzaWRlX3BhbmVsLnBhY2tfcHJvcGFnYXRlKEZhbHNlKQogICAgICAgIAogICAgICAgIGN0ay5DVGtMYWJlbCgKICAgICAgICAgICAgc2lkZV9wYW5lbCwgdGV4dD0iU2NhbiBMb2ciLAogICAgICAgICAgICBmb250PXRoZW1lX21hbmFnZXIuZm9udCgiaGVhZGluZ19tZCIpLCB0ZXh0X2NvbG9yPWNbInRleHRfcHJpbWFyeSJdCiAgICAgICAgKS5wYWNrKGFuY2hvcj0idyIsIHBhZHg9MjAsIHBhZHk9KDIwLCAxMCkpCiAgICAgICAgCiAgICAgICAgIyBMaXZlIGNsb2NrCiAgICAgICAgc2VsZi5sYmxfY2xvY2sgPSBjdGsuQ1RrTGFiZWwoCiAgICAgICAgICAgIHNpZGVfcGFuZWwsIHRleHQ9IjAwOjAwOjAwIiwKICAgICAgICAgICAgZm9udD1jdGsuQ1RrRm9udChmYW1pbHk9IkNvdXJpZXIgTmV3Iiwgc2l6ZT0yNCwgd2VpZ2h0PSJib2xkIiksCiAgICAgICAgICAgIHRleHRfY29sb3I9Y1siYWNjZW50Il0KICAgICAgICApCiAgICAgICAgc2VsZi5sYmxfY2xvY2sucGFjayhwYWR5PSgwLCAyMCkpCiAgICAgICAgCiAgICAgICAgIyBTdGF0dXMgQm94CiAgICAgICAgc2VsZi5zdGF0dXNfYm94ID0gY3RrLkNUa0ZyYW1lKHNpZGVfcGFuZWwsIGZnX2NvbG9yPWNbImJnX3NlY29uZGFyeSJdLCBjb3JuZXJfcmFkaXVzPTgpCiAgICAgICAgc2VsZi5zdGF0dXNfYm94LnBhY2soZmlsbD0ieCIsIHBhZHg9MjAsIHBhZHk9KDAsIDIwKSkKICAgICAgICAKICAgICAgICBzZWxmLmxibF9zdGF0dXNfaWNvbiA9IGN0ay5DVGtMYWJlbChzZWxmLnN0YXR1c19ib3gsIHRleHQ9IuKPsyIsIGZvbnQ9Y3RrLkNUa0ZvbnQoc2l6ZT0zMikpCiAgICAgICAgc2VsZi5sYmxfc3RhdHVzX2ljb24ucGFjayhwYWR5PSgxNSwgNSkpCiAgICAgICAgCiAgICAgICAgc2VsZi5sYmxfc3RhdHVzX3RleHQgPSBjdGsuQ1RrTGFiZWwoCiAgICAgICAgICAgIHNlbGYuc3RhdHVzX2JveCwgdGV4dD0iV2FpdGluZyBmb3Igc2Nhbi4uLiIsCiAgICAgICAgICAgIGZvbnQ9dGhlbWVfbWFuYWdlci5mb250KCJib2R5X21kIiksIHRleHRfY29sb3I9Y1sidGV4dF9zZWNvbmRhcnkiXQogICAgICAgICkKICAgICAgICBzZWxmLmxibF9zdGF0dXNfdGV4dC5wYWNrKHBhZHk9KDAsIDE1KSwgcGFkeD0xMCkKICAgICAgICAKICAgICAgICAjIFJlY2VudCBTY2FucyBMaXN0CiAgICAgICAgc2VsZi5zY2FuX2xpc3QgPSBjdGsuQ1RrU2Nyb2xsYWJsZUZyYW1lKHNpZGVfcGFuZWwsIGZnX2NvbG9yPSJ0cmFuc3BhcmVudCIpCiAgICAgICAgc2VsZi5zY2FuX2xpc3QucGFjayhmaWxsPSJib3RoIiwgZXhwYW5kPVRydWUsIHBhZHg9MTAsIHBhZHk9KDAsIDEwKSkKCiAgICAgICAgIyBTdGFydCBDbG9jayBVcGRhdGUKICAgICAgICBzZWxmLl91cGRhdGVfY2xvY2soKQoKICAgIGRlZiBfdXBkYXRlX2Nsb2NrKHNlbGYpOgogICAgICAgIHNlbGYubGJsX2Nsb2NrLmNvbmZpZ3VyZSh0ZXh0PWdldF9jdXJyZW50X3RpbWVfc3RyKCkpCiAgICAgICAgc2VsZi5hZnRlcigxMDAwLCBzZWxmLl91cGRhdGVfY2xvY2spCgogICAgZGVmIHRvZ2dsZV9jYW1lcmEoc2VsZik6CiAgICAgICAgYyA9IHRoZW1lX21hbmFnZXIuY29sb3JzCiAgICAgICAgaWYgbm90IHNlbGYuY2FtZXJhX2FjdGl2ZToKICAgICAgICAgICAgIyBTdGFydAogICAgICAgICAgICBjYW1faWR4ID0gaW50KGRiLmdldF9zZXR0aW5nKCJjYW1lcmFfaW5kZXgiLCAiMCIpKQogICAgICAgICAgICBzZWxmLmNhcCA9IGN2Mi5WaWRlb0NhcHR1cmUoY2FtX2lkeCkKICAgICAgICAgICAgCiAgICAgICAgICAgIGlmIG5vdCBzZWxmLmNhcC5pc09wZW5lZCgpOgogICAgICAgICAgICAgICAgc2VsZi5zaG93X3N0YXR1cygiQ2FtZXJhIEVycm9yIiwgIuKdjCIsIGNbImVycm9yIl0pCiAgICAgICAgICAgICAgICByZXR1cm4KICAgICAgICAgICAgICAgIAogICAgICAgICAgICBzZWxmLmNhbWVyYV9hY3RpdmUgPSBUcnVlCiAgICAgICAgICAgIHNlbGYuYnRuX3RvZ2dsZV9jYW0uY29uZmlndXJlKAogICAgICAgICAgICAgICAgdGV4dD0iU3RvcCBDYW1lcmEiLCBmZ19jb2xvcj1jWyJhY2NlbnRfcmVkIl0sIGhvdmVyX2NvbG9yPWNbImVycm9yIl0KICAgICAgICAgICAgKQogICAgICAgICAgICBzZWxmLmxibF92aWRlby5jb25maWd1cmUodGV4dD0iIikKICAgICAgICAgICAgCiAgICAgICAgICAgICMgUHJlLWxvYWQgd2hvIGhhcyBiZWVuIG1hcmtlZCB0b2RheSB0byBwcmV2ZW50IERCIHF1ZXJpZXMgb24gZXZlcnkgZnJhbWUKICAgICAgICAgICAgdG9kYXlfcmVjb3JkcyA9IGRiLmdldF90b2RheV9hdHRlbmRhbmNlKCkKICAgICAgICAgICAgc2VsZi5tYXJrZWRfdG9kYXkgPSB7clsidXNlcl9pZCJdIGZvciByIGluIHRvZGF5X3JlY29yZHN9CiAgICAgICAgICAgIAogICAgICAgICAgICBzZWxmLl91cGRhdGVfZnJhbWUoKQogICAgICAgIGVsc2U6CiAgICAgICAgICAgICMgU3RvcAogICAgICAgICAgICBzZWxmLmNhbWVyYV9hY3RpdmUgPSBGYWxzZQogICAgICAgICAgICBpZiBzZWxmLmNhcDoKICAgICAgICAgICAgICAgIHNlbGYuY2FwLnJlbGVhc2UoKQogICAgICAgICAgICBzZWxmLmJ0bl90b2dnbGVfY2FtLmNvbmZpZ3VyZSgKICAgICAgICAgICAgICAgIHRleHQ9IlN0YXJ0IENhbWVyYSIsIGZnX2NvbG9yPWNbImFjY2VudF9ncmVlbiJdLCBob3Zlcl9jb2xvcj1jWyJzdWNjZXNzIl0KICAgICAgICAgICAgKQogICAgICAgICAgICBzZWxmLmxibF92aWRlby5jb25maWd1cmUoaW1hZ2U9Tm9uZSwgdGV4dD0iQ2FtZXJhIE9mZmxpbmUiKQogICAgICAgICAgICBzZWxmLnNob3dfc3RhdHVzKCJXYWl0aW5nIGZvciBzY2FuLi4uIiwgIuKPsyIsIGNbInRleHRfc2Vjb25kYXJ5Il0pCgogICAgZGVmIF91cGRhdGVfZnJhbWUoc2VsZik6CiAgICAgICAgaWYgbm90IHNlbGYuY2FtZXJhX2FjdGl2ZToKICAgICAgICAgICAgcmV0dXJuCiAgICAgICAgICAgIAogICAgICAgIHJldCwgZnJhbWUgPSBzZWxmLmNhcC5yZWFkKCkKICAgICAgICBpZiByZXQ6CiAgICAgICAgICAgICMgUHJvY2VzcyByZWNvZ25pdGlvbiBldmVyeSBmZXcgZnJhbWVzIG9yIGluIGEgYmFja2dyb3VuZCB0aHJlYWQgZm9yIHNtb290aCBVSQogICAgICAgICAgICAjIEZvciBzaW1wbGljaXR5IGFuZCBzdGFiaWxpdHksIHdlIHByb2Nlc3MgaW4gdGhlIG1haW4gdGhyZWFkIGJ1dCBjYW4gc2NhbGUgZG93biBmcmFtZQogICAgICAgICAgICBzZWxmLmxhc3RfcmVzdWx0cyA9IGVuZ2luZS5yZWNvZ25pemVfZmFjZXMoZnJhbWUpCiAgICAgICAgICAgIHNlbGYuX3Byb2Nlc3NfcmVzdWx0cyhzZWxmLmxhc3RfcmVzdWx0cykKICAgICAgICAgICAgCiAgICAgICAgICAgICMgRHJhdyBib3hlcwogICAgICAgICAgICBhbm5vdGF0ZWQgPSBlbmdpbmUuZHJhd19yZWNvZ25pdGlvbl9yZXN1bHRzKGZyYW1lLCBzZWxmLmxhc3RfcmVzdWx0cywgc2VsZi5tYXJrZWRfdG9kYXkpCiAgICAgICAgICAgIAogICAgICAgICAgICAjIENvbnZlcnQgZm9yIFRraW50ZXIKICAgICAgICAgICAgcmdiID0gY3YyLmN2dENvbG9yKGFubm90YXRlZCwgY3YyLkNPTE9SX0JHUjJSR0IpCiAgICAgICAgICAgIGltZyA9IFBJTC5JbWFnZS5mcm9tYXJyYXkocmdiKQogICAgICAgICAgICAKICAgICAgICAgICAgIyBSZXNpemUgdG8gZml0IGZyYW1lCiAgICAgICAgICAgIHcsIGggPSBzZWxmLmNhbV9mcmFtZS53aW5mb193aWR0aCgpLCBzZWxmLmNhbV9mcmFtZS53aW5mb19oZWlnaHQoKQogICAgICAgICAgICBpZiB3ID4gMTAgYW5kIGggPiAxMDoKICAgICAgICAgICAgICAgICMgVXNlIENUa0ltYWdlIGZvciBDdXN0b21Ua2ludGVyCiAgICAgICAgICAgICAgICBjdGtfaW1nID0gY3RrLkNUa0ltYWdlKGxpZ2h0X2ltYWdlPWltZywgZGFya19pbWFnZT1pbWcsIHNpemU9KHcsIGgpKQogICAgICAgICAgICAgICAgc2VsZi5sYmxfdmlkZW8uY29uZmlndXJlKGltYWdlPWN0a19pbWcpCiAgICAgICAgICAgIAogICAgICAgIHNlbGYuYWZ0ZXIoMzAsIHNlbGYuX3VwZGF0ZV9mcmFtZSkgICMgfjMwIGZwcwoKICAgIGRlZiBfcHJvY2Vzc19yZXN1bHRzKHNlbGYsIHJlc3VsdHMpOgogICAgICAgICIiIkhhbmRsZSBidXNpbmVzcyBsb2dpYyBmb3IgcmVjb2duaXplZCBmYWNlcy4iIiIKICAgICAgICBjID0gdGhlbWVfbWFuYWdlci5jb2xvcnMKICAgICAgICBzb3VuZF9lbmFibGVkID0gZGIuZ2V0X3NldHRpbmcoInNvdW5kX2VuYWJsZWQiLCAidHJ1ZSIpID09ICJ0cnVlIgogICAgICAgIAogICAgICAgIGZvciByIGluIHJlc3VsdHM6CiAgICAgICAgICAgIHVpZCA9IHJbInVzZXJfaWQiXQogICAgICAgICAgICBuYW1lID0gclsibmFtZSJdCiAgICAgICAgICAgIAogICAgICAgICAgICBpZiBuYW1lID09ICJVbmtub3duIjoKICAgICAgICAgICAgICAgIHNlbGYuc2hvd19zdGF0dXMoIlVua25vd24gRmFjZSBEZXRlY3RlZCIsICLinZMiLCBjWyJhY2NlbnRfeWVsbG93Il0pCiAgICAgICAgICAgICAgICBjb250aW51ZQogICAgICAgICAgICAgICAgCiAgICAgICAgICAgIGlmIHVpZCBpbiBzZWxmLm1hcmtlZF90b2RheToKICAgICAgICAgICAgICAgICMgQWxyZWFkeSBtYXJrZWQKICAgICAgICAgICAgICAgIHNlbGYuc2hvd19zdGF0dXMoZiJ7bmFtZX0gKEFscmVhZHkgTWFya2VkKSIsICLinJMiLCBjWyJhY2NlbnQiXSkKICAgICAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgICAgICAgICAKICAgICAgICAgICAgIyBWYWxpZCBuZXcgZmFjZSwgYXR0ZW1wdCB0byBtYXJrCiAgICAgICAgICAgIHJlcyA9IGRiLm1hcmtfYXR0ZW5kYW5jZSh1aWQpCiAgICAgICAgICAgIGlmIHJlc1sic3VjY2VzcyJdOgogICAgICAgICAgICAgICAgc2VsZi5tYXJrZWRfdG9kYXkuYWRkKHVpZCkKICAgICAgICAgICAgICAgIHNlbGYuc2hvd19zdGF0dXMoZiJBdHRlbmRhbmNlIE1hcmtlZDpcbntuYW1lfSIsICLinIUiLCBjWyJzdWNjZXNzIl0pCiAgICAgICAgICAgICAgICBpZiBzb3VuZF9lbmFibGVkOiBzb3VuZF9tYW5hZ2VyLnBsYXlfc3VjY2VzcygpCiAgICAgICAgICAgICAgICBzZWxmLl9hZGRfdG9fbG9nKG5hbWUsIGdldF9jdXJyZW50X3RpbWVfc3RyKCksIFRydWUpCiAgICAgICAgICAgIGVsaWYgcmVzWyJhbHJlYWR5X21hcmtlZCJdOgogICAgICAgICAgICAgICAgc2VsZi5tYXJrZWRfdG9kYXkuYWRkKHVpZCkgIyBDYWNoZSBpdAogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgc2VsZi5zaG93X3N0YXR1cyhmIkVycm9yOiB7cmVzWydtZXNzYWdlJ119IiwgIuKdjCIsIGNbImVycm9yIl0pCgogICAgZGVmIHNob3dfc3RhdHVzKHNlbGYsIHRleHQsIGljb24sIGNvbG9yKToKICAgICAgICBzZWxmLmxibF9zdGF0dXNfdGV4dC5jb25maWd1cmUodGV4dD10ZXh0LCB0ZXh0X2NvbG9yPWNvbG9yKQogICAgICAgIHNlbGYubGJsX3N0YXR1c19pY29uLmNvbmZpZ3VyZSh0ZXh0PWljb24sIHRleHRfY29sb3I9Y29sb3IpCgogICAgZGVmIF9hZGRfdG9fbG9nKHNlbGYsIG5hbWUsIHRpbWVfc3RyLCBzdWNjZXNzKToKICAgICAgICBjID0gdGhlbWVfbWFuYWdlci5jb2xvcnMKICAgICAgICBjb2xvciA9IGNbInN1Y2Nlc3MiXSBpZiBzdWNjZXNzIGVsc2UgY1siZXJyb3IiXQogICAgICAgIGljb24gPSAi4pyFIiBpZiBzdWNjZXNzIGVsc2UgIuKdjCIKICAgICAgICAKICAgICAgICBsb2dfaXRlbSA9IGN0ay5DVGtGcmFtZShzZWxmLnNjYW5fbGlzdCwgZmdfY29sb3I9Y1siYmdfc2Vjb25kYXJ5Il0sIGNvcm5lcl9yYWRpdXM9NikKICAgICAgICBsb2dfaXRlbS5wYWNrKGZpbGw9IngiLCBwYWR5PTIpCiAgICAgICAgCiAgICAgICAgY3RrLkNUa0xhYmVsKGxvZ19pdGVtLCB0ZXh0PWljb24sIHRleHRfY29sb3I9Y29sb3IpLnBhY2soc2lkZT0ibGVmdCIsIHBhZHg9KDEwLCA1KSwgcGFkeT04KQogICAgICAgIAogICAgICAgIGluZm9fZnJhbWUgPSBjdGsuQ1RrRnJhbWUobG9nX2l0ZW0sIGZnX2NvbG9yPSJ0cmFuc3BhcmVudCIpCiAgICAgICAgaW5mb19mcmFtZS5wYWNrKHNpZGU9ImxlZnQiLCBmaWxsPSJib3RoIiwgZXhwYW5kPVRydWUpCiAgICAgICAgCiAgICAgICAgY3RrLkNUa0xhYmVsKGluZm9fZnJhbWUsIHRleHQ9bmFtZSwgZm9udD10aGVtZV9tYW5hZ2VyLmZvbnQoImJ1dHRvbiIpLCB0ZXh0X2NvbG9yPWNbInRleHRfcHJpbWFyeSJdKS5wYWNrKGFuY2hvcj0idyIpCiAgICAgICAgY3RrLkNUa0xhYmVsKGluZm9fZnJhbWUsIHRleHQ9dGltZV9zdHIsIGZvbnQ9dGhlbWVfbWFuYWdlci5mb250KCJjYXB0aW9uIiksIHRleHRfY29sb3I9Y1sidGV4dF9tdXRlZCJdKS5wYWNrKGFuY2hvcj0idyIpCgogICAgZGVmIHN0b3Aoc2VsZik6CiAgICAgICAgIiIiQ2FsbGVkIHdoZW4gbmF2aWdhdGluZyBhd2F5LiIiIgogICAgICAgIGlmIHNlbGYuY2FtZXJhX2FjdGl2ZToKICAgICAgICAgICAgc2VsZi50b2dnbGVfY2FtZXJhKCkK', 'gui/pages/records.py': 'IiIiCuKVlOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVlwrilZEgICAgICAgICAgICAgIFJFQ09SRFMg4oCUIEZhY2UgQXR0ZW5kYW5jZSBTeXN0ZW0gICAgICAgICAgICAgICDilZEK4pWRICBWaWV3LCBmaWx0ZXIsIGFuZCBleHBvcnQgYXR0ZW5kYW5jZSByZWNvcmRzICAgICAgICAgICAgICAgIOKVkQrilZrilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZ0KIiIiCgppbXBvcnQgY3VzdG9tdGtpbnRlciBhcyBjdGsKZnJvbSBkYXRhYmFzZS5kYl9tYW5hZ2VyIGltcG9ydCBkYgpmcm9tIHV0aWxzLmhlbHBlcnMgaW1wb3J0IHRoZW1lX21hbmFnZXIsIG9wZW5fZmlsZQpmcm9tIGRhdGV0aW1lIGltcG9ydCBkYXRldGltZSwgZGF0ZQoKY2xhc3MgUmVjb3Jkc1BhZ2UoY3RrLkNUa0ZyYW1lKToKICAgIGRlZiBfX2luaXRfXyhzZWxmLCBwYXJlbnQpOgogICAgICAgIGMgPSB0aGVtZV9tYW5hZ2VyLmNvbG9ycwogICAgICAgIHN1cGVyKCkuX19pbml0X18ocGFyZW50LCBmZ19jb2xvcj1jWyJiZ19wcmltYXJ5Il0sIGNvcm5lcl9yYWRpdXM9MCkKICAgICAgICAKICAgICAgICBzZWxmLnBhY2tfcHJvcGFnYXRlKEZhbHNlKQogICAgICAgIHNlbGYucmVjb3JkcyA9IFtdCiAgICAgICAgc2VsZi5fYnVpbGRfdWkoKQogICAgICAgIHNlbGYucmVmcmVzaF9kYXRhKCkKCiAgICBkZWYgX2J1aWxkX3VpKHNlbGYpOgogICAgICAgIGMgPSB0aGVtZV9tYW5hZ2VyLmNvbG9ycwogICAgICAgIAogICAgICAgICMg4pSA4pSAIEhlYWRlciAmIEZpbHRlcnMg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACiAgICAgICAgaGVhZGVyID0gY3RrLkNUa0ZyYW1lKHNlbGYsIGZnX2NvbG9yPSJ0cmFuc3BhcmVudCIpCiAgICAgICAgaGVhZGVyLnBhY2soZmlsbD0ieCIsIHBhZHg9MzAsIHBhZHk9KDMwLCAyMCkpCiAgICAgICAgCiAgICAgICAgY3RrLkNUa0xhYmVsKAogICAgICAgICAgICBoZWFkZXIsIHRleHQ9IkF0dGVuZGFuY2UgUmVjb3JkcyIsCiAgICAgICAgICAgIGZvbnQ9dGhlbWVfbWFuYWdlci5mb250KCJoZWFkaW5nX2xnIiksIHRleHRfY29sb3I9Y1sidGV4dF9wcmltYXJ5Il0KICAgICAgICApLnBhY2soc2lkZT0ibGVmdCIpCiAgICAgICAgCiAgICAgICAgIyBFeHBvcnQgQnV0dG9ucwogICAgICAgIGJ0bl9mcmFtZSA9IGN0ay5DVGtGcmFtZShoZWFkZXIsIGZnX2NvbG9yPSJ0cmFuc3BhcmVudCIpCiAgICAgICAgYnRuX2ZyYW1lLnBhY2soc2lkZT0icmlnaHQiKQogICAgICAgIAogICAgICAgIGN0ay5DVGtCdXR0b24oCiAgICAgICAgICAgIGJ0bl9mcmFtZSwgdGV4dD0i8J+ThCBFeHBvcnQgQ1NWIiwgd2lkdGg9MTIwLAogICAgICAgICAgICBmb250PXRoZW1lX21hbmFnZXIuZm9udCgiYnV0dG9uIiksIGZnX2NvbG9yPWNbImJnX2hvdmVyIl0sIHRleHRfY29sb3I9Y1sidGV4dF9wcmltYXJ5Il0sCiAgICAgICAgICAgIGNvbW1hbmQ9c2VsZi5fZXhwb3J0X2NzdgogICAgICAgICkucGFjayhzaWRlPSJsZWZ0IiwgcGFkeD01KQogICAgICAgIAogICAgICAgIGN0ay5DVGtCdXR0b24oCiAgICAgICAgICAgIGJ0bl9mcmFtZSwgdGV4dD0i8J+TiiBFeHBvcnQgRXhjZWwiLCB3aWR0aD0xMjAsCiAgICAgICAgICAgIGZvbnQ9dGhlbWVfbWFuYWdlci5mb250KCJidXR0b24iKSwgZmdfY29sb3I9Y1siYWNjZW50X2dyZWVuIl0sIGhvdmVyX2NvbG9yPWNbInN1Y2Nlc3MiXSwKICAgICAgICAgICAgY29tbWFuZD1zZWxmLl9leHBvcnRfZXhjZWwKICAgICAgICApLnBhY2soc2lkZT0ibGVmdCIsIHBhZHg9NSkKICAgICAgICAKICAgICAgICAjIEZpbHRlcnMgQm94CiAgICAgICAgZmlsdGVyX2JveCA9IGN0ay5DVGtGcmFtZShzZWxmLCBmZ19jb2xvcj1jWyJiZ19jYXJkIl0sIGNvcm5lcl9yYWRpdXM9OCkKICAgICAgICBmaWx0ZXJfYm94LnBhY2soZmlsbD0ieCIsIHBhZHg9MzAsIHBhZHk9KDAsIDIwKSkKICAgICAgICAKICAgICAgICAjIFNpbXBsZSBEYXRlIEZpbHRlciAoVG9kYXksIEFsbCBUaW1lKQogICAgICAgIHNlbGYudmFyX2RhdGUgPSBjdGsuU3RyaW5nVmFyKHZhbHVlPSJUb2RheSIpCiAgICAgICAgY3RrLkNUa1NlZ21lbnRlZEJ1dHRvbigKICAgICAgICAgICAgZmlsdGVyX2JveCwgdmFsdWVzPVsiVG9kYXkiLCAiTGFzdCA3IERheXMiLCAiVGhpcyBNb250aCIsICJBbGwgVGltZSJdLAogICAgICAgICAgICB2YXJpYWJsZT1zZWxmLnZhcl9kYXRlLCBjb21tYW5kPXNlbGYuX2FwcGx5X2ZpbHRlcnMKICAgICAgICApLnBhY2soc2lkZT0ibGVmdCIsIHBhZHg9MjAsIHBhZHk9MTUpCiAgICAgICAgCiAgICAgICAgIyBSZWZyZXNoIEJ1dHRvbgogICAgICAgIGN0ay5DVGtCdXR0b24oCiAgICAgICAgICAgIGZpbHRlcl9ib3gsIHRleHQ9IvCflIQgUmVmcmVzaCIsIHdpZHRoPTEwMCwKICAgICAgICAgICAgZmdfY29sb3I9InRyYW5zcGFyZW50IiwgYm9yZGVyX3dpZHRoPTEsIGJvcmRlcl9jb2xvcj1jWyJib3JkZXIiXSwKICAgICAgICAgICAgdGV4dF9jb2xvcj1jWyJ0ZXh0X3ByaW1hcnkiXSwgaG92ZXJfY29sb3I9Y1siYmdfaG92ZXIiXSwKICAgICAgICAgICAgY29tbWFuZD1zZWxmLnJlZnJlc2hfZGF0YQogICAgICAgICkucGFjayhzaWRlPSJyaWdodCIsIHBhZHg9MjAsIHBhZHk9MTUpCgogICAgICAgICMg4pSA4pSAIFRhYmxlIEFyZWEg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACiAgICAgICAgdGFibGVfY29udGFpbmVyID0gY3RrLkNUa0ZyYW1lKHNlbGYsIGZnX2NvbG9yPWNbImJnX2NhcmQiXSwgY29ybmVyX3JhZGl1cz0xMikKICAgICAgICB0YWJsZV9jb250YWluZXIucGFjayhmaWxsPSJib3RoIiwgZXhwYW5kPVRydWUsIHBhZHg9MzAsIHBhZHk9KDAsIDMwKSkKICAgICAgICAKICAgICAgICAjIFRhYmxlIEhlYWRlcgogICAgICAgIHRoZWFkID0gY3RrLkNUa0ZyYW1lKHRhYmxlX2NvbnRhaW5lciwgZmdfY29sb3I9Y1sidGFibGVfaGVhZGVyIl0sIGNvcm5lcl9yYWRpdXM9NikKICAgICAgICB0aGVhZC5wYWNrKGZpbGw9IngiLCBwYWR4PTIwLCBwYWR5PSgyMCwgMTApKQogICAgICAgIHRoZWFkLmdyaWRfY29sdW1uY29uZmlndXJlKCgwLCAxLCAyLCAzLCA0LCA1KSwgd2VpZ2h0PTEpCiAgICAgICAgCiAgICAgICAgaGVhZGVycyA9IFsiRGF0ZSIsICJUaW1lIiwgIk5hbWUiLCAiSUQgLyBSb2xsIiwgIkRlcGFydG1lbnQiLCAiU3RhdHVzIl0KICAgICAgICBmb3IgaSwgdGV4dCBpbiBlbnVtZXJhdGUoaGVhZGVycyk6CiAgICAgICAgICAgIGN0ay5DVGtMYWJlbCgKICAgICAgICAgICAgICAgIHRoZWFkLCB0ZXh0PXRleHQsIGZvbnQ9dGhlbWVfbWFuYWdlci5mb250KCJidXR0b24iKSwgdGV4dF9jb2xvcj1jWyJ0ZXh0X3NlY29uZGFyeSJdCiAgICAgICAgICAgICkuZ3JpZChyb3c9MCwgY29sdW1uPWksIHBhZHg9MTAsIHBhZHk9OCwgc3RpY2t5PSJ3IikKICAgICAgICAgICAgCiAgICAgICAgIyBUYWJsZSBCb2R5IChTY3JvbGxhYmxlKQogICAgICAgIHNlbGYudGJvZHkgPSBjdGsuQ1RrU2Nyb2xsYWJsZUZyYW1lKHRhYmxlX2NvbnRhaW5lciwgZmdfY29sb3I9InRyYW5zcGFyZW50IikKICAgICAgICBzZWxmLnRib2R5LnBhY2soZmlsbD0iYm90aCIsIGV4cGFuZD1UcnVlLCBwYWR4PTIwLCBwYWR5PSgwLCAyMCkpCiAgICAgICAgc2VsZi50Ym9keS5ncmlkX2NvbHVtbmNvbmZpZ3VyZSgoMCwgMSwgMiwgMywgNCwgNSksIHdlaWdodD0xKQoKICAgIGRlZiBfYXBwbHlfZmlsdGVycyhzZWxmLCAqYXJncyk6CiAgICAgICAgc2VsZi5yZWZyZXNoX2RhdGEoKQoKICAgIGRlZiByZWZyZXNoX2RhdGEoc2VsZik6CiAgICAgICAgZm9yIHdpZGdldCBpbiBzZWxmLnRib2R5LndpbmZvX2NoaWxkcmVuKCk6CiAgICAgICAgICAgIHdpZGdldC5kZXN0cm95KCkKICAgICAgICAgICAgCiAgICAgICAgZGF0ZV9maWx0ZXIgPSBzZWxmLnZhcl9kYXRlLmdldCgpCiAgICAgICAgCiAgICAgICAgIyBDb21wdXRlIHN0YXJ0L2VuZCBkYXRlcyBiYXNlZCBvbiBzZWxlY3Rpb24KICAgICAgICAjIEZvciBzaW1wbGljaXR5LCB3ZSBqdXN0IHBhc3Mgc3RyaW5nIHBhcmFtZXRlcnMgdG8gb3VyIGRiIGZ1bmN0aW9uIGlmIG5lZWRlZAogICAgICAgIGltcG9ydCBkYXRldGltZSBhcyBkdAogICAgICAgIHRvZGF5ID0gZHQuZGF0ZS50b2RheSgpCiAgICAgICAgCiAgICAgICAgc3RhcnRfc3RyID0gTm9uZQogICAgICAgIGVuZF9zdHIgPSB0b2RheS5zdHJmdGltZSgiJVktJW0tJWQiKQogICAgICAgIAogICAgICAgIGlmIGRhdGVfZmlsdGVyID09ICJUb2RheSI6CiAgICAgICAgICAgIHN0YXJ0X3N0ciA9IHRvZGF5LnN0cmZ0aW1lKCIlWS0lbS0lZCIpCiAgICAgICAgZWxpZiBkYXRlX2ZpbHRlciA9PSAiTGFzdCA3IERheXMiOgogICAgICAgICAgICBzdGFydF9zdHIgPSAodG9kYXkgLSBkdC50aW1lZGVsdGEoZGF5cz03KSkuc3RyZnRpbWUoIiVZLSVtLSVkIikKICAgICAgICBlbGlmIGRhdGVfZmlsdGVyID09ICJUaGlzIE1vbnRoIjoKICAgICAgICAgICAgc3RhcnRfc3RyID0gdG9kYXkucmVwbGFjZShkYXk9MSkuc3RyZnRpbWUoIiVZLSVtLSVkIikKICAgICAgICBlbGlmIGRhdGVfZmlsdGVyID09ICJBbGwgVGltZSI6CiAgICAgICAgICAgIHN0YXJ0X3N0ciA9IE5vbmUKICAgICAgICAgICAgZW5kX3N0ciA9IE5vbmUKICAgICAgICAgICAgCiAgICAgICAgc2VsZi5yZWNvcmRzID0gZGIuZ2V0X2F0dGVuZGFuY2VfcmVjb3JkcyhzdGFydF9kYXRlPXN0YXJ0X3N0ciwgZW5kX2RhdGU9ZW5kX3N0cikKICAgICAgICBjID0gdGhlbWVfbWFuYWdlci5jb2xvcnMKICAgICAgICAKICAgICAgICBpZiBub3Qgc2VsZi5yZWNvcmRzOgogICAgICAgICAgICBjdGsuQ1RrTGFiZWwoCiAgICAgICAgICAgICAgICBzZWxmLnRib2R5LCB0ZXh0PSJObyByZWNvcmRzIGZvdW5kLiIsCiAgICAgICAgICAgICAgICB0ZXh0X2NvbG9yPWNbInRleHRfbXV0ZWQiXSwgZm9udD10aGVtZV9tYW5hZ2VyLmZvbnQoImJvZHlfbWQiKQogICAgICAgICAgICApLmdyaWQocm93PTAsIGNvbHVtbj0wLCBjb2x1bW5zcGFuPTYsIHBhZHk9NDApCiAgICAgICAgICAgIHJldHVybgogICAgICAgICAgICAKICAgICAgICBmb3Igcm93X2lkeCwgciBpbiBlbnVtZXJhdGUoc2VsZi5yZWNvcmRzKToKICAgICAgICAgICAgYmcgPSBjWyJ0YWJsZV9yb3ciXSBpZiByb3dfaWR4ICUgMiA9PSAwIGVsc2UgY1sidGFibGVfcm93X2FsdCJdCiAgICAgICAgICAgIHJvd19mcmFtZSA9IGN0ay5DVGtGcmFtZShzZWxmLnRib2R5LCBmZ19jb2xvcj1iZywgY29ybmVyX3JhZGl1cz02KQogICAgICAgICAgICByb3dfZnJhbWUuZ3JpZChyb3c9cm93X2lkeCwgY29sdW1uPTAsIGNvbHVtbnNwYW49Niwgc3RpY2t5PSJldyIsIHBhZHk9MikKICAgICAgICAgICAgcm93X2ZyYW1lLmdyaWRfY29sdW1uY29uZmlndXJlKCgwLCAxLCAyLCAzLCA0LCA1KSwgd2VpZ2h0PTEpCiAgICAgICAgICAgIAogICAgICAgICAgICBjdGsuQ1RrTGFiZWwocm93X2ZyYW1lLCB0ZXh0PXJbImRhdGUiXSwgdGV4dF9jb2xvcj1jWyJ0ZXh0X3ByaW1hcnkiXSkuZ3JpZChyb3c9MCwgY29sdW1uPTAsIHBhZHg9MTAsIHBhZHk9MTAsIHN0aWNreT0idyIpCiAgICAgICAgICAgIGN0ay5DVGtMYWJlbChyb3dfZnJhbWUsIHRleHQ9clsidGltZSJdLCB0ZXh0X2NvbG9yPWNbInRleHRfc2Vjb25kYXJ5Il0pLmdyaWQocm93PTAsIGNvbHVtbj0xLCBwYWR4PTEwLCBwYWR5PTEwLCBzdGlja3k9InciKQogICAgICAgICAgICBjdGsuQ1RrTGFiZWwocm93X2ZyYW1lLCB0ZXh0PXJbIm5hbWUiXSwgdGV4dF9jb2xvcj1jWyJ0ZXh0X3ByaW1hcnkiXSwgZm9udD10aGVtZV9tYW5hZ2VyLmZvbnQoImJ1dHRvbiIpKS5ncmlkKHJvdz0wLCBjb2x1bW49MiwgcGFkeD0xMCwgcGFkeT0xMCwgc3RpY2t5PSJ3IikKICAgICAgICAgICAgY3RrLkNUa0xhYmVsKHJvd19mcmFtZSwgdGV4dD1yWyJyb2xsX251bWJlciJdLCB0ZXh0X2NvbG9yPWNbInRleHRfc2Vjb25kYXJ5Il0pLmdyaWQocm93PTAsIGNvbHVtbj0zLCBwYWR4PTEwLCBwYWR5PTEwLCBzdGlja3k9InciKQogICAgICAgICAgICBjdGsuQ1RrTGFiZWwocm93X2ZyYW1lLCB0ZXh0PXJbImRlcGFydG1lbnQiXSwgdGV4dF9jb2xvcj1jWyJ0ZXh0X3NlY29uZGFyeSJdKS5ncmlkKHJvdz0wLCBjb2x1bW49NCwgcGFkeD0xMCwgcGFkeT0xMCwgc3RpY2t5PSJ3IikKICAgICAgICAgICAgCiAgICAgICAgICAgIHN0YXR1c19jb2xvciA9IGNbInN1Y2Nlc3MiXSBpZiByWyJzdGF0dXMiXSA9PSAiUHJlc2VudCIgZWxzZSBjWyJlcnJvciJdCiAgICAgICAgICAgIGN0ay5DVGtMYWJlbChyb3dfZnJhbWUsIHRleHQ9clsic3RhdHVzIl0sIHRleHRfY29sb3I9c3RhdHVzX2NvbG9yLCBmb250PXRoZW1lX21hbmFnZXIuZm9udCgiYmFkZ2UiKSkuZ3JpZChyb3c9MCwgY29sdW1uPTUsIHBhZHg9MTAsIHBhZHk9MTAsIHN0aWNreT0idyIpCgogICAgZGVmIF9leHBvcnRfY3N2KHNlbGYpOgogICAgICAgIHBhdGggPSBkYi5leHBvcnRfdG9fY3N2KHNlbGYucmVjb3JkcykKICAgICAgICBpZiBwYXRoOiBvcGVuX2ZpbGUocGF0aCkKCiAgICBkZWYgX2V4cG9ydF9leGNlbChzZWxmKToKICAgICAgICBwYXRoID0gZGIuZXhwb3J0X3RvX2V4Y2VsKHNlbGYucmVjb3JkcykKICAgICAgICBpZiBwYXRoOiBvcGVuX2ZpbGUocGF0aCkK', 'gui/pages/__init__.py': 'IyBQYWdlcyBwYWNrYWdlCg==', 'gui/pages/dashboard.py': 'IiIiCuKVlOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVlwrilZEgICAgICAgICAgICAgREFTSEJPQVJEIOKAlCBGYWNlIEF0dGVuZGFuY2UgU3lzdGVtICAgICAgICAgICAgICDilZEK4pWRICBIb21lIHNjcmVlbiB3aXRoIHN1bW1hcnkgY2FyZHMgYW5kIHJlY2VudCBhY3Rpdml0eSAgICAgICAgIOKVkQrilZrilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZ0KIiIiCgppbXBvcnQgY3VzdG9tdGtpbnRlciBhcyBjdGsKZnJvbSBkYXRhYmFzZS5kYl9tYW5hZ2VyIGltcG9ydCBkYgpmcm9tIHV0aWxzLmhlbHBlcnMgaW1wb3J0IHRoZW1lX21hbmFnZXIsIGdldF9jdXJyZW50X2RhdGVfc3RyCgpjbGFzcyBEYXNoYm9hcmRQYWdlKGN0ay5DVGtGcmFtZSk6CiAgICBkZWYgX19pbml0X18oc2VsZiwgcGFyZW50KToKICAgICAgICBjID0gdGhlbWVfbWFuYWdlci5jb2xvcnMKICAgICAgICBzdXBlcigpLl9faW5pdF9fKHBhcmVudCwgZmdfY29sb3I9Y1siYmdfcHJpbWFyeSJdLCBjb3JuZXJfcmFkaXVzPTApCiAgICAgICAgCiAgICAgICAgc2VsZi5wYWNrX3Byb3BhZ2F0ZShGYWxzZSkKICAgICAgICBzZWxmLl9idWlsZF91aSgpCiAgICAgICAgc2VsZi5yZWZyZXNoX2RhdGEoKQoKICAgIGRlZiBfYnVpbGRfdWkoc2VsZik6CiAgICAgICAgYyA9IHRoZW1lX21hbmFnZXIuY29sb3JzCiAgICAgICAgCiAgICAgICAgIyDilIDilIAgSGVhZGVyIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgAogICAgICAgIGhlYWRlciA9IGN0ay5DVGtGcmFtZShzZWxmLCBmZ19jb2xvcj0idHJhbnNwYXJlbnQiKQogICAgICAgIGhlYWRlci5wYWNrKGZpbGw9IngiLCBwYWR4PTMwLCBwYWR5PSgzMCwgMjApKQogICAgICAgIAogICAgICAgIGN0ay5DVGtMYWJlbCgKICAgICAgICAgICAgaGVhZGVyLCB0ZXh0PSJEYXNoYm9hcmQgT3ZlcnZpZXciLAogICAgICAgICAgICBmb250PXRoZW1lX21hbmFnZXIuZm9udCgiaGVhZGluZ19sZyIpLCB0ZXh0X2NvbG9yPWNbInRleHRfcHJpbWFyeSJdCiAgICAgICAgKS5wYWNrKHNpZGU9ImxlZnQiKQogICAgICAgIAogICAgICAgIHNlbGYuZGF0ZV9sYWJlbCA9IGN0ay5DVGtMYWJlbCgKICAgICAgICAgICAgaGVhZGVyLCB0ZXh0PWdldF9jdXJyZW50X2RhdGVfc3RyKCksCiAgICAgICAgICAgIGZvbnQ9dGhlbWVfbWFuYWdlci5mb250KCJib2R5X21kIiksIHRleHRfY29sb3I9Y1sidGV4dF9zZWNvbmRhcnkiXQogICAgICAgICkKICAgICAgICBzZWxmLmRhdGVfbGFiZWwucGFjayhzaWRlPSJyaWdodCIpCiAgICAgICAgCiAgICAgICAgIyDilIDilIAgQ2FyZHMgQ29udGFpbmVyIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgAogICAgICAgIGNhcmRzX2ZyYW1lID0gY3RrLkNUa0ZyYW1lKHNlbGYsIGZnX2NvbG9yPSJ0cmFuc3BhcmVudCIpCiAgICAgICAgY2FyZHNfZnJhbWUucGFjayhmaWxsPSJ4IiwgcGFkeD0zMCwgcGFkeT0oMCwgMjApKQogICAgICAgIGNhcmRzX2ZyYW1lLmdyaWRfY29sdW1uY29uZmlndXJlKCgwLCAxLCAyKSwgd2VpZ2h0PTEsIHVuaWZvcm09ImNhcmQiKQogICAgICAgIAogICAgICAgICMgVG90YWwgVXNlcnMgQ2FyZAogICAgICAgIHNlbGYubGJsX3RvdGFsX3VzZXJzID0gc2VsZi5fY3JlYXRlX3N1bW1hcnlfY2FyZCgKICAgICAgICAgICAgY2FyZHNfZnJhbWUsICJUb3RhbCBSZWdpc3RlcmVkIiwgIjAiLCAi8J+RpCIsIGNbImFjY2VudF9wdXJwbGUiXSwgMAogICAgICAgICkKICAgICAgICAKICAgICAgICAjIFRvZGF5IFByZXNlbnQgQ2FyZAogICAgICAgIHNlbGYubGJsX3ByZXNlbnQgPSBzZWxmLl9jcmVhdGVfc3VtbWFyeV9jYXJkKAogICAgICAgICAgICBjYXJkc19mcmFtZSwgIlRvZGF5J3MgQXR0ZW5kYW5jZSIsICIwIiwgIuKchSIsIGNbImFjY2VudF9ncmVlbiJdLCAxCiAgICAgICAgKQogICAgICAgIAogICAgICAgICMgQXR0ZW5kYW5jZSAlIENhcmQKICAgICAgICBzZWxmLmxibF9wZXJjZW50ID0gc2VsZi5fY3JlYXRlX3N1bW1hcnlfY2FyZCgKICAgICAgICAgICAgY2FyZHNfZnJhbWUsICJBdmVyYWdlIEF0dGVuZGFuY2UiLCAiMCUiLCAi8J+TiCIsIGNbImFjY2VudCJdLCAyCiAgICAgICAgKQogICAgICAgIAogICAgICAgICMg4pSA4pSAIFJlY2VudCBBY3Rpdml0eSBUYWJsZSDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIAKICAgICAgICBhY3Rpdml0eV9mcmFtZSA9IGN0ay5DVGtGcmFtZShzZWxmLCBmZ19jb2xvcj1jWyJiZ19jYXJkIl0sIGNvcm5lcl9yYWRpdXM9MTIpCiAgICAgICAgYWN0aXZpdHlfZnJhbWUucGFjayhmaWxsPSJib3RoIiwgZXhwYW5kPVRydWUsIHBhZHg9MzAsIHBhZHk9KDAsIDMwKSkKICAgICAgICAKICAgICAgICBjdGsuQ1RrTGFiZWwoCiAgICAgICAgICAgIGFjdGl2aXR5X2ZyYW1lLCB0ZXh0PSJSZWNlbnQgU2NhbnMiLAogICAgICAgICAgICBmb250PXRoZW1lX21hbmFnZXIuZm9udCgiaGVhZGluZ19tZCIpLCB0ZXh0X2NvbG9yPWNbInRleHRfcHJpbWFyeSJdCiAgICAgICAgKS5wYWNrKGFuY2hvcj0idyIsIHBhZHg9MjAsIHBhZHk9KDIwLCAxMCkpCiAgICAgICAgCiAgICAgICAgIyBUYWJsZSBIZWFkZXIKICAgICAgICB0aGVhZCA9IGN0ay5DVGtGcmFtZShhY3Rpdml0eV9mcmFtZSwgZmdfY29sb3I9Y1sidGFibGVfaGVhZGVyIl0sIGNvcm5lcl9yYWRpdXM9NikKICAgICAgICB0aGVhZC5wYWNrKGZpbGw9IngiLCBwYWR4PTIwLCBwYWR5PSgwLCAxMCkpCiAgICAgICAgdGhlYWQuZ3JpZF9jb2x1bW5jb25maWd1cmUoKDAsIDEsIDIsIDMpLCB3ZWlnaHQ9MSkKICAgICAgICAKICAgICAgICBoZWFkZXJzID0gWyJOYW1lIiwgIklEIC8gUm9sbCBObyIsICJEZXBhcnRtZW50IiwgIlRpbWUiXQogICAgICAgIGZvciBpLCB0ZXh0IGluIGVudW1lcmF0ZShoZWFkZXJzKToKICAgICAgICAgICAgY3RrLkNUa0xhYmVsKAogICAgICAgICAgICAgICAgdGhlYWQsIHRleHQ9dGV4dCwgZm9udD10aGVtZV9tYW5hZ2VyLmZvbnQoImJ1dHRvbiIpLCB0ZXh0X2NvbG9yPWNbInRleHRfc2Vjb25kYXJ5Il0KICAgICAgICAgICAgKS5ncmlkKHJvdz0wLCBjb2x1bW49aSwgcGFkeD0xMCwgcGFkeT04LCBzdGlja3k9InciKQogICAgICAgICAgICAKICAgICAgICAjIFRhYmxlIEJvZHkgKFNjcm9sbGFibGUpCiAgICAgICAgc2VsZi50Ym9keSA9IGN0ay5DVGtTY3JvbGxhYmxlRnJhbWUoYWN0aXZpdHlfZnJhbWUsIGZnX2NvbG9yPSJ0cmFuc3BhcmVudCIpCiAgICAgICAgc2VsZi50Ym9keS5wYWNrKGZpbGw9ImJvdGgiLCBleHBhbmQ9VHJ1ZSwgcGFkeD0yMCwgcGFkeT0oMCwgMjApKQogICAgICAgIHNlbGYudGJvZHkuZ3JpZF9jb2x1bW5jb25maWd1cmUoKDAsIDEsIDIsIDMpLCB3ZWlnaHQ9MSkKCiAgICBkZWYgX2NyZWF0ZV9zdW1tYXJ5X2NhcmQoc2VsZiwgcGFyZW50LCB0aXRsZSwgdmFsdWUsIGljb24sIGNvbG9yLCBjb2wpOgogICAgICAgIGMgPSB0aGVtZV9tYW5hZ2VyLmNvbG9ycwogICAgICAgIGNhcmQgPSBjdGsuQ1RrRnJhbWUocGFyZW50LCBmZ19jb2xvcj1jWyJiZ19jYXJkIl0sIGNvcm5lcl9yYWRpdXM9MTIsIGhlaWdodD0xMjApCiAgICAgICAgY2FyZC5ncmlkKHJvdz0wLCBjb2x1bW49Y29sLCBwYWR4PTEwLCBzdGlja3k9Im5zZXciKQogICAgICAgIGNhcmQucGFja19wcm9wYWdhdGUoRmFsc2UpCiAgICAgICAgCiAgICAgICAgIyBUb3AgYm9yZGVyCiAgICAgICAgYm9yZGVyID0gY3RrLkNUa0ZyYW1lKGNhcmQsIGZnX2NvbG9yPWNvbG9yLCBoZWlnaHQ9NCwgY29ybmVyX3JhZGl1cz0wKQogICAgICAgIGJvcmRlci5wYWNrKGZpbGw9IngiLCBzaWRlPSJ0b3AiKQogICAgICAgIAogICAgICAgIGNvbnRlbnQgPSBjdGsuQ1RrRnJhbWUoY2FyZCwgZmdfY29sb3I9InRyYW5zcGFyZW50IikKICAgICAgICBjb250ZW50LnBhY2soZmlsbD0iYm90aCIsIGV4cGFuZD1UcnVlLCBwYWR4PTIwLCBwYWR5PTE1KQogICAgICAgIAogICAgICAgIGhlYWRlciA9IGN0ay5DVGtGcmFtZShjb250ZW50LCBmZ19jb2xvcj0idHJhbnNwYXJlbnQiKQogICAgICAgIGhlYWRlci5wYWNrKGZpbGw9IngiKQogICAgICAgIAogICAgICAgIGN0ay5DVGtMYWJlbCgKICAgICAgICAgICAgaGVhZGVyLCB0ZXh0PXRpdGxlLCBmb250PXRoZW1lX21hbmFnZXIuZm9udCgiYm9keV9tZCIpLCB0ZXh0X2NvbG9yPWNbInRleHRfc2Vjb25kYXJ5Il0KICAgICAgICApLnBhY2soc2lkZT0ibGVmdCIpCiAgICAgICAgCiAgICAgICAgY3RrLkNUa0xhYmVsKAogICAgICAgICAgICBoZWFkZXIsIHRleHQ9aWNvbiwgZm9udD1jdGsuQ1RrRm9udChzaXplPTE4KSwgdGV4dF9jb2xvcj1jb2xvcgogICAgICAgICkucGFjayhzaWRlPSJyaWdodCIpCiAgICAgICAgCiAgICAgICAgdmFsdWVfbGJsID0gY3RrLkNUa0xhYmVsKAogICAgICAgICAgICBjb250ZW50LCB0ZXh0PXZhbHVlLCBmb250PXRoZW1lX21hbmFnZXIuZm9udCgiaGVhZGluZ194bCIpLCB0ZXh0X2NvbG9yPWNbInRleHRfcHJpbWFyeSJdCiAgICAgICAgKQogICAgICAgIHZhbHVlX2xibC5wYWNrKGFuY2hvcj0idyIsIHBhZHk9KDEwLCAwKSkKICAgICAgICAKICAgICAgICByZXR1cm4gdmFsdWVfbGJsCgogICAgZGVmIHJlZnJlc2hfZGF0YShzZWxmKToKICAgICAgICAiIiJGZXRjaCBsYXRlc3QgZGF0YSBmcm9tIERCIGFuZCB1cGRhdGUgVUkuIiIiCiAgICAgICAgdG90YWwgPSBkYi5nZXRfdG90YWxfdXNlcnMoKQogICAgICAgIHByZXNlbnQgPSBkYi5nZXRfdG9kYXlfY291bnQoKQogICAgICAgIHBlcmNlbnQgPSBkYi5nZXRfYXR0ZW5kYW5jZV9wZXJjZW50YWdlKGRheXM9NykKICAgICAgICAKICAgICAgICBzZWxmLmxibF90b3RhbF91c2Vycy5jb25maWd1cmUodGV4dD1zdHIodG90YWwpKQogICAgICAgIHNlbGYubGJsX3ByZXNlbnQuY29uZmlndXJlKHRleHQ9c3RyKHByZXNlbnQpKQogICAgICAgIHNlbGYubGJsX3BlcmNlbnQuY29uZmlndXJlKHRleHQ9ZiJ7cGVyY2VudH0lIikKICAgICAgICBzZWxmLmRhdGVfbGFiZWwuY29uZmlndXJlKHRleHQ9Z2V0X2N1cnJlbnRfZGF0ZV9zdHIoKSkKICAgICAgICAKICAgICAgICAjIFVwZGF0ZSBUYWJsZQogICAgICAgIGZvciB3aWRnZXQgaW4gc2VsZi50Ym9keS53aW5mb19jaGlsZHJlbigpOgogICAgICAgICAgICB3aWRnZXQuZGVzdHJveSgpCiAgICAgICAgICAgIAogICAgICAgIHJlY2VudCA9IGRiLmdldF90b2RheV9hdHRlbmRhbmNlKClbOjE1XSAgIyBUb3AgMTUgdG9kYXkKICAgICAgICBjID0gdGhlbWVfbWFuYWdlci5jb2xvcnMKICAgICAgICAKICAgICAgICBpZiBub3QgcmVjZW50OgogICAgICAgICAgICBjdGsuQ1RrTGFiZWwoCiAgICAgICAgICAgICAgICBzZWxmLnRib2R5LCB0ZXh0PSJObyBhdHRlbmRhbmNlIHJlY29yZGVkIHRvZGF5LiIsCiAgICAgICAgICAgICAgICB0ZXh0X2NvbG9yPWNbInRleHRfbXV0ZWQiXSwgZm9udD10aGVtZV9tYW5hZ2VyLmZvbnQoImJvZHlfbWQiKQogICAgICAgICAgICApLmdyaWQocm93PTAsIGNvbHVtbj0wLCBjb2x1bW5zcGFuPTQsIHBhZHk9MzApCiAgICAgICAgICAgIHJldHVybgogICAgICAgICAgICAKICAgICAgICBmb3Igcm93X2lkeCwgciBpbiBlbnVtZXJhdGUocmVjZW50KToKICAgICAgICAgICAgYmcgPSBjWyJ0YWJsZV9yb3ciXSBpZiByb3dfaWR4ICUgMiA9PSAwIGVsc2UgY1sidGFibGVfcm93X2FsdCJdCiAgICAgICAgICAgIHJvd19mcmFtZSA9IGN0ay5DVGtGcmFtZShzZWxmLnRib2R5LCBmZ19jb2xvcj1iZywgY29ybmVyX3JhZGl1cz02KQogICAgICAgICAgICByb3dfZnJhbWUuZ3JpZChyb3c9cm93X2lkeCwgY29sdW1uPTAsIGNvbHVtbnNwYW49NCwgc3RpY2t5PSJldyIsIHBhZHk9MikKICAgICAgICAgICAgcm93X2ZyYW1lLmdyaWRfY29sdW1uY29uZmlndXJlKCgwLCAxLCAyLCAzKSwgd2VpZ2h0PTEpCiAgICAgICAgICAgIAogICAgICAgICAgICBjdGsuQ1RrTGFiZWwocm93X2ZyYW1lLCB0ZXh0PXJbIm5hbWUiXSwgdGV4dF9jb2xvcj1jWyJ0ZXh0X3ByaW1hcnkiXSkuZ3JpZChyb3c9MCwgY29sdW1uPTAsIHBhZHg9MTAsIHBhZHk9MTAsIHN0aWNreT0idyIpCiAgICAgICAgICAgIGN0ay5DVGtMYWJlbChyb3dfZnJhbWUsIHRleHQ9clsicm9sbF9udW1iZXIiXSwgdGV4dF9jb2xvcj1jWyJ0ZXh0X3NlY29uZGFyeSJdKS5ncmlkKHJvdz0wLCBjb2x1bW49MSwgcGFkeD0xMCwgcGFkeT0xMCwgc3RpY2t5PSJ3IikKICAgICAgICAgICAgY3RrLkNUa0xhYmVsKHJvd19mcmFtZSwgdGV4dD1yWyJkZXBhcnRtZW50Il0sIHRleHRfY29sb3I9Y1sidGV4dF9zZWNvbmRhcnkiXSkuZ3JpZChyb3c9MCwgY29sdW1uPTIsIHBhZHg9MTAsIHBhZHk9MTAsIHN0aWNreT0idyIpCiAgICAgICAgICAgIGN0ay5DVGtMYWJlbChyb3dfZnJhbWUsIHRleHQ9clsidGltZSJdLCB0ZXh0X2NvbG9yPWNbImFjY2VudCJdKS5ncmlkKHJvdz0wLCBjb2x1bW49MywgcGFkeD0xMCwgcGFkeT0xMCwgc3RpY2t5PSJ3IikK', 'gui/pages/settings.py': 'IiIiCuKVlOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVlwrilZEgICAgICAgICAgICAgIFNFVFRJTkdTIOKAlCBGYWNlIEF0dGVuZGFuY2UgU3lzdGVtICAgICAgICAgICAgICDilZEK4pWRICBBcHAgY29uZmlndXJhdGlvbiwgY2FtZXJhIHNlbGVjdGlvbiwgYW5kIGJhY2t1cHMgICAgICAgICAgIOKVkQrilZrilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZ0KIiIiCgppbXBvcnQgY3VzdG9tdGtpbnRlciBhcyBjdGsKZnJvbSBkYXRhYmFzZS5kYl9tYW5hZ2VyIGltcG9ydCBkYgpmcm9tIGZhY2VfcmVjb2duaXRpb25fZW5naW5lLnJlY29nbml6ZXIgaW1wb3J0IGVuZ2luZQpmcm9tIHV0aWxzLmhlbHBlcnMgaW1wb3J0IHRoZW1lX21hbmFnZXIsIGxpc3RfYXZhaWxhYmxlX2NhbWVyYXMsIG9wZW5fZmlsZQoKY2xhc3MgU2V0dGluZ3NQYWdlKGN0ay5DVGtGcmFtZSk6CiAgICBkZWYgX19pbml0X18oc2VsZiwgcGFyZW50KToKICAgICAgICBjID0gdGhlbWVfbWFuYWdlci5jb2xvcnMKICAgICAgICBzdXBlcigpLl9faW5pdF9fKHBhcmVudCwgZmdfY29sb3I9Y1siYmdfcHJpbWFyeSJdLCBjb3JuZXJfcmFkaXVzPTApCiAgICAgICAgCiAgICAgICAgc2VsZi5wYWNrX3Byb3BhZ2F0ZShGYWxzZSkKICAgICAgICBzZWxmLl9idWlsZF91aSgpCgogICAgZGVmIF9idWlsZF91aShzZWxmKToKICAgICAgICBjID0gdGhlbWVfbWFuYWdlci5jb2xvcnMKICAgICAgICAKICAgICAgICAjIEhlYWRlcgogICAgICAgIGhlYWRlciA9IGN0ay5DVGtGcmFtZShzZWxmLCBmZ19jb2xvcj0idHJhbnNwYXJlbnQiKQogICAgICAgIGhlYWRlci5wYWNrKGZpbGw9IngiLCBwYWR4PTMwLCBwYWR5PSgzMCwgMjApKQogICAgICAgIGN0ay5DVGtMYWJlbCgKICAgICAgICAgICAgaGVhZGVyLCB0ZXh0PSJTeXN0ZW0gU2V0dGluZ3MiLAogICAgICAgICAgICBmb250PXRoZW1lX21hbmFnZXIuZm9udCgiaGVhZGluZ19sZyIpLCB0ZXh0X2NvbG9yPWNbInRleHRfcHJpbWFyeSJdCiAgICAgICAgKS5wYWNrKHNpZGU9ImxlZnQiKQoKICAgICAgICAjIFNjcm9sbGFibGUgY29udGFpbmVyIGZvciBzZXR0aW5ncyBjYXRlZ29yaWVzCiAgICAgICAgc2Nyb2xsID0gY3RrLkNUa1Njcm9sbGFibGVGcmFtZShzZWxmLCBmZ19jb2xvcj0idHJhbnNwYXJlbnQiKQogICAgICAgIHNjcm9sbC5wYWNrKGZpbGw9ImJvdGgiLCBleHBhbmQ9VHJ1ZSwgcGFkeD0yMCwgcGFkeT0oMCwgMjApKQoKICAgICAgICAjIOKUgOKUgCBHZW5lcmFsIFNldHRpbmdzIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgAogICAgICAgIGdlbl9mcmFtZSA9IHNlbGYuX2NyZWF0ZV9zZWN0aW9uKHNjcm9sbCwgIkdlbmVyYWwgU2V0dGluZ3MiKQogICAgICAgIAogICAgICAgICMgVGhlbWUgVG9nZ2xlCiAgICAgICAgdGhlbWVfdmFsID0gZGIuZ2V0X3NldHRpbmcoInRoZW1lIiwgImRhcmsiKQogICAgICAgIHNlbGYuc3dfdGhlbWUgPSBjdGsuQ1RrU3dpdGNoKGdlbl9mcmFtZSwgdGV4dD0iRGFyayBNb2RlIiwgZm9udD10aGVtZV9tYW5hZ2VyLmZvbnQoImJvZHlfbWQiKSkKICAgICAgICBpZiB0aGVtZV92YWwgPT0gImRhcmsiOiBzZWxmLnN3X3RoZW1lLnNlbGVjdCgpCiAgICAgICAgc2VsZi5zd190aGVtZS5wYWNrKGFuY2hvcj0idyIsIHBhZHg9MjAsIHBhZHk9MTApCiAgICAgICAgCiAgICAgICAgIyBTb3VuZCBUb2dnbGUKICAgICAgICBzb3VuZF92YWwgPSBkYi5nZXRfc2V0dGluZygic291bmRfZW5hYmxlZCIsICJ0cnVlIikKICAgICAgICBzZWxmLnN3X3NvdW5kID0gY3RrLkNUa1N3aXRjaChnZW5fZnJhbWUsIHRleHQ9IkVuYWJsZSBTb3VuZCBFZmZlY3RzIiwgZm9udD10aGVtZV9tYW5hZ2VyLmZvbnQoImJvZHlfbWQiKSkKICAgICAgICBpZiBzb3VuZF92YWwgPT0gInRydWUiOiBzZWxmLnN3X3NvdW5kLnNlbGVjdCgpCiAgICAgICAgc2VsZi5zd19zb3VuZC5wYWNrKGFuY2hvcj0idyIsIHBhZHg9MjAsIHBhZHk9MTApCgogICAgICAgICMg4pSA4pSAIEhhcmR3YXJlIFNldHRpbmdzIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgAogICAgICAgIGh3X2ZyYW1lID0gc2VsZi5fY3JlYXRlX3NlY3Rpb24oc2Nyb2xsLCAiSGFyZHdhcmUgJiBSZWNvZ25pdGlvbiIpCiAgICAgICAgCiAgICAgICAgIyBDYW1lcmEgU2VsZWN0aW9uCiAgICAgICAgY2FtX2ZyYW1lID0gY3RrLkNUa0ZyYW1lKGh3X2ZyYW1lLCBmZ19jb2xvcj0idHJhbnNwYXJlbnQiKQogICAgICAgIGNhbV9mcmFtZS5wYWNrKGZpbGw9IngiLCBwYWR4PTIwLCBwYWR5PTEwKQogICAgICAgIGN0ay5DVGtMYWJlbChjYW1fZnJhbWUsIHRleHQ9IkFjdGl2ZSBDYW1lcmEgSW5kZXgiLCBmb250PXRoZW1lX21hbmFnZXIuZm9udCgiYm9keV9tZCIpKS5wYWNrKHNpZGU9ImxlZnQiKQogICAgICAgIAogICAgICAgIGNhbXMgPSBbc3RyKGkpIGZvciBpIGluIGxpc3RfYXZhaWxhYmxlX2NhbWVyYXMoKV0KICAgICAgICBpZiBub3QgY2FtczogY2FtcyA9IFsiMCJdCiAgICAgICAgc2VsZi5jYW1fY29tYm8gPSBjdGsuQ1RrQ29tYm9Cb3goY2FtX2ZyYW1lLCB2YWx1ZXM9Y2Ftcywgd2lkdGg9MTAwKQogICAgICAgIHNlbGYuY2FtX2NvbWJvLnNldChkYi5nZXRfc2V0dGluZygiY2FtZXJhX2luZGV4IiwgIjAiKSkKICAgICAgICBzZWxmLmNhbV9jb21iby5wYWNrKHNpZGU9InJpZ2h0IikKICAgICAgICAKICAgICAgICAjIFJlY29nbml0aW9uIFRvbGVyYW5jZQogICAgICAgIHRvbF9mcmFtZSA9IGN0ay5DVGtGcmFtZShod19mcmFtZSwgZmdfY29sb3I9InRyYW5zcGFyZW50IikKICAgICAgICB0b2xfZnJhbWUucGFjayhmaWxsPSJ4IiwgcGFkeD0yMCwgcGFkeT0xMCkKICAgICAgICBjdGsuQ1RrTGFiZWwodG9sX2ZyYW1lLCB0ZXh0PSJSZWNvZ25pdGlvbiBTdHJpY3RuZXNzIiwgZm9udD10aGVtZV9tYW5hZ2VyLmZvbnQoImJvZHlfbWQiKSkucGFjayhzaWRlPSJsZWZ0IikKICAgICAgICAKICAgICAgICBzZWxmLnRvbF9zbGlkZXIgPSBjdGsuQ1RrU2xpZGVyKHRvbF9mcmFtZSwgZnJvbV89MC4zLCB0bz0wLjcsIG51bWJlcl9vZl9zdGVwcz00MCkKICAgICAgICBzZWxmLnRvbF9zbGlkZXIuc2V0KGZsb2F0KGRiLmdldF9zZXR0aW5nKCJjb25maWRlbmNlX3RocmVzaG9sZCIsICIwLjU1IikpKQogICAgICAgIHNlbGYudG9sX3NsaWRlci5wYWNrKHNpZGU9InJpZ2h0IiwgZmlsbD0ieCIsIGV4cGFuZD1UcnVlLCBwYWR4PSgyMCwgMCkpCgogICAgICAgICMg4pSA4pSAIERhdGEgTWFuYWdlbWVudCDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIAKICAgICAgICBkYXRhX2ZyYW1lID0gc2VsZi5fY3JlYXRlX3NlY3Rpb24oc2Nyb2xsLCAiRGF0YSAmIEJhY2t1cCIpCiAgICAgICAgCiAgICAgICAgIyBBY3Rpb24gQnV0dG9ucwogICAgICAgIGJ0bl9jb250YWluZXIgPSBjdGsuQ1RrRnJhbWUoZGF0YV9mcmFtZSwgZmdfY29sb3I9InRyYW5zcGFyZW50IikKICAgICAgICBidG5fY29udGFpbmVyLnBhY2soZmlsbD0ieCIsIHBhZHg9MjAsIHBhZHk9MTUpCiAgICAgICAgCiAgICAgICAgY3RrLkNUa0J1dHRvbigKICAgICAgICAgICAgYnRuX2NvbnRhaW5lciwgdGV4dD0iTWFudWFsIERhdGFiYXNlIEJhY2t1cCIsIAogICAgICAgICAgICBmZ19jb2xvcj1jWyJhY2NlbnQiXSwgaG92ZXJfY29sb3I9Y1siYWNjZW50X2hvdmVyIl0sCiAgICAgICAgICAgIGNvbW1hbmQ9c2VsZi5fZG9fYmFja3VwCiAgICAgICAgKS5wYWNrKHNpZGU9ImxlZnQiLCBwYWR4PSgwLCAxMCkpCiAgICAgICAgCiAgICAgICAgY3RrLkNUa0J1dHRvbigKICAgICAgICAgICAgYnRuX2NvbnRhaW5lciwgdGV4dD0iUmV0cmFpbiBGYWNlIE1vZGVsIiwgCiAgICAgICAgICAgIGZnX2NvbG9yPWNbImFjY2VudF9ncmVlbiJdLCBob3Zlcl9jb2xvcj1jWyJzdWNjZXNzIl0sCiAgICAgICAgICAgIGNvbW1hbmQ9c2VsZi5fZG9fcmV0cmFpbgogICAgICAgICkucGFjayhzaWRlPSJsZWZ0IiwgcGFkeD0xMCkKICAgICAgICAKICAgICAgICAjIE5vdGlmaWNhdGlvbiBMYWJlbAogICAgICAgIHNlbGYubGJsX3N0YXR1cyA9IGN0ay5DVGtMYWJlbChkYXRhX2ZyYW1lLCB0ZXh0PSIiLCB0ZXh0X2NvbG9yPWNbInN1Y2Nlc3MiXSkKICAgICAgICBzZWxmLmxibF9zdGF0dXMucGFjayhwYWR5PTUpCgogICAgICAgICMg4pSA4pSAIFNhdmUgQnV0dG9uIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgAogICAgICAgIHNhdmVfYnRuID0gY3RrLkNUa0J1dHRvbigKICAgICAgICAgICAgc2VsZiwgdGV4dD0iU2F2ZSBBbGwgU2V0dGluZ3MiLCBoZWlnaHQ9NDUsCiAgICAgICAgICAgIGZvbnQ9dGhlbWVfbWFuYWdlci5mb250KCJoZWFkaW5nX21kIiksCiAgICAgICAgICAgIGZnX2NvbG9yPWNbImFjY2VudCJdLCBob3Zlcl9jb2xvcj1jWyJhY2NlbnRfaG92ZXIiXSwKICAgICAgICAgICAgY29tbWFuZD1zZWxmLl9zYXZlX3NldHRpbmdzCiAgICAgICAgKQogICAgICAgIHNhdmVfYnRuLnBhY2soZmlsbD0ieCIsIHBhZHg9MzAsIHBhZHk9KDAsIDMwKSkKCiAgICBkZWYgX2NyZWF0ZV9zZWN0aW9uKHNlbGYsIHBhcmVudCwgdGl0bGUpOgogICAgICAgIGMgPSB0aGVtZV9tYW5hZ2VyLmNvbG9ycwogICAgICAgIGZyYW1lID0gY3RrLkNUa0ZyYW1lKHBhcmVudCwgZmdfY29sb3I9Y1siYmdfY2FyZCJdLCBjb3JuZXJfcmFkaXVzPTEyKQogICAgICAgIGZyYW1lLnBhY2soZmlsbD0ieCIsIHBhZHk9KDAsIDIwKSkKICAgICAgICBjdGsuQ1RrTGFiZWwoCiAgICAgICAgICAgIGZyYW1lLCB0ZXh0PXRpdGxlLCBmb250PXRoZW1lX21hbmFnZXIuZm9udCgiaGVhZGluZ19tZCIpLCB0ZXh0X2NvbG9yPWNbInRleHRfcHJpbWFyeSJdCiAgICAgICAgKS5wYWNrKGFuY2hvcj0idyIsIHBhZHg9MjAsIHBhZHk9KDIwLCAxMCkpCiAgICAgICAgIyBEaXZpZGVyCiAgICAgICAgY3RrLkNUa0ZyYW1lKGZyYW1lLCBoZWlnaHQ9MSwgZmdfY29sb3I9Y1siYm9yZGVyIl0pLnBhY2soZmlsbD0ieCIsIHBhZHg9MjAsIHBhZHk9KDAsIDEwKSkKICAgICAgICByZXR1cm4gZnJhbWUKCiAgICBkZWYgX3NhdmVfc2V0dGluZ3Moc2VsZik6CiAgICAgICAgdGhlbWUgPSAiZGFyayIgaWYgc2VsZi5zd190aGVtZS5nZXQoKSBlbHNlICJsaWdodCIKICAgICAgICBzb3VuZCA9ICJ0cnVlIiBpZiBzZWxmLnN3X3NvdW5kLmdldCgpIGVsc2UgImZhbHNlIgogICAgICAgIGNhbV9pZHggPSBzZWxmLmNhbV9jb21iby5nZXQoKQogICAgICAgIHRvbCA9IHN0cihyb3VuZChzZWxmLnRvbF9zbGlkZXIuZ2V0KCksIDIpKQogICAgICAgIAogICAgICAgIGRiLnNldF9zZXR0aW5nKCJ0aGVtZSIsIHRoZW1lKQogICAgICAgIGRiLnNldF9zZXR0aW5nKCJzb3VuZF9lbmFibGVkIiwgc291bmQpCiAgICAgICAgZGIuc2V0X3NldHRpbmcoImNhbWVyYV9pbmRleCIsIGNhbV9pZHgpCiAgICAgICAgZGIuc2V0X3NldHRpbmcoImNvbmZpZGVuY2VfdGhyZXNob2xkIiwgdG9sKQogICAgICAgIAogICAgICAgIGVuZ2luZS5zZXRfdG9sZXJhbmNlKGZsb2F0KHRvbCkpCiAgICAgICAgCiAgICAgICAgc2VsZi5sYmxfc3RhdHVzLmNvbmZpZ3VyZSh0ZXh0PSJTZXR0aW5ncyBzYXZlZCBzdWNjZXNzZnVsbHkhIChUaGVtZSBjaGFuZ2VzIHJlcXVpcmUgcmVzdGFydCkiKQogICAgICAgIHNlbGYuYWZ0ZXIoMzAwMCwgbGFtYmRhOiBzZWxmLmxibF9zdGF0dXMuY29uZmlndXJlKHRleHQ9IiIpKQoKICAgIGRlZiBfZG9fYmFja3VwKHNlbGYpOgogICAgICAgIHBhdGggPSBkYi5iYWNrdXBfZGF0YWJhc2UoKQogICAgICAgIHNlbGYubGJsX3N0YXR1cy5jb25maWd1cmUodGV4dD1mIkJhY2t1cCBzYXZlZCB0bzoge3BhdGh9IikKICAgICAgICAKICAgIGRlZiBfZG9fcmV0cmFpbihzZWxmKToKICAgICAgICBzZWxmLmxibF9zdGF0dXMuY29uZmlndXJlKHRleHQ9IlJldHJhaW5pbmcgbW9kZWwuLi4gUGxlYXNlIHdhaXQuIikKICAgICAgICBzZWxmLnVwZGF0ZSgpCiAgICAgICAgc3VjY2VzcyA9IGVuZ2luZS50cmFpbl9tb2RlbCgpCiAgICAgICAgaWYgc3VjY2VzczoKICAgICAgICAgICAgc2VsZi5sYmxfc3RhdHVzLmNvbmZpZ3VyZSh0ZXh0PSJNb2RlbCByZXRyYWluZWQgc3VjY2Vzc2Z1bGx5LiIpCiAgICAgICAgZWxzZToKICAgICAgICAgICAgc2VsZi5sYmxfc3RhdHVzLmNvbmZpZ3VyZSh0ZXh0PSJNb2RlbCByZXRyYWluaW5nIGZhaWxlZC4iLCB0ZXh0X2NvbG9yPXRoZW1lX21hbmFnZXIuY29sb3JzWyJlcnJvciJdKQo=', 'gui/pages/analytics.py': 'IiIiCuKVlOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVlwrilZEgICAgICAgICAgICAgQU5BTFlUSUNTIOKAlCBGYWNlIEF0dGVuZGFuY2UgU3lzdGVtICAgICAgICAgICAgICDilZEK4pWRICBWaXN1YWwgY2hhcnRzIGFuZCBzdGF0aXN0aWNzICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIOKVkQrilZrilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZ0KIiIiCgppbXBvcnQgY3VzdG9tdGtpbnRlciBhcyBjdGsKaW1wb3J0IG1hdHBsb3RsaWIKbWF0cGxvdGxpYi51c2UoIlRrQWdnIikKZnJvbSBtYXRwbG90bGliLmZpZ3VyZSBpbXBvcnQgRmlndXJlCmZyb20gbWF0cGxvdGxpYi5iYWNrZW5kcy5iYWNrZW5kX3RrYWdnIGltcG9ydCBGaWd1cmVDYW52YXNUa0FnZwpmcm9tIGRhdGFiYXNlLmRiX21hbmFnZXIgaW1wb3J0IGRiCmZyb20gdXRpbHMuaGVscGVycyBpbXBvcnQgdGhlbWVfbWFuYWdlcgoKY2xhc3MgQW5hbHl0aWNzUGFnZShjdGsuQ1RrRnJhbWUpOgogICAgZGVmIF9faW5pdF9fKHNlbGYsIHBhcmVudCk6CiAgICAgICAgYyA9IHRoZW1lX21hbmFnZXIuY29sb3JzCiAgICAgICAgc3VwZXIoKS5fX2luaXRfXyhwYXJlbnQsIGZnX2NvbG9yPWNbImJnX3ByaW1hcnkiXSwgY29ybmVyX3JhZGl1cz0wKQogICAgICAgIHNlbGYucGFja19wcm9wYWdhdGUoRmFsc2UpCiAgICAgICAgc2VsZi5fYnVpbGRfdWkoKQoKICAgIGRlZiBfYnVpbGRfdWkoc2VsZik6CiAgICAgICAgYyA9IHRoZW1lX21hbmFnZXIuY29sb3JzCiAgICAgICAgCiAgICAgICAgIyBIZWFkZXIKICAgICAgICBoZWFkZXIgPSBjdGsuQ1RrRnJhbWUoc2VsZiwgZmdfY29sb3I9InRyYW5zcGFyZW50IikKICAgICAgICBoZWFkZXIucGFjayhmaWxsPSJ4IiwgcGFkeD0zMCwgcGFkeT0oMzAsIDIwKSkKICAgICAgICBjdGsuQ1RrTGFiZWwoCiAgICAgICAgICAgIGhlYWRlciwgdGV4dD0iQXR0ZW5kYW5jZSBBbmFseXRpY3MiLAogICAgICAgICAgICBmb250PXRoZW1lX21hbmFnZXIuZm9udCgiaGVhZGluZ19sZyIpLCB0ZXh0X2NvbG9yPWNbInRleHRfcHJpbWFyeSJdCiAgICAgICAgKS5wYWNrKHNpZGU9ImxlZnQiKQoKICAgICAgICAjIENvbnRhaW5lciBmb3IgQ2hhcnRzCiAgICAgICAgY2hhcnRzX2ZyYW1lID0gY3RrLkNUa0ZyYW1lKHNlbGYsIGZnX2NvbG9yPSJ0cmFuc3BhcmVudCIpCiAgICAgICAgY2hhcnRzX2ZyYW1lLnBhY2soZmlsbD0iYm90aCIsIGV4cGFuZD1UcnVlLCBwYWR4PTMwLCBwYWR5PSgwLCAzMCkpCiAgICAgICAgY2hhcnRzX2ZyYW1lLmdyaWRfY29sdW1uY29uZmlndXJlKCgwLCAxKSwgd2VpZ2h0PTEsIHVuaWZvcm09ImNvbCIpCiAgICAgICAgY2hhcnRzX2ZyYW1lLmdyaWRfcm93Y29uZmlndXJlKDAsIHdlaWdodD0xKQoKICAgICAgICAjIENoYXJ0IDE6IDctRGF5IFRyZW5kCiAgICAgICAgdHJlbmRfY2FyZCA9IGN0ay5DVGtGcmFtZShjaGFydHNfZnJhbWUsIGZnX2NvbG9yPWNbImJnX2NhcmQiXSwgY29ybmVyX3JhZGl1cz0xMikKICAgICAgICB0cmVuZF9jYXJkLmdyaWQocm93PTAsIGNvbHVtbj0wLCBzdGlja3k9Im5zZXciLCBwYWR4PSgwLCAxMCkpCiAgICAgICAgdHJlbmRfY2FyZC5wYWNrX3Byb3BhZ2F0ZShGYWxzZSkKICAgICAgICBjdGsuQ1RrTGFiZWwodHJlbmRfY2FyZCwgdGV4dD0iNy1EYXkgQXR0ZW5kYW5jZSBUcmVuZCIsIGZvbnQ9dGhlbWVfbWFuYWdlci5mb250KCJoZWFkaW5nX21kIiksIHRleHRfY29sb3I9Y1sidGV4dF9wcmltYXJ5Il0pLnBhY2socGFkeT0oMjAsIDEwKSkKICAgICAgICAKICAgICAgICBzZWxmLmZpZ190cmVuZCA9IEZpZ3VyZShmaWdzaXplPSg1LCA0KSwgZHBpPTEwMCkKICAgICAgICBzZWxmLmF4X3RyZW5kID0gc2VsZi5maWdfdHJlbmQuYWRkX3N1YnBsb3QoMTExKQogICAgICAgIHNlbGYuY2FudmFzX3RyZW5kID0gRmlndXJlQ2FudmFzVGtBZ2coc2VsZi5maWdfdHJlbmQsIG1hc3Rlcj10cmVuZF9jYXJkKQogICAgICAgIHNlbGYuY2FudmFzX3RyZW5kLmdldF90a193aWRnZXQoKS5wYWNrKGZpbGw9ImJvdGgiLCBleHBhbmQ9VHJ1ZSwgcGFkeD0xMCwgcGFkeT0xMCkKCiAgICAgICAgIyBDaGFydCAyOiBEZXBhcnRtZW50IEJyZWFrZG93bgogICAgICAgIGRlcHRfY2FyZCA9IGN0ay5DVGtGcmFtZShjaGFydHNfZnJhbWUsIGZnX2NvbG9yPWNbImJnX2NhcmQiXSwgY29ybmVyX3JhZGl1cz0xMikKICAgICAgICBkZXB0X2NhcmQuZ3JpZChyb3c9MCwgY29sdW1uPTEsIHN0aWNreT0ibnNldyIsIHBhZHg9KDEwLCAwKSkKICAgICAgICBkZXB0X2NhcmQucGFja19wcm9wYWdhdGUoRmFsc2UpCiAgICAgICAgY3RrLkNUa0xhYmVsKGRlcHRfY2FyZCwgdGV4dD0iVXNlcnMgYnkgRGVwYXJ0bWVudCIsIGZvbnQ9dGhlbWVfbWFuYWdlci5mb250KCJoZWFkaW5nX21kIiksIHRleHRfY29sb3I9Y1sidGV4dF9wcmltYXJ5Il0pLnBhY2socGFkeT0oMjAsIDEwKSkKICAgICAgICAKICAgICAgICBzZWxmLmZpZ19kZXB0ID0gRmlndXJlKGZpZ3NpemU9KDUsIDQpLCBkcGk9MTAwKQogICAgICAgIHNlbGYuYXhfZGVwdCA9IHNlbGYuZmlnX2RlcHQuYWRkX3N1YnBsb3QoMTExKQogICAgICAgIHNlbGYuY2FudmFzX2RlcHQgPSBGaWd1cmVDYW52YXNUa0FnZyhzZWxmLmZpZ19kZXB0LCBtYXN0ZXI9ZGVwdF9jYXJkKQogICAgICAgIHNlbGYuY2FudmFzX2RlcHQuZ2V0X3RrX3dpZGdldCgpLnBhY2soZmlsbD0iYm90aCIsIGV4cGFuZD1UcnVlLCBwYWR4PTEwLCBwYWR5PTEwKQoKICAgICAgICBzZWxmLl9zdHlsZV9maWd1cmVzKCkKCiAgICBkZWYgX3N0eWxlX2ZpZ3VyZXMoc2VsZik6CiAgICAgICAgYyA9IHRoZW1lX21hbmFnZXIuY29sb3JzCiAgICAgICAgYmcgPSBjWyJiZ19jYXJkIl0KICAgICAgICB0ZXh0X2NvbG9yID0gY1sidGV4dF9wcmltYXJ5Il0KCiAgICAgICAgZm9yIGZpZyBpbiBbc2VsZi5maWdfdHJlbmQsIHNlbGYuZmlnX2RlcHRdOgogICAgICAgICAgICBmaWcucGF0Y2guc2V0X2ZhY2Vjb2xvcihiZykKICAgICAgICAgICAgCiAgICAgICAgZm9yIGF4IGluIFtzZWxmLmF4X3RyZW5kLCBzZWxmLmF4X2RlcHRdOgogICAgICAgICAgICBheC5zZXRfZmFjZWNvbG9yKGJnKQogICAgICAgICAgICBheC50aWNrX3BhcmFtcyhjb2xvcnM9dGV4dF9jb2xvcikKICAgICAgICAgICAgZm9yIHNwaW5lIGluIGF4LnNwaW5lcy52YWx1ZXMoKToKICAgICAgICAgICAgICAgIHNwaW5lLnNldF9jb2xvcihjWyJib3JkZXIiXSkKCiAgICBkZWYgcmVmcmVzaF9kYXRhKHNlbGYpOgogICAgICAgIGMgPSB0aGVtZV9tYW5hZ2VyLmNvbG9ycwogICAgICAgIHNlbGYuX3N0eWxlX2ZpZ3VyZXMoKQogICAgICAgIAogICAgICAgICMgVXBkYXRlIFRyZW5kIENoYXJ0CiAgICAgICAgc2VsZi5heF90cmVuZC5jbGVhcigpCiAgICAgICAgdHJlbmRfZGF0YSA9IGRiLmdldF9hdHRlbmRhbmNlX3RyZW5kKDcpCiAgICAgICAgaWYgdHJlbmRfZGF0YToKICAgICAgICAgICAgZGF0ZXMgPSBbZFsiZGF0ZSJdWy01Ol0gZm9yIGQgaW4gdHJlbmRfZGF0YV0gIyBNTS1ERAogICAgICAgICAgICBjb3VudHMgPSBbZFsiY291bnQiXSBmb3IgZCBpbiB0cmVuZF9kYXRhXQogICAgICAgICAgICAKICAgICAgICAgICAgc2VsZi5heF90cmVuZC5iYXIoZGF0ZXMsIGNvdW50cywgY29sb3I9Y1siYWNjZW50Il0sIGFscGhhPTAuOCkKICAgICAgICAgICAgc2VsZi5heF90cmVuZC5zZXRfeWxhYmVsKCJTdHVkZW50cyBQcmVzZW50IiwgY29sb3I9Y1sidGV4dF9zZWNvbmRhcnkiXSkKICAgICAgICAKICAgICAgICBzZWxmLmZpZ190cmVuZC50aWdodF9sYXlvdXQoKQogICAgICAgIHNlbGYuY2FudmFzX3RyZW5kLmRyYXcoKQoKICAgICAgICAjIFVwZGF0ZSBEZXBhcnRtZW50IENoYXJ0CiAgICAgICAgc2VsZi5heF9kZXB0LmNsZWFyKCkKICAgICAgICB1c2VycyA9IGRiLmdldF9hbGxfdXNlcnMoKQogICAgICAgIGlmIHVzZXJzOgogICAgICAgICAgICBkZXB0X2NvdW50cyA9IHt9CiAgICAgICAgICAgIGZvciB1IGluIHVzZXJzOgogICAgICAgICAgICAgICAgZGVwdF9jb3VudHNbdVsiZGVwYXJ0bWVudCJdXSA9IGRlcHRfY291bnRzLmdldCh1WyJkZXBhcnRtZW50Il0sIDApICsgMQogICAgICAgICAgICAgICAgCiAgICAgICAgICAgIGxhYmVscyA9IGxpc3QoZGVwdF9jb3VudHMua2V5cygpKQogICAgICAgICAgICBzaXplcyA9IGxpc3QoZGVwdF9jb3VudHMudmFsdWVzKCkpCiAgICAgICAgICAgIAogICAgICAgICAgICAjIFVzZSBjaGFydCBjb2xvcnMgZnJvbSB0aGVtZQogICAgICAgICAgICBjaGFydF9jb2xvcnMgPSBjLmdldCgiY2hhcnRfY29sb3JzIiwgWyIjMjE4OEZGIiwgIiMzRkI5NTAiLCAiI0JDOENGRiIsICIjRDI5OTIyIiwgIiNGODUxNDkiXSkKICAgICAgICAgICAgCiAgICAgICAgICAgIHNlbGYuYXhfZGVwdC5waWUoCiAgICAgICAgICAgICAgICBzaXplcywgbGFiZWxzPWxhYmVscywgY29sb3JzPWNoYXJ0X2NvbG9ycywKICAgICAgICAgICAgICAgIGF1dG9wY3Q9JyUxLjFmJSUnLCBzdGFydGFuZ2xlPTkwLAogICAgICAgICAgICAgICAgdGV4dHByb3BzPXsnY29sb3InOiBjWyJ0ZXh0X3ByaW1hcnkiXX0KICAgICAgICAgICAgKQogICAgICAgICAgICBzZWxmLmF4X2RlcHQuYXhpcygnZXF1YWwnKQogICAgICAgICAgICAKICAgICAgICBzZWxmLmZpZ19kZXB0LnRpZ2h0X2xheW91dCgpCiAgICAgICAgc2VsZi5jYW52YXNfZGVwdC5kcmF3KCkK', 'data/.gitkeep': 'IyBEYXRhIGRpcmVjdG9yaWVzIOKAlCB0aGVzZSBhcmUgY3JlYXRlZCBhdXRvbWF0aWNhbGx5IGJ5IHRoZSBhcHAgb24gZmlyc3QgcnVuLgojIGZhY2VfZGF0YS8gICA6IFJhdyBjYXB0dXJlZCBmYWNlIGltYWdlcywgb3JnYW5pc2VkIHBlciB1c2VyLgojIGJhY2t1cHMvICAgICA6IFRpbWVzdGFtcGVkIGRhdGFiYXNlIGJhY2t1cCBmaWxlcy4KIyAuZ2l0a2VlcCBmaWxlcyBiZWxvdyBlbnN1cmUgZ2l0IHRyYWNrcyBlbXB0eSBkaXJlY3Rvcmllcy4K'}

def extract_all():
    print("Extracting Face Detection Attendance Management System files...")
    # Create required empty directories that might not have files
    empty_dirs = ["data", "data/backups", "data/face_data", "exports", "logs"]
    for d in empty_dirs:
        os.makedirs(d, exist_ok=True)
        print(f"Created directory: {d}")
        
    for rel_path, b64_content in FILES.items():
        dir_name = os.path.dirname(rel_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        
        content = base64.b64decode(b64_content.encode("utf-8"))
        with open(rel_path, "wb") as f:
            f.write(content)
        print(f"Extracted: {rel_path}")
    print("Extraction complete!\n")

if __name__ == "__main__":
    extract_all()
    
    # Run the main entry point if it exists
    if os.path.exists("main.py"):
        print("Starting FaceTrack Pro...")
        import subprocess
        try:
            subprocess.run([sys.executable, "main.py"])
        except KeyboardInterrupt:
            print("\nApplication closed.")
    else:
        print("Error: main.py not found.")


# ============================================================
# File: ./seed_demo_data.py
# ============================================================

"""
╔══════════════════════════════════════════════════════════════╗
║         SEED DEMO DATA — Face Attendance System             ║
║  Populates the database with sample users and attendance    ║
║  records so you can explore the dashboard immediately.      ║
╚══════════════════════════════════════════════════════════════╝

Run this ONCE to populate the database with sample data:
    python seed_demo_data.py

WARNING: Running again will attempt duplicate inserts (safely ignored).
"""

import os
import sys
import random
from datetime import date, timedelta

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database.db_manager import DatabaseManager

print("=" * 55)
print("  FaceTrack Pro — Demo Data Seeder")
print("=" * 55)

db = DatabaseManager()

# ── Sample Users ─────────────────────────────────────────────
DEMO_USERS = [
    ("Alice Johnson",   "EMP-001", "Engineering",   "alice@demo.com",   "9876543210"),
    ("Bob Smith",       "EMP-002", "HR",             "bob@demo.com",     "9876543211"),
    ("Carol Williams",  "EMP-003", "Engineering",   "carol@demo.com",   "9876543212"),
    ("David Brown",     "STU-101", "Computer Sci",  "david@demo.com",   "9876543213"),
    ("Eva Martinez",    "STU-102", "Computer Sci",  "eva@demo.com",     "9876543214"),
    ("Frank Lee",       "STU-103", "Electronics",   "frank@demo.com",   "9876543215"),
    ("Grace Kim",       "EMP-004", "Sales",          "grace@demo.com",   "9876543216"),
    ("Henry Davis",     "STU-104", "Mechanical",    "henry@demo.com",   "9876543217"),
    ("Isla Moore",      "EMP-005", "Finance",        "isla@demo.com",    "9876543218"),
    ("Jack Wilson",     "STU-105", "Electronics",   "jack@demo.com",    "9876543219"),
]

print("\n[1/2] Adding demo users...")
user_ids = []
for name, roll, dept, email, phone in DEMO_USERS:
    uid = db.add_user(name=name, roll_number=roll, department=dept,
                      email=email, phone=phone)
    if uid > 0:
        user_ids.append(uid)
        print(f"     ✅  {name} ({roll})")
    else:
        # User already exists — fetch their ID
        existing = db.get_user_by_roll(roll)
        if existing:
            user_ids.append(existing["id"])
        print(f"     ⚠️   {name} ({roll}) — already exists, skipping.")

print(f"\n   Total active users: {db.get_total_users()}")

# ── Sample Attendance (last 14 days) ─────────────────────────
print("\n[2/2] Generating attendance for the last 14 days...")

import sqlite3

today = date.today()
total_inserted = 0

for uid in user_ids:
    # Each user has ~75% attendance probability per day
    for days_back in range(14, -1, -1):
        attendance_date = today - timedelta(days=days_back)
        date_str = attendance_date.strftime("%Y-%m-%d")

        # Skip weekends for realism
        if attendance_date.weekday() >= 5:
            continue

        # Random attendance (75% chance present)
        if random.random() < 0.75:
            time_str = f"{random.randint(8, 9):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
            try:
                with db._get_connection() as conn:
                    conn.execute(
                        "INSERT OR IGNORE INTO attendance (user_id, date, time, status) VALUES (?, ?, ?, ?)",
                        (uid, date_str, time_str, "Present")
                    )
                    conn.commit()
                    total_inserted += 1
            except Exception:
                pass

print(f"     ✅  {total_inserted} attendance records inserted.\n")

print("=" * 55)
print(f"  Today's attendance: {db.get_today_count()} records")
print(f"  Total users       : {db.get_total_users()}")
print(f"  Avg attendance %  : {db.get_attendance_percentage(days=14)}%")
print("=" * 55)
print("\n  ✅ Demo data ready! Run `python main.py` to launch.\n")


# ============================================================
# File: ./main.py
# ============================================================

"""
╔══════════════════════════════════════════════════════════════╗
║            FACE ATTENDANCE SYSTEM - MAIN ENTRY POINT        ║
║  Initializes the GUI, manages routing between pages,        ║
║  and schedules background tasks (auto-backup, reload).      ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import sys
import threading
import logging

# ── Ensure project root is on PYTHONPATH ─────────────────────
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

import customtkinter as ctk
from utils.helpers import theme_manager, sound_manager
from database.db_manager import db

# GUI Components
from gui.splash_screen import SplashScreen
from gui.sidebar import Sidebar
from gui.notification import ToastNotification

# Pages
from gui.pages.dashboard import DashboardPage
from gui.pages.attendance import AttendancePage
from gui.pages.register import RegisterPage
from gui.pages.records import RecordsPage
from gui.pages.analytics import AnalyticsPage
from gui.pages.settings import SettingsPage

# ── Logging ──────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  [%(levelname)s]  %(name)s — %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(os.path.join(ROOT, "logs", "app.log"), encoding="utf-8"),
    ]
)
os.makedirs(os.path.join(ROOT, "logs"), exist_ok=True)
logger = logging.getLogger(__name__)


# ═══════════════════════════════════════════════════════════════
#  Main Application Window
# ═══════════════════════════════════════════════════════════════
class FaceAttendanceApp(ctk.CTk):
    """
    Top-level application window.
    Manages the sidebar + page container layout and all navigation.
    """

    def __init__(self):
        super().__init__()

        # ── Apply saved theme ─────────────────────────────────
        saved_theme = db.get_setting("theme", "dark")
        ctk.set_appearance_mode(saved_theme)
        theme_manager.mode   = saved_theme
        theme_manager.colors = (
            theme_manager.DARK if saved_theme == "dark" else theme_manager.LIGHT
        )

        # ── Window setup ──────
        # self.withdraw()  # Disabled to fix macOS black screen bug
        self.title("FaceTrack Pro — AI Attendance System")
        self.geometry("1200x720")
        self.minsize(960, 620)
        self.configure(fg_color=theme_manager.colors["bg_primary"])

        # State
        self.pages        = {}
        self.current_page = None

        logger.info("Application starting — bypassing splash screen.")
        self._build_main_ui()
        # Schedule auto-backup in background (runs 30 s after launch)
        threading.Timer(30, self._auto_backup).start()


    # ── Main UI ───────────────────────────────────────────────
    def _build_main_ui(self):
        """Construct sidebar + page container."""
        c = theme_manager.colors

        # Root grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Sidebar
        self.sidebar = Sidebar(self, on_navigate=self.navigate)
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        # Right-side container (pages live here)
        self.container = ctk.CTkFrame(
            self, fg_color=c["bg_primary"], corner_radius=0
        )
        self.container.grid(row=0, column=1, sticky="nsew")

        # Instantiate all pages (lazy if slow)
        self.pages["dashboard"]  = DashboardPage(self.container)
        self.pages["attendance"] = AttendancePage(self.container)
        self.pages["register"]   = RegisterPage(self.container)
        self.pages["records"]    = RecordsPage(self.container)
        self.pages["analytics"]  = AnalyticsPage(self.container)
        self.pages["settings"]   = SettingsPage(self.container)

        # Start on dashboard
        self.navigate("dashboard")

    # ── Navigation ────────────────────────────────────────────
    def navigate(self, page_key: str):
        """
        Switch the visible page.
        - Stops webcam if leaving attendance page.
        - Calls refresh_data() on the target page if available.
        """
        # Stop camera when leaving attendance page
        if (self.current_page == "attendance"
                and page_key != "attendance"
                and "attendance" in self.pages):
            self.pages["attendance"].stop()

        # Hide current page
        if self.current_page and self.current_page in self.pages:
            self.pages[self.current_page].pack_forget()

        # Show target page
        page = self.pages.get(page_key)
        if page:
            page.pack(fill="both", expand=True)
            self.current_page = page_key

            # Refresh data (non-blocking)
            if hasattr(page, "refresh_data"):
                try:
                    page.refresh_data()
                except Exception as e:
                    logger.error(f"refresh_data error on {page_key}: {e}")

            logger.info(f"Navigated to: {page_key}")

    # ── Toast Helper ──────────────────────────────────────────
    def notify(self, message: str, type_: str = "info"):
        """Show a toast notification from anywhere in the app."""
        ToastNotification(self, message, type_=type_)

    # ── Auto Backup ───────────────────────────────────────────
    def _auto_backup(self):
        """Silently backup the database if auto-backup is enabled."""
        try:
            if db.get_setting("auto_backup", "true") == "true":
                path = db.backup_database()
                logger.info(f"Auto-backup completed: {path}")
        except Exception as e:
            logger.error(f"Auto-backup failed: {e}")

    # ── Clean Shutdown ────────────────────────────────────────
    def on_close(self):
        """Gracefully stop camera and exit."""
        if "attendance" in self.pages:
            try:
                self.pages["attendance"].stop()
            except Exception:
                pass
        logger.info("Application closed.")
        self.destroy()


# ═══════════════════════════════════════════════════════════════
#  Entry Point
# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    app = FaceAttendanceApp()
    app.protocol("WM_DELETE_WINDOW", app.on_close)  # Handle window-close cleanly
    app.mainloop()


# ============================================================
# File: ./test_ctk.py
# ============================================================

import customtkinter as ctk
app = ctk.CTk()
app.title("Test")
app.geometry("400x300")
ctk.CTkLabel(app, text="CTk is working!").pack(expand=True)
app.mainloop()


# ============================================================
# File: ./verify_install.py
# ============================================================

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


# ============================================================
# File: ./database/db_manager.py
# ============================================================

"""
╔══════════════════════════════════════════════════════════════╗
║         DATABASE MANAGER — Face Attendance System           ║
║  Handles all SQLite operations: users, attendance, settings ║
╚══════════════════════════════════════════════════════════════╝

This module is responsible for:
  - Creating / connecting to the SQLite database
  - Creating all tables (users, attendance, settings, audit log)
  - CRUD operations (Create, Read, Update, Delete)
  - Exporting attendance to CSV / Excel
  - Analytics queries (attendance %, totals, trends)
"""

import sqlite3
import os
import shutil
import pandas as pd
from datetime import datetime, date, timedelta
import logging

# ── Paths ────────────────────────────────────────────────────
BASE_DIR   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH    = os.path.join(BASE_DIR, "data", "attendance.db")
BACKUP_DIR = os.path.join(BASE_DIR, "data", "backups")
EXPORT_DIR = os.path.join(BASE_DIR, "exports")

# Ensure required directories exist
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
os.makedirs(BACKUP_DIR, exist_ok=True)
os.makedirs(EXPORT_DIR, exist_ok=True)

# ── Logging ──────────────────────────────────────────────────
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ═══════════════════════════════════════════════════════════════
#  DatabaseManager Class
# ═══════════════════════════════════════════════════════════════
class DatabaseManager:
    """Central database manager for the attendance system."""

    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        self._create_tables()
        logger.info(f"Database connected: {self.db_path}")

    # ── Connection helper ────────────────────────────────────
    def _get_connection(self):
        """Return a new SQLite connection with row_factory for dict-like rows."""
        conn = sqlite3.connect(self.db_path, timeout=10)
        conn.row_factory = sqlite3.Row          # rows accessible as dicts
        conn.execute("PRAGMA journal_mode=WAL")  # better concurrency
        conn.execute("PRAGMA foreign_keys=ON")   # enforce FK constraints
        return conn

    # ── Table Creation ───────────────────────────────────────
    def _create_tables(self):
        """Create all database tables if they don't already exist."""
        with self._get_connection() as conn:
            cursor = conn.cursor()

            # ── users table ──────────────────────────────────
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id          INTEGER PRIMARY KEY AUTOINCREMENT,
                    name        TEXT    NOT NULL,
                    roll_number TEXT    UNIQUE NOT NULL,
                    department  TEXT    NOT NULL,
                    email       TEXT,
                    phone       TEXT,
                    photo_path  TEXT,
                    registered_at TEXT  DEFAULT (datetime('now','localtime')),
                    is_active   INTEGER DEFAULT 1
                )
            """)

            # ── attendance table ─────────────────────────────
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS attendance (
                    id          INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id     INTEGER NOT NULL,
                    date        TEXT    NOT NULL,
                    time        TEXT    NOT NULL,
                    status      TEXT    DEFAULT 'Present',
                    marked_by   TEXT    DEFAULT 'Face Recognition',
                    FOREIGN KEY (user_id) REFERENCES users(id),
                    UNIQUE(user_id, date)           -- one entry per person per day
                )
            """)

            # ── settings table ───────────────────────────────
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS settings (
                    key         TEXT PRIMARY KEY,
                    value       TEXT NOT NULL,
                    updated_at  TEXT DEFAULT (datetime('now','localtime'))
                )
            """)

            # ── audit_log table ──────────────────────────────
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS audit_log (
                    id          INTEGER PRIMARY KEY AUTOINCREMENT,
                    action      TEXT    NOT NULL,
                    details     TEXT,
                    timestamp   TEXT    DEFAULT (datetime('now','localtime'))
                )
            """)

            conn.commit()

            # Insert default settings
            self._insert_default_settings(cursor, conn)

    def _insert_default_settings(self, cursor, conn):
        """Insert default app settings if they don't exist."""
        defaults = {
            "theme":              "dark",
            "confidence_threshold": "0.55",
            "camera_index":       "0",
            "auto_backup":        "true",
            "sound_enabled":      "true",
            "backup_interval_days": "7",
            "admin_password":     "admin123",
        }
        for key, value in defaults.items():
            cursor.execute(
                "INSERT OR IGNORE INTO settings (key, value) VALUES (?, ?)",
                (key, value)
            )
        conn.commit()

    # ══════════════════════════════════════════════════════════
    #  USER OPERATIONS
    # ══════════════════════════════════════════════════════════

    def add_user(self, name: str, roll_number: str, department: str,
                 email: str = "", phone: str = "", photo_path: str = "") -> int:
        """
        Register a new user.
        Returns the new user's ID, or -1 on failure.
        """
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO users (name, roll_number, department, email, phone, photo_path)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (name.strip(), roll_number.strip(), department.strip(),
                      email.strip(), phone.strip(), photo_path))
                conn.commit()
                uid = cursor.lastrowid
                self._log_action("USER_ADDED", f"Name={name}, Roll={roll_number}, Dept={department}")
                logger.info(f"User added: {name} (ID={uid})")
                return uid
        except sqlite3.IntegrityError:
            logger.warning(f"User with roll number '{roll_number}' already exists.")
            return -1
        except Exception as e:
            logger.error(f"Error adding user: {e}")
            return -1

    def get_all_users(self, active_only: bool = True) -> list:
        """Return a list of all users (dicts)."""
        with self._get_connection() as conn:
            query = "SELECT * FROM users"
            if active_only:
                query += " WHERE is_active = 1"
            query += " ORDER BY name"
            rows = conn.execute(query).fetchall()
            return [dict(r) for r in rows]

    def get_user_by_id(self, user_id: int) -> dict | None:
        """Return a single user dict, or None if not found."""
        with self._get_connection() as conn:
            row = conn.execute(
                "SELECT * FROM users WHERE id = ?", (user_id,)
            ).fetchone()
            return dict(row) if row else None

    def get_user_by_roll(self, roll_number: str) -> dict | None:
        """Return user by roll number."""
        with self._get_connection() as conn:
            row = conn.execute(
                "SELECT * FROM users WHERE roll_number = ?", (roll_number,)
            ).fetchone()
            return dict(row) if row else None

    def update_user(self, user_id: int, **kwargs) -> bool:
        """Update user fields. Pass keyword arguments matching column names."""
        allowed = {"name", "department", "email", "phone", "photo_path", "is_active"}
        fields  = {k: v for k, v in kwargs.items() if k in allowed}
        if not fields:
            return False
        set_clause = ", ".join(f"{k} = ?" for k in fields)
        values     = list(fields.values()) + [user_id]
        try:
            with self._get_connection() as conn:
                conn.execute(f"UPDATE users SET {set_clause} WHERE id = ?", values)
                conn.commit()
            return True
        except Exception as e:
            logger.error(f"Error updating user {user_id}: {e}")
            return False

    def delete_user(self, user_id: int) -> bool:
        """Soft-delete a user (mark inactive)."""
        return self.update_user(user_id, is_active=0)

    def get_total_users(self) -> int:
        with self._get_connection() as conn:
            return conn.execute(
                "SELECT COUNT(*) FROM users WHERE is_active = 1"
            ).fetchone()[0]

    # ══════════════════════════════════════════════════════════
    #  ATTENDANCE OPERATIONS
    # ══════════════════════════════════════════════════════════

    def mark_attendance(self, user_id: int, status: str = "Present") -> dict:
        """
        Mark attendance for a user for today.
        Returns: {"success": bool, "message": str, "already_marked": bool}
        """
        today     = date.today().strftime("%Y-%m-%d")
        now_time  = datetime.now().strftime("%H:%M:%S")
        try:
            with self._get_connection() as conn:
                conn.execute("""
                    INSERT INTO attendance (user_id, date, time, status)
                    VALUES (?, ?, ?, ?)
                """, (user_id, today, now_time, status))
                conn.commit()
                self._log_action("ATTENDANCE_MARKED",
                                 f"UserID={user_id}, Date={today}, Time={now_time}")
                return {"success": True, "message": "Attendance marked successfully!",
                        "already_marked": False}
        except sqlite3.IntegrityError:
            # UNIQUE constraint: already marked today
            return {"success": False,
                    "message": "Attendance already marked for today.",
                    "already_marked": True}
        except Exception as e:
            logger.error(f"Error marking attendance: {e}")
            return {"success": False, "message": str(e), "already_marked": False}

    def is_attendance_marked_today(self, user_id: int) -> bool:
        """Check if attendance is already marked for today."""
        today = date.today().strftime("%Y-%m-%d")
        with self._get_connection() as conn:
            row = conn.execute(
                "SELECT id FROM attendance WHERE user_id = ? AND date = ?",
                (user_id, today)
            ).fetchone()
            return row is not None

    def get_attendance_records(self, start_date: str = None, end_date: str = None,
                               user_id: int = None, department: str = None) -> list:
        """
        Fetch attendance records with optional filters.
        Returns list of dicts with user info joined.
        """
        query = """
            SELECT a.id, a.user_id, u.name, u.roll_number, u.department,
                   a.date, a.time, a.status, a.marked_by
            FROM attendance a
            JOIN users u ON a.user_id = u.id
            WHERE 1=1
        """
        params = []
        if start_date:
            query += " AND a.date >= ?"
            params.append(start_date)
        if end_date:
            query += " AND a.date <= ?"
            params.append(end_date)
        if user_id:
            query += " AND a.user_id = ?"
            params.append(user_id)
        if department:
            query += " AND u.department = ?"
            params.append(department)
        query += " ORDER BY a.date DESC, a.time DESC"

        with self._get_connection() as conn:
            rows = conn.execute(query, params).fetchall()
            return [dict(r) for r in rows]

    def get_today_attendance(self) -> list:
        """Return today's attendance records."""
        today = date.today().strftime("%Y-%m-%d")
        return self.get_attendance_records(start_date=today, end_date=today)

    def get_today_count(self) -> int:
        """Return count of students marked present today."""
        return len(self.get_today_attendance())

    def get_attendance_percentage(self, user_id: int = None,
                                  days: int = 30) -> float:
        """
        Calculate attendance percentage over the last N days.
        If user_id is given, calculates for that user; otherwise overall.
        """
        start = (date.today() - timedelta(days=days)).strftime("%Y-%m-%d")
        end   = date.today().strftime("%Y-%m-%d")
        records = self.get_attendance_records(start_date=start, end_date=end,
                                              user_id=user_id)
        if not records:
            return 0.0
        if user_id:
            return min(100.0, round(len(records) / days * 100, 1))
        # Overall: unique days / total_days
        unique_days = len(set(r["date"] for r in records))
        return round(unique_days / days * 100, 1)

    def get_attendance_trend(self, days: int = 7) -> list:
        """Return daily attendance counts for the last N days (for charts)."""
        result = []
        for i in range(days - 1, -1, -1):
            d = (date.today() - timedelta(days=i)).strftime("%Y-%m-%d")
            count = len(self.get_attendance_records(start_date=d, end_date=d))
            result.append({"date": d, "count": count})
        return result

    # ══════════════════════════════════════════════════════════
    #  EXPORT OPERATIONS
    # ══════════════════════════════════════════════════════════

    def export_to_csv(self, records: list = None, filename: str = None) -> str:
        """Export attendance records to CSV. Returns file path."""
        if records is None:
            records = self.get_attendance_records()
        if not records:
            return ""
        df = pd.DataFrame(records)
        if filename is None:
            filename = f"attendance_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        path = os.path.join(EXPORT_DIR, filename)
        df.to_csv(path, index=False)
        logger.info(f"Exported CSV: {path}")
        return path

    def export_to_excel(self, records: list = None, filename: str = None) -> str:
        """Export attendance records to Excel. Returns file path."""
        if records is None:
            records = self.get_attendance_records()
        if not records:
            return ""
        df = pd.DataFrame(records)
        if filename is None:
            filename = f"attendance_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        path = os.path.join(EXPORT_DIR, filename)
        with pd.ExcelWriter(path, engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name="Attendance", index=False)
            # Auto-size columns
            worksheet = writer.sheets["Attendance"]
            for col in worksheet.columns:
                max_len = max(len(str(cell.value or "")) for cell in col) + 2
                worksheet.column_dimensions[col[0].column_letter].width = max_len
        logger.info(f"Exported Excel: {path}")
        return path

    # ══════════════════════════════════════════════════════════
    #  SETTINGS OPERATIONS
    # ══════════════════════════════════════════════════════════

    def get_setting(self, key: str, default: str = "") -> str:
        """Retrieve a setting value by key."""
        with self._get_connection() as conn:
            row = conn.execute(
                "SELECT value FROM settings WHERE key = ?", (key,)
            ).fetchone()
            return row[0] if row else default

    def set_setting(self, key: str, value: str):
        """Insert or update a setting."""
        with self._get_connection() as conn:
            conn.execute("""
                INSERT INTO settings (key, value, updated_at)
                VALUES (?, ?, datetime('now','localtime'))
                ON CONFLICT(key) DO UPDATE SET
                    value = excluded.value,
                    updated_at = excluded.updated_at
            """, (key, value))
            conn.commit()

    def get_all_settings(self) -> dict:
        """Return all settings as a dict."""
        with self._get_connection() as conn:
            rows = conn.execute("SELECT key, value FROM settings").fetchall()
            return {r[0]: r[1] for r in rows}

    # ══════════════════════════════════════════════════════════
    #  BACKUP OPERATIONS
    # ══════════════════════════════════════════════════════════

    def backup_database(self) -> str:
        """Create a timestamped backup of the database. Returns backup path."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(BACKUP_DIR, f"attendance_backup_{timestamp}.db")
        shutil.copy2(self.db_path, backup_path)
        self._log_action("BACKUP_CREATED", f"Path={backup_path}")
        logger.info(f"Database backed up: {backup_path}")
        return backup_path

    def get_departments(self) -> list:
        """Return list of unique departments."""
        with self._get_connection() as conn:
            rows = conn.execute(
                "SELECT DISTINCT department FROM users WHERE is_active=1 ORDER BY department"
            ).fetchall()
            return [r[0] for r in rows]

    # ══════════════════════════════════════════════════════════
    #  AUDIT LOG
    # ══════════════════════════════════════════════════════════

    def _log_action(self, action: str, details: str = ""):
        """Write to audit log."""
        try:
            with self._get_connection() as conn:
                conn.execute(
                    "INSERT INTO audit_log (action, details) VALUES (?, ?)",
                    (action, details)
                )
                conn.commit()
        except Exception:
            pass  # Audit log failures should not crash the app

    def get_audit_log(self, limit: int = 100) -> list:
        """Return recent audit log entries."""
        with self._get_connection() as conn:
            rows = conn.execute(
                "SELECT * FROM audit_log ORDER BY timestamp DESC LIMIT ?",
                (limit,)
            ).fetchall()
            return [dict(r) for r in rows]


# ── Singleton instance (import and use directly) ─────────────
db = DatabaseManager()


# ============================================================
# File: ./database/__init__.py
# ============================================================

# Database package


# ============================================================
# File: ./utils/__init__.py
# ============================================================

# Utilities package


# ============================================================
# File: ./utils/helpers.py
# ============================================================

"""
╔══════════════════════════════════════════════════════════════╗
║             UTILITIES — Face Attendance System              ║
║  Shared helpers: sound, theme, time, notifications, camera  ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import sys
import threading
import platform
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ═══════════════════════════════════════════════════════════════
#  SOUND MANAGER
# ═══════════════════════════════════════════════════════════════
class SoundManager:
    """
    Play sound effects using pygame.mixer.
    Falls back silently if pygame is unavailable.
    """

    def __init__(self):
        self._available = False
        try:
            import pygame
            pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
            self._pygame = pygame
            self._available = True
        except Exception as e:
            logger.warning(f"Sound unavailable: {e}")

    def play_success(self):
        """Play a success tone (attendance marked)."""
        self._beep(frequency=880, duration=0.15)

    def play_error(self):
        """Play an error tone (already marked / unknown)."""
        self._beep(frequency=300, duration=0.2)

    def play_notification(self):
        """Play a soft notification sound."""
        self._beep(frequency=660, duration=0.1)

    def _beep(self, frequency: int, duration: float):
        """Generate and play a sine-wave beep in a background thread."""
        if not self._available:
            return
        threading.Thread(
            target=self._play_beep_thread,
            args=(frequency, duration),
            daemon=True
        ).start()

    def _play_beep_thread(self, frequency: int, duration: float):
        try:
            import numpy as np
            import pygame
            sample_rate = 44100
            samples     = int(sample_rate * duration)
            t           = np.linspace(0, duration, samples, False)
            wave        = (np.sin(2 * np.pi * frequency * t) * 32767).astype(np.int16)
            stereo      = np.column_stack([wave, wave])
            sound       = pygame.sndarray.make_sound(stereo)
            sound.play()
            pygame.time.wait(int(duration * 1000) + 50)
        except Exception:
            pass


# ═══════════════════════════════════════════════════════════════
#  THEME MANAGER
# ═══════════════════════════════════════════════════════════════
class ThemeManager:
    """
    Centralized color palette and font definitions.
    Supports Dark (default) and Light modes.
    """

    DARK = {
        "bg_primary":      "#0D1117",
        "bg_secondary":    "#161B22",
        "bg_card":         "#1C2333",
        "bg_sidebar":      "#0D1117",
        "bg_hover":        "#21262D",
        "accent":          "#2188FF",
        "accent_hover":    "#1F78E8",
        "accent_green":    "#3FB950",
        "accent_red":      "#F85149",
        "accent_yellow":   "#D29922",
        "accent_purple":   "#BC8CFF",
        "text_primary":    "#E6EDF3",
        "text_secondary":  "#8B949E",
        "text_muted":      "#484F58",
        "border":          "#30363D",
        "border_active":   "#2188FF",
        "success":         "#3FB950",
        "warning":         "#D29922",
        "error":           "#F85149",
        "table_header":    "#1C2333",
        "table_row":       "#161B22",
        "table_row_alt":   "#1C2333",
        "scrollbar":       "#21262D",
        "button_text":     "#FFFFFF",
        "sidebar_active":  "#21262D",
        "chart_colors":   ["#2188FF", "#3FB950", "#BC8CFF", "#D29922", "#F85149"],
    }

    LIGHT = {
        "bg_primary":      "#F6F8FA",
        "bg_secondary":    "#FFFFFF",
        "bg_card":         "#FFFFFF",
        "bg_sidebar":      "#F6F8FA",
        "bg_hover":        "#EFF2F5",
        "accent":          "#0969DA",
        "accent_hover":    "#0860CA",
        "accent_green":    "#1A7F37",
        "accent_red":      "#CF222E",
        "accent_yellow":   "#9A6700",
        "accent_purple":   "#8250DF",
        "text_primary":    "#1F2328",
        "text_secondary":  "#57606A",
        "text_muted":      "#8C959F",
        "border":          "#D0D7DE",
        "border_active":   "#0969DA",
        "success":         "#1A7F37",
        "warning":         "#9A6700",
        "error":           "#CF222E",
        "table_header":    "#F6F8FA",
        "table_row":       "#FFFFFF",
        "table_row_alt":   "#F6F8FA",
        "scrollbar":       "#D0D7DE",
        "button_text":     "#FFFFFF",
        "sidebar_active":  "#EFF2F5",
        "chart_colors":   ["#0969DA", "#1A7F37", "#8250DF", "#9A6700", "#CF222E"],
    }

    FONTS = {
        "heading_xl":  ("Helvetica Neue", 28, "bold"),
        "heading_lg":  ("Helvetica Neue", 22, "bold"),
        "heading_md":  ("Helvetica Neue", 18, "bold"),
        "heading_sm":  ("Helvetica Neue", 15, "bold"),
        "body_lg":     ("Helvetica Neue", 14, "normal"),
        "body_md":     ("Helvetica Neue", 13, "normal"),
        "body_sm":     ("Helvetica Neue", 12, "normal"),
        "caption":     ("Helvetica Neue", 11, "normal"),
        "mono":        ("Courier New",    12, "normal"),
        "button":      ("Helvetica Neue", 13, "bold"),
        "badge":       ("Helvetica Neue", 10, "bold"),
    }

    def __init__(self, mode: str = "dark"):
        self.mode = mode
        self.colors = self.DARK if mode == "dark" else self.LIGHT

    def toggle(self):
        self.mode   = "light" if self.mode == "dark" else "dark"
        self.colors = self.DARK if self.mode == "dark" else self.LIGHT
        return self.mode

    def get(self, key: str) -> str:
        return self.colors.get(key, "#FFFFFF")

    def font(self, key: str) -> tuple:
        return self.FONTS.get(key, ("Helvetica Neue", 13, "normal"))


# ═══════════════════════════════════════════════════════════════
#  TIME UTILITIES
# ═══════════════════════════════════════════════════════════════
def get_current_time_str() -> str:
    """Return formatted current time: HH:MM:SS"""
    return datetime.now().strftime("%H:%M:%S")


def get_current_date_str() -> str:
    """Return formatted current date: Day, DD Month YYYY"""
    return datetime.now().strftime("%A, %d %B %Y")


def get_timestamp() -> str:
    """Return full timestamp string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_date(date_str: str) -> str:
    """Convert YYYY-MM-DD to readable DD Mon YYYY."""
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return dt.strftime("%d %b %Y")
    except Exception:
        return date_str


# ═══════════════════════════════════════════════════════════════
#  CAMERA UTILITIES
# ═══════════════════════════════════════════════════════════════
def list_available_cameras(max_check: int = 5) -> list:
    """
    Detect available camera indices.
    Returns a list of valid integer indices.
    """
    import cv2
    available = []
    for i in range(max_check):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            available.append(i)
            cap.release()
    return available if available else [0]


# ═══════════════════════════════════════════════════════════════
#  VALIDATION UTILITIES
# ═══════════════════════════════════════════════════════════════
def validate_user_input(name: str, roll: str, dept: str) -> tuple[bool, str]:
    """
    Validate registration form inputs.
    Returns: (is_valid: bool, error_message: str)
    """
    if not name or len(name.strip()) < 2:
        return False, "Name must be at least 2 characters."
    if not roll or len(roll.strip()) < 1:
        return False, "Roll number / ID is required."
    if not dept or len(dept.strip()) < 1:
        return False, "Department / Class is required."
    # Reject special characters in roll number
    import re
    if not re.match(r"^[A-Za-z0-9\-_/]+$", roll.strip()):
        return False, "Roll number may only contain letters, digits, -, _, /."
    return True, ""


def open_file(path: str):
    """Open a file with the system default application."""
    try:
        if platform.system() == "Darwin":
            os.system(f'open "{path}"')
        elif platform.system() == "Windows":
            os.startfile(path)
        else:
            os.system(f'xdg-open "{path}"')
    except Exception as e:
        logger.error(f"Cannot open file: {e}")


# ── Singletons ────────────────────────────────────────────────
sound_manager = SoundManager()
theme_manager = ThemeManager(mode="dark")


# ============================================================
# File: ./face_recognition_engine/recognizer.py
# ============================================================

"""
╔══════════════════════════════════════════════════════════════╗
║      FACE RECOGNITION ENGINE — Face Attendance System       ║
║  Handles face encoding, training, and real-time detection   ║
╚══════════════════════════════════════════════════════════════╝

This module handles:
  - Capturing face images for new users
  - Encoding faces and saving encodings to disk
  - Loading existing encodings from disk
  - Real-time face recognition from webcam frames
  - Confidence scoring and unknown face handling
"""

import cv2
import face_recognition
import numpy as np
import os
import pickle
import logging
from datetime import datetime

# ── Paths ────────────────────────────────────────────────────
BASE_DIR       = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FACE_DATA_DIR  = os.path.join(BASE_DIR, "data", "face_data")
ENCODINGS_FILE = os.path.join(BASE_DIR, "data", "face_encodings.pkl")

os.makedirs(FACE_DATA_DIR, exist_ok=True)

# ── Logging ──────────────────────────────────────────────────
logger = logging.getLogger(__name__)


# ═══════════════════════════════════════════════════════════════
#  FaceRecognitionEngine Class
# ═══════════════════════════════════════════════════════════════
class FaceRecognitionEngine:
    """
    Core face recognition engine.
    Manages encoding storage, model training, and live recognition.
    """

    def __init__(self):
        # Loaded encodings: {"encodings": [...], "ids": [...], "names": [...]}
        self.known_encodings = []
        self.known_ids       = []
        self.known_names     = []

        # Tolerance: lower = stricter matching (0.4-0.6 is typical)
        self.tolerance = 0.50

        # Haar cascade for fast face detection (pre-check before deep encoding)
        cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        self.face_cascade = cv2.CascadeClassifier(cascade_path)

        # Load existing encodings from disk
        self.load_encodings()
        logger.info("FaceRecognitionEngine initialized.")

    # ══════════════════════════════════════════════════════════
    #  ENCODING PERSISTENCE
    # ══════════════════════════════════════════════════════════

    def save_encodings(self):
        """Save all known encodings to disk as a pickle file."""
        data = {
            "encodings": self.known_encodings,
            "ids":       self.known_ids,
            "names":     self.known_names,
        }
        with open(ENCODINGS_FILE, "wb") as f:
            pickle.dump(data, f)
        logger.info(f"Encodings saved: {len(self.known_encodings)} faces.")

    def load_encodings(self):
        """Load encodings from disk (if file exists)."""
        if os.path.exists(ENCODINGS_FILE):
            try:
                with open(ENCODINGS_FILE, "rb") as f:
                    data = pickle.load(f)
                self.known_encodings = data.get("encodings", [])
                self.known_ids       = data.get("ids", [])
                self.known_names     = data.get("names", [])
                logger.info(f"Loaded {len(self.known_encodings)} face encodings.")
            except Exception as e:
                logger.error(f"Error loading encodings: {e}")
                self.known_encodings = []
                self.known_ids       = []
                self.known_names     = []
        else:
            logger.info("No encoding file found. Starting fresh.")

    def reload_encodings(self):
        """Public method to reload encodings from disk (call after training)."""
        self.load_encodings()

    # ══════════════════════════════════════════════════════════
    #  FACE CAPTURE (Registration)
    # ══════════════════════════════════════════════════════════

    def capture_face_images(self, user_id: int, user_name: str,
                            num_images: int = 30,
                            camera_index: int = 0,
                            progress_callback=None,
                            frame_callback=None) -> bool:
        """
        Capture `num_images` face images from webcam for a new user.

        Args:
            user_id:           Database ID of the user
            user_name:         Display name (for folder naming)
            num_images:        Number of face images to capture
            camera_index:      Webcam index (0 = default)
            progress_callback: Called with (current, total) for progress bar
            frame_callback:    Called with each BGR frame for live preview

        Returns:
            True if successful, False otherwise.
        """
        # Create user-specific folder
        safe_name   = "".join(c for c in user_name if c.isalnum() or c in "_ -")
        user_folder = os.path.join(FACE_DATA_DIR, f"{user_id}_{safe_name}")
        os.makedirs(user_folder, exist_ok=True)

        cap = cv2.VideoCapture(camera_index)
        if not cap.isOpened():
            logger.error("Cannot open camera for capture.")
            return False

        cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        cap.set(cv2.CAP_PROP_FPS,          30)

        captured = 0
        attempt  = 0
        max_attempts = num_images * 10  # avoid infinite loop

        logger.info(f"Capturing {num_images} images for: {user_name}")

        while captured < num_images and attempt < max_attempts:
            ret, frame = cap.read()
            if not ret:
                attempt += 1
                continue

            attempt += 1
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Detect faces using fast HOG model
            face_locations = face_recognition.face_locations(rgb_frame, model="hog")

            if len(face_locations) == 1:   # exactly one face — ideal
                top, right, bottom, left = face_locations[0]

                # Draw green rectangle around face
                display = frame.copy()
                cv2.rectangle(display, (left, top), (right, bottom), (0, 255, 100), 2)
                cv2.putText(display, f"Capturing: {captured+1}/{num_images}",
                            (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 100), 2)

                # Save face image
                face_img = frame[top:bottom, left:right]
                img_path = os.path.join(user_folder, f"{captured:04d}.jpg")
                cv2.imwrite(img_path, face_img)
                captured += 1

                if progress_callback:
                    progress_callback(captured, num_images)
                if frame_callback:
                    frame_callback(display)

            elif len(face_locations) == 0:
                # No face detected — show warning on frame
                display = frame.copy()
                cv2.putText(display, "No face detected. Look at camera.",
                            (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 100, 255), 2)
                if frame_callback:
                    frame_callback(display)
            else:
                # Multiple faces — ask user to be alone
                display = frame.copy()
                cv2.putText(display, "Multiple faces! Stay alone in frame.",
                            (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 50, 255), 2)
                if frame_callback:
                    frame_callback(display)

        cap.release()

        if captured >= num_images:
            logger.info(f"Captured {captured} images for {user_name}.")
            return True
        else:
            logger.warning(f"Only captured {captured}/{num_images} images.")
            return captured > 5  # Accept partial if at least 5 images

    # ══════════════════════════════════════════════════════════
    #  TRAINING
    # ══════════════════════════════════════════════════════════

    def train_model(self, progress_callback=None) -> bool:
        """
        Scan all face image folders, encode each face,
        and save encodings to disk.

        Args:
            progress_callback: Called with (current, total) during training

        Returns:
            True on success, False on failure.
        """
        logger.info("Starting model training...")

        # Discover all user folders
        user_folders = [
            d for d in os.listdir(FACE_DATA_DIR)
            if os.path.isdir(os.path.join(FACE_DATA_DIR, d))
        ]

        if not user_folders:
            logger.warning("No face data found to train on.")
            return False

        new_encodings = []
        new_ids       = []
        new_names     = []

        total_images = sum(
            len(os.listdir(os.path.join(FACE_DATA_DIR, f)))
            for f in user_folders
        )
        processed = 0

        for folder_name in user_folders:
            # Folder format: "userID_userName"
            parts   = folder_name.split("_", 1)
            user_id = int(parts[0]) if parts[0].isdigit() else -1
            name    = parts[1] if len(parts) > 1 else folder_name

            folder_path = os.path.join(FACE_DATA_DIR, folder_name)
            image_files = [
                f for f in os.listdir(folder_path)
                if f.lower().endswith((".jpg", ".jpeg", ".png"))
            ]

            encodings_for_user = []

            for img_file in image_files:
                img_path = os.path.join(folder_path, img_file)
                try:
                    image     = face_recognition.load_image_file(img_path)
                    encodings = face_recognition.face_encodings(image)

                    if encodings:
                        encodings_for_user.append(encodings[0])
                except Exception as e:
                    logger.warning(f"Could not encode {img_path}: {e}")

                processed += 1
                if progress_callback:
                    progress_callback(processed, total_images)

            # Use mean encoding for better robustness
            if encodings_for_user:
                mean_encoding = np.mean(encodings_for_user, axis=0)
                new_encodings.append(mean_encoding)
                new_ids.append(user_id)
                new_names.append(name)
                logger.info(f"Trained: {name} ({len(encodings_for_user)} images)")

        if new_encodings:
            self.known_encodings = new_encodings
            self.known_ids       = new_ids
            self.known_names     = new_names
            self.save_encodings()
            logger.info(f"Training complete. {len(new_encodings)} users trained.")
            return True
        else:
            logger.error("No valid encodings found during training.")
            return False

    # ══════════════════════════════════════════════════════════
    #  REAL-TIME RECOGNITION
    # ══════════════════════════════════════════════════════════

    def recognize_faces(self, frame: np.ndarray) -> list:
        """
        Recognize faces in a single BGR frame.

        Args:
            frame: OpenCV BGR image (numpy array)

        Returns:
            List of dicts: [
                {
                  "name":       str,        # recognized name or "Unknown"
                  "user_id":    int,        # DB user ID or -1
                  "confidence": float,      # 0.0 – 1.0 (higher = more confident)
                  "location":  (top, right, bottom, left)
                }
            ]
        """
        if not self.known_encodings:
            return []

        # Resize frame to 1/4 size for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small   = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Detect face locations (HOG is faster than CNN on CPU)
        face_locations = face_recognition.face_locations(rgb_small, model="hog")

        if not face_locations:
            return []

        # Compute encodings for all detected faces
        face_encodings = face_recognition.face_encodings(rgb_small, face_locations)

        results = []
        for encoding, location in zip(face_encodings, face_locations):
            # Compare against all known encodings
            distances = face_recognition.face_distance(self.known_encodings, encoding)

            best_match_idx  = np.argmin(distances)
            best_distance   = distances[best_match_idx]
            confidence      = 1.0 - best_distance   # closer to 1 = more confident

            # Scale location back to full frame size
            top, right, bottom, left = location
            top    *= 4
            right  *= 4
            bottom *= 4
            left   *= 4

            if best_distance <= self.tolerance:
                results.append({
                    "name":       self.known_names[best_match_idx],
                    "user_id":    self.known_ids[best_match_idx],
                    "confidence": round(confidence, 3),
                    "location":   (top, right, bottom, left),
                })
            else:
                results.append({
                    "name":       "Unknown",
                    "user_id":    -1,
                    "confidence": round(confidence, 3),
                    "location":   (top, right, bottom, left),
                })

        return results

    def draw_recognition_results(self, frame: np.ndarray,
                                 results: list,
                                 marked_today: set = None) -> np.ndarray:
        """
        Draw bounding boxes and labels on a frame.

        Args:
            frame:        BGR frame to draw on
            results:      Output of recognize_faces()
            marked_today: Set of user_ids already marked today

        Returns:
            Annotated BGR frame
        """
        marked_today = marked_today or set()
        overlay      = frame.copy()

        for r in results:
            top, right, bottom, left = r["location"]
            name       = r["name"]
            confidence = r["confidence"]
            user_id    = r["user_id"]
            already    = user_id in marked_today

            # Color coding
            if name == "Unknown":
                color = (0, 50, 255)    # Red-ish
                label = "Unknown"
            elif already:
                color = (0, 200, 255)   # Amber — already marked
                label = f"{name} ✓ (Already Marked)"
            else:
                color = (0, 220, 80)    # Green — recognized, not yet marked
                label = f"{name} ({int(confidence * 100)}%)"

            # Draw filled rectangle for label background
            cv2.rectangle(overlay, (left, top), (right, bottom), color, 2)
            cv2.rectangle(overlay, (left, bottom - 30), (right, bottom), color, cv2.FILLED)
            cv2.putText(overlay, label,
                        (left + 6, bottom - 8),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1)

        # Blend overlay for semi-transparency
        return cv2.addWeighted(overlay, 0.85, frame, 0.15, 0)

    # ══════════════════════════════════════════════════════════
    #  UTILITIES
    # ══════════════════════════════════════════════════════════

    def get_registered_count(self) -> int:
        """Number of users currently loaded in memory."""
        return len(self.known_encodings)

    def remove_user_encodings(self, user_id: int) -> bool:
        """Remove encodings for a specific user and retrain."""
        indices_to_remove = [
            i for i, uid in enumerate(self.known_ids) if uid == user_id
        ]
        if not indices_to_remove:
            return False
        for i in sorted(indices_to_remove, reverse=True):
            self.known_encodings.pop(i)
            self.known_ids.pop(i)
            self.known_names.pop(i)
        self.save_encodings()
        return True

    def set_tolerance(self, value: float):
        """Adjust recognition tolerance (0.4 = strict, 0.6 = lenient)."""
        self.tolerance = max(0.3, min(0.7, value))
        logger.info(f"Tolerance set to {self.tolerance}")


# ── Singleton instance ────────────────────────────────────────
engine = FaceRecognitionEngine()


# ============================================================
# File: ./face_recognition_engine/__init__.py
# ============================================================

# Face recognition engine package


# ============================================================
# File: ./gui/sidebar.py
# ============================================================

"""
╔══════════════════════════════════════════════════════════════╗
║              SIDEBAR — Face Attendance System               ║
║  Left navigation panel with animated hover effects          ║
╚══════════════════════════════════════════════════════════════╝
"""

import customtkinter as ctk
from utils.helpers import theme_manager


# ── Navigation items: (icon, label, page_key) ─────────────────
NAV_ITEMS = [
    ("🏠", "Dashboard",       "dashboard"),
    ("📷", "Attendance",      "attendance"),
    ("👤", "Register User",   "register"),
    ("📋", "View Records",    "records"),
    ("📊", "Analytics",       "analytics"),
    ("⚙️",  "Settings",        "settings"),
]


class Sidebar(ctk.CTkFrame):
    """
    Left-side navigation sidebar.
    Calls on_navigate(page_key) when a nav item is clicked.
    """

    def __init__(self, parent, on_navigate, **kwargs):
        c = theme_manager.colors
        super().__init__(
            parent,
            width=220,
            corner_radius=0,
            fg_color=c["bg_sidebar"],
            **kwargs
        )
        self.on_navigate   = on_navigate
        self.active_key    = "dashboard"
        self._buttons      = {}

        self.pack_propagate(False)
        self._build_ui()

    def _build_ui(self):
        c = theme_manager.colors

        # ── Logo / App Name ───────────────────────────────────
        logo_frame = ctk.CTkFrame(self, fg_color="transparent", height=80)
        logo_frame.pack(fill="x", padx=0, pady=0)
        logo_frame.pack_propagate(False)

        ctk.CTkLabel(
            logo_frame, text="👁 FaceTrack",
            font=ctk.CTkFont(family="Helvetica Neue", size=20, weight="bold"),
            text_color=c["text_primary"]
        ).pack(pady=(22, 0))

        ctk.CTkLabel(
            logo_frame, text="Pro",
            font=ctk.CTkFont(size=11),
            text_color=c["accent"]
        ).pack(pady=(0, 10))

        # ── Divider ───────────────────────────────────────────
        ctk.CTkFrame(self, height=1, fg_color=c["border"]).pack(fill="x", padx=16)

        # ── Navigation Buttons ────────────────────────────────
        nav_frame = ctk.CTkFrame(self, fg_color="transparent")
        nav_frame.pack(fill="both", expand=True, pady=(12, 0))

        for icon, label, key in NAV_ITEMS:
            btn = self._create_nav_button(nav_frame, icon, label, key)
            self._buttons[key] = btn

        # ── Bottom: Version ───────────────────────────────────
        ctk.CTkLabel(
            self, text="v2.0.0 Professional",
            font=ctk.CTkFont(size=10),
            text_color=c["text_muted"]
        ).pack(side="bottom", pady=12)

        # Set initial active state
        self._set_active("dashboard")

    def _create_nav_button(self, parent, icon: str, label: str, key: str):
        """Create a single navigation button with hover animation."""
        c   = theme_manager.colors
        btn = ctk.CTkButton(
            parent,
            text=f"  {icon}   {label}",
            font=ctk.CTkFont(family="Helvetica Neue", size=13, weight="bold"),
            fg_color="transparent",
            text_color=c["text_secondary"],
            hover_color=c["bg_hover"],
            anchor="w",
            height=44,
            corner_radius=8,
            command=lambda k=key: self._on_click(k)
        )
        btn.pack(fill="x", padx=12, pady=2)
        return btn

    def _on_click(self, key: str):
        self._set_active(key)
        self.on_navigate(key)

    def _set_active(self, key: str):
        """Highlight the active navigation item."""
        c = theme_manager.colors
        # Deactivate all
        for k, btn in self._buttons.items():
            btn.configure(
                fg_color="transparent",
                text_color=c["text_secondary"]
            )
        # Activate selected
        if key in self._buttons:
            self._buttons[key].configure(
                fg_color=c["sidebar_active"],
                text_color=c["text_primary"]
            )
            self.active_key = key

    def refresh_theme(self):
        """Re-apply theme colors (called on theme toggle)."""
        c = theme_manager.colors
        self.configure(fg_color=c["bg_sidebar"])
        self._set_active(self.active_key)


# ============================================================
# File: ./gui/notification.py
# ============================================================

"""
╔══════════════════════════════════════════════════════════════╗
║          NOTIFICATION — Face Attendance System              ║
║  Toast-style popup notifications                            ║
╚══════════════════════════════════════════════════════════════╝
"""

import customtkinter as ctk
import threading
import time

class ToastNotification:
    """
    Displays a floating toast-style notification in the bottom-right corner.
    Auto-dismisses after a set duration.
    
    Usage:
        ToastNotification(root, "Attendance Marked!", type_="success")
    """

    def __init__(self, parent, message: str, type_: str = "info", duration: float = 3.0):
        """
        Args:
            parent:   The root/parent Tkinter window.
            message:  The text to display.
            type_:    One of 'success', 'error', 'warning', 'info'.
            duration: Seconds before auto-dismiss.
        """
        self.parent   = parent
        self.message  = message
        self.type_    = type_
        self.duration = duration

        # Color mapping
        colors = {
            "success": ("#3FB950", "✅"),
            "error":   ("#F85149", "❌"),
            "warning": ("#D29922", "⚠️"),
            "info":    ("#2188FF", "ℹ️"),
        }
        self.color, self.icon = colors.get(type_, colors["info"])

        self._build()

    def _build(self):
        # Create a Toplevel window (no title bar)
        self.toast = ctk.CTkToplevel(self.parent)
        self.toast.overrideredirect(True)
        self.toast.attributes("-topmost", True)
        self.toast.configure(fg_color="#1C2333")
        self.toast.attributes("-alpha", 0.0)  # Start invisible

        # Content
        frame = ctk.CTkFrame(self.toast, fg_color="#1C2333", corner_radius=10,
                              border_width=1, border_color=self.color)
        frame.pack(padx=2, pady=2)

        ctk.CTkLabel(frame, text=self.icon, font=ctk.CTkFont(size=18)).pack(
            side="left", padx=(15, 5), pady=12
        )
        ctk.CTkLabel(
            frame, text=self.message,
            font=ctk.CTkFont(family="Helvetica Neue", size=13),
            text_color="#E6EDF3",
            wraplength=260
        ).pack(side="left", padx=(0, 15), pady=12)

        self.toast.update_idletasks()
        w = self.toast.winfo_reqwidth()
        h = self.toast.winfo_reqheight()
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        # Position: bottom-right
        x = sw - w - 20
        y = sh - h - 60
        self.toast.geometry(f"+{x}+{y}")

        # Fade-in then auto-dismiss
        threading.Thread(target=self._animate, daemon=True).start()

    def _animate(self):
        """Fade in → wait → fade out."""
        # Fade in
        for i in range(1, 11):
            self.toast.after(0, lambda v=i/10: self.toast.attributes("-alpha", v))
            time.sleep(0.03)

        time.sleep(self.duration)

        # Fade out
        for i in range(10, 0, -1):
            self.toast.after(0, lambda v=i/10: self.toast.attributes("-alpha", v))
            time.sleep(0.03)

        self.toast.after(0, self.toast.destroy)


# ============================================================
# File: ./gui/__init__.py
# ============================================================

# GUI package


# ============================================================
# File: ./gui/splash_screen.py
# ============================================================

"""
╔══════════════════════════════════════════════════════════════╗
║          SPLASH SCREEN — Face Attendance System             ║
║  Professional startup screen with animated progress bar     ║
╚══════════════════════════════════════════════════════════════╝
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import font as tkfont
import threading
import time


class SplashScreen(ctk.CTkToplevel):
    """
    Animated splash screen shown while the app loads.
    Automatically closes and calls on_complete when loading finishes.
    """

    def __init__(self, parent, on_complete):
        super().__init__(parent)
        self.on_complete = on_complete
        self._progress   = 0.0
        self._tasks      = []

        self._setup_window()
        self._build_ui()
        self._start_loading()

    def _setup_window(self):
        """Configure splash window: no title bar, centered, always on top."""
        self.overrideredirect(True)       # No title bar
        self.attributes("-topmost", True)

        w, h = 520, 340
        sw   = self.winfo_screenwidth()
        sh   = self.winfo_screenheight()
        x    = (sw - w) // 2
        y    = (sh - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y}")
        self.configure(fg_color="#0D1117")
        self.resizable(False, False)

        # Rounded corners on macOS
        try:
            self.attributes("-transparent", True)
        except Exception:
            pass

    def _build_ui(self):
        """Build all UI elements."""
        # ── Background gradient frame ─────────────────────────
        main = ctk.CTkFrame(self, fg_color="#0D1117", corner_radius=16)
        main.pack(fill="both", expand=True, padx=2, pady=2)

        # ── Accent top border ─────────────────────────────────
        accent = ctk.CTkFrame(main, fg_color="#2188FF",
                               height=4, corner_radius=0)
        accent.pack(fill="x", side="top")

        # ── Logo / Icon ───────────────────────────────────────
        ctk.CTkLabel(main, text="👁",
                     font=ctk.CTkFont(size=64)).pack(pady=(30, 0))

        # ── App Title ─────────────────────────────────────────
        ctk.CTkLabel(main, text="FaceTrack Pro",
                     font=ctk.CTkFont(family="Helvetica Neue",
                                      size=32, weight="bold"),
                     text_color="#E6EDF3").pack(pady=(8, 2))

        # ── Subtitle ──────────────────────────────────────────
        ctk.CTkLabel(main, text="AI-Powered Attendance System",
                     font=ctk.CTkFont(size=14),
                     text_color="#8B949E").pack()

        # ── Version ───────────────────────────────────────────
        ctk.CTkLabel(main, text="v2.0.0  •  Professional Edition",
                     font=ctk.CTkFont(size=11),
                     text_color="#484F58").pack(pady=(4, 0))

        # ── Progress Bar ──────────────────────────────────────
        progress_frame = ctk.CTkFrame(main, fg_color="transparent")
        progress_frame.pack(fill="x", padx=50, pady=(30, 8))

        self.progress_bar = ctk.CTkProgressBar(
            progress_frame,
            mode="determinate",
            height=6,
            corner_radius=3,
            fg_color="#21262D",
            progress_color="#2188FF",
        )
        self.progress_bar.pack(fill="x")
        self.progress_bar.set(0)

        # ── Status Label ──────────────────────────────────────
        self.status_label = ctk.CTkLabel(
            main,
            text="Initializing...",
            font=ctk.CTkFont(size=12),
            text_color="#8B949E"
        )
        self.status_label.pack()

        # ── Footer ────────────────────────────────────────────
        ctk.CTkLabel(main, text="© 2024 FaceTrack Pro  •  All rights reserved",
                     font=ctk.CTkFont(size=10),
                     text_color="#21262D").pack(side="bottom", pady=12)

    def _start_loading(self):
        """Run loading tasks in a background thread."""
        self._tasks = [
            (0.10, "Loading configuration..."),
            (0.25, "Connecting to database..."),
            (0.45, "Loading face encodings..."),
            (0.65, "Initializing camera..."),
            (0.80, "Building interface..."),
            (0.95, "Almost ready..."),
            (1.00, "Welcome to FaceTrack Pro!"),
        ]
        threading.Thread(target=self._run_tasks, daemon=True).start()

    def _run_tasks(self):
        """Simulate loading tasks with smooth progress animation."""
        for progress, message in self._tasks:
            # Animate to target progress smoothly
            steps = 20
            start = self._progress
            delta = (progress - start) / steps
            for _ in range(steps):
                self._progress += delta
                self._update_progress(self._progress, message)
                time.sleep(0.03)

        time.sleep(0.4)
        self._finish()

    def _update_progress(self, value: float, message: str):
        """Thread-safe UI update."""
        try:
            self.after(0, lambda: self.progress_bar.set(value))
            self.after(0, lambda: self.status_label.configure(text=message))
        except Exception:
            pass

    def _finish(self):
        """Close splash and call on_complete callback."""
        try:
            self.after(200, self._close)
        except Exception:
            pass

    def _close(self):
        try:
            self.on_complete()
            self.destroy()
        except Exception:
            pass


# ============================================================
# File: ./gui/admin_login.py
# ============================================================

"""
╔══════════════════════════════════════════════════════════════╗
║           ADMIN LOGIN DIALOG — Face Attendance System       ║
║  Simple password-protected gate before admin areas          ║
╚══════════════════════════════════════════════════════════════╝
"""

import customtkinter as ctk
from database.db_manager import db
from utils.helpers import theme_manager


class AdminLoginDialog(ctk.CTkToplevel):
    """
    A modal admin login dialog.
    
    Usage:
        dialog = AdminLoginDialog(parent)
        parent.wait_window(dialog)
        if dialog.authenticated:
            ... # proceed
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.authenticated = False
        self._attempts     = 0
        self._max_attempts = 3

        self._setup_window()
        self._build_ui()
        self.grab_set()           # Make modal
        self.ent_password.focus() # Focus password field

    def _setup_window(self):
        self.title("Admin Authentication")
        self.geometry("400x300")
        self.resizable(False, False)
        c = theme_manager.colors
        self.configure(fg_color=c["bg_secondary"])
        self.attributes("-topmost", True)

        # Center on parent
        self.update_idletasks()
        pw, ph = self.winfo_reqwidth(), self.winfo_reqheight()
        px = self.master.winfo_rootx() + (self.master.winfo_width()  - pw) // 2
        py = self.master.winfo_rooty() + (self.master.winfo_height() - ph) // 2
        self.geometry(f"+{px}+{py}")

    def _build_ui(self):
        c = theme_manager.colors

        ctk.CTkLabel(
            self, text="🔐  Admin Login",
            font=theme_manager.font("heading_md"),
            text_color=c["text_primary"]
        ).pack(pady=(35, 5))

        ctk.CTkLabel(
            self, text="Enter the admin password to continue.",
            font=theme_manager.font("body_sm"),
            text_color=c["text_secondary"]
        ).pack(pady=(0, 25))

        self.ent_password = ctk.CTkEntry(
            self, placeholder_text="Password",
            show="•", height=42, width=280,
            font=theme_manager.font("body_md")
        )
        self.ent_password.pack()
        self.ent_password.bind("<Return>", lambda _: self._try_login())

        self.lbl_error = ctk.CTkLabel(
            self, text="", text_color=c["error"],
            font=theme_manager.font("body_sm")
        )
        self.lbl_error.pack(pady=8)

        ctk.CTkButton(
            self, text="Authenticate", width=280, height=42,
            font=theme_manager.font("button"),
            fg_color=c["accent"], hover_color=c["accent_hover"],
            command=self._try_login
        ).pack()

        ctk.CTkButton(
            self, text="Cancel", width=280, height=36,
            font=theme_manager.font("body_sm"),
            fg_color="transparent",
            text_color=c["text_secondary"],
            hover_color=c["bg_hover"],
            command=self.destroy
        ).pack(pady=(8, 0))

    def _try_login(self):
        password = self.ent_password.get()
        stored   = db.get_setting("admin_password", "admin123")

        if password == stored:
            self.authenticated = True
            self.destroy()
        else:
            self._attempts += 1
            remaining = self._max_attempts - self._attempts
            if remaining <= 0:
                self.lbl_error.configure(text="Too many failed attempts.")
                self.after(1500, self.destroy)
            else:
                self.lbl_error.configure(
                    text=f"Incorrect password. {remaining} attempt(s) left."
                )
                self.ent_password.delete(0, "end")


# ============================================================
# File: ./gui/pages/register.py
# ============================================================

"""
╔══════════════════════════════════════════════════════════════╗
║              REGISTER — Face Attendance System              ║
║  Add new users and capture training face images             ║
╚══════════════════════════════════════════════════════════════╝
"""

import customtkinter as ctk
import cv2
import PIL.Image, PIL.ImageTk
import threading
from database.db_manager import db
from face_recognition_engine.recognizer import engine
from utils.helpers import theme_manager, validate_user_input

class RegisterPage(ctk.CTkFrame):
    def __init__(self, parent):
        c = theme_manager.colors
        super().__init__(parent, fg_color=c["bg_primary"], corner_radius=0)
        
        self.pack_propagate(False)
        self.is_capturing = False
        self._build_ui()

    def _build_ui(self):
        c = theme_manager.colors
        
        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=6)
        self.grid_rowconfigure(0, weight=1)
        
        # ── Left: Form ───────────────────────────────────────
        form_panel = ctk.CTkFrame(self, fg_color=c["bg_card"], corner_radius=12)
        form_panel.grid(row=0, column=0, sticky="nsew", padx=(30, 15), pady=30)
        form_panel.pack_propagate(False)
        
        ctk.CTkLabel(
            form_panel, text="New User Registration",
            font=theme_manager.font("heading_lg"), text_color=c["text_primary"]
        ).pack(anchor="w", padx=25, pady=(25, 20))
        
        # Inputs
        self.ent_name = self._create_input(form_panel, "Full Name *", "e.g. John Doe")
        self.ent_roll = self._create_input(form_panel, "ID / Roll Number *", "e.g. EMP-101")
        
        # Department dropdown (fetch existing or allow new)
        dept_frame = ctk.CTkFrame(form_panel, fg_color="transparent")
        dept_frame.pack(fill="x", padx=25, pady=10)
        ctk.CTkLabel(dept_frame, text="Department / Class *", font=theme_manager.font("button"), text_color=c["text_secondary"]).pack(anchor="w", pady=(0, 5))
        
        depts = db.get_departments()
        if not depts: depts = ["IT", "HR", "Engineering", "Sales"]
        self.ent_dept = ctk.CTkComboBox(dept_frame, values=depts, height=40, font=theme_manager.font("body_md"))
        self.ent_dept.pack(fill="x")
        
        self.ent_email = self._create_input(form_panel, "Email Address", "Optional")
        self.ent_phone = self._create_input(form_panel, "Phone Number", "Optional")
        
        # Error Label
        self.lbl_error = ctk.CTkLabel(form_panel, text="", text_color=c["error"], font=theme_manager.font("body_sm"))
        self.lbl_error.pack(pady=10)
        
        # Buttons
        self.btn_capture = ctk.CTkButton(
            form_panel, text="Start Capture & Train", height=45,
            font=theme_manager.font("heading_md"), fg_color=c["accent"], hover_color=c["accent_hover"],
            command=self._start_registration
        )
        self.btn_capture.pack(fill="x", padx=25, pady=(10, 10))

        # ── Right: Preview & Progress ────────────────────────
        preview_panel = ctk.CTkFrame(self, fg_color="transparent")
        preview_panel.grid(row=0, column=1, sticky="nsew", padx=(15, 30), pady=30)
        preview_panel.pack_propagate(False)
        
        # Camera display label
        self.cam_frame = ctk.CTkFrame(preview_panel, fg_color="#000000", corner_radius=12)
        self.cam_frame.pack(fill="both", expand=True, pady=(0, 20))
        self.cam_frame.pack_propagate(False)
        
        self.lbl_video = ctk.CTkLabel(self.cam_frame, text="Camera Preview", text_color="#555555")
        self.lbl_video.pack(expand=True)
        
        # Progress UI
        self.progress_frame = ctk.CTkFrame(preview_panel, fg_color=c["bg_card"], corner_radius=12, height=120)
        self.progress_frame.pack(fill="x")
        self.progress_frame.pack_propagate(False)
        
        self.lbl_status = ctk.CTkLabel(self.progress_frame, text="Ready", font=theme_manager.font("body_lg"), text_color=c["text_primary"])
        self.lbl_status.pack(pady=(20, 10))
        
        self.progress_bar = ctk.CTkProgressBar(self.progress_frame, mode="determinate", height=8, fg_color=c["bg_secondary"], progress_color=c["accent"])
        self.progress_bar.pack(fill="x", padx=30)
        self.progress_bar.set(0)

    def _create_input(self, parent, label, placeholder):
        c = theme_manager.colors
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", padx=25, pady=10)
        
        ctk.CTkLabel(frame, text=label, font=theme_manager.font("button"), text_color=c["text_secondary"]).pack(anchor="w", pady=(0, 5))
        ent = ctk.CTkEntry(frame, placeholder_text=placeholder, height=40, font=theme_manager.font("body_md"))
        ent.pack(fill="x")
        return ent

    def _start_registration(self):
        if self.is_capturing:
            return
            
        # 1. Validate
        name = self.ent_name.get()
        roll = self.ent_roll.get()
        dept = self.ent_dept.get()
        
        is_valid, err = validate_user_input(name, roll, dept)
        if not is_valid:
            self.lbl_error.configure(text=err)
            return
            
        self.lbl_error.configure(text="")
        
        # 2. Check if user exists
        if db.get_user_by_roll(roll):
            self.lbl_error.configure(text="User with this ID already exists.")
            return

        # 3. Add to DB
        uid = db.add_user(
            name=name, roll_number=roll, department=dept,
            email=self.ent_email.get(), phone=self.ent_phone.get()
        )
        if uid == -1:
            self.lbl_error.configure(text="Database error. Check logs.")
            return

        # 4. Start Capture & Train Thread
        self.is_capturing = True
        self._set_ui_state("disabled")
        self.progress_bar.set(0)
        self.lbl_status.configure(text="Capturing face images... Please look at the camera.")
        
        threading.Thread(target=self._capture_process, args=(uid, name), daemon=True).start()

    def _capture_process(self, uid, name):
        cam_idx = int(db.get_setting("camera_index", "0"))
        
        # Capture
        success = engine.capture_face_images(
            user_id=uid,
            user_name=name,
            num_images=30,
            camera_index=cam_idx,
            progress_callback=self._update_progress,
            frame_callback=self._update_preview
        )
        
        if success:
            self.after(0, lambda: self.lbl_status.configure(text="Training model... This may take a minute."))
            self.after(0, lambda: self.progress_bar.set(0))
            
            # Train
            train_success = engine.train_model(progress_callback=self._update_train_progress)
            
            if train_success:
                self.after(0, lambda: self._registration_complete(True, "Registration and Training Successful!"))
            else:
                self.after(0, lambda: self._registration_complete(False, "Training failed. Please try again."))
        else:
            self.after(0, lambda: self._registration_complete(False, "Capture failed. No faces detected."))

    def _update_progress(self, current, total):
        pct = current / total
        self.after(0, lambda: self.progress_bar.set(pct))
        
    def _update_train_progress(self, current, total):
        pct = current / total if total > 0 else 0
        self.after(0, lambda: self.progress_bar.set(pct))

    def _update_preview(self, frame):
        try:
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = PIL.Image.fromarray(rgb)
            w, h = self.cam_frame.winfo_width(), self.cam_frame.winfo_height()
            if w > 10 and h > 10:
                img = img.resize((w, h), PIL.Image.Resampling.LANCZOS)
            imgtk = PIL.ImageTk.PhotoImage(image=img)
            
            self.after(0, self._set_image, imgtk)
        except Exception:
            pass
            
    def _set_image(self, imgtk):
        self.lbl_video.imgtk = imgtk
        self.lbl_video.configure(image=imgtk)

    def _registration_complete(self, success, msg):
        self.is_capturing = False
        self._set_ui_state("normal")
        c = theme_manager.colors
        
        if success:
            self.lbl_status.configure(text=msg, text_color=c["success"])
            self.progress_bar.set(1.0)
            self._clear_form()
        else:
            self.lbl_status.configure(text=msg, text_color=c["error"])
            
        self.lbl_video.configure(image=None, text="Camera Preview")

    def _set_ui_state(self, state):
        self.ent_name.configure(state=state)
        self.ent_roll.configure(state=state)
        self.ent_dept.configure(state=state)
        self.ent_email.configure(state=state)
        self.ent_phone.configure(state=state)
        self.btn_capture.configure(state=state)

    def _clear_form(self):
        self.ent_name.delete(0, 'end')
        self.ent_roll.delete(0, 'end')
        self.ent_email.delete(0, 'end')
        self.ent_phone.delete(0, 'end')


# ============================================================
# File: ./gui/pages/attendance.py
# ============================================================

"""
╔══════════════════════════════════════════════════════════════╗
║             ATTENDANCE — Face Attendance System             ║
║  Live webcam feed and real-time face recognition scanning   ║
╚══════════════════════════════════════════════════════════════╝
"""

import customtkinter as ctk
import cv2
import PIL.Image, PIL.ImageTk
from database.db_manager import db
from face_recognition_engine.recognizer import engine
from utils.helpers import theme_manager, sound_manager, get_current_time_str
import threading

class AttendancePage(ctk.CTkFrame):
    def __init__(self, parent):
        c = theme_manager.colors
        super().__init__(parent, fg_color=c["bg_primary"], corner_radius=0)
        
        self.pack_propagate(False)
        self.camera_active = False
        self.cap = None
        self.marked_today = set()  # Cache to prevent DB spam
        self.last_results = []
        
        self._build_ui()

    def _build_ui(self):
        c = theme_manager.colors
        
        # ── Main Layout ──────────────────────────────────────
        self.grid_columnconfigure(0, weight=7)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)
        
        # ── Left: Camera View ────────────────────────────────
        cam_container = ctk.CTkFrame(self, fg_color="transparent")
        cam_container.grid(row=0, column=0, sticky="nsew", padx=(30, 15), pady=30)
        cam_container.pack_propagate(False)
        
        header = ctk.CTkFrame(cam_container, fg_color="transparent")
        header.pack(fill="x", pady=(0, 15))
        
        ctk.CTkLabel(
            header, text="Live Scanner",
            font=theme_manager.font("heading_lg"), text_color=c["text_primary"]
        ).pack(side="left")
        
        self.btn_toggle_cam = ctk.CTkButton(
            header, text="Start Camera",
            font=theme_manager.font("button"),
            fg_color=c["accent_green"], hover_color=c["success"],
            command=self.toggle_camera
        )
        self.btn_toggle_cam.pack(side="right")
        
        # Camera display label
        self.cam_frame = ctk.CTkFrame(cam_container, fg_color="#000000", corner_radius=12)
        self.cam_frame.pack(fill="both", expand=True)
        self.cam_frame.pack_propagate(False)
        
        self.lbl_video = ctk.CTkLabel(self.cam_frame, text="Camera Offline", text_color="#555555")
        self.lbl_video.pack(expand=True)
        
        # ── Right: Status & Logs ─────────────────────────────
        side_panel = ctk.CTkFrame(self, fg_color=c["bg_card"], corner_radius=12)
        side_panel.grid(row=0, column=1, sticky="nsew", padx=(15, 30), pady=30)
        side_panel.pack_propagate(False)
        
        ctk.CTkLabel(
            side_panel, text="Scan Log",
            font=theme_manager.font("heading_md"), text_color=c["text_primary"]
        ).pack(anchor="w", padx=20, pady=(20, 10))
        
        # Live clock
        self.lbl_clock = ctk.CTkLabel(
            side_panel, text="00:00:00",
            font=ctk.CTkFont(family="Courier New", size=24, weight="bold"),
            text_color=c["accent"]
        )
        self.lbl_clock.pack(pady=(0, 20))
        
        # Status Box
        self.status_box = ctk.CTkFrame(side_panel, fg_color=c["bg_secondary"], corner_radius=8)
        self.status_box.pack(fill="x", padx=20, pady=(0, 20))
        
        self.lbl_status_icon = ctk.CTkLabel(self.status_box, text="⏳", font=ctk.CTkFont(size=32))
        self.lbl_status_icon.pack(pady=(15, 5))
        
        self.lbl_status_text = ctk.CTkLabel(
            self.status_box, text="Waiting for scan...",
            font=theme_manager.font("body_md"), text_color=c["text_secondary"]
        )
        self.lbl_status_text.pack(pady=(0, 15), padx=10)
        
        # Recent Scans List
        self.scan_list = ctk.CTkScrollableFrame(side_panel, fg_color="transparent")
        self.scan_list.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        # Start Clock Update
        self._update_clock()

    def _update_clock(self):
        self.lbl_clock.configure(text=get_current_time_str())
        self.after(1000, self._update_clock)

    def toggle_camera(self):
        c = theme_manager.colors
        if not self.camera_active:
            # Start
            cam_idx = int(db.get_setting("camera_index", "0"))
            self.cap = cv2.VideoCapture(cam_idx)
            
            if not self.cap.isOpened():
                self.show_status("Camera Error", "❌", c["error"])
                return
                
            self.camera_active = True
            self.btn_toggle_cam.configure(
                text="Stop Camera", fg_color=c["accent_red"], hover_color=c["error"]
            )
            self.lbl_video.configure(text="")
            
            # Pre-load who has been marked today to prevent DB queries on every frame
            today_records = db.get_today_attendance()
            self.marked_today = {r["user_id"] for r in today_records}
            
            self._update_frame()
        else:
            # Stop
            self.camera_active = False
            if self.cap:
                self.cap.release()
            self.btn_toggle_cam.configure(
                text="Start Camera", fg_color=c["accent_green"], hover_color=c["success"]
            )
            self.lbl_video.configure(image=None, text="Camera Offline")
            self.show_status("Waiting for scan...", "⏳", c["text_secondary"])

    def _update_frame(self):
        if not self.camera_active:
            return
            
        ret, frame = self.cap.read()
        if ret:
            # Process recognition every few frames or in a background thread for smooth UI
            # For simplicity and stability, we process in the main thread but can scale down frame
            self.last_results = engine.recognize_faces(frame)
            self._process_results(self.last_results)
            
            # Draw boxes
            annotated = engine.draw_recognition_results(frame, self.last_results, self.marked_today)
            
            # Convert for Tkinter
            rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
            img = PIL.Image.fromarray(rgb)
            
            # Resize to fit frame
            w, h = self.cam_frame.winfo_width(), self.cam_frame.winfo_height()
            if w > 10 and h > 10:
                # Use CTkImage for CustomTkinter
                ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(w, h))
                self.lbl_video.configure(image=ctk_img)
            
        self.after(30, self._update_frame)  # ~30 fps

    def _process_results(self, results):
        """Handle business logic for recognized faces."""
        c = theme_manager.colors
        sound_enabled = db.get_setting("sound_enabled", "true") == "true"
        
        for r in results:
            uid = r["user_id"]
            name = r["name"]
            
            if name == "Unknown":
                self.show_status("Unknown Face Detected", "❓", c["accent_yellow"])
                continue
                
            if uid in self.marked_today:
                # Already marked
                self.show_status(f"{name} (Already Marked)", "✓", c["accent"])
                continue
                
            # Valid new face, attempt to mark
            res = db.mark_attendance(uid)
            if res["success"]:
                self.marked_today.add(uid)
                self.show_status(f"Attendance Marked:\n{name}", "✅", c["success"])
                if sound_enabled: sound_manager.play_success()
                self._add_to_log(name, get_current_time_str(), True)
            elif res["already_marked"]:
                self.marked_today.add(uid) # Cache it
            else:
                self.show_status(f"Error: {res['message']}", "❌", c["error"])

    def show_status(self, text, icon, color):
        self.lbl_status_text.configure(text=text, text_color=color)
        self.lbl_status_icon.configure(text=icon, text_color=color)

    def _add_to_log(self, name, time_str, success):
        c = theme_manager.colors
        color = c["success"] if success else c["error"]
        icon = "✅" if success else "❌"
        
        log_item = ctk.CTkFrame(self.scan_list, fg_color=c["bg_secondary"], corner_radius=6)
        log_item.pack(fill="x", pady=2)
        
        ctk.CTkLabel(log_item, text=icon, text_color=color).pack(side="left", padx=(10, 5), pady=8)
        
        info_frame = ctk.CTkFrame(log_item, fg_color="transparent")
        info_frame.pack(side="left", fill="both", expand=True)
        
        ctk.CTkLabel(info_frame, text=name, font=theme_manager.font("button"), text_color=c["text_primary"]).pack(anchor="w")
        ctk.CTkLabel(info_frame, text=time_str, font=theme_manager.font("caption"), text_color=c["text_muted"]).pack(anchor="w")

    def stop(self):
        """Called when navigating away."""
        if self.camera_active:
            self.toggle_camera()


# ============================================================
# File: ./gui/pages/records.py
# ============================================================

"""
╔══════════════════════════════════════════════════════════════╗
║              RECORDS — Face Attendance System                ║
║  View, filter, and export attendance records                 ║
╚══════════════════════════════════════════════════════════════╝
"""

import customtkinter as ctk
from database.db_manager import db
from utils.helpers import theme_manager, open_file
from datetime import datetime, date

class RecordsPage(ctk.CTkFrame):
    def __init__(self, parent):
        c = theme_manager.colors
        super().__init__(parent, fg_color=c["bg_primary"], corner_radius=0)
        
        self.pack_propagate(False)
        self.records = []
        self._build_ui()
        self.refresh_data()

    def _build_ui(self):
        c = theme_manager.colors
        
        # ── Header & Filters ─────────────────────────────────
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=30, pady=(30, 20))
        
        ctk.CTkLabel(
            header, text="Attendance Records",
            font=theme_manager.font("heading_lg"), text_color=c["text_primary"]
        ).pack(side="left")
        
        # Export Buttons
        btn_frame = ctk.CTkFrame(header, fg_color="transparent")
        btn_frame.pack(side="right")
        
        ctk.CTkButton(
            btn_frame, text="📄 Export CSV", width=120,
            font=theme_manager.font("button"), fg_color=c["bg_hover"], text_color=c["text_primary"],
            command=self._export_csv
        ).pack(side="left", padx=5)
        
        ctk.CTkButton(
            btn_frame, text="📊 Export Excel", width=120,
            font=theme_manager.font("button"), fg_color=c["accent_green"], hover_color=c["success"],
            command=self._export_excel
        ).pack(side="left", padx=5)
        
        # Filters Box
        filter_box = ctk.CTkFrame(self, fg_color=c["bg_card"], corner_radius=8)
        filter_box.pack(fill="x", padx=30, pady=(0, 20))
        
        # Simple Date Filter (Today, All Time)
        self.var_date = ctk.StringVar(value="Today")
        ctk.CTkSegmentedButton(
            filter_box, values=["Today", "Last 7 Days", "This Month", "All Time"],
            variable=self.var_date, command=self._apply_filters
        ).pack(side="left", padx=20, pady=15)
        
        # Refresh Button
        ctk.CTkButton(
            filter_box, text="🔄 Refresh", width=100,
            fg_color="transparent", border_width=1, border_color=c["border"],
            text_color=c["text_primary"], hover_color=c["bg_hover"],
            command=self.refresh_data
        ).pack(side="right", padx=20, pady=15)

        # ── Table Area ───────────────────────────────────────
        table_container = ctk.CTkFrame(self, fg_color=c["bg_card"], corner_radius=12)
        table_container.pack(fill="both", expand=True, padx=30, pady=(0, 30))
        
        # Table Header
        thead = ctk.CTkFrame(table_container, fg_color=c["table_header"], corner_radius=6)
        thead.pack(fill="x", padx=20, pady=(20, 10))
        thead.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        
        headers = ["Date", "Time", "Name", "ID / Roll", "Department", "Status"]
        for i, text in enumerate(headers):
            ctk.CTkLabel(
                thead, text=text, font=theme_manager.font("button"), text_color=c["text_secondary"]
            ).grid(row=0, column=i, padx=10, pady=8, sticky="w")
            
        # Table Body (Scrollable)
        self.tbody = ctk.CTkScrollableFrame(table_container, fg_color="transparent")
        self.tbody.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        self.tbody.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

    def _apply_filters(self, *args):
        self.refresh_data()

    def refresh_data(self):
        for widget in self.tbody.winfo_children():
            widget.destroy()
            
        date_filter = self.var_date.get()
        
        # Compute start/end dates based on selection
        # For simplicity, we just pass string parameters to our db function if needed
        import datetime as dt
        today = dt.date.today()
        
        start_str = None
        end_str = today.strftime("%Y-%m-%d")
        
        if date_filter == "Today":
            start_str = today.strftime("%Y-%m-%d")
        elif date_filter == "Last 7 Days":
            start_str = (today - dt.timedelta(days=7)).strftime("%Y-%m-%d")
        elif date_filter == "This Month":
            start_str = today.replace(day=1).strftime("%Y-%m-%d")
        elif date_filter == "All Time":
            start_str = None
            end_str = None
            
        self.records = db.get_attendance_records(start_date=start_str, end_date=end_str)
        c = theme_manager.colors
        
        if not self.records:
            ctk.CTkLabel(
                self.tbody, text="No records found.",
                text_color=c["text_muted"], font=theme_manager.font("body_md")
            ).grid(row=0, column=0, columnspan=6, pady=40)
            return
            
        for row_idx, r in enumerate(self.records):
            bg = c["table_row"] if row_idx % 2 == 0 else c["table_row_alt"]
            row_frame = ctk.CTkFrame(self.tbody, fg_color=bg, corner_radius=6)
            row_frame.grid(row=row_idx, column=0, columnspan=6, sticky="ew", pady=2)
            row_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
            
            ctk.CTkLabel(row_frame, text=r["date"], text_color=c["text_primary"]).grid(row=0, column=0, padx=10, pady=10, sticky="w")
            ctk.CTkLabel(row_frame, text=r["time"], text_color=c["text_secondary"]).grid(row=0, column=1, padx=10, pady=10, sticky="w")
            ctk.CTkLabel(row_frame, text=r["name"], text_color=c["text_primary"], font=theme_manager.font("button")).grid(row=0, column=2, padx=10, pady=10, sticky="w")
            ctk.CTkLabel(row_frame, text=r["roll_number"], text_color=c["text_secondary"]).grid(row=0, column=3, padx=10, pady=10, sticky="w")
            ctk.CTkLabel(row_frame, text=r["department"], text_color=c["text_secondary"]).grid(row=0, column=4, padx=10, pady=10, sticky="w")
            
            status_color = c["success"] if r["status"] == "Present" else c["error"]
            ctk.CTkLabel(row_frame, text=r["status"], text_color=status_color, font=theme_manager.font("badge")).grid(row=0, column=5, padx=10, pady=10, sticky="w")

    def _export_csv(self):
        path = db.export_to_csv(self.records)
        if path: open_file(path)

    def _export_excel(self):
        path = db.export_to_excel(self.records)
        if path: open_file(path)


# ============================================================
# File: ./gui/pages/__init__.py
# ============================================================

# Pages package


# ============================================================
# File: ./gui/pages/dashboard.py
# ============================================================

"""
╔══════════════════════════════════════════════════════════════╗
║             DASHBOARD — Face Attendance System               ║
║  Home screen with summary cards and recent activity          ║
╚══════════════════════════════════════════════════════════════╝
"""

import customtkinter as ctk
from database.db_manager import db
from utils.helpers import theme_manager, get_current_date_str

class DashboardPage(ctk.CTkFrame):
    def __init__(self, parent):
        c = theme_manager.colors
        super().__init__(parent, fg_color=c["bg_primary"], corner_radius=0)
        
        self.pack_propagate(False)
        self._build_ui()
        self.refresh_data()

    def _build_ui(self):
        c = theme_manager.colors
        
        # ── Header ───────────────────────────────────────────
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=30, pady=(30, 20))
        
        ctk.CTkLabel(
            header, text="Dashboard Overview",
            font=theme_manager.font("heading_lg"), text_color=c["text_primary"]
        ).pack(side="left")
        
        self.date_label = ctk.CTkLabel(
            header, text=get_current_date_str(),
            font=theme_manager.font("body_md"), text_color=c["text_secondary"]
        )
        self.date_label.pack(side="right")
        
        # ── Cards Container ──────────────────────────────────
        cards_frame = ctk.CTkFrame(self, fg_color="transparent")
        cards_frame.pack(fill="x", padx=30, pady=(0, 20))
        cards_frame.grid_columnconfigure((0, 1, 2), weight=1, uniform="card")
        
        # Total Users Card
        self.lbl_total_users = self._create_summary_card(
            cards_frame, "Total Registered", "0", "👤", c["accent_purple"], 0
        )
        
        # Today Present Card
        self.lbl_present = self._create_summary_card(
            cards_frame, "Today's Attendance", "0", "✅", c["accent_green"], 1
        )
        
        # Attendance % Card
        self.lbl_percent = self._create_summary_card(
            cards_frame, "Average Attendance", "0%", "📈", c["accent"], 2
        )
        
        # ── Recent Activity Table ────────────────────────────
        activity_frame = ctk.CTkFrame(self, fg_color=c["bg_card"], corner_radius=12)
        activity_frame.pack(fill="both", expand=True, padx=30, pady=(0, 30))
        
        ctk.CTkLabel(
            activity_frame, text="Recent Scans",
            font=theme_manager.font("heading_md"), text_color=c["text_primary"]
        ).pack(anchor="w", padx=20, pady=(20, 10))
        
        # Table Header
        thead = ctk.CTkFrame(activity_frame, fg_color=c["table_header"], corner_radius=6)
        thead.pack(fill="x", padx=20, pady=(0, 10))
        thead.grid_columnconfigure((0, 1, 2, 3), weight=1)
        
        headers = ["Name", "ID / Roll No", "Department", "Time"]
        for i, text in enumerate(headers):
            ctk.CTkLabel(
                thead, text=text, font=theme_manager.font("button"), text_color=c["text_secondary"]
            ).grid(row=0, column=i, padx=10, pady=8, sticky="w")
            
        # Table Body (Scrollable)
        self.tbody = ctk.CTkScrollableFrame(activity_frame, fg_color="transparent")
        self.tbody.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        self.tbody.grid_columnconfigure((0, 1, 2, 3), weight=1)

    def _create_summary_card(self, parent, title, value, icon, color, col):
        c = theme_manager.colors
        card = ctk.CTkFrame(parent, fg_color=c["bg_card"], corner_radius=12, height=120)
        card.grid(row=0, column=col, padx=10, sticky="nsew")
        card.pack_propagate(False)
        
        # Top border
        border = ctk.CTkFrame(card, fg_color=color, height=4, corner_radius=0)
        border.pack(fill="x", side="top")
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=20, pady=15)
        
        header = ctk.CTkFrame(content, fg_color="transparent")
        header.pack(fill="x")
        
        ctk.CTkLabel(
            header, text=title, font=theme_manager.font("body_md"), text_color=c["text_secondary"]
        ).pack(side="left")
        
        ctk.CTkLabel(
            header, text=icon, font=ctk.CTkFont(size=18), text_color=color
        ).pack(side="right")
        
        value_lbl = ctk.CTkLabel(
            content, text=value, font=theme_manager.font("heading_xl"), text_color=c["text_primary"]
        )
        value_lbl.pack(anchor="w", pady=(10, 0))
        
        return value_lbl

    def refresh_data(self):
        """Fetch latest data from DB and update UI."""
        total = db.get_total_users()
        present = db.get_today_count()
        percent = db.get_attendance_percentage(days=7)
        
        self.lbl_total_users.configure(text=str(total))
        self.lbl_present.configure(text=str(present))
        self.lbl_percent.configure(text=f"{percent}%")
        self.date_label.configure(text=get_current_date_str())
        
        # Update Table
        for widget in self.tbody.winfo_children():
            widget.destroy()
            
        recent = db.get_today_attendance()[:15]  # Top 15 today
        c = theme_manager.colors
        
        if not recent:
            ctk.CTkLabel(
                self.tbody, text="No attendance recorded today.",
                text_color=c["text_muted"], font=theme_manager.font("body_md")
            ).grid(row=0, column=0, columnspan=4, pady=30)
            return
            
        for row_idx, r in enumerate(recent):
            bg = c["table_row"] if row_idx % 2 == 0 else c["table_row_alt"]
            row_frame = ctk.CTkFrame(self.tbody, fg_color=bg, corner_radius=6)
            row_frame.grid(row=row_idx, column=0, columnspan=4, sticky="ew", pady=2)
            row_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
            
            ctk.CTkLabel(row_frame, text=r["name"], text_color=c["text_primary"]).grid(row=0, column=0, padx=10, pady=10, sticky="w")
            ctk.CTkLabel(row_frame, text=r["roll_number"], text_color=c["text_secondary"]).grid(row=0, column=1, padx=10, pady=10, sticky="w")
            ctk.CTkLabel(row_frame, text=r["department"], text_color=c["text_secondary"]).grid(row=0, column=2, padx=10, pady=10, sticky="w")
            ctk.CTkLabel(row_frame, text=r["time"], text_color=c["accent"]).grid(row=0, column=3, padx=10, pady=10, sticky="w")


# ============================================================
# File: ./gui/pages/settings.py
# ============================================================

"""
╔══════════════════════════════════════════════════════════════╗
║              SETTINGS — Face Attendance System               ║
║  App configuration, camera selection, and backups            ║
╚══════════════════════════════════════════════════════════════╝
"""

import customtkinter as ctk
from database.db_manager import db
from face_recognition_engine.recognizer import engine
from utils.helpers import theme_manager, list_available_cameras, open_file

class SettingsPage(ctk.CTkFrame):
    def __init__(self, parent):
        c = theme_manager.colors
        super().__init__(parent, fg_color=c["bg_primary"], corner_radius=0)
        
        self.pack_propagate(False)
        self._build_ui()

    def _build_ui(self):
        c = theme_manager.colors
        
        # Header
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=30, pady=(30, 20))
        ctk.CTkLabel(
            header, text="System Settings",
            font=theme_manager.font("heading_lg"), text_color=c["text_primary"]
        ).pack(side="left")

        # Scrollable container for settings categories
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        # ── General Settings ─────────────────────────────────
        gen_frame = self._create_section(scroll, "General Settings")
        
        # Theme Toggle
        theme_val = db.get_setting("theme", "dark")
        self.sw_theme = ctk.CTkSwitch(gen_frame, text="Dark Mode", font=theme_manager.font("body_md"))
        if theme_val == "dark": self.sw_theme.select()
        self.sw_theme.pack(anchor="w", padx=20, pady=10)
        
        # Sound Toggle
        sound_val = db.get_setting("sound_enabled", "true")
        self.sw_sound = ctk.CTkSwitch(gen_frame, text="Enable Sound Effects", font=theme_manager.font("body_md"))
        if sound_val == "true": self.sw_sound.select()
        self.sw_sound.pack(anchor="w", padx=20, pady=10)

        # ── Hardware Settings ────────────────────────────────
        hw_frame = self._create_section(scroll, "Hardware & Recognition")
        
        # Camera Selection
        cam_frame = ctk.CTkFrame(hw_frame, fg_color="transparent")
        cam_frame.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(cam_frame, text="Active Camera Index", font=theme_manager.font("body_md")).pack(side="left")
        
        cams = [str(i) for i in list_available_cameras()]
        if not cams: cams = ["0"]
        self.cam_combo = ctk.CTkComboBox(cam_frame, values=cams, width=100)
        self.cam_combo.set(db.get_setting("camera_index", "0"))
        self.cam_combo.pack(side="right")
        
        # Recognition Tolerance
        tol_frame = ctk.CTkFrame(hw_frame, fg_color="transparent")
        tol_frame.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(tol_frame, text="Recognition Strictness", font=theme_manager.font("body_md")).pack(side="left")
        
        self.tol_slider = ctk.CTkSlider(tol_frame, from_=0.3, to=0.7, number_of_steps=40)
        self.tol_slider.set(float(db.get_setting("confidence_threshold", "0.55")))
        self.tol_slider.pack(side="right", fill="x", expand=True, padx=(20, 0))

        # ── Data Management ──────────────────────────────────
        data_frame = self._create_section(scroll, "Data & Backup")
        
        # Action Buttons
        btn_container = ctk.CTkFrame(data_frame, fg_color="transparent")
        btn_container.pack(fill="x", padx=20, pady=15)
        
        ctk.CTkButton(
            btn_container, text="Manual Database Backup", 
            fg_color=c["accent"], hover_color=c["accent_hover"],
            command=self._do_backup
        ).pack(side="left", padx=(0, 10))
        
        ctk.CTkButton(
            btn_container, text="Retrain Face Model", 
            fg_color=c["accent_green"], hover_color=c["success"],
            command=self._do_retrain
        ).pack(side="left", padx=10)
        
        # Notification Label
        self.lbl_status = ctk.CTkLabel(data_frame, text="", text_color=c["success"])
        self.lbl_status.pack(pady=5)

        # ── Save Button ──────────────────────────────────────
        save_btn = ctk.CTkButton(
            self, text="Save All Settings", height=45,
            font=theme_manager.font("heading_md"),
            fg_color=c["accent"], hover_color=c["accent_hover"],
            command=self._save_settings
        )
        save_btn.pack(fill="x", padx=30, pady=(0, 30))

    def _create_section(self, parent, title):
        c = theme_manager.colors
        frame = ctk.CTkFrame(parent, fg_color=c["bg_card"], corner_radius=12)
        frame.pack(fill="x", pady=(0, 20))
        ctk.CTkLabel(
            frame, text=title, font=theme_manager.font("heading_md"), text_color=c["text_primary"]
        ).pack(anchor="w", padx=20, pady=(20, 10))
        # Divider
        ctk.CTkFrame(frame, height=1, fg_color=c["border"]).pack(fill="x", padx=20, pady=(0, 10))
        return frame

    def _save_settings(self):
        theme = "dark" if self.sw_theme.get() else "light"
        sound = "true" if self.sw_sound.get() else "false"
        cam_idx = self.cam_combo.get()
        tol = str(round(self.tol_slider.get(), 2))
        
        db.set_setting("theme", theme)
        db.set_setting("sound_enabled", sound)
        db.set_setting("camera_index", cam_idx)
        db.set_setting("confidence_threshold", tol)
        
        engine.set_tolerance(float(tol))
        
        self.lbl_status.configure(text="Settings saved successfully! (Theme changes require restart)")
        self.after(3000, lambda: self.lbl_status.configure(text=""))

    def _do_backup(self):
        path = db.backup_database()
        self.lbl_status.configure(text=f"Backup saved to: {path}")
        
    def _do_retrain(self):
        self.lbl_status.configure(text="Retraining model... Please wait.")
        self.update()
        success = engine.train_model()
        if success:
            self.lbl_status.configure(text="Model retrained successfully.")
        else:
            self.lbl_status.configure(text="Model retraining failed.", text_color=theme_manager.colors["error"])


# ============================================================
# File: ./gui/pages/analytics.py
# ============================================================

"""
╔══════════════════════════════════════════════════════════════╗
║             ANALYTICS — Face Attendance System               ║
║  Visual charts and statistics                                ║
╚══════════════════════════════════════════════════════════════╝
"""

import customtkinter as ctk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from database.db_manager import db
from utils.helpers import theme_manager

class AnalyticsPage(ctk.CTkFrame):
    def __init__(self, parent):
        c = theme_manager.colors
        super().__init__(parent, fg_color=c["bg_primary"], corner_radius=0)
        self.pack_propagate(False)
        self._build_ui()

    def _build_ui(self):
        c = theme_manager.colors
        
        # Header
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=30, pady=(30, 20))
        ctk.CTkLabel(
            header, text="Attendance Analytics",
            font=theme_manager.font("heading_lg"), text_color=c["text_primary"]
        ).pack(side="left")

        # Container for Charts
        charts_frame = ctk.CTkFrame(self, fg_color="transparent")
        charts_frame.pack(fill="both", expand=True, padx=30, pady=(0, 30))
        charts_frame.grid_columnconfigure((0, 1), weight=1, uniform="col")
        charts_frame.grid_rowconfigure(0, weight=1)

        # Chart 1: 7-Day Trend
        trend_card = ctk.CTkFrame(charts_frame, fg_color=c["bg_card"], corner_radius=12)
        trend_card.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        trend_card.pack_propagate(False)
        ctk.CTkLabel(trend_card, text="7-Day Attendance Trend", font=theme_manager.font("heading_md"), text_color=c["text_primary"]).pack(pady=(20, 10))
        
        self.fig_trend = Figure(figsize=(5, 4), dpi=100)
        self.ax_trend = self.fig_trend.add_subplot(111)
        self.canvas_trend = FigureCanvasTkAgg(self.fig_trend, master=trend_card)
        self.canvas_trend.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

        # Chart 2: Department Breakdown
        dept_card = ctk.CTkFrame(charts_frame, fg_color=c["bg_card"], corner_radius=12)
        dept_card.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        dept_card.pack_propagate(False)
        ctk.CTkLabel(dept_card, text="Users by Department", font=theme_manager.font("heading_md"), text_color=c["text_primary"]).pack(pady=(20, 10))
        
        self.fig_dept = Figure(figsize=(5, 4), dpi=100)
        self.ax_dept = self.fig_dept.add_subplot(111)
        self.canvas_dept = FigureCanvasTkAgg(self.fig_dept, master=dept_card)
        self.canvas_dept.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

        self._style_figures()

    def _style_figures(self):
        c = theme_manager.colors
        bg = c["bg_card"]
        text_color = c["text_primary"]

        for fig in [self.fig_trend, self.fig_dept]:
            fig.patch.set_facecolor(bg)
            
        for ax in [self.ax_trend, self.ax_dept]:
            ax.set_facecolor(bg)
            ax.tick_params(colors=text_color)
            for spine in ax.spines.values():
                spine.set_color(c["border"])

    def refresh_data(self):
        c = theme_manager.colors
        self._style_figures()
        
        # Update Trend Chart
        self.ax_trend.clear()
        trend_data = db.get_attendance_trend(7)
        if trend_data:
            dates = [d["date"][-5:] for d in trend_data] # MM-DD
            counts = [d["count"] for d in trend_data]
            
            self.ax_trend.bar(dates, counts, color=c["accent"], alpha=0.8)
            self.ax_trend.set_ylabel("Students Present", color=c["text_secondary"])
        
        self.fig_trend.tight_layout()
        self.canvas_trend.draw()

        # Update Department Chart
        self.ax_dept.clear()
        users = db.get_all_users()
        if users:
            dept_counts = {}
            for u in users:
                dept_counts[u["department"]] = dept_counts.get(u["department"], 0) + 1
                
            labels = list(dept_counts.keys())
            sizes = list(dept_counts.values())
            
            # Use chart colors from theme
            chart_colors = c.get("chart_colors", ["#2188FF", "#3FB950", "#BC8CFF", "#D29922", "#F85149"])
            
            self.ax_dept.pie(
                sizes, labels=labels, colors=chart_colors,
                autopct='%1.1f%%', startangle=90,
                textprops={'color': c["text_primary"]}
            )
            self.ax_dept.axis('equal')
            
        self.fig_dept.tight_layout()
        self.canvas_dept.draw()
