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

import config as cf
from App import model
import csv
import datetime
"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def newAnalyzer():
    Taxis = model.newAnalyzer()
    model.create_Hash(Taxis)
    return Taxis

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def loadFile(Taxis, tripfile):
    """
    """
    total_trips = 0
    tripfile = cf.data_dir + tripfile
    input_file = csv.DictReader(open(tripfile, encoding="utf-8"),
                                delimiter=",")
    for trip in input_file:
        total_trips += 1 
        model.addTrip(Taxis,trip)
    return [Taxis,total_trips]
    
# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________
def Mejor_Hora (Taxis,initialTime,finalTime,vertexA,vertexB):
    initialTime = datetime.datetime.strptime(initialTime, '%H:%M')
    initialTime = model.compareTime(initialTime)
    finalTime = datetime.datetime.strptime(finalTime, '%H:%M')
    finalTime = model.compareTime(finalTime)
    return model.MejorHora(Taxis, initialTime.time(), finalTime.time(),vertexA,vertexB)
def req2(Taxis,date,num):
    date =  datetime.datetime.strptime(date, '%Y-%m-%d')
    return model.req2(Taxis,date.date(),num)
def req21(Taxis,date1,date2,num):
    date1 =  datetime.datetime.strptime(date1, '%Y-%m-%d')
    date2 =  datetime.datetime.strptime(date2, '%Y-%m-%d')
    return model.req21(Taxis,date1.date(),date2.date(),num)