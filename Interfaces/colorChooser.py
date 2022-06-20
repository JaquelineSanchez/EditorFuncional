#Otro tipo de ventana emergente
from tkinter import *
#importamos explicitamente los widget
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

#configuracion de la raiz
root = Tk()
root.title("Popups")

def color():
    #devuelve una tupla con el color en rgb y en hexadecimal
    color = ColorChooser.askcolor(title="Elige un color")
    print(color)
    root.quit()

def abrirRuta():
    #devuelve una cadena con la ruta al archivo
    ruta = FileDialog.askopenfilename(title="Abrir archivo",
    #Establecer tipos de archivos que se pueden abrir
    filetypes=(("Fichero de texto","*.txt"),("Fichero de python","*.py"),
    ("Todos","*.*")))

def guardarArchivo():
    #devuelve archivo abierto == open ruta en formato write (por defecto)
    archivo = FileDialog.asksaveasfile(title="Guardar archivo",
    mode="a+",defaultextension=".txt")
    if archivo is not None:
        archivo.write("Hola")
        archivo.close()

Button(root,text="Has clic", command=guardarArchivo).pack()


#bucle de la app
root.mainloop()