# Made by Harsh Bardhan Kumar and Team
"""
╔══════════════════════════════════════════════════════════════╗
║              REGISTER — Face Attendance System              ║
║  Add new users and capture training face images             ║
╚══════════════════════════════════════════════════════════════╝
"""

import customtkinter as ctk
import cv2
import PIL.Image, PIL.ImageTk
import threading
from database.db_manager import db
from face_recognition_engine.recognizer import engine
from utils.helpers import theme_manager, validate_user_input

class RegisterPage(ctk.CTkFrame):
    def __init__(self, parent):
        c = theme_manager.colors
        super().__init__(parent, fg_color=c["bg_primary"], corner_radius=0)
        
        self.pack_propagate(False)
        self.is_capturing = False
        self._build_ui()

    def _build_ui(self):
        c = theme_manager.colors
        
        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=6)
        self.grid_rowconfigure(0, weight=1)
        
        # ── Left: Form ───────────────────────────────────────
        form_panel = ctk.CTkFrame(self, fg_color=c["bg_card"], corner_radius=12)
        form_panel.grid(row=0, column=0, sticky="nsew", padx=(30, 15), pady=30)
        form_panel.pack_propagate(False)
        
        ctk.CTkLabel(
            form_panel, text="New User Registration",
            font=theme_manager.font("heading_lg"), text_color=c["text_primary"]
        ).pack(anchor="w", padx=25, pady=(25, 20))
        
        # Inputs
        self.ent_name = self._create_input(form_panel, "Full Name *", "e.g. John Doe")
        self.ent_roll = self._create_input(form_panel, "ID / Roll Number *", "e.g. EMP-101")
        
        # Department dropdown (fetch existing or allow new)
        dept_frame = ctk.CTkFrame(form_panel, fg_color="transparent")
        dept_frame.pack(fill="x", padx=25, pady=10)
        ctk.CTkLabel(dept_frame, text="Department / Class *", font=theme_manager.font("button"), text_color=c["text_secondary"]).pack(anchor="w", pady=(0, 5))
        
        depts = db.get_departments()
        if not depts: depts = ["IT", "HR", "Engineering", "Sales"]
        self.ent_dept = ctk.CTkComboBox(dept_frame, values=depts, height=40, font=theme_manager.font("body_md"))
        self.ent_dept.pack(fill="x")
        
        self.ent_email = self._create_input(form_panel, "Email Address", "Optional")
        self.ent_phone = self._create_input(form_panel, "Phone Number", "Optional")
        
        # Error Label
        self.lbl_error = ctk.CTkLabel(form_panel, text="", text_color=c["error"], font=theme_manager.font("body_sm"))
        self.lbl_error.pack(pady=10)
        
        # Buttons
        self.btn_capture = ctk.CTkButton(
            form_panel, text="Start Capture & Train", height=45,
            font=theme_manager.font("heading_md"), fg_color=c["accent"], hover_color=c["accent_hover"],
            command=self._start_registration
        )
        self.btn_capture.pack(fill="x", padx=25, pady=(10, 10))

        # ── Right: Preview & Progress ────────────────────────
        preview_panel = ctk.CTkFrame(self, fg_color="transparent")
        preview_panel.grid(row=0, column=1, sticky="nsew", padx=(15, 30), pady=30)
        preview_panel.pack_propagate(False)
        
        # Camera display label
        self.cam_frame = ctk.CTkFrame(preview_panel, fg_color="#000000", corner_radius=12)
        self.cam_frame.pack(fill="both", expand=True, pady=(0, 20))
        self.cam_frame.pack_propagate(False)
        
        self.lbl_video = ctk.CTkLabel(self.cam_frame, text="Camera Preview", text_color="#555555")
        self.lbl_video.pack(expand=True)
        
        # Progress UI
        self.progress_frame = ctk.CTkFrame(preview_panel, fg_color=c["bg_card"], corner_radius=12, height=120)
        self.progress_frame.pack(fill="x")
        self.progress_frame.pack_propagate(False)
        
        self.lbl_status = ctk.CTkLabel(self.progress_frame, text="Ready", font=theme_manager.font("body_lg"), text_color=c["text_primary"])
        self.lbl_status.pack(pady=(20, 10))
        
        self.progress_bar = ctk.CTkProgressBar(self.progress_frame, mode="determinate", height=8, fg_color=c["bg_secondary"], progress_color=c["accent"])
        self.progress_bar.pack(fill="x", padx=30)
        self.progress_bar.set(0)

    def _create_input(self, parent, label, placeholder):
        c = theme_manager.colors
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", padx=25, pady=10)
        
        ctk.CTkLabel(frame, text=label, font=theme_manager.font("button"), text_color=c["text_secondary"]).pack(anchor="w", pady=(0, 5))
        ent = ctk.CTkEntry(frame, placeholder_text=placeholder, height=40, font=theme_manager.font("body_md"))
        ent.pack(fill="x")
        return ent

    def _start_registration(self):
        if self.is_capturing:
            return
            
        # 1. Validate
        name = self.ent_name.get().strip()
        roll = self.ent_roll.get().strip()
        dept = self.ent_dept.get().strip()
        
        is_valid, err = validate_user_input(name, roll, dept)
        if not is_valid:
            self.lbl_error.configure(text=err)
            return
            
        self.lbl_error.configure(text="")
        
        # 2. Check if user exists
        if db.get_user_by_roll(roll):
            self.lbl_error.configure(text="User with this ID already exists.")
            return

        # 3. Add to DB
        uid = db.add_user(
            name=name, roll_number=roll, department=dept,
            email=self.ent_email.get(), phone=self.ent_phone.get()
        )
        if uid == -1:
            self.lbl_error.configure(text="Database error. Check logs.")
            return

        # 4. Start Capture & Train Thread
        self.is_capturing = True
        self._set_ui_state("disabled")
        self.progress_bar.set(0)
        self.lbl_status.configure(text="Capturing face images... Please look at the camera.")
        
        threading.Thread(target=self._capture_process, args=(uid, name), daemon=True).start()

    def _capture_process(self, uid, name):
        cam_idx = int(db.get_setting("camera_index", "0"))
        
        # Capture
        success = engine.capture_face_images(
            user_id=uid,
            user_name=name,
            num_images=30,
            camera_index=cam_idx,
            progress_callback=self._update_progress,
            frame_callback=self._update_preview
        )
        
        if success:
            self.after(0, lambda: self.lbl_status.configure(text="Training model... This may take a minute."))
            self.after(0, lambda: self.progress_bar.set(0))
            
            # Train
            train_success = engine.train_model(progress_callback=self._update_train_progress)
            
            if train_success:
                self.after(0, lambda: self._registration_complete(True, "Registration and Training Successful!"))
            else:
                self.after(0, lambda: self._registration_complete(False, "Training failed. Please try again."))
        else:
            self.after(0, lambda: self._registration_complete(False, "Capture failed. No faces detected."))

    def _update_progress(self, current, total):
        pct = current / total
        self.after(0, lambda: self.progress_bar.set(pct))
        
    def _update_train_progress(self, current, total):
        pct = current / total if total > 0 else 0
        self.after(0, lambda: self.progress_bar.set(pct))

    def _update_preview(self, frame):
        # Pass a copy of the frame to the main thread safely
        self.after(0, self._process_preview_frame, frame.copy())
            
    def _process_preview_frame(self, frame):
        try:
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = PIL.Image.fromarray(rgb)
            w, h = self.cam_frame.winfo_width(), self.cam_frame.winfo_height()
            if w > 10 and h > 10:
                ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(w, h))
                self.lbl_video.configure(image=ctk_img)
        except Exception:
            pass

    def _registration_complete(self, success, msg):
        self.is_capturing = False
        self._set_ui_state("normal")
        c = theme_manager.colors
        
        if success:
            self.lbl_status.configure(text=msg, text_color=c["success"])
            self.progress_bar.set(1.0)
            self._clear_form()
        else:
            self.lbl_status.configure(text=msg, text_color=c["error"])
            
        self.lbl_video.configure(image=None, text="Camera Preview")

    def _set_ui_state(self, state):
        self.ent_name.configure(state=state)
        self.ent_roll.configure(state=state)
        self.ent_dept.configure(state=state)
        self.ent_email.configure(state=state)
        self.ent_phone.configure(state=state)
        self.btn_capture.configure(state=state)

    def _clear_form(self):
        self.ent_name.delete(0, 'end')
        self.ent_roll.delete(0, 'end')
        self.ent_email.delete(0, 'end')
        self.ent_phone.delete(0, 'end')
