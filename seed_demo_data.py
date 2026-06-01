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
