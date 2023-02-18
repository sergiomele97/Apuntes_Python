numeros = [1, 2, 3, 4, 5, 6, 7, 8]


def mifuncion(x):
    if x % 2 == 0:
        return True


resultado = filter(mifuncion, numeros)      # Guarda los valores que son True
print(list(resultado))

print(str("pepepepepe".startswith("pep")))

print(list(map(mifuncion, numeros)))        # Map aplica a todos


cursos = ["java", "Python", "git"]
asistentes = [15, 5, 20]

demo = zip(cursos, asistentes)
print(list(demo))
