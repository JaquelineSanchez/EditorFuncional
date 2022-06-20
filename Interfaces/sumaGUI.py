from tkinter import *

def sumar():
    r.set(float(n1.get()) + float(n2.get()))
    borrarNumeros()

def borrarNumeros():
    n1.set("")
    n2.set("")


root = Tk()
root.config(border=5)

n1 = StringVar()
n2 = StringVar()
r = StringVar()

Label(root, text="Numero 1:").pack()
Entry(root, justify="center", textvariable=n1).pack()   #primer numero
Label(root, text="Numero 2:").pack()
Entry(root, justify="center", textvariable=n2).pack()   #segundo numero
Label(root, text=" ").pack()
Button(root,text="Sumar", command=sumar).pack()
Label(root, text="\nResultado:").pack()
Entry(root, justify="center", textvariable=r,state="disabled").pack()   #resultado





#bucle de la app
root.mainloop()