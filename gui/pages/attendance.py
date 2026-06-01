# Made by Harsh Bardhan Kumar and Team
"""
╔══════════════════════════════════════════════════════════════╗
║             ATTENDANCE — Face Attendance System             ║
║  Live webcam feed and real-time face recognition scanning   ║
╚══════════════════════════════════════════════════════════════╝
"""

import customtkinter as ctk
import cv2
import PIL.Image, PIL.ImageTk
from database.db_manager import db
from face_recognition_engine.recognizer import engine
from utils.helpers import theme_manager, sound_manager, get_current_time_str
import threading

class AttendancePage(ctk.CTkFrame):
    def __init__(self, parent):
        c = theme_manager.colors
        super().__init__(parent, fg_color=c["bg_primary"], corner_radius=0)
        
        self.pack_propagate(False)
        self.camera_active = False
        self.cap = None
        self.marked_today = set()  # Cache to prevent DB spam
        self.last_results = []
        self.ctk_img = None        # Persistent reference to reuse image container and prevent TclErrors
        
        # Threading support for asynchronous processing
        self.processing_lock = threading.Lock()
        self.next_frame_to_process = None
        self.is_processing = False
        
        self._build_ui()

    def _build_ui(self):
        c = theme_manager.colors
        
        # ── Main Layout ──────────────────────────────────────
        self.grid_columnconfigure(0, weight=7)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)
        
        # ── Left: Camera View ────────────────────────────────
        cam_container = ctk.CTkFrame(self, fg_color="transparent")
        cam_container.grid(row=0, column=0, sticky="nsew", padx=(30, 15), pady=30)
        cam_container.pack_propagate(False)
        
        header = ctk.CTkFrame(cam_container, fg_color="transparent")
        header.pack(fill="x", pady=(0, 15))
        
        ctk.CTkLabel(
            header, text="Live Scanner",
            font=theme_manager.font("heading_lg"), text_color=c["text_primary"]
        ).pack(side="left")
        
        self.btn_toggle_cam = ctk.CTkButton(
            header, text="Start Camera",
            font=theme_manager.font("button"),
            fg_color=c["accent_green"], hover_color=c["success"],
            command=self.toggle_camera
        )
        self.btn_toggle_cam.pack(side="right")
        
        # Camera display label
        self.cam_frame = ctk.CTkFrame(cam_container, fg_color="#000000", corner_radius=12)
        self.cam_frame.pack(fill="both", expand=True)
        self.cam_frame.pack_propagate(False)
        
        self.lbl_video = ctk.CTkLabel(self.cam_frame, text="Camera Offline", text_color="#555555")
        self.lbl_video.pack(expand=True)
        
        # ── Right: Status & Logs ─────────────────────────────
        side_panel = ctk.CTkFrame(self, fg_color=c["bg_card"], corner_radius=12)
        side_panel.grid(row=0, column=1, sticky="nsew", padx=(15, 30), pady=30)
        side_panel.pack_propagate(False)
        
        ctk.CTkLabel(
            side_panel, text="Scan Log",
            font=theme_manager.font("heading_md"), text_color=c["text_primary"]
        ).pack(anchor="w", padx=20, pady=(20, 10))
        
        # Live clock
        self.lbl_clock = ctk.CTkLabel(
            side_panel, text="00:00:00",
            font=ctk.CTkFont(family="Courier New", size=24, weight="bold"),
            text_color=c["accent"]
        )
        self.lbl_clock.pack(pady=(0, 20))
        
        # Status Box
        self.status_box = ctk.CTkFrame(side_panel, fg_color=c["bg_secondary"], corner_radius=8)
        self.status_box.pack(fill="x", padx=20, pady=(0, 20))
        
        self.lbl_status_icon = ctk.CTkLabel(self.status_box, text="⏳", font=ctk.CTkFont(size=32))
        self.lbl_status_icon.pack(pady=(15, 5))
        
        self.lbl_status_text = ctk.CTkLabel(
            self.status_box, text="Waiting for scan...",
            font=theme_manager.font("body_md"), text_color=c["text_secondary"]
        )
        self.lbl_status_text.pack(pady=(0, 15), padx=10)
        
        # Recent Scans List
        self.scan_list = ctk.CTkScrollableFrame(side_panel, fg_color="transparent")
        self.scan_list.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        # Start Clock Update
        self._update_clock()

    def _update_clock(self):
        self.lbl_clock.configure(text=get_current_time_str())
        self.after(1000, self._update_clock)

    def toggle_camera(self):
        c = theme_manager.colors
        if not self.camera_active:
            # Start
            cam_idx = int(db.get_setting("camera_index", "0"))
            self.cap = cv2.VideoCapture(cam_idx)
            
            if not self.cap.isOpened():
                self.show_status("Camera Error", "❌", c["error"])
                return
                
            self.camera_active = True
            self.btn_toggle_cam.configure(
                text="Stop Camera", fg_color=c["accent_red"], hover_color=c["error"]
            )
            
            # Safely clear old image references to avoid TclErrors
            try:
                self.lbl_video.configure(image="", text="")
            except Exception:
                try:
                    self.lbl_video.configure(image=None, text="")
                except Exception:
                    pass
            self.ctk_img = None
            
            # Reset processing state
            self.next_frame_to_process = None
            self.is_processing = False
            
            # Pre-load who has been marked today to prevent DB queries on every frame
            today_records = db.get_today_attendance()
            self.marked_today = {r["user_id"] for r in today_records}
            
            self._update_frame()
        else:
            # Stop
            self.camera_active = False
            if self.cap:
                self.cap.release()
            self.btn_toggle_cam.configure(
                text="Start Camera", fg_color=c["accent_green"], hover_color=c["success"]
            )
            
            # Safely remove image reference before garbage collecting the CTkImage
            try:
                self.lbl_video.configure(image="", text="Camera Offline")
            except Exception:
                try:
                    self.lbl_video.configure(image=None, text="Camera Offline")
                except Exception:
                    pass
            
            self.ctk_img = None
            self.show_status("Waiting for scan...", "⏳", c["text_secondary"])
            self.next_frame_to_process = None
            self.is_processing = False

    def _update_frame(self):
        if not self.camera_active:
            return
            
        ret, frame = self.cap.read()
        if ret:
            # Queue frame for background recognition
            with self.processing_lock:
                self.next_frame_to_process = frame.copy()
            
            # Launch background thread if not already running
            if not self.is_processing:
                self.is_processing = True
                threading.Thread(target=self._background_recognition, daemon=True).start()
            
            # Draw boxes using the latest available/cached recognition results
            annotated = engine.draw_recognition_results(frame, self.last_results, self.marked_today)
            
            # Convert for Tkinter
            rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
            img = PIL.Image.fromarray(rgb)
            
            # Resize to fit frame
            w, h = self.cam_frame.winfo_width(), self.cam_frame.winfo_height()
            if w > 10 and h > 10:
                if self.ctk_img is None:
                    self.ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(w, h))
                    self.lbl_video.configure(image=self.ctk_img)
                else:
                    self.ctk_img.configure(light_image=img, dark_image=img, size=(w, h))
            
        # Run webcam acquisition rapidly for buttery smooth GUI rendering
        self.after(20, self._update_frame)

    def _background_recognition(self):
        """Asynchronous worker for background face recognition processing."""
        import time
        while self.camera_active:
            frame_to_process = None
            with self.processing_lock:
                if self.next_frame_to_process is not None:
                    frame_to_process = self.next_frame_to_process
                    self.next_frame_to_process = None
            
            if frame_to_process is None:
                time.sleep(0.01)
                continue
                
            # Perform expensive face recognition processing in background thread
            results = engine.recognize_faces(frame_to_process)
            
            # Marshall results back to the GUI main thread safely
            self.after(0, lambda r=results: self._process_recognition_results(r))
            
            # Limit background recognition throughput (to 10 checks per second max) to prevent CPU starvation
            time.sleep(0.1)
            
        self.is_processing = False

    def _process_recognition_results(self, results):
        """Callback executed on the GUI thread to handle completed recognition results."""
        self.last_results = results
        self._process_results(results)

    def _process_results(self, results):
        """Handle business logic for recognized faces."""
        c = theme_manager.colors
        sound_enabled = db.get_setting("sound_enabled", "true") == "true"
        
        for r in results:
            uid = r["user_id"]
            name = r["name"]
            
            if name == "Unknown":
                self.show_status("Unknown Face Detected", "❓", c["accent_yellow"])
                continue
                
            if uid in self.marked_today:
                # Already marked
                self.show_status(f"{name} (Already Marked)", "✓", c["accent"])
                continue
                
            # Valid new face, attempt to mark
            res = db.mark_attendance(uid)
            if res["success"]:
                self.marked_today.add(uid)
                self.show_status(f"Attendance Marked:\n{name}", "✅", c["success"])
                if sound_enabled: sound_manager.play_success()
                self._add_to_log(name, get_current_time_str(), True)
            elif res["already_marked"]:
                self.marked_today.add(uid) # Cache it
            else:
                self.show_status(f"Error: {res['message']}", "❌", c["error"])

    def show_status(self, text, icon, color):
        self.lbl_status_text.configure(text=text, text_color=color)
        self.lbl_status_icon.configure(text=icon, text_color=color)

    def _add_to_log(self, name, time_str, success):
        c = theme_manager.colors
        color = c["success"] if success else c["error"]
        icon = "✅" if success else "❌"
        
        log_item = ctk.CTkFrame(self.scan_list, fg_color=c["bg_secondary"], corner_radius=6)
        log_item.pack(fill="x", pady=2)
        
        ctk.CTkLabel(log_item, text=icon, text_color=color).pack(side="left", padx=(10, 5), pady=8)
        
        info_frame = ctk.CTkFrame(log_item, fg_color="transparent")
        info_frame.pack(side="left", fill="both", expand=True)
        
        ctk.CTkLabel(info_frame, text=name, font=theme_manager.font("button"), text_color=c["text_primary"]).pack(anchor="w")
        ctk.CTkLabel(info_frame, text=time_str, font=theme_manager.font("caption"), text_color=c["text_muted"]).pack(anchor="w")

    def stop(self):
        """Called when navigating away."""
        if self.camera_active:
            self.toggle_camera()
