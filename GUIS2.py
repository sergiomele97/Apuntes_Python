import tkinter
from tkinter import filedialog

window = tkinter.Tk()

def salir(event):
    print("Adios")
    window.quit()

def saludar(event):
    print("Han hecho click en saludar")

def saludarDobleClick(event):
    print("Han hecho doble click en saludar")

def buscarArchivo(event):
    filename = filedialog.askopenfilename()
    print(filename)


boton = tkinter.Button(window, text="Haz click")
boton.pack()
boton.bind("<Button-1>", saludar)
boton.bind("<Double-1>", saludarDobleClick)

boton_salir = tkinter.Button(window, text="Salir")
boton_salir.pack()
boton_salir.bind("<Button-1>", salir)

boton_file = tkinter.Button(window, text="Abrir archivo")
boton_file.pack()
boton_file.bind("<Button-1>", buscarArchivo)

window.mainloop()