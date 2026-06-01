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

## 🚀 One-Click Quick Start (All Platforms)

Running **FaceTrack Pro** is now entirely automated. The unified `launch.py` script automatically handles virtual environment creation, checks and installs dependencies, seeds demo data if the database is empty, and starts the application.

### Step 1 — Prerequisites
Install **CMake** (required to compile the `face_recognition` library if not already compiled on your system):
```bash
# macOS
brew install cmake

# Ubuntu / Debian
sudo apt install cmake build-essential
```
*(Windows users: download and run the installer from [cmake.org](https://cmake.org/download/) and select "Add to system PATH")*

### Step 2 — Run in One Go!
Simply run the bootstrapper script from the project root:

```bash
# macOS / Linux / Git Bash
python3 launch.py

# Windows Command Prompt / PowerShell
python launch.py
```

That's it! The launcher will take care of the rest and pop up the application window on your screen.

---

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
