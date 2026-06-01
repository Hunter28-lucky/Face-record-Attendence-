"""
╔══════════════════════════════════════════════════════════════╗
║             DASHBOARD — Face Attendance System              ║
║  Home screen with summary cards and recent activity         ║
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
