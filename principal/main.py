from .database.bd import conecta_banco
from principal.views.login_screen import Login_Screen
from principal.views.home_screen import Home_Screen
import customtkinter as ctk

conecta_banco()
app = ctk.CTk()
ctk.set_appearance_mode('dark')
app.title("Cofre senhas")
app.geometry('1200x650+340+200')


home_frame = Home_Screen(master=app)

def show_home_screen():
    login_frame.hide()
    home_frame.show()

login_frame = Login_Screen(master=app,on_login_transition_callback=show_home_screen)
login_frame.pack(pady=50, padx=50, fill="both", expand = True)
app.mainloop()