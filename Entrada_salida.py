# Formatear una cadena

numero = 511
texto = "quijote"
otromas = 1.2

print(f"El numero {numero} y el texto {texto.upper()}")


class Juguete:
    nombre = ""
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):      # Sobrecarga del metodo __str__
        return f"Mi nombre es {self.nombre} y mi precio {self.precio}"


j1 = Juguete("Potato", 10.5)
print(str(j1))
