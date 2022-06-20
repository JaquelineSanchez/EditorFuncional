#textos muy largos o multilinea
from tkinter import *

#configuracion de la raiz
root = Tk()

texto = Text(root)
texto.pack()
#La configuracion de tamaña funciona con # de caracteres
texto.config(width=30,height=10)
#asi es 30 caracteres en un renglon y 10 lineas

texto.config(font=("Verdana",12),padx=5,pady=5, selectbackground= "red")




#bucle de la app
root.mainloop()