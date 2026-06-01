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
