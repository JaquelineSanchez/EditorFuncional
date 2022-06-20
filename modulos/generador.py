import math
import random

def leerNumero(ini,fin,mensaje):
    while True:
        num = int(input(mensaje))
        if num >= ini and num <= fin:
            return num

#el mio
def generador():
    numeros = leerNumero(1,20,"¿Cuántos números quieres generar? [1-20]: ")            
    modo = leerNumero(1,3,"¿Como quieres redondear los números? [1]Al alza [2]a la baja [3]Normal : ")            
    aleatorios = []
    enteros = []
    for x in range(numeros):
        nw = random.uniform(0,101)
        aleatorios.append(nw)
    for num in aleatorios:
        if modo == 1:
            n = math.ceil(num)
            enteros.append(n)            
        elif modo == 2:
            n = math.floor(num)
            enteros.append(n)            
        else:
            n = round(num)
            enteros.append(n)            
        print("normal: {} y redondeado: {}".format(num,n))
    return enteros        

#El del profe
def generador2():
    numeros = leerNumero(1,20,"¿Cuantos números quieres generar? [1-20]: ")
    modo = leerNumero(1,3,"¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")
    
    lista = []
    
    for i in range(numeros):
        numero = random.uniform(0,101)
        if modo == 1:
            print("{} => {}".format(numero, math.ceil(numero)) )
            numero = math.ceil(numero)
        elif modo == 2:
            print("{} => {}".format(numero, math.floor(numero)) )
            numero = math.floor(numero)
        elif modo == 3:
            print("{} => {}".format(numero, round(numero)) )
            numero = round(numero)     
        lista.append(numero)
        
    return lista

generador()    