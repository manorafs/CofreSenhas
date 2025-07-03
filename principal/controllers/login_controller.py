from principal.database.bd import *

def login_user(username, password, on_sucess_callback= None, on_failure_callback = None):
    sql = "SELECT username FROM users WHERE username = %s"
    valores = (username,)
    try:
        cur.execute(sql,valores)
        usuario = cur.fetchone()
    except Exception as e:
        print("Erro não esperado.",e)
    if usuario is None:
        print("Usuário inválido:")   
    else:
        sql = "SELECT password_hash FROM users WHERE username = %s"
        valores = (username,)
        try:
            cur.execute(sql,valores)
            usuario_pass = cur.fetchone()
            print(username)
            print(usuario)
            print(usuario_pass)
        except Exception as e:
            print("ERRO",e)      
        if username == usuario[0] and password == usuario_pass[0]:
                if on_sucess_callback:
                    on_sucess_callback()
        else:
            print("Senha inválida!")  
            if on_failure_callback:
                on_failure_callback()          
