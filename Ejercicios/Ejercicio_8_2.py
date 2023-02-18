import pickle


class Vehiculo:
    nombre = None

    def __init__(self, nombre):
        self.nombre = nombre


coche = Vehiculo("ferrari")


try:
    f = open("../vehiculo.txt", "x")
    f.close()
except:
    pass


f2 = open("../vehiculo.txt", "wb")

pickle.dump(coche, f2)

f2.close()


f3 = open("../vehiculo.txt", "rb")

objetorecargado = pickle.load(f3)

f3.close()


print(objetorecargado.nombre)
