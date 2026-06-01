# Made by Harsh Bardhan Kumar and Team
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
        except sqlite3.IntegrityError as e:
            err_msg = str(e).lower()
            if "foreign key" in err_msg:
                logger.error(f"Foreign Key violation for user_id {user_id}: {e}")
                return {"success": False,
                        "message": f"User ID {user_id} does not exist in the database.",
                        "already_marked": False}
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
