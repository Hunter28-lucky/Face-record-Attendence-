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
