from principal.views.screen import ScreenBase
import customtkinter as ctk

class Home_Screen(ScreenBase):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
    
        self.label_boasvindas = ctk.CTkLabel(self,text='Olá! Seja bem vindo ao administrador de senhas!')
        self.label_boasvindas.pack(pady=10)