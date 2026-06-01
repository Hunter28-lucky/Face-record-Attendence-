# Table of Contents

| Page No | Title |
| :--- | :--- |
| i | [Title Page](#title-page) |
| ii | [Declaration Of Student](#declaration-of-student) |
| iii | [Certificate](#certificate) |
| iv | [Approval Certificate](#approval-certificate) |
| v | [Acknowledgement](#acknowledgement) |
| vi | [Abstract](#abstract) |
| 1 | [1. Introduction](#1-introduction) |
| 2 | [2. Literature Survey](#2-literature-survey) |
| 4 | [3. Requirement Analysis](#3-requirement-analysis) |
| 6 | [4. System Design](#4-system-design) |
| 10 | [5. Technologies Used](#5-technologies-used) |
| 12 | [6. Implementation](#6-implementation) |
| 18 | [7. Testing](#7-testing) |
| 21 | [8. Result and Output Screens](#8-result-and-output-screens) |
| 25 | [9. Advantages and Limitations](#9-advantages-and-limitations) |
| 27 | [10. Future Scope](#10-future-scope) |
| 28 | [11. Conclusion](#11-conclusion) |
| 29 | [12. Reference](#12-reference) |
| 30 | [13. Appendix](#13-appendix) |

---

<div style="page-break-after: always;"></div>

## Title Page

<div align="center">
  
# **AI-Powered Face Recognition Attendance System**

**A Project Report**

*Submitted in partial fulfillment of the requirements for the award of the degree of*

**Bachelor of Technology / Master of Computer Applications**

*in*

**Computer Science and Engineering**

*by*

**[Student Name 1] (Roll No: [12345])**<br>
**[Student Name 2] (Roll No: [12346])**<br>
**[Student Name 3] (Roll No: [12347])**

*Under the guidance of*

**[Professor's / Guide's Name]**<br>
*[Designation, Department]*

*(Insert College / University Logo Here)*

**Department of Computer Science and Engineering**<br>
**[Name of the College / University]**<br>
**[Academic Year: 2026-2027]**

</div>

---

<div style="page-break-after: always;"></div>

## Declaration Of Student

We hereby declare that the project entitled **"AI-Powered Face Recognition Attendance System"** submitted for the fulfillment of the degree is our original work and has not been submitted previously to any other university or institution for the award of any degree or diploma. 

The empirical findings and the system developed in this project are based on the data collected by us. All the sources of information used in this report, including code libraries, research papers, and technical documentations, have been duly acknowledged.

<br><br>
**Date:** _______________  
**Place:** _______________  

<br><br>
1. **[Student Name 1]** _______________________ (Signature)
2. **[Student Name 2]** _______________________ (Signature)
3. **[Student Name 3]** _______________________ (Signature)

---

<div style="page-break-after: always;"></div>

## Certificate

This is to certify that the project entitled **"AI-Powered Face Recognition Attendance System"** has been successfully completed by **[Student Name 1]**, **[Student Name 2]**, and **[Student Name 3]** under my guidance in partial fulfillment of the degree requirements for Bachelor of Technology / Master of Computer Applications in Computer Science and Engineering at [Name of the College / University].

The work presented in this report is authentic and has been carried out to my satisfaction. 

<br><br><br>

**[Professor's / Guide's Name]**  
*(Project Guide)*  
[Designation], Department of CSE  
[College Name]  

<br><br>

**[HOD's Name]**  
*(Head of Department)*  
Department of CSE  
[College Name]  

---

<div style="page-break-after: always;"></div>

## Approval Certificate

This project report entitled **"AI-Powered Face Recognition Attendance System"** by **[Student Names]** is approved for the examination and evaluation as a partial fulfillment of the degree requirements.

<br><br><br><br>

_________________________________  
**Internal Examiner**  
Date: 

<br><br><br><br>

_________________________________  
**External Examiner**  
Date: 

---

<div style="page-break-after: always;"></div>

## Acknowledgement

We would like to express our deep gratitude to our project guide **[Guide's Name]** for their continuous support, valuable insights, and encouragement throughout the development of this project. Their technical expertise and constructive feedback have been instrumental in shaping this software into a production-grade system.

We also extend our sincere thanks to our Head of Department, **[HOD's Name]**, and the Principal of **[College Name]** for providing us with the necessary infrastructure and environment to carry out this research and development work.

Finally, we would like to thank our families and friends for their unwavering moral support during the course of this project.

---

<div style="page-break-after: always;"></div>

## Abstract

Traditional attendance management systems, such as manual roll calls, RFID tags, or biometric fingerprint scanners, are often plagued by inefficiencies, time consumption, proxy attendance, and hygiene concerns (especially post-pandemic). To address these challenges, this project introduces the **AI-Powered Face Recognition Attendance System (FaceTrack Pro)**—a contactless, highly accurate, and automated solution for educational institutions and corporate environments.

Built using Python, OpenCV, and the `face_recognition` (dlib) library, the system leverages Histogram of Oriented Gradients (HOG) and Convolutional Neural Networks (CNN) for precise face detection and 128-dimensional biometric encoding. A modern, dark-themed Graphical User Interface (GUI) powered by CustomTkinter ensures a seamless user experience for both administrators and regular users. 

Key features include real-time live face scanning with automated duplicate prevention, instantaneous model training via automated image capture (30 samples per user), comprehensive SQLite database management, and robust data analytics with CSV/Excel export capabilities. The system successfully demonstrates high-speed, contactless attendance marking with a recognition tolerance threshold designed to minimize false positives, resulting in a production-ready desktop application that significantly optimizes administrative overhead.

---

<div style="page-break-after: always;"></div>

## 1. Introduction

### 1.1 Overview
In modern educational and corporate ecosystems, tracking attendance is a critical administrative task. Traditional methods like paper-based registers or ID card scanning are not only tedious but also prone to human error and fraudulent practices like "buddy punching." Face recognition technology, a subset of biometric artificial intelligence, offers a seamless, non-intrusive alternative by utilizing unique facial landmarks to identify individuals instantly.

### 1.2 Problem Statement
Existing attendance systems face several critical issues:
- **Manual Systems:** Extremely time-consuming, prone to data loss, and require manual data entry for analytics.
- **RFID/Smart Cards:** Cards can be lost, stolen, or shared among peers, leading to proxy attendance.
- **Fingerprint Scanners:** Require physical contact, raising hygiene concerns, and can fail due to wet or dirty fingers.
- **High Deployment Costs:** Many enterprise-grade AI attendance systems require expensive proprietary hardware and cloud subscriptions.

### 1.3 Objectives
The primary objectives of this project are:
1. To develop an automated, highly accurate face recognition attendance system using accessible consumer webcams.
2. To build a user-friendly, responsive desktop application using Python and CustomTkinter.
3. To implement a secure, local SQLite database to manage user profiles and daily attendance logs.
4. To provide robust analytics and export features (CSV/Excel) for administrative reporting.
5. To ensure the system operates entirely offline to protect biometric data privacy.

### 1.4 Scope of the Project
The system is designed to handle small to medium-scale deployments (e.g., classrooms, small offices, department-level tracking). The scope includes module development for user registration, automated facial training, live webcam recognition, and an administrative dashboard for data management. Current deployment is targeted at Windows, macOS, and Linux desktop environments.

---

## 2. Literature Survey

### 2.1 Existing Systems
Over the past decade, various biometric attendance systems have been proposed:
- **Eigenfaces and Fisherfaces (PCA/LDA):** Early attempts used Principal Component Analysis. While computationally light, they suffered greatly under varying lighting conditions and facial expressions.
- **Haar Cascades:** Popularized by Viola-Jones in 2001, Haar cascades are fast but often struggle with profile faces and occlusions.
- **Deep Learning Approaches:** Modern architectures like FaceNet (Google), DeepFace (Facebook), and dlib's ResNet model map faces into high-dimensional Euclidean spaces where distances directly correspond to facial similarity.

### 2.2 Proposed System vs Existing Systems
Unlike early systems relying on fragile algorithms, the proposed **FaceTrack Pro** utilizes the `face_recognition` library, which is built on dlib's state-of-the-art C++ toolkit. 
- **Accuracy:** Achieves ~99.38% accuracy on the standard Labeled Faces in the Wild (LFW) benchmark.
- **Cost-Effectiveness:** Runs on standard CPU architectures using HOG (Histogram of Oriented Gradients) without requiring expensive GPU hardware, unlike heavy FaceNet implementations.
- **User Interface:** Replaces archaic Tkinter designs with a highly polished, modern CustomTkinter interface featuring dark/light modes and interactive data visualizations.

### 2.3 Feasibility Study
- **Technical Feasibility:** The required libraries (OpenCV, dlib, pandas) are mature, well-documented, and actively maintained in the Python ecosystem.
- **Economic Feasibility:** The project utilizes entirely open-source libraries. The only hardware required is a standard PC and a generic USB/integrated webcam, bringing deployment costs to near zero.
- **Operational Feasibility:** The one-click installation scripts (`install.bat` / `install.sh`) and intuitive GUI make the system easily operable by non-technical administrative staff.

---

## 3. Requirement Analysis

### 3.1 Hardware Requirements
- **Processor:** Intel Core i3 (7th Gen) / AMD Ryzen 3 or higher. (Multi-core recommended for dlib).
- **RAM:** Minimum 4GB (8GB recommended for smooth GUI and camera stream handling).
- **Storage:** 500MB of free disk space for the application, plus additional space for SQLite database backups and captured face datasets.
- **Camera:** Integrated laptop webcam or standard USB webcam (720p minimum recommended).

### 3.2 Software Requirements
- **Operating System:** Windows 10/11, macOS 10.15+, or Ubuntu/Debian Linux.
- **Programming Language:** Python 3.9 or higher.
- **Build Tools:** CMake (Required for compiling dlib's C++ core).
- **Core Libraries:**
  - `opencv-python` (Computer Vision)
  - `face_recognition` & `dlib` (Biometric AI)
  - `customtkinter` & `Pillow` (GUI Toolkit)
  - `pandas` & `openpyxl` (Data Export)
  - `matplotlib` (Analytics)
  - `pygame` (Audio Notifications)

### 3.3 Functional Requirements
- **User Registration:** The system must allow admins to add new users by capturing 30 sequential frames of their face.
- **Real-Time Detection:** The system must scan the live camera feed and match faces against the trained database within 0.5 seconds.
- **Anti-Duplication:** The system must mark a user "Present" only once per calendar day.
- **Data Export:** The system must allow administrators to filter attendance by date and export to `.csv` or `.xlsx`.

### 3.4 Non-Functional Requirements
- **Security:** Administrative pages (Settings, User Deletion) must be protected by a secure login gateway.
- **Performance:** The live scanner must maintain a minimum of 15-30 FPS to ensure a fluid user experience.
- **Reliability:** The system must automatically backup the SQLite database to prevent data loss in case of sudden power failures.

---

## 4. System Design

### 4.1 System Architecture
The application follows a modular, Model-View-Controller (MVC) inspired architecture:
1. **Presentation Layer (GUI):** Managed by `customtkinter`. Includes the Sidebar, Dashboard, Live Scanner, and Settings views.
2. **Business Logic Layer:** Managed by the `FaceRecognitionEngine`. Handles threading, camera resource allocation, face encoding generation, and Euclidean distance thresholding.
3. **Data Access Layer:** Managed by `DatabaseManager`. Handles direct SQLite transactions, ensures database integrity via schema constraints, and executes Pandas dataframes for exports.

### 4.2 Data Flow Diagram (DFD)
**Level 0 (Context Diagram):**
- **User** -> Stands in front of Camera -> **System** -> Marks Attendance -> Saves to Database.
- **Admin** -> Interacts with GUI -> **System** -> Registers Users / Generates Reports.

**Level 1 (Core Process):**
1. Camera captures frame (BGR format).
2. OpenCV converts frame to RGB.
3. dlib (HOG) extracts face bounding boxes.
4. dlib generates 128-d face encodings.
5. System compares new encoding against `face_encodings.pkl` database using L2 norm (Euclidean distance).
6. If distance < Tolerance (e.g., 0.50), trigger `mark_attendance()`.
7. SQLite validates UNIQUE constraint (User ID + Date).
8. Pygame triggers Success Audio. GUI triggers Toast Notification.

### 4.3 Database Schema (Entity Relationship)
The local SQLite database (`attendance.db`) consists of four primary tables:

**1. `users` Table:**
- `id` (INTEGER, Primary Key, Auto-increment)
- `name` (TEXT)
- `roll_number` (TEXT, Unique)
- `department` (TEXT)
- `email`, `phone`, `photo_path` (TEXT)
- `is_active` (INTEGER, Default 1 - used for soft deletion)

**2. `attendance` Table:**
- `id` (INTEGER, Primary Key)
- `user_id` (INTEGER, Foreign Key referencing `users.id`)
- `date` (TEXT, YYYY-MM-DD)
- `time` (TEXT, HH:MM:SS)
- `status` (TEXT, Default 'Present')
- *Constraint:* UNIQUE(`user_id`, `date`)

**3. `settings` Table:**
- Key-Value store for GUI theme, camera index, tolerance thresholds, and admin passwords.

**4. `audit_log` Table:**
- Tracks system actions (e.g., "USER_ADDED", "BACKUP_CREATED") for security traceability.

---

## 5. Technologies Used

### 5.1 Python 3
Python was chosen as the core language due to its unparalleled ecosystem for Machine Learning, Data Science, and rapid prototyping. 

### 5.2 OpenCV (Open Source Computer Vision Library)
OpenCV handles all low-level camera operations, image resizing, color space conversions (BGR to RGB), and drawing visual overlays (bounding boxes, text) on the live video feed.

### 5.3 `face_recognition` & `dlib`
The `face_recognition` library acts as a high-level wrapper around dlib. 
- **dlib** is a modern C++ toolkit containing machine learning algorithms. We utilize its pre-trained ResNet network, which maps faces to a 128-dimensional hypersphere.
- The distance between two encodings dictates similarity. A distance of `0.6` is the standard threshold, but this system defaults to a stricter `0.5` to prevent false positives in high-security environments.

### 5.4 CustomTkinter
Standard Tkinter looks dated on modern operating systems. CustomTkinter provides hardware-accelerated, modern UI elements (rounded corners, dark mode, smooth sliders, tab views) that match native Windows 11 and macOS design languages.

### 5.5 SQLite3 & Pandas
- **SQLite3:** A lightweight, serverless relational database engine built directly into Python. Ideal for desktop applications requiring zero network configuration.
- **Pandas/OpenPyXL:** Used in the analytics and records modules to rapidly convert SQL query results into structured Excel (`.xlsx`) and CSV reports.

---

## 6. Implementation

### 6.1 Modular Code Structure
The codebase is structured for maximum maintainability:
- `main.py`: The entry point. Initializes the CustomTkinter window, handles page routing, and starts background auto-backup threads.
- `config.py`: A centralized file containing all tunable constants (Paths, Tolerance levels, Camera FPS targets).
- `database/db_manager.py`: Contains the `DatabaseManager` singleton class that abstracts all raw SQL queries.
- `face_recognition_engine/recognizer.py`: Contains the `FaceRecognitionEngine` class. It manages the `VideoCapture` object, runs the `face_encodings()` methods, and manages the `face_encodings.pkl` file.
- `gui/pages/`: Contains separate Python files for each UI view (`dashboard.py`, `attendance.py`, `register.py`, `records.py`, `analytics.py`, `settings.py`).
- `utils/helpers.py`: Contains utility classes for Theme management (Dark/Light colors), Sound management (Pygame audio threads), and validation functions.

### 6.2 The Registration Algorithm
1. Admin inputs user details (Name, Roll No).
2. SQLite creates a new entry in `users` and returns a new `user_id`.
3. The camera opens and captures exactly 30 frames containing a single face.
4. Each frame is cropped and saved to `data/face_data/<user_id>_<name>/`.
5. The `FaceRecognitionEngine` scans the folder, encodes all 30 images, averages the vectors to create a highly accurate master encoding, and appends it to `face_encodings.pkl`.

### 6.3 The Live Recognition Algorithm
1. The webcam reads frames in a continuous `while` loop within a dedicated background thread to prevent GUI freezing.
2. Every frame is resized by 25% (e.g., `fx=0.25, fy=0.25`) to drastically speed up processing.
3. `face_locations = face_recognition.face_locations(rgb_small_frame, model="hog")`
4. `face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)`
5. For each detected face, the system calculates `face_recognition.face_distance(known_encodings, face_encoding)`.
6. `numpy.argmin()` finds the closest match. If the distance is below the threshold, the user ID is extracted.
7. A database call `mark_attendance(user_id)` is made.

### 6.4 Concurrency and Multithreading
Running camera processing (I/O and CPU heavy) on the same thread as a GUI (Tkinter `mainloop`) causes severe lag. The system implements Python's `threading` module:
- The camera loop runs in a `daemon=True` thread.
- Frame updates are pushed back to the GUI thread using CustomTkinter's thread-safe `.after()` callbacks.

---

## 7. Testing

### 7.1 Unit Testing
Individual modules were tested in isolation. 
- **Database Module:** Verified that duplicate attendance entries on the same day for the same user throw an `IntegrityError` and are safely caught.
- **Camera Module:** `test_cam.py` was used to iterate through available OpenCV backends (`CAP_AVFOUNDATION`, `CAP_DSHOW`) to ensure cross-platform camera initialization without fatal crashes.

### 7.2 Integration Testing
- Tested the data flow from `register.py` capturing images -> `recognizer.py` generating encodings -> `db_manager.py` saving the user ID. 
- Verified that deleting a user from the GUI successfully marks `is_active=0` in the database and ignores their face encoding during live scans.

### 7.3 System Testing (Real-World Scenarios)
1. **Varying Lighting:** Tested the system in bright daylight and dim office lighting. The HOG model performed admirably, though extreme darkness required screen illumination.
2. **Multiple Faces:** Tested the live scanner with 3+ people in the frame. The system successfully identified all known users simultaneously and drew individual bounding boxes.
3. **Spoofing Attempts:** Tested by holding up a printed photograph. Standard 2D face recognition is vulnerable to this. (Noted in Limitations).

### 7.4 Test Cases and Results
| Test Case ID | Description | Expected Output | Actual Output | Status |
|:---|:---|:---|:---|:---|
| TC_01 | Register a new user with valid inputs | User added, 30 frames captured, model trained | As expected | **Pass** |
| TC_02 | Register user with existing Roll No | Show error toast notification | Shown successfully | **Pass** |
| TC_03 | Live scan an unregistered face | Draw red box labeled "Unknown" | Box drawn, no DB entry | **Pass** |
| TC_04 | Live scan a registered face | Mark present, play success sound | Marked present, audio played | **Pass** |
| TC_05 | Live scan the same face twice in one day | Ignore second scan, do not duplicate DB row | Handled by UNIQUE constraint | **Pass** |
| TC_06 | Export records to CSV | Generate .csv file in `exports/` folder | File generated successfully | **Pass** |

---

## 8. Result and Output Screens

*(Note to student: Insert screenshots of your running application here)*

### 8.1 Splash Screen and Dashboard
The application launches with an animated splash screen leading into the primary Dashboard. The dashboard displays key metrics: Total Users, Today's Attendance Count, Attendance Percentage, and a scrolling list of recently marked individuals.

### 8.2 Registration Screen
A form interface where administrators input student/employee details. Upon submission, a live camera feed appears, displaying a progress bar as it automatically captures 30 valid facial samples.

### 8.3 Live Attendance Scanner
The core interface displaying the live webcam feed. 
- **Green Bounding Box:** Indicates a recognized user, displaying their Name and Confidence Score (e.g., "John Doe - 82%").
- **Red Bounding Box:** Indicates an unknown individual. 
- Animated toast notifications appear at the bottom of the screen to confirm attendance marking.

### 8.4 Analytics and Records
- **Records Page:** A data grid showing the full `attendance` database table with date-range picker filters and "Export to Excel" functionality.
- **Analytics Page:** Displays a Matplotlib-generated 7-day trend line chart and a department-wise pie chart to visualize attendance statistics.

---

## 9. Advantages and Limitations

### 9.1 Advantages
1. **Contactless and Hygienic:** Prevents the transmission of germs associated with fingerprint scanners.
2. **High Speed & Throughput:** Can process multiple faces in a single frame simultaneously, eliminating queues.
3. **Automated Data Processing:** Eliminates manual data entry. Reports are generated instantly in standard formats.
4. **Cost-Effective:** Requires zero specialized hardware beyond a standard computer and webcam.
5. **Privacy-Preserving:** All biometric encodings are stored locally on the host machine. No images or data are sent to third-party cloud servers.

### 9.2 Limitations
1. **Liveness Detection (Spoofing):** The current HOG-based implementation does not feature depth sensing or liveness detection, making it susceptible to spoofing via high-resolution photographs or digital screens.
2. **Hardware Dependency:** While optimized for CPU, maintaining 30 FPS with multiple faces in the frame requires a moderately powerful modern CPU. 
3. **Lighting Dependency:** Extreme backlight or complete darkness severely hampers the HOG descriptor's ability to locate facial landmarks.
4. **Physical Changes:** Drastic changes in facial hair, heavy makeup, or thick glasses might occasionally lower the confidence score below the strict tolerance threshold.

---

## 10. Future Scope

The foundational architecture of FaceTrack Pro allows for significant future enhancements:
1. **Anti-Spoofing / Liveness Detection:** Integrating a blink-detection algorithm (using eye aspect ratio) or utilizing infrared/depth cameras (like Intel RealSense or Apple FaceID hardware) to prevent photo spoofing.
2. **Cloud Synchronization:** Migrating the local SQLite database to a cloud-based PostgreSQL or Firebase instance to allow multi-device synchronization (e.g., multiple entry gates in a large university).
3. **Mobile Application Integration:** Developing a companion Android/iOS application (via Flutter/React Native) to allow users to view their own attendance records remotely.
4. **Automated Email/SMS Alerts:** Integrating SMTP or Twilio APIs to automatically notify parents or managers when an individual is marked absent for consecutive days.
5. **GPU Acceleration:** Providing native support for CUDA/TensorRT to utilize Nvidia GPUs, allowing for the deployment of heavier, highly accurate CNN models in real-time.

---

## 11. Conclusion

The "AI-Powered Face Recognition Attendance System" successfully demonstrates the practical application of modern computer vision and deep learning techniques to solve real-world administrative inefficiencies. By integrating the robust `face_recognition` library with a sophisticated, user-centric CustomTkinter GUI and a reliable SQLite backend, the project achieves its goal of creating a production-ready, contactless attendance solution.

Testing confirms that the system operates with high accuracy, effectively prevents duplicate entries, and provides administrators with instantaneous analytical insights. While certain limitations regarding 2D spoofing exist, the system serves as a highly effective, low-cost upgrade over traditional manual and RFID-based attendance tracking paradigms, laying a strong foundation for future enterprise-level scaling.

---

## 12. Reference

1. **Geitgey, A. (2017).** *Face Recognition Library*. GitHub. Available at: https://github.com/ageitgey/face_recognition
2. **King, D. E. (2009).** *Dlib-ml: A Machine Learning Toolkit*. Journal of Machine Learning Research, 10, 1755-1758.
3. **Bradski, G. (2000).** *The OpenCV Library*. Dr. Dobb's Journal of Software Tools.
4. **Dalal, N., & Triggs, B. (2005).** *Histograms of Oriented Gradients for Human Detection*. IEEE Computer Society Conference on Computer Vision and Pattern Recognition (CVPR).
5. Python Software Foundation. *Python 3 Documentation*. Available at: https://docs.python.org/3/
6. Schimansky, T. *CustomTkinter: A modern and customizable python UI-library based on Tkinter*. Available at: https://github.com/TomSchimansky/CustomTkinter

---

<div style="page-break-after: always;"></div>

## 13. Appendix

### 13.1 Installation Guide

**For Windows:**
1. Install Python 3.9 or higher from `python.org`. Ensure "Add Python to PATH" is checked during installation.
2. Install CMake (required for building `dlib`).
3. Open Command Prompt in the project folder and run:
   ```cmd
   pip install -r requirements.txt
   ```
4. Run the pre-launch verifier:
   ```cmd
   python verify_install.py
   ```
5. Launch the application:
   ```cmd
   python main.py
   ```

**For macOS / Linux:**
1. Open Terminal and install CMake:
   ```bash
   brew install cmake      # macOS
   sudo apt install cmake  # Ubuntu/Debian
   ```
2. Navigate to the project directory and install requirements:
   ```bash
   pip3 install -r requirements.txt
   ```
3. Launch the application:
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

### 13.2 Core Code Snippet (Real-Time Recognition Loop)

```python
# From recognizer.py (Simplified)
def process_frame(self, frame):
    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Find all faces in current frame
    face_locations = face_recognition.face_locations(rgb_small_frame, model="hog")
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        # Calculate distances to all known faces
        face_distances = face_recognition.face_distance(self.known_encodings, face_encoding)
        
        if len(face_distances) > 0:
            best_match_index = np.argmin(face_distances)
            
            # Check if distance is below strict tolerance (e.g., 0.50)
            if face_distances[best_match_index] <= self.tolerance:
                user_id = self.known_ids[best_match_index]
                user_name = self.known_names[best_match_index]
                
                # Trigger attendance marking in database
                self.mark_attendance_callback(user_id)
```
