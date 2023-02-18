import tkinter

window = tkinter.Tk()

lista = ["Windows", "macOS", "Linux", "MS DOS"]         # Listbox
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, height=10, listvariable=lista_items)
listbox.grid(column=0, row=0, sticky=tkinter.W)

label_saludo = tkinter.Label(window, text="hola", bg="yellow", fg="blue")
label_saludo.grid(column=1, row=0, sticky=tkinter.E)

window.mainloop()