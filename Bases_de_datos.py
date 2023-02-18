import sqlite3
import getpass

''' Fichero "miaplicacion.db"
1|vroman|miclave
2|usuario|clave
'''


def main():
    crear_usuario(3, "pepe", "supercontraseña")


def main2():
    username = input("Nombre de usuario: ")
    password = getpass.getpass("Contraseña: ")

    if verifica_credenciales(username, password):
        print("login correcto")

    else:
        print("Login incorrecto")


def verifica_credenciales(username, password):
    conn = sqlite3.connect("miaplicacion.db")
    cursor = conn.cursor()

    query = f"SELECT id FROM users WHERE username='{username}' AND password='{password}'"
    rows = cursor.execute(query)
    data = rows.fetchone()
    print(type(data))

    cursor.close()
    conn.close()

    if data == None:
        return False
    else:
        return True


def crear_usuario(identificador, usuario, clave):
    conn = sqlite3.connect("miaplicacion.db")
    cursor = conn.cursor()

    query = f"INSERT INTO users (id, username, password) VALUES({identificador}, '{usuario}', '{clave}')"

    rows = cursor.execute(query)
    print(type(rows))

    conn.commit()   # Las operaciones que modifican la BD hay que usar el commit
    cursor.close()  # Otra opcion es usar el parametro isolation_level=None
    conn.close()


if __name__ == "__main__":
    main()
