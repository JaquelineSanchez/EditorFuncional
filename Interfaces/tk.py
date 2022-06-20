from tkinter import *

#Raiz de la interfaz
root = Tk()

#Nombre de ventana
root.title("Nombre de la ventana")

#De esta manera no se puede modificar el tamaño
root.resizable(0,0)
"""
Argumentos
0,0 = No cambia el tamaño
0,1 = Solo cambia de manera vertical
1,0 = Solo cambia de manera horizontal
1,1 = Puede cambiar en los dos sentidos
"""

#Cambiar el icono de la ventana terminacion en .ico
root.iconbitmap("hola.ico")

#Al abrir directo del explorador de archivos 
# si cambiamos la extension por .pyw entonces solo aparece la ventana

#Abajo de todo porque es lo ultimo antes de mostrar
root.mainloop()