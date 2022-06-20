from io import open
import pickle


class Personaje:

    def __init__(self,nombre,vida,ataq,defensa,alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataq
        self.defensa = defensa
        self.alcance = alcance

    def __str__(self):
        return "Nombre: {}, Vida: {}, Ataque: {}, Defensa {}, Alcance: {}".format(self.nombre, self.vida, self.ataque, self.defensa, self.alcance)

class Gestor:

    personajes = []

    def __init__(self):
        self.cargar()

    def cargar(self):
        fichero = open("personajes.pckl","ab+")
        fichero.seek(0)
        try:
            self.personajes = pickle.load(fichero)
        except:
            print("Fichero vacio.")
        finally:
            fichero.close()
            print("Se han cargado {} personajes".format(len(self.personajes)))

    def agregar(self,p):
        nom = p.nombre
        for personaje in self.personajes:
            if personaje.nombre == nom:
                return "Error: Ya existe este personaje."
        self.personajes.append(p)
        self.guardar()
        return "Agregado correctamente"

    def guardar(self):
        fichero = open("personajes.pckl","wb")
        pickle.dump(self.personajes, fichero)
        fichero.close()

    def mostrar(self):
        if len(self.personajes) == 0:
            print("El gestor esta vacio")
        else:
            for p in self.personajes:
                print(p)

    def borrar(self, nom):
        for p in self.personajes:
            if p.nombre == nom:
                self.personajes.remove(p)
                break
        self.guardar()

gestor = Gestor()

print(gestor.agregar(Personaje("Caballero",4,2,4,2)))
print(gestor.agregar(Personaje("Guerrero",2,4,2,4)))
print(gestor.agregar(Personaje("Arquero",2,4,1,8)))

gestor.mostrar()
print(gestor.agregar(Personaje("Arquero",2,4,1,8)))
gestor.borrar("Arquero")
gestor.mostrar()
