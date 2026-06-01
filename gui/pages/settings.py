"""
╔══════════════════════════════════════════════════════════════╗
║              SETTINGS — Face Attendance System              ║
║  App configuration, camera selection, and backups           ║
╚══════════════════════════════════════════════════════════════╝
"""

import customtkinter as ctk
from database.db_manager import db
from face_recognition_engine.recognizer import engine
from utils.helpers import theme_manager, list_available_cameras, open_file

class SettingsPage(ctk.CTkFrame):
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
            header, text="System Settings",
            font=theme_manager.font("heading_lg"), text_color=c["text_primary"]
        ).pack(side="left")

        # Scrollable container for settings categories
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        # ── General Settings ─────────────────────────────────
        gen_frame = self._create_section(scroll, "General Settings")
        
        # Theme Toggle
        theme_val = db.get_setting("theme", "dark")
        self.sw_theme = ctk.CTkSwitch(gen_frame, text="Dark Mode", font=theme_manager.font("body_md"))
        if theme_val == "dark": self.sw_theme.select()
        self.sw_theme.pack(anchor="w", padx=20, pady=10)
        
        # Sound Toggle
        sound_val = db.get_setting("sound_enabled", "true")
        self.sw_sound = ctk.CTkSwitch(gen_frame, text="Enable Sound Effects", font=theme_manager.font("body_md"))
        if sound_val == "true": self.sw_sound.select()
        self.sw_sound.pack(anchor="w", padx=20, pady=10)

        # ── Hardware Settings ────────────────────────────────
        hw_frame = self._create_section(scroll, "Hardware & Recognition")
        
        # Camera Selection
        cam_frame = ctk.CTkFrame(hw_frame, fg_color="transparent")
        cam_frame.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(cam_frame, text="Active Camera Index", font=theme_manager.font("body_md")).pack(side="left")
        
        cams = [str(i) for i in list_available_cameras()]
        if not cams: cams = ["0"]
        self.cam_combo = ctk.CTkComboBox(cam_frame, values=cams, width=100)
        self.cam_combo.set(db.get_setting("camera_index", "0"))
        self.cam_combo.pack(side="right")
        
        # Recognition Tolerance
        tol_frame = ctk.CTkFrame(hw_frame, fg_color="transparent")
        tol_frame.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(tol_frame, text="Recognition Strictness", font=theme_manager.font("body_md")).pack(side="left")
        
        self.tol_slider = ctk.CTkSlider(tol_frame, from_=0.3, to=0.7, number_of_steps=40)
        self.tol_slider.set(float(db.get_setting("confidence_threshold", "0.55")))
        self.tol_slider.pack(side="right", fill="x", expand=True, padx=(20, 0))

        # ── Data Management ──────────────────────────────────
        data_frame = self._create_section(scroll, "Data & Backup")
        
        # Action Buttons
        btn_container = ctk.CTkFrame(data_frame, fg_color="transparent")
        btn_container.pack(fill="x", padx=20, pady=15)
        
        ctk.CTkButton(
            btn_container, text="Manual Database Backup", 
            fg_color=c["accent"], hover_color=c["accent_hover"],
            command=self._do_backup
        ).pack(side="left", padx=(0, 10))
        
        ctk.CTkButton(
            btn_container, text="Retrain Face Model", 
            fg_color=c["accent_green"], hover_color=c["success"],
            command=self._do_retrain
        ).pack(side="left", padx=10)
        
        # Notification Label
        self.lbl_status = ctk.CTkLabel(data_frame, text="", text_color=c["success"])
        self.lbl_status.pack(pady=5)

        # ── Save Button ──────────────────────────────────────
        save_btn = ctk.CTkButton(
            self, text="Save All Settings", height=45,
            font=theme_manager.font("heading_md"),
            fg_color=c["accent"], hover_color=c["accent_hover"],
            command=self._save_settings
        )
        save_btn.pack(fill="x", padx=30, pady=(0, 30))

    def _create_section(self, parent, title):
        c = theme_manager.colors
        frame = ctk.CTkFrame(parent, fg_color=c["bg_card"], corner_radius=12)
        frame.pack(fill="x", pady=(0, 20))
        ctk.CTkLabel(
            frame, text=title, font=theme_manager.font("heading_md"), text_color=c["text_primary"]
        ).pack(anchor="w", padx=20, pady=(20, 10))
        # Divider
        ctk.CTkFrame(frame, height=1, fg_color=c["border"]).pack(fill="x", padx=20, pady=(0, 10))
        return frame

    def _save_settings(self):
        theme = "dark" if self.sw_theme.get() else "light"
        sound = "true" if self.sw_sound.get() else "false"
        cam_idx = self.cam_combo.get()
        tol = str(round(self.tol_slider.get(), 2))
        
        db.set_setting("theme", theme)
        db.set_setting("sound_enabled", sound)
        db.set_setting("camera_index", cam_idx)
        db.set_setting("confidence_threshold", tol)
        
        engine.set_tolerance(float(tol))
        
        self.lbl_status.configure(text="Settings saved successfully! (Theme changes require restart)")
        self.after(3000, lambda: self.lbl_status.configure(text=""))

    def _do_backup(self):
        path = db.backup_database()
        self.lbl_status.configure(text=f"Backup saved to: {path}")
        
    def _do_retrain(self):
        self.lbl_status.configure(text="Retraining model... Please wait.")
        self.update()
        success = engine.train_model()
        if success:
            self.lbl_status.configure(text="Model retrained successfully.")
        else:
            self.lbl_status.configure(text="Model retraining failed.", text_color=theme_manager.colors["error"])
