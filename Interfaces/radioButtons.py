#Para que el usario escoja una de varias opciones
from tkinter import *

def seleccionar():
    monitor.config(text = "has seleccionado la opción {}".format(op.get()))

def reiniciar():
    op.set(None)
    monitor.config(text="")

#configuracion de la raiz
root = Tk()

op = IntVar()

Radiobutton(root, text = "Opción 1",variable = op, value = 1, command = seleccionar).pack()
Radiobutton(root, text = "Opción 2",variable = op, value = 2, command = seleccionar).pack()
Radiobutton(root, text = "Opción 3",variable = op, value = 3, command = seleccionar).pack()

monitor = Label(root)
monitor.pack()

Button(root,text = "Reiniciar",command = reiniciar).pack()

# bucle de la app
root.mainloop()