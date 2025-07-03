import customtkinter as ctk

class ScreenBase(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
    def show(self):
        self.pack(pady=10, padx=10, fill="both", expand = True)

    def hide(self):
        self.pack_forget()
