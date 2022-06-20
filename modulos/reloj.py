import datetime 
import time
import os

while True:
    #limpiar pantalla
    os.system('cls')
    #obtener la fecha y hora actual
    dt = datetime.datetime.now()
    #Imprimir hora
    print("{}:{}:{}".format(dt.hour,dt.minute,dt.second))
    #Pausar un segundo
    time.sleep(1)