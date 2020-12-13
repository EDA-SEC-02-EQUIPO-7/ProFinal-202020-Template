"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """


import sys
import config
from App import controller
from DISClib.ADT import stack
import timeit
assert config
import datetime
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________

Taxi_File = "taxi-trips-wrvz-psew-subset-large.csv"
# ___________________________________________________
#  Menu principal
# ___________________________________________________
def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido al servicio de consulta de Chicago Taxi Service\nEstas son las consultas que puede realizar:\n")
    print("1- Inicializar Analizador")
    print("2- Cargar información de rutas")
    print("3- Consultar el reporte de Información Compañías y Taxis")
    print("4- Consultar el sistema de Puntos y Premios a Taxis")
    print("5- Consultar el Mejor Horario en Taxi entre 2 “community areas” ")
    print("*******************************************")
    print("\n")
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')
    if int(inputs) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        Taxis = controller.newAnalyzer()
    if int(inputs) == 2:
        print("\nCargando los Datos de Chicago Taxi Service ....")
        controller.loadFile(Taxis,Taxi_File)
    if int(inputs)== 3:
        print("Optimizar servicio")
        x=input("digite 0 para el top M compañias con más taxis afiliados, 1 para el top n de compañias com más servicios")
        if x =="0":
            m=int(input("¿cuantos desea saber?"))
            y=controller.req11(Taxis,m)
        if x=="1":
            n=int(input("¿cuantos desea saber?"))
            y=controller.req12(Taxis,n)
        iterator = it.newIterator(y)   
        indicepelicula = 0                 
        while  it.hasNext(iterator):
            element = it.next(iterator)
            indicepelicula += 1
            print(str(indicepelicula) + ".  " + element["company"]+" con una cantidad de "+str(element["cantidad"]))

    if int(inputs)==4:
        print("mejor taxi fechas")
        x=input("si desea en rango digite 1, en caso de una fecha especifica 0: ")
        if x == "0":
            date = input("Escriba la fecha en formato (AAAA-MM-DD): ")
            num = input("Cuantos quiere saber")
            taxi=controller.req2(Taxis,date,num)
            iterator = it.newIterator(taxi)   
            indicepelicula = 0                 
            while  it.hasNext(iterator):
                element = it.next(iterator)
                indicepelicula += 1
                print(str(indicepelicula) + ".  " + element)
        if x=="1":
            date1 = input("Escriba la fecha de inicio en formato (AAAA-MM-DD): ")
            date2 = input("Escriba la fecha final en formato (AAAA-MM-DD): ")
            num = input("Cuantos quiere saber")
            taxi=controller.req21(Taxis,date1,date2,num)
            iterator = it.newIterator(taxi)   
            indicepelicula = 0                 
            while  it.hasNext(iterator):
                element = it.next(iterator)
                indicepelicula += 1
                print(str(indicepelicula) + ".  " + element)

    if int(inputs) == 5:
        initial = input("Escriba su limite horario inferior en fomato HH:MM: ")
        final = input ("Escriba su superior horario inferior en fomato HH:MM: ")
        vertexA = input ("Escriba el community area de salida, por ejemplo (32.0): ")
        vertexB = input ("Escriba el community area de llegada por ejemplo (76.0): ")
        resp = controller.Mejor_Hora(Taxis,initial,final,vertexA,vertexB)
        Timepo = resp[0]
        print ("El mejor horario para iniciar su viaje es a las {} con una duracion de {} segundos  ".format(Timepo,resp[1]))
    if int(inputs) == 0:
        sys.exit(0)

"""
Menu principal
"""