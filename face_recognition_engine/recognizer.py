# Made by Harsh Bardhan Kumar and Team
"""
╔══════════════════════════════════════════════════════════════╗
║      FACE RECOGNITION ENGINE — Face Attendance System       ║
║  Handles face encoding, training, and real-time detection   ║
╚══════════════════════════════════════════════════════════════╝

This module handles:
  - Capturing face images for new users
  - Encoding faces and saving encodings to disk
  - Loading existing encodings from disk
  - Real-time face recognition from webcam frames
  - Confidence scoring and unknown face handling
"""

import cv2
import face_recognition
import numpy as np
import os
import pickle
import logging
from datetime import datetime

# ── Paths ────────────────────────────────────────────────────
BASE_DIR       = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FACE_DATA_DIR  = os.path.join(BASE_DIR, "data", "face_data")
ENCODINGS_FILE = os.path.join(BASE_DIR, "data", "face_encodings.pkl")

os.makedirs(FACE_DATA_DIR, exist_ok=True)

# ── Logging ──────────────────────────────────────────────────
logger = logging.getLogger(__name__)


# ═══════════════════════════════════════════════════════════════
#  FaceRecognitionEngine Class
# ═══════════════════════════════════════════════════════════════
class FaceRecognitionEngine:
    """
    Core face recognition engine.
    Manages encoding storage, model training, and live recognition.
    """

    def __init__(self):
        # Loaded encodings: {"encodings": [...], "ids": [...], "names": [...]}
        self.known_encodings = []
        self.known_ids       = []
        self.known_names     = []

        # Tolerance: lower = stricter matching (0.4-0.6 is typical)
        self.tolerance = 0.50

        # Haar cascade for fast face detection (pre-check before deep encoding)
        cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        self.face_cascade = cv2.CascadeClassifier(cascade_path)

        # Load existing encodings from disk
        self.load_encodings()
        logger.info("FaceRecognitionEngine initialized.")

    # ══════════════════════════════════════════════════════════
    #  ENCODING PERSISTENCE
    # ══════════════════════════════════════════════════════════

    def save_encodings(self):
        """Save all known encodings to disk as a pickle file."""
        data = {
            "encodings": self.known_encodings,
            "ids":       self.known_ids,
            "names":     self.known_names,
        }
        with open(ENCODINGS_FILE, "wb") as f:
            pickle.dump(data, f)
        logger.info(f"Encodings saved: {len(self.known_encodings)} faces.")

    def load_encodings(self):
        """Load encodings from disk (if file exists)."""
        if os.path.exists(ENCODINGS_FILE):
            try:
                with open(ENCODINGS_FILE, "rb") as f:
                    data = pickle.load(f)
                raw_encodings = data.get("encodings", [])
                raw_ids       = data.get("ids", [])
                raw_names     = data.get("names", [])
                
                # Dynamically sync with SQLite database to filter out any stale encodings
                try:
                    from database.db_manager import db
                    active_user_ids = {u["id"] for u in db.get_all_users(active_only=True)}
                except Exception as db_err:
                    logger.warning(f"Could not connect to database for encoding validation: {db_err}")
                    active_user_ids = None

                self.known_encodings = []
                self.known_ids       = []
                self.known_names     = []

                for enc, uid, name in zip(raw_encodings, raw_ids, raw_names):
                    if active_user_ids is None or uid in active_user_ids:
                        self.known_encodings.append(enc)
                        self.known_ids.append(uid)
                        self.known_names.append(name)
                    else:
                        logger.warning(f"Filtering out stale face encoding for User ID {uid} ({name.strip()}) - not active in database.")
                
                logger.info(f"Loaded {len(self.known_encodings)} face encodings.")
            except Exception as e:
                logger.error(f"Error loading encodings: {e}")
                self.known_encodings = []
                self.known_ids       = []
                self.known_names     = []
        else:
            logger.info("No encoding file found. Starting fresh.")

    def reload_encodings(self):
        """Public method to reload encodings from disk (call after training)."""
        self.load_encodings()

    # ══════════════════════════════════════════════════════════
    #  FACE CAPTURE (Registration)
    # ══════════════════════════════════════════════════════════

    def capture_face_images(self, user_id: int, user_name: str,
                            num_images: int = 30,
                            camera_index: int = 0,
                            progress_callback=None,
                            frame_callback=None) -> bool:
        """
        Capture `num_images` face images from webcam for a new user.

        Args:
            user_id:           Database ID of the user
            user_name:         Display name (for folder naming)
            num_images:        Number of face images to capture
            camera_index:      Webcam index (0 = default)
            progress_callback: Called with (current, total) for progress bar
            frame_callback:    Called with each BGR frame for live preview

        Returns:
            True if successful, False otherwise.
        """
        # Create user-specific folder
        safe_name   = "".join(c for c in user_name if c.isalnum() or c in "_ -")
        user_folder = os.path.join(FACE_DATA_DIR, f"{user_id}_{safe_name}")
        os.makedirs(user_folder, exist_ok=True)

        cap = cv2.VideoCapture(camera_index)
        if not cap.isOpened():
            logger.error("Cannot open camera for capture.")
            return False

        cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        cap.set(cv2.CAP_PROP_FPS,          30)

        captured = 0
        attempt  = 0
        max_attempts = num_images * 10  # avoid infinite loop

        logger.info(f"Capturing {num_images} images for: {user_name}")

        while captured < num_images and attempt < max_attempts:
            ret, frame = cap.read()
            if not ret:
                attempt += 1
                continue

            attempt += 1
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Resize frame to half size for 4x faster face detection
            small_rgb = cv2.resize(rgb_frame, (0, 0), fx=0.5, fy=0.5)
            face_locations = face_recognition.face_locations(small_rgb, model="hog")
            
            # Scale coordinates back to original frame size
            face_locations = [(t * 2, r * 2, b * 2, l * 2) for (t, r, b, l) in face_locations]

            if len(face_locations) == 1:   # exactly one face — ideal
                top, right, bottom, left = face_locations[0]

                # Draw green rectangle around face
                display = frame.copy()
                cv2.rectangle(display, (left, top), (right, bottom), (0, 255, 100), 2)
                cv2.putText(display, f"Capturing: {captured+1}/{num_images}",
                            (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 100), 2)

                # Save face image
                face_img = frame[top:bottom, left:right]
                img_path = os.path.join(user_folder, f"{captured:04d}.jpg")
                cv2.imwrite(img_path, face_img)
                captured += 1

                if progress_callback:
                    progress_callback(captured, num_images)
                if frame_callback:
                    frame_callback(display)

            elif len(face_locations) == 0:
                # No face detected — show warning on frame
                display = frame.copy()
                cv2.putText(display, "No face detected. Look at camera.",
                            (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 100, 255), 2)
                if frame_callback:
                    frame_callback(display)
            else:
                # Multiple faces — ask user to be alone
                display = frame.copy()
                cv2.putText(display, "Multiple faces! Stay alone in frame.",
                            (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 50, 255), 2)
                if frame_callback:
                    frame_callback(display)

        cap.release()

        if captured >= num_images:
            logger.info(f"Captured {captured} images for {user_name}.")
            return True
        else:
            logger.warning(f"Only captured {captured}/{num_images} images.")
            return captured > 5  # Accept partial if at least 5 images

    # ══════════════════════════════════════════════════════════
    #  TRAINING
    # ══════════════════════════════════════════════════════════

    def train_model(self, progress_callback=None) -> bool:
        """
        Scan all face image folders, encode each face,
        and save encodings to disk.

        Args:
            progress_callback: Called with (current, total) during training

        Returns:
            True on success, False on failure.
        """
        logger.info("Starting model training...")

        # Discover all user folders
        user_folders = [
            d for d in os.listdir(FACE_DATA_DIR)
            if os.path.isdir(os.path.join(FACE_DATA_DIR, d))
        ]

        if not user_folders:
            logger.warning("No face data found to train on.")
            return False

        # Get active user IDs from database to filter out deleted/stale folders
        try:
            from database.db_manager import db
            active_user_ids = {u["id"] for u in db.get_all_users(active_only=True)}
        except Exception as db_err:
            logger.warning(f"Could not connect to database for folder validation: {db_err}")
            active_user_ids = None

        new_encodings = []
        new_ids       = []
        new_names     = []

        # Count total images for progress tracking, excluding stale folders
        valid_folders = []
        for folder_name in user_folders:
            parts   = folder_name.split("_", 1)
            user_id = int(parts[0]) if parts[0].isdigit() else -1
            if active_user_ids is None or user_id in active_user_ids:
                valid_folders.append((folder_name, user_id))
            else:
                logger.warning(f"Skipping stale training folder '{folder_name}' - User ID not in database.")

        if not valid_folders:
            logger.warning("No valid face data folders found to train on.")
            return False

        total_images = sum(
            len(os.listdir(os.path.join(FACE_DATA_DIR, f[0])))
            for f in valid_folders
        )
        processed = 0

        for folder_name, user_id in valid_folders:
            parts   = folder_name.split("_", 1)
            name    = parts[1] if len(parts) > 1 else folder_name

            folder_path = os.path.join(FACE_DATA_DIR, folder_name)
            image_files = [
                f for f in os.listdir(folder_path)
                if f.lower().endswith((".jpg", ".jpeg", ".png"))
            ]

            encodings_for_user = []

            for img_file in image_files:
                img_path = os.path.join(folder_path, img_file)
                try:
                    image     = face_recognition.load_image_file(img_path)
                    encodings = face_recognition.face_encodings(image)

                    if encodings:
                        encodings_for_user.append(encodings[0])
                except Exception as e:
                    logger.warning(f"Could not encode {img_path}: {e}")

                processed += 1
                if progress_callback:
                    progress_callback(processed, total_images)

            # Use mean encoding for better robustness
            if encodings_for_user:
                mean_encoding = np.mean(encodings_for_user, axis=0)
                new_encodings.append(mean_encoding)
                new_ids.append(user_id)
                new_names.append(name)
                logger.info(f"Trained: {name} ({len(encodings_for_user)} images)")

        if new_encodings:
            self.known_encodings = new_encodings
            self.known_ids       = new_ids
            self.known_names     = new_names
            self.save_encodings()
            logger.info(f"Training complete. {len(new_encodings)} users trained.")
            return True
        else:
            logger.error("No valid encodings found during training.")
            return False

    # ══════════════════════════════════════════════════════════
    #  REAL-TIME RECOGNITION
    # ══════════════════════════════════════════════════════════

    def recognize_faces(self, frame: np.ndarray) -> list:
        """
        Recognize faces in a single BGR frame.

        Args:
            frame: OpenCV BGR image (numpy array)

        Returns:
            List of dicts: [
                {
                  "name":       str,        # recognized name or "Unknown"
                  "user_id":    int,        # DB user ID or -1
                  "confidence": float,      # 0.0 – 1.0 (higher = more confident)
                  "location":  (top, right, bottom, left)
                }
            ]
        """
        if not self.known_encodings:
            return []

        # Resize frame to 1/4 size for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small   = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Detect face locations (HOG is faster than CNN on CPU)
        face_locations = face_recognition.face_locations(rgb_small, model="hog")

        if not face_locations:
            return []

        # Compute encodings for all detected faces
        face_encodings = face_recognition.face_encodings(rgb_small, face_locations)

        results = []
        for encoding, location in zip(face_encodings, face_locations):
            # Compare against all known encodings
            distances = face_recognition.face_distance(self.known_encodings, encoding)

            best_match_idx  = np.argmin(distances)
            best_distance   = distances[best_match_idx]
            confidence      = 1.0 - best_distance   # closer to 1 = more confident

            # Scale location back to full frame size
            top, right, bottom, left = location
            top    *= 4
            right  *= 4
            bottom *= 4
            left   *= 4

            if best_distance <= self.tolerance:
                results.append({
                    "name":       self.known_names[best_match_idx],
                    "user_id":    self.known_ids[best_match_idx],
                    "confidence": round(confidence, 3),
                    "location":   (top, right, bottom, left),
                })
            else:
                results.append({
                    "name":       "Unknown",
                    "user_id":    -1,
                    "confidence": round(confidence, 3),
                    "location":   (top, right, bottom, left),
                })

        return results

    def draw_recognition_results(self, frame: np.ndarray,
                                 results: list,
                                 marked_today: set = None) -> np.ndarray:
        """
        Draw bounding boxes and labels on a frame.

        Args:
            frame:        BGR frame to draw on
            results:      Output of recognize_faces()
            marked_today: Set of user_ids already marked today

        Returns:
            Annotated BGR frame
        """
        marked_today = marked_today or set()
        overlay      = frame.copy()

        for r in results:
            top, right, bottom, left = r["location"]
            name       = r["name"]
            confidence = r["confidence"]
            user_id    = r["user_id"]
            already    = user_id in marked_today

            # Color coding
            if name == "Unknown":
                color = (0, 50, 255)    # Red-ish
                label = "Unknown"
            elif already:
                color = (0, 200, 255)   # Amber — already marked
                label = f"{name} ✓ (Already Marked)"
            else:
                color = (0, 220, 80)    # Green — recognized, not yet marked
                label = f"{name} ({int(confidence * 100)}%)"

            # Draw filled rectangle for label background
            cv2.rectangle(overlay, (left, top), (right, bottom), color, 2)
            cv2.rectangle(overlay, (left, bottom - 30), (right, bottom), color, cv2.FILLED)
            cv2.putText(overlay, label,
                        (left + 6, bottom - 8),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1)

        # Blend overlay for semi-transparency
        return cv2.addWeighted(overlay, 0.85, frame, 0.15, 0)

    # ══════════════════════════════════════════════════════════
    #  UTILITIES
    # ══════════════════════════════════════════════════════════

    def get_registered_count(self) -> int:
        """Number of users currently loaded in memory."""
        return len(self.known_encodings)

    def remove_user_encodings(self, user_id: int) -> bool:
        """Remove encodings for a specific user and retrain."""
        indices_to_remove = [
            i for i, uid in enumerate(self.known_ids) if uid == user_id
        ]
        if not indices_to_remove:
            return False
        for i in sorted(indices_to_remove, reverse=True):
            self.known_encodings.pop(i)
            self.known_ids.pop(i)
            self.known_names.pop(i)
        self.save_encodings()
        return True

    def set_tolerance(self, value: float):
        """Adjust recognition tolerance (0.4 = strict, 0.6 = lenient)."""
        self.tolerance = max(0.3, min(0.7, value))
        logger.info(f"Tolerance set to {self.tolerance}")


# ── Singleton instance ────────────────────────────────────────
engine = FaceRecognitionEngine()
