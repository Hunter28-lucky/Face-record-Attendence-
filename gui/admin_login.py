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
