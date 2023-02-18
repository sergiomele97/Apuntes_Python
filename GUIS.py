import tkinter
from tkinter import ttk

window = tkinter.Tk()   # Crear una ventana

label_saludo = tkinter.Label(window, text="hola", bg="yellow", fg="blue")
label_saludo.pack(ipadx=30, ipady=30, expand=True)

label_adios = tkinter.Label(window, text="adios", bg="red", fg="blue")
label_adios.pack(fill="both", side="right")
window.mainloop()


window2 = tkinter.Tk()  # Crear ventana

# Definir dimensiones del grid
window2.columnconfigure(0, weight=1)
window2.columnconfigure(1, weight=3)

username_label = ttk.Label(window2, text="Username:")
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

username_entry = ttk.Entry(window2)
username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

password_label = ttk.Label(window2, text="Password:")
password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

password_entry = ttk.Entry(window2, show="*")
password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

login_button = ttk.Button(window2, text="Login")
login_button.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)

window2.mainloop()


window3 = tkinter.Tk()

lista = ["Windows", "macOS", "Linux", "MS DOS"]         # Listbox
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window3, height=20, listvariable=lista_items)
listbox.grid(column=90, row=80, sticky=tkinter.W)


seleccionado = tkinter.StringVar()          # Radiobutton

r1 = ttk.Radiobutton(window3, text="Si", value="1", variable=seleccionado)
r2 = ttk.Radiobutton(window3, text="No", value="2", variable=seleccionado)
r1.grid(column=0, row=1, pady=5, padx=5)
r2.grid(column=0, row=2, pady=5, padx=5)


label1 = tkinter.Label(window3, text="Posicionamiento absoluto", bg="blue", fg="white")
label1.place(x=60, y=50)

label1 = tkinter.Label(window3, text="Otro mas", bg="blue", fg="white")
label1.place(x=90, y=40)

fram = ttk.Frame(window3)

window3.mainloop()
