import cv2
import sys

backends = [
    ("CAP_ANY", cv2.CAP_ANY),
    ("CAP_AVFOUNDATION", cv2.CAP_AVFOUNDATION),
    ("CAP_DSHOW", cv2.CAP_DSHOW) if hasattr(cv2, 'CAP_DSHOW') else ("CAP_DSHOW", -1)
]

for name, backend in backends:
    if backend == -1: continue
    print(f"Testing {name}...")
    cap = cv2.VideoCapture(0, backend)
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            print(f"  SUCCESS! Read frame {frame.shape}")
        else:
            print("  FAILED to read frame.")
        cap.release()
    else:
        print("  FAILED to open.")
