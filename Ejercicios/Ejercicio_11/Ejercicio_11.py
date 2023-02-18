import sqlite3


def main():
    crear_tabla()

    insertar_datos(1, "Sofia", "Gomez")
    insertar_datos(2, "Alejandro", "Pascual")
    insertar_datos(3, "Pepito", "Gomez")
    insertar_datos(4, "Alejandro", "pepito")
    insertar_datos(5, "Mortadelo", "Gomez")
    insertar_datos(6, "Otrotio", "Pascual")
    insertar_datos(7, "Vengava", "Gomez")
    insertar_datos(8, "Yaestaria", "Pascual")

    buscar_alumno("Mortadelo", "Gomez")


def crear_tabla():
    conn = sqlite3.connect("alumnos.db")    # Crea/abre la BD
    try:
        query = '''create table Alumnos (
                        id integer primary key,
                        nombre text,
                        apellido text)                
                '''

        conn.execute(query)
        print("Se creo la tabla alumnos")

    except:
        print("La tabla alumnos ya exite")

    conn.close()


def insertar_datos(identificador, nombre, apellido):
    try:
        conn = sqlite3.connect("alumnos.db")
        cursor = conn.cursor()

        query = f"INSERT INTO Alumnos (id, nombre, apellido) VALUES({identificador}, '{nombre}', '{apellido}')"

        cursor.execute(query)

        conn.commit()
        cursor.close()
        conn.close()

    except:
        pass


def buscar_alumno(nombre, apellido):
    conn = sqlite3.connect("alumnos.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM Alumnos WHERE nombre='{nombre}' AND apellido='{apellido}'"
    rows = cursor.execute(query)
    data = rows.fetchone()
    print(data)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
