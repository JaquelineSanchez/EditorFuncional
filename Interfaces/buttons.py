from tkinter import *

def saludo():
    print("hola mundo")

def crearLabel():
    Label(root, text="Feliz dia! <3").pack()

#configuracion de la raiz
root = Tk()
#command sirve para indicar la accion 
# y la funcion siempre debe estar declarada antes
Button(root,text="clic aqui",command=crearLabel).pack()



#bucle de la app
root.mainloop()