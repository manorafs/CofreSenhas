import customtkinter as ctk
from bd import *

def login_user():
    sql = "SELECT username FROM users WHERE username = %s"
    valores = (campo_usuario.get(), )

    try:
        cur.execute(sql,valores)
        usuario = cur.fetchone()
    except Exception as e:
        print("Erro não esperado.",e)
    if usuario is None:
        print("Usuário inválido:")   
    else:
        sql = "SELECT password_hash FROM users WHERE username = %s"
        valores = (campo_usuario.get(), )
        
        try:
            cur.execute(sql,valores)
            usuario_pass = cur.fetchone()
            print(campo_usuario.get())
            print(usuario)
            print(usuario_pass)
        except Exception as e:
            print("ERRO",e)
      ###  if usuario_pass is None:
        #    print("Erro ao obter senha!")    
        #    return
        
        if campo_usuario.get() == usuario[0] and campo_senha.get() == usuario_pass[0]:
                print("Logado com sucesso")
        else:
            print("Senha inválida!")            




#setando a tela:
ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.title("Cofre senhas")
app.geometry('300x300')
#inicia a app.

label_usuario = ctk.CTkLabel(app,text='Usuário')
label_usuario.pack(pady=10)
campo_usuario = ctk.CTkEntry(app,placeholder_text='Digite seu usuário: ')
campo_usuario.pack(pady=10)

label_senha = ctk.CTkLabel(app,text='Senha')
label_senha.pack(pady=10)
campo_senha = ctk.CTkEntry(app,placeholder_text='Digite sua senha: ')
campo_senha.pack(pady=10)

botao_login = ctk.CTkButton(app,text='Login',command=login_user)
resultado_login = ctk.CTkLabel(app,text='')
botao_login.pack(pady=10)
app.mainloop()
