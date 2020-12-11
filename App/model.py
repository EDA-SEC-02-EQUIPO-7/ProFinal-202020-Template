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
import config
from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error
assert config
import datetime
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.DataStructures import mapentry as me


"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

# -----------------------------------------------------
#                       API
# -----------------------------------------------------

# Funciones para agregar informacion al grafo
def newAnalyzer():
    Taxis = {
        "Hash":None}
    Taxis["Hash"] = m.newMap(maptype='',
                            comparefunction=compareArea)
    Taxis["lst"] = ["00:00","00:15","00:30","00:45","01:00","01:15","01:30","01:45","02:00","02:15","02:30","02:45","03:00","03:15",
    "03:30","03:45","04:00","04:15","04:30","04:45","05:00","05:15","05:30","5:45","06:00","06:15","06:30","06:45","07:00",
    "07:15","07:30","07:45","08:00","08:15","08:30","08:45","09:00","09:15","09:30","09:45","10:00","10:15","10:30","10:45",
    "11:00","11:15","11:30","11:45","12:00","12:15","12:30","12:45","13:00","13:15","13:30","13:45","14:00","14:15","14:30",
    "14:45","15:00","15:15","15:30","15:45","16:00","16:15","16:30","16:45","17:00","17:15","17:30","17:45","18:00","18:15",
    "18:30","18:45","19:00","19:15","19:30","19:45","20:00","20:15","20:30","20:45","21:00","21:15","21:30","21:45","22:00",
    "22:15","22:30","22:45","23:00","23:15","23:30","23:45"]
    return Taxis

def addTrip (Taxis,trip):
    if (trip["trip_seconds"] != "") and (trip["pickup_community_area"] != trip["trip_start_timestamp"] ):
        origin = trip["pickup_community_area"]
        destination = trip["dropoff_community_area"]
        start_time = (trip["trip_start_timestamp"])[0:-4]
        start_time = start_time.replace("T"," ")
        start_time = datetime.datetime.strptime(start_time,'%Y-%m-%d %H:%M:%S') 
        start_time = compareTime(start_time)
        time = (trip["trip_seconds"])
        duration = int(float(time))
        if origin != destination:
            add_community_area(Taxis,origin,start_time)
            add_community_area(Taxis,destination,start_time)
            add_connection(Taxis,origin,destination,duration,start_time)

def create_Hash (Taxis):
    for i in Taxis["lst"]:
        timeHash = datetime.datetime.strptime(i,"%H:%M")
        EachGraph = gr.newGraph(datastructure="ADJ_LIST",
                                directed=True,
                                size=1000,
                                comparefunction=compareArea)
        m.put(Taxis["Hash"],timeHash.time(),EachGraph)

        
def add_connection(Taxis,origin, destination, duration,start_time):
    graph = me.getValue(m.get(Taxis["Hash"],start_time.time()))
    edge=gr.getEdge(graph,origin,destination)
    if edge is None:
        gr.addEdge(graph,origin,destination,duration)
    else:
        initial =edge["weight"]
        edge["weight"]=((int(initial)+int(duration))/2)

def add_community_area(Taxis, community_area,start_time):
    """
    Adiciona una estación como un vertice del grafo
    """
    Graph = me.getValue(m.get(Taxis["Hash"],start_time.time()))
    try:
        if not gr.containsVertex(Graph, community_area):
            gr.insertVertex(Graph, community_area)
        return Taxis
    except Exception as exp:
        error.reraise(exp, 'model:add_community_area')
 # ==============================
# Requerimientos 
# ==============================

def MejorHora(Taxis,límite_Inferior,límite_Superior,vertexA,vertexB):
    for i in Taxis["lst"]:
        timeHash = datetime.datetime.strptime(i,"%H:%M")
        if (timeHash.hour >= límite_Inferior.hour  ) and (timeHash.hour  <= límite_Superior.hour ):
            print (timeHash)



       

# ==============================
# Funciones de consulta
# ==============================

# ==============================
# Funciones Helper
# ==============================

# ==============================
# Funciones de Comparacion
# ==============================
def compareTime(hora):
    if hora.minute>=0 and hora.minute<7.5:
        hora=hora.replace(minute=0)
    if hora.minute>=7.5 and hora.minute<15:
        hora=hora.replace(minute=15)
    if hora.minute>=15 and hora.minute<22.5:
        hora=hora.replace(minute=15)
    if hora.minute>=22.5 and hora.minute<=30:
        hora=hora.replace(minute=30)
    if hora.minute>=30 and hora.minute<37.5:
        hora=hora.replace(minute=30)
    if hora.minute>=37.5 and hora.minute<45:
        hora=hora.replace(minute=45)
    if hora.minute>=45 and hora.minute<52.5:
        hora=hora.replace(minute=45)
    if hora.minute>=52.5 and hora.minute<60:
        hora=hora.replace(minute=30)
        x=hora.hour+1
        x%=24
        hora=hora.replace(hour=x)
    return hora

def compareArea (area1,area2):
    #Compara dos community_area
    area2 = area2['key']
    if (area1 == area2):
        return 0
    elif (area1 > area2):
        return 1
    else:
        return -1
    