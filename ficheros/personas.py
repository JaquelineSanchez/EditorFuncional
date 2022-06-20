#Crear un scrip que:
#lea los datos de un fichero de texto, 
#que transforme cada fila en un diccionario 
#y lo añada a una lista llamada personas. 
#Luego rocorre las personas de la lista 
#y para cada una muestra de forma amigable todos sus campos.


from io import open

fichero = open('personas.txt','r',encoding="utf8")
lineas = fichero.readlines()
fichero.close()

print("\tLista de Personas:")
personas = []
for fila in lineas:
    datos = fila.replace("\n","").split(';')
    personas.append({"id":datos[0],"nombre":datos[1],"apellido":datos[2],"nacimiento":datos[3]})
for p in personas:
    print("ID: {}, Nombre: {}, Apellido: {}, Fecha de nacimiento: {}".format(p["id"], p["nombre"], p["apellido"],p["nacimiento"]))

