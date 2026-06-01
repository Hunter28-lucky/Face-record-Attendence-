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
