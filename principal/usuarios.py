from bd import *
from tela import *
def login_user():
    try:
        sql = "SELECT username, password_hash FROM users WHERE username = %s and password = %s"
        valores = (campo_usuario,campo_senha)
        cur.execute(sql,valores)
        usuarios = cur.fetchone()
        print("          LISTANDO USUÁRIOS          ")
        print("--------------------------------------")
        for usuario in usuarios:
            
            print(f"ID: {usuario[0]} | {usuario[1]}")
    except Exception as e:
        print("Erro ao listar usuarios: ",e)
    finally:
        cur.close()
        conn.close()