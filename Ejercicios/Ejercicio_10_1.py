import tkinter
from tkinter import ttk

window = tkinter.Tk()


def reiniciar(event):
    global seleccionado
    seleccionado.set(None)


seleccionado = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text="Si", value="1", variable=seleccionado)
r2 = ttk.Radiobutton(window, text="No", value="2", variable=seleccionado)
r3 = ttk.Radiobutton(window, text="Quizas", value="3", variable=seleccionado)
r1.grid(column=0, row=1, pady=5, padx=5, sticky=tkinter.W)
r2.grid(column=0, row=2, pady=5, padx=5, sticky=tkinter.W)
r3.grid(column=0, row=3, pady=5, padx=5, sticky=tkinter.W)


boton = tkinter.Button(window, text="Reiniciar")
boton.grid(column=1, row=1, pady=5, padx=5, sticky=tkinter.E)
boton.bind("<Button-1>", reiniciar)

window.mainloop()
