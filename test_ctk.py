import customtkinter as ctk
app = ctk.CTk()
app.title("Test")
app.geometry("400x300")
ctk.CTkLabel(app, text="CTk is working!").pack(expand=True)
app.mainloop()
