
variableglobal = 1


def nombrefuncion(parametrostr="adios"):
    print(parametrostr)
    global variableglobal
    variableglobal = 2
    print(str(variableglobal))
    pass


def muchoparametro(*args):
    resultado = 0
    for arg in args:
        resultado += arg
    print(resultado)
    return resultado


nombrefuncion("holaaaaa")

resul = muchoparametro(1, 2, 4, 1, 5, 1, 3, 1, 2)

print(resul)

anonima = lambda nombre: print("soy una funcion sin nombre", nombre)
anonima("hola pepe")
