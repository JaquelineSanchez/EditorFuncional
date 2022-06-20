#Botones de seleccion
from tkinter import *

def seleccion():
    cadena = "Preparando café "
    if (leche.get()):
        cadena += "con leche "
    else:
        cadena +="sin leche "
    
    if (azucar.get()):
        cadena += "y con azúcar. "
    else:
        cadena +="y sin azúcar."

    monitor.config(text=cadena)

#configuracion de la raiz
root = Tk()
root.title("Cafetería")
root.config(bd = 15)

leche = IntVar()     #1 si, 0 no
azucar = IntVar()    #1 si, 0 no

imagen = PhotoImage(file="imagen.gif")
Label(root,image=imagen).pack(side="left")

frame = Frame(root)
frame.pack(side="left",)

Label(frame,text="¿Cómo quieres el café?").pack(anchor="w")
#configuracion de valores por defecto (off) y seleccionado (on)
Checkbutton(frame,text="Con leche", variable = leche, onvalue=1, offvalue=0, command = seleccion).pack(anchor="w")
Checkbutton(frame,text="Con azúcar", variable = azucar, onvalue=1, offvalue=0, command = seleccion).pack(anchor="w")

monitor = Label(frame)
monitor.pack(anchor="w") #anclada a la izquierda

#bucle de la app
root.mainloop()