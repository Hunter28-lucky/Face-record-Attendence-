"""
╔══════════════════════════════════════════════════════════════╗
║             ANALYTICS — Face Attendance System              ║
║  Visual charts and statistics                               ║
╚══════════════════════════════════════════════════════════════╝
"""

import customtkinter as ctk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from database.db_manager import db
from utils.helpers import theme_manager

class AnalyticsPage(ctk.CTkFrame):
    def __init__(self, parent):
        c = theme_manager.colors
        super().__init__(parent, fg_color=c["bg_primary"], corner_radius=0)
        self.pack_propagate(False)
        self._build_ui()

    def _build_ui(self):
        c = theme_manager.colors
        
        # Header
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=30, pady=(30, 20))
        ctk.CTkLabel(
            header, text="Attendance Analytics",
            font=theme_manager.font("heading_lg"), text_color=c["text_primary"]
        ).pack(side="left")

        # Container for Charts
        charts_frame = ctk.CTkFrame(self, fg_color="transparent")
        charts_frame.pack(fill="both", expand=True, padx=30, pady=(0, 30))
        charts_frame.grid_columnconfigure((0, 1), weight=1, uniform="col")
        charts_frame.grid_rowconfigure(0, weight=1)

        # Chart 1: 7-Day Trend
        trend_card = ctk.CTkFrame(charts_frame, fg_color=c["bg_card"], corner_radius=12)
        trend_card.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        trend_card.pack_propagate(False)
        ctk.CTkLabel(trend_card, text="7-Day Attendance Trend", font=theme_manager.font("heading_md"), text_color=c["text_primary"]).pack(pady=(20, 10))
        
        self.fig_trend = Figure(figsize=(5, 4), dpi=100)
        self.ax_trend = self.fig_trend.add_subplot(111)
        self.canvas_trend = FigureCanvasTkAgg(self.fig_trend, master=trend_card)
        self.canvas_trend.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

        # Chart 2: Department Breakdown
        dept_card = ctk.CTkFrame(charts_frame, fg_color=c["bg_card"], corner_radius=12)
        dept_card.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        dept_card.pack_propagate(False)
        ctk.CTkLabel(dept_card, text="Users by Department", font=theme_manager.font("heading_md"), text_color=c["text_primary"]).pack(pady=(20, 10))
        
        self.fig_dept = Figure(figsize=(5, 4), dpi=100)
        self.ax_dept = self.fig_dept.add_subplot(111)
        self.canvas_dept = FigureCanvasTkAgg(self.fig_dept, master=dept_card)
        self.canvas_dept.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

        self._style_figures()

    def _style_figures(self):
        c = theme_manager.colors
        bg = c["bg_card"]
        text_color = c["text_primary"]

        for fig in [self.fig_trend, self.fig_dept]:
            fig.patch.set_facecolor(bg)
            
        for ax in [self.ax_trend, self.ax_dept]:
            ax.set_facecolor(bg)
            ax.tick_params(colors=text_color)
            for spine in ax.spines.values():
                spine.set_color(c["border"])

    def refresh_data(self):
        c = theme_manager.colors
        self._style_figures()
        
        # Update Trend Chart
        self.ax_trend.clear()
        trend_data = db.get_attendance_trend(7)
        if trend_data:
            dates = [d["date"][-5:] for d in trend_data] # MM-DD
            counts = [d["count"] for d in trend_data]
            
            self.ax_trend.bar(dates, counts, color=c["accent"], alpha=0.8)
            self.ax_trend.set_ylabel("Students Present", color=c["text_secondary"])
        
        self.fig_trend.tight_layout()
        self.canvas_trend.draw()

        # Update Department Chart
        self.ax_dept.clear()
        users = db.get_all_users()
        if users:
            dept_counts = {}
            for u in users:
                dept_counts[u["department"]] = dept_counts.get(u["department"], 0) + 1
                
            labels = list(dept_counts.keys())
            sizes = list(dept_counts.values())
            
            # Use chart colors from theme
            chart_colors = c.get("chart_colors", ["#2188FF", "#3FB950", "#BC8CFF", "#D29922", "#F85149"])
            
            self.ax_dept.pie(
                sizes, labels=labels, colors=chart_colors,
                autopct='%1.1f%%', startangle=90,
                textprops={'color': c["text_primary"]}
            )
            self.ax_dept.axis('equal')
            
        self.fig_dept.tight_layout()
        self.canvas_dept.draw()
