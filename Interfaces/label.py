from tkinter import *

#configuracion de la raiz
root = Tk()
"""
#Variables dinamicas
texto = StringVar()
texto.set("Un nuevo texto")

#Configuracion de un marco
frame = Frame(root,width=480, height=320)
frame.pack()
#Si la etiqueta no se va a utilizar puede ser
Label(root, text = "-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-").pack(anchor="nw")

#dentro de donde va a ir = frame y lo que va a decir = texto
label = Label(frame, text = "¡Hola mundo!")
label.place(x=100,y=100) #donde va aparecer (x,y)

#Configuracion de label
label.config(bg = "green", fg ="blue", font = ("Verdana",24))

#Configurar dinamicamente
label.config(textvariable=texto)
"""
#Configurando una imagen como label
imagen = PhotoImage(file = "imagen.gif")
Label(root,image=imagen,bd = 0).pack()

#Bucle de la app
root.mainloop()