
str_paises = input("Introduzca la lista de paises separados por comas\n")

lista_paises = str_paises.split(",")

lista_paises = list(set(lista_paises))

lista_paises.sort()

print(",".join(lista_paises))
