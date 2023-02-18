from abc import abstractmethod


class Juguete:      # Clase madre
    encendido = False

    def enciende(self):
        self.encendido = True
        pass


class Dino(Juguete):    # Herencia
    nombre = None

    def __init__(self, nombre):    # Constructor
        print("Estoy en el constructor", nombre)
        self.nombre = nombre        # Así se definen las propiedades de los objetos (dentro del constructor)

    def __del__(self):              # Destructor
        print("Estoy en el destructor de la clase", self.__class__)


class Estatica:     # Clase estatica
    numero = 1

    @staticmethod
    def incrementa():
        Estatica.numero += 1


class Animal:
    @abstractmethod
    def sonido(self):
        pass


d = Dino("minidinosaurio")      # Instanciar la clase con el metodo constructor
d.enciende()

del d  # Invocar el metodo destructor

Estatica.incrementa()
print(Estatica.numero)
