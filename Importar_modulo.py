import Modulos
import sys
import pprint
from operaciones import suma  # paquete

Modulos.main()

pprint.pprint(sys.path)     # Imprime donde busca modulos

print(suma.suma(4, 5))
