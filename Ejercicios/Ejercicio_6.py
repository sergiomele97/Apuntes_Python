class Vehiculo:
    color = None
    ruedas = 0
    puertas = 0

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0

    def __init__(self, velocidad, cilindrada, color, ruedas, puertas):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


    def __repr__(self):
        return "Soy el objeto de la clase coche"


ferrari = Coche(45, 45, "rojo", 4, 4)

print(repr(ferrari))
