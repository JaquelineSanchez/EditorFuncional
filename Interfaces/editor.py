#Proyecto de la unidad
from tkinter import *
from tkinter import filedialog as FileDialog
from tkinter import messagebox as MessageBox

ruta = ""  #para la direccion de archivos

def nuevo():
    global ruta
    mensaje.set("Archivo nuevo")
    ruta = ""
    #Borrar contenido desde el caracter 1.0 hasta el final
    texto.delete(1.0,"end")
    root.title("Mi editor")

def abrir():
    global ruta
    mensaje.set("Archivo abierto")
    # '.' abrir directorio actual
    ruta = FileDialog.askopenfilename(
        initialdir='.',
        filetypes=(("Archivo de texto",".txt"),),
        title=" Abrir archivo de texto")
    
    if ruta != "":
        #abrir en modo lectura
        archivo = open(ruta,'r')
        contenido = archivo.read()
        texto.delete(1.0,"end")
        texto.insert('insert',contenido)
        archivo.close()
        root.title(ruta + " - Mi editor")

def guardar():
    global ruta
    if ruta != "":
        #-1c para que no agregue saltos de linea
        contenido = texto.get(1.0,"end-1c")
        #Abriendo archivo en modo de escritura
        archivo = open(ruta,'w+')
        archivo.write(contenido)
        archivo.close()
        MessageBox.showinfo("Guardar","El archivo se guardo con exito :)")
    else:
        guardarComo()

def guardarComo():
    global ruta
    archivo = FileDialog.asksaveasfile(title = "Guardar archivo",
    defaultextension=".txt", mode = "w")
    if archivo is not None:
        ruta = archivo.name
        contenido = texto.get(1.0,"end-1c")
        #Abriendo archivo en modo de escritura
        archivo = open(ruta,'w+')
        archivo.write(contenido)
        archivo.close()
        root.title(ruta + " - Mi editor")
        MessageBox.showinfo("Guardar","El archivo se guardo con exito :)")
    else:
        ruta = ""
        mensaje.set("Guardado cancelado")

#Configuracion de la raiz
root = Tk()
root.title("Mi editor")

#Creación de menú superior
menubar = Menu(root)
archivoMenu = Menu(menubar,tearoff=0)
archivoMenu.add_command(label="Nuevo", command=nuevo)
archivoMenu.add_command(label="Abrir", command=abrir)
archivoMenu.add_command(label="Guardar", command=guardar)
archivoMenu.add_command(label="Guardar como...", command=guardarComo)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir",command=root.quit)

menubar.add_cascade(menu = archivoMenu, label = "Archivo")
root.config(menu=menubar)

#caja de texto
texto = Text(root)
#mismo tamaño de la venta
texto.pack(fill = "both", expand=1)
texto.config(bd=0,bg="black",padx=5,pady=5,font=("Consolas",12),fg="white")

#monitoreo de actividad
mensaje = StringVar()
mensaje.set("Bienvenid@ a tu editor")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")

#Bucle de la app
root.mainloop()