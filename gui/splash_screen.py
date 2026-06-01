# Made by Harsh Bardhan Kumar and Team
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
        ctk.CTkLabel(main, text="Smart Attendance System",
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
