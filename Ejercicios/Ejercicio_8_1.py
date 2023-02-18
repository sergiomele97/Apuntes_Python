
try:
    f = open("../archivo.txt", "x")
    f.close()
except:
    pass

f2 = open("../archivo.txt", "w")

f2.write("Holaholahola\nFin del comunicado")

f2.close()
