class Alumno:
    nombre = None
    nota = None

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def is_aprovado(self):
        if self.nota >= 5:
            print(self.nombre, "ha aprobado con nota", self.nota)
        elif self.nota < 5:
            print(self.nombre, "ha suspendido con nota", self.nota)


manolo = Alumno("Manolo", 7)

manolo.is_aprovado()
