from principal.views.screen import ScreenBase
from principal.database.bd import *
from principal.controllers.login_controller import login_user


#setando a tela:
import customtkinter as ctk
#inicia a app.

class Login_Screen(ScreenBase):
    def __init__(self,master,on_login_transition_callback = None,**kwargs):
        super().__init__(master, **kwargs)
        self.on_login_transition_callback = on_login_transition_callback

        self.label_usuario = ctk.CTkLabel(self,text='Usuário')
        self.label_usuario.pack(pady=10)
        self.campo_usuario = ctk.CTkEntry(self,placeholder_text='Digite seu usuário: ')
        self.campo_usuario.pack(pady=10)

        self.label_senha = ctk.CTkLabel(self,text='Senha')
        self.label_senha.pack(pady=10)
        self.campo_senha = ctk.CTkEntry(self,placeholder_text='Digite sua senha: ')
        self.campo_senha.pack(pady=10)

        self.botao_login = ctk.CTkButton(self,text='Login',command=self.funcao_auxiliar)
        self.resultado_login = ctk.CTkLabel(self,text='')
        self.botao_login.pack(pady=10)

    def funcao_auxiliar(self):
        login_user(self.campo_usuario.get(),
                   self.campo_senha.get(),
                   on_sucess_callback=self._handle_login_sucess,
                   on_failure_callback=self._handle_login_failure)
    def _handle_login_sucess(self):
        print("Login bem sucedido, escondendo tela e partindo para outra")
        self.hide()
        if self.on_login_transition_callback:
            self.on_login_transition_callback()
        
        

    def _handle_login_failure(self):
        print("Usuário ou senha incorretos!")
        self.resultado_login.configure(text="Usuario ou senha incorretos")
        self.show()
       
