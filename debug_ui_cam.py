import customtkinter as ctk
import cv2
import PIL.Image, PIL.ImageTk
import sys

app = ctk.CTk()
app.geometry("800x600")

lbl = ctk.CTkLabel(app, text="Waiting...")
lbl.pack(fill="both", expand=True)

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
#cap = cv2.VideoCapture(0)

def update():
    ret, frame = cap.read()
    if ret:
        print(f"Read frame! {frame.shape}")
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = PIL.Image.fromarray(rgb).resize((400, 300))
        imgtk = PIL.ImageTk.PhotoImage(image=img)
        lbl.imgtk = imgtk
        lbl.configure(image=imgtk, text="")
    else:
        print("Failed to read frame")
    app.after(50, update)

update()
app.after(3000, app.destroy)
app.mainloop()
