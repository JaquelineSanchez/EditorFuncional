#Como un input pero de manera grafica
from tkinter import *

#Configuracion de la raiz
root = Tk()
"""
#Marco 1
frame = Frame(root)
frame.pack()

#crear entrada
entry = Entry(frame)
entry.pack(side="right")
label = Label(frame,text = "Nombre")
label.pack(side = "left")

#Marco 2
frame2 = Frame(root)
frame2.pack()

#crear entrada
entry = Entry(frame2)
entry.pack(side="right")
label = Label(frame2,text = "Apellido")
label.pack(side = "left")
"""
#usando cuadricula (grid)

label = Label(root,text = "Nombre")
#grid tiene posiciones 
#ademas de tipo de justificacion(norte,sur,este.oeste)
# y pady que es para tener separaciones
label.grid(row =0,column=0,sticky="e",padx=5,pady=5)
#crear entrada
entry = Entry(root)
entry.grid(row =0,column=1,padx=5,pady=5)
#Se puede cambiar la justificacion de inserciones
entry.config(justify="center")

label2 = Label(root,text = "Apellido")
label2.grid(row =1,column=0,sticky="e",padx=5,pady=5)
#crear entrada
entry2 = Entry(root)
entry2.grid(row =1,column=1,padx=5,pady=5)
entry2.config(justify="right")

#Campo para contraseña
label3 = Label(root,text = "Contraseña")
label3.grid(row =2,column=0,sticky="e",padx=5,pady=5)
#crear entrada
entry3 = Entry(root)
entry3.grid(row =2,column=1,padx=5,pady=5)
#show es para que muestre un caracter especial 
#en lugar de lo que se escribe
entry3.config(justify="center",show="*")

#Bucle de la app
root.mainloop()