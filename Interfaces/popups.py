#ventanas emergentes || cuadros de dialogo
from tkinter import *
#Se tiene que importar de manera explicita
from tkinter import messagebox as MessageBox

#configuracion de la raíz
root = Tk()
root.title("Popups")

#Mostrar informacion
def saludo():
    #argumento 1: titulo de la ventana
    #argumento 2: Mensaje a mostrar
    MessageBox.showinfo("Hola","Hola mundo!")

#dar una advertencia
def advertencia():
    MessageBox.showwarning("Alerta","Esto es un virus")

#informar errores
def error():
    MessageBox.showerror("Error","Ha ocurrido un error inesperado :'c")

#Hacer preguntas de si | no
def preguntar():
    """
    #devuelve una cadena de texto Yes | no
    r = MessageBox.askquestion("Salir","¿Segur@ de que quieres salir?")
    if r == "yes":
        root.quit()
    """
    # lo mismo pero con true y false
    r = MessageBox.askyesno("Salir","¿Deseas salir sin guardar?")
    if r:
        root.destroy()

#aceptar o cancelar
def permitir():
    r = MessageBox.askokcancel("Confirmar","¿Eliminar registro?")
    if r:
        MessageBox.showinfo("Listo","Se eliminó el registro")

def reintentar():
    r = MessageBox.askretrycancel("Reintentar","No se puede conectar")
    if r:
        MessageBox.showinfo("Listo","Conexión exitosa")

Button(root,text="Clic aquí", command=reintentar,bg="red").pack()

#bucle de la app
root.mainloop()