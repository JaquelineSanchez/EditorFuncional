"""
deberás crear un script llamado contador.py 
que realice varias tareas sobre un fichero 
llamado contador.txt que almacenará un contador 
de visitas (será un número)
"""

from io import open

def cargar():
    try:
        fichero = open("contador.txt","a+")        
        fichero.seek(0)
        numero = int(fichero.read())        
    except:
        numero = 0
    finally:
        fichero.close()
    return numero    

def guardar(num):
    fichero = open("contador.txt","w")
    fichero.write(str(num))
    fichero.close()

def realizar(accion = None):
    n = cargar()
    if accion == "inc":
        n += 1        
        guardar(n)
        print("El contador incremento, ahora esta en: {}".format(n))
    elif accion == "dec":
        n -= 1
        guardar(n)
        print("El contador decremento, ahora esta en: {}".format(n))
    else:
        print("El contador esta en el numero: {}".format(n))

realizar()
realizar("inc")
realizar("inc")
realizar("dec")