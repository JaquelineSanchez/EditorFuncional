#los menu son las opciones en cascada 
#que viene en la parte de arriba como pestañas 
from tkinter import *

#configuracion de la raiz 
root = Tk()
root.title("Barra de menu")

#menu que engloba a los demas
menubar = Menu(root)
#Para empaquetar no se usa pack
root.config(menu=menubar)

#crear submenus hijo de menubar 
#donde tearoff=0 indica que no cree por defecto nada
fileMenu = Menu(menubar, tearoff=0)
#agregar opciones
fileMenu.add_command(label="Nuevo")
fileMenu.add_command(label="Abrir")
fileMenu.add_command(label="Guardar")
fileMenu.add_command(label="Cerrar")
#Crear un separador
fileMenu.add_separator()
#root.quit es para cerrar la interfaz
fileMenu.add_command(label="Salir", command=root.quit)

editMenu = Menu(menubar, tearoff=0)
editMenu.add_command(label="Cortar")
editMenu.add_command(label="Copiar")
editMenu.add_command(label="Pegar")

helpMenu = Menu(menubar, tearoff=0)
helpMenu.add_command(label="Manual")
helpMenu.add_command(label="Ayuda web")
helpMenu.add_separator()
helpMenu.add_command(label="Acerca de...")


#Añadir menus a la ventana
menubar.add_cascade(label="Archivo", menu=fileMenu)
menubar.add_cascade(label="Editar", menu=editMenu)
menubar.add_cascade(label="Ayuda", menu=helpMenu)



#bucle de la app
root.mainloop()