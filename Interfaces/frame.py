from tkinter import *

#Raiz de la interfaz
root = Tk()
#Nombre de ventana
root.title("Haciendo pruebas")
#Cambiar el icono de la ventana terminacion en .ico
root.iconbitmap("hola.ico")
#Redimensionar ventana
root.resizable(1,1)

#agregar un marco con medidas especificas
frame = Frame(root, width = 480, height = 320)
frame.pack(fill = 'both', expand = 1) #Poner todo dentro de la raiz arriba y al medio
#Opciones dentro del pack 
#fill=y|both para rellenar el widget
#expand=1 para rellenar en altura
frame.config(cursor = "pirate") #tipo de cursor
frame.config(bg = "lightblue") #Color de fondo
frame.config(bd = 25) #borde del marco
frame.config(relief = "sunken") #Tipo de borde

#Mismas modificaciones pero en la raiz
root.config(cursor = "arrow") #tipo de cursor
root.config(bg = "blue") #Color de fondo
root.config(bd = 15) #borde del marco
root.config(relief = "ridge") #Tipo de borde

#Abajo de todo porque es lo ultimo antes de mostrar
root.mainloop()