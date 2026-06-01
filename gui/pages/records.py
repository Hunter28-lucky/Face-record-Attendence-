# Made by Harsh Bardhan Kumar and Team
"""
╔══════════════════════════════════════════════════════════════╗
║              RECORDS — Face Attendance System               ║
║  View, filter, and export attendance records                ║
╚══════════════════════════════════════════════════════════════╝
"""

import customtkinter as ctk
from database.db_manager import db
from utils.helpers import theme_manager, open_file
from datetime import datetime, date

class RecordsPage(ctk.CTkFrame):
    def __init__(self, parent):
        c = theme_manager.colors
        super().__init__(parent, fg_color=c["bg_primary"], corner_radius=0)
        
        self.pack_propagate(False)
        self.records = []
        self._build_ui()
        self.refresh_data()

    def _build_ui(self):
        c = theme_manager.colors
        
        # ── Header & Filters ─────────────────────────────────
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=30, pady=(30, 20))
        
        ctk.CTkLabel(
            header, text="Attendance Records",
            font=theme_manager.font("heading_lg"), text_color=c["text_primary"]
        ).pack(side="left")
        
        # Export Buttons
        btn_frame = ctk.CTkFrame(header, fg_color="transparent")
        btn_frame.pack(side="right")
        
        ctk.CTkButton(
            btn_frame, text="📄 Export CSV", width=120,
            font=theme_manager.font("button"), fg_color=c["bg_hover"], text_color=c["text_primary"],
            command=self._export_csv
        ).pack(side="left", padx=5)
        
        ctk.CTkButton(
            btn_frame, text="📊 Export Excel", width=120,
            font=theme_manager.font("button"), fg_color=c["accent_green"], hover_color=c["success"],
            command=self._export_excel
        ).pack(side="left", padx=5)
        
        # Filters Box
        filter_box = ctk.CTkFrame(self, fg_color=c["bg_card"], corner_radius=8)
        filter_box.pack(fill="x", padx=30, pady=(0, 20))
        
        # Simple Date Filter (Today, All Time)
        self.var_date = ctk.StringVar(value="Today")
        ctk.CTkSegmentedButton(
            filter_box, values=["Today", "Last 7 Days", "This Month", "All Time"],
            variable=self.var_date, command=self._apply_filters
        ).pack(side="left", padx=20, pady=15)
        
        # Refresh Button
        ctk.CTkButton(
            filter_box, text="🔄 Refresh", width=100,
            fg_color="transparent", border_width=1, border_color=c["border"],
            text_color=c["text_primary"], hover_color=c["bg_hover"],
            command=self.refresh_data
        ).pack(side="right", padx=20, pady=15)

        # ── Table Area ───────────────────────────────────────
        table_container = ctk.CTkFrame(self, fg_color=c["bg_card"], corner_radius=12)
        table_container.pack(fill="both", expand=True, padx=30, pady=(0, 30))
        
        # Table Header
        thead = ctk.CTkFrame(table_container, fg_color=c["table_header"], corner_radius=6)
        thead.pack(fill="x", padx=20, pady=(20, 10))
        thead.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        
        headers = ["Date", "Time", "Name", "ID / Roll", "Department", "Status"]
        for i, text in enumerate(headers):
            ctk.CTkLabel(
                thead, text=text, font=theme_manager.font("button"), text_color=c["text_secondary"]
            ).grid(row=0, column=i, padx=10, pady=8, sticky="w")
            
        # Table Body (Scrollable)
        self.tbody = ctk.CTkScrollableFrame(table_container, fg_color="transparent")
        self.tbody.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        self.tbody.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

    def _apply_filters(self, *args):
        self.refresh_data()

    def refresh_data(self):
        for widget in self.tbody.winfo_children():
            widget.destroy()
            
        date_filter = self.var_date.get()
        
        # Compute start/end dates based on selection
        # For simplicity, we just pass string parameters to our db function if needed
        import datetime as dt
        today = dt.date.today()
        
        start_str = None
        end_str = today.strftime("%Y-%m-%d")
        
        if date_filter == "Today":
            start_str = today.strftime("%Y-%m-%d")
        elif date_filter == "Last 7 Days":
            start_str = (today - dt.timedelta(days=7)).strftime("%Y-%m-%d")
        elif date_filter == "This Month":
            start_str = today.replace(day=1).strftime("%Y-%m-%d")
        elif date_filter == "All Time":
            start_str = None
            end_str = None
            
        self.records = db.get_attendance_records(start_date=start_str, end_date=end_str)
        c = theme_manager.colors
        
        if not self.records:
            ctk.CTkLabel(
                self.tbody, text="No records found.",
                text_color=c["text_muted"], font=theme_manager.font("body_md")
            ).grid(row=0, column=0, columnspan=6, pady=40)
            return
            
        for row_idx, r in enumerate(self.records):
            bg = c["table_row"] if row_idx % 2 == 0 else c["table_row_alt"]
            row_frame = ctk.CTkFrame(self.tbody, fg_color=bg, corner_radius=6)
            row_frame.grid(row=row_idx, column=0, columnspan=6, sticky="ew", pady=2)
            row_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
            
            ctk.CTkLabel(row_frame, text=r["date"], text_color=c["text_primary"]).grid(row=0, column=0, padx=10, pady=10, sticky="w")
            ctk.CTkLabel(row_frame, text=r["time"], text_color=c["text_secondary"]).grid(row=0, column=1, padx=10, pady=10, sticky="w")
            ctk.CTkLabel(row_frame, text=r["name"], text_color=c["text_primary"], font=theme_manager.font("button")).grid(row=0, column=2, padx=10, pady=10, sticky="w")
            ctk.CTkLabel(row_frame, text=r["roll_number"], text_color=c["text_secondary"]).grid(row=0, column=3, padx=10, pady=10, sticky="w")
            ctk.CTkLabel(row_frame, text=r["department"], text_color=c["text_secondary"]).grid(row=0, column=4, padx=10, pady=10, sticky="w")
            
            status_color = c["success"] if r["status"] == "Present" else c["error"]
            ctk.CTkLabel(row_frame, text=r["status"], text_color=status_color, font=theme_manager.font("badge")).grid(row=0, column=5, padx=10, pady=10, sticky="w")

    def _export_csv(self):
        path = db.export_to_csv(self.records)
        if path: open_file(path)

    def _export_excel(self):
        path = db.export_to_excel(self.records)
        if path: open_file(path)
