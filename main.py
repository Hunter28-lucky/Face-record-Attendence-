# Made by Harsh Bardhan Kumar and Team
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
        self.title("FaceTrack Pro — Attendance System")
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
