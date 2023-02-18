f = open("fichero.txt", "r")    # Instancia una clase

datos = f.read()

f.close()

f = open("fichero.txt", "r")

datos2 = f.readlines()

f.close()

print(datos)
print(datos2)


f2 = open("escribir.txt", "w")

f2.write("holaholahola\n")

f2.close()
