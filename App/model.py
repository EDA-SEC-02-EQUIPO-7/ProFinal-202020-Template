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
from DISClib.ADT import orderedmap as om
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
from DISClib.ADT import indexmaxpq as imaxpq


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
                            comparefunction=compareStopIds)
    Taxis["lst"] = ["00:00","00:15","00:30","00:45","01:00","01:15","01:30","01:45","02:00","02:15","02:30","02:45","03:00","03:15","03:30","03:45","04:00","04:15","04:30","04:45","05:00","05:15","05:30","5:45","06:00","06:15","06:30","06:45","07:00","07:15","07:30","07:45","08:00","08:15","08:30","08:45","09:00","09:15","09:30","09:45","10:00","10:15","10:30","10:45","11:00","11:15","11:30","11:45","12:00","12:15","12:30","12:45","13:00","13:15","13:30","13:45","14:00","14:15","14:30","14:45","15:00","15:15","15:30","15:45","16:00","16:15","16:30","16:45","17:00","17:15","17:30","17:45","18:00","18:15","18:30","18:45","19:00","19:15","19:30","19:45","20:00","20:15","20:30","20:45","21:00","21:15","21:30","21:45","22:00","22:15","22:30","22:45","23:00","23:15","23:30","23:45"]
    Taxis["dateIndex"]=om.newMap(omaptype='BST',
                                comparefunction=compareDates)
    Taxis["Brand"]= m.newMap(maptype='',
                            comparefunction=compareStopIds)
    Taxis["ids"]=m.newMap(maptype='',
                            comparefunction=compareStopIds)
    Taxis["afiliado"]=imaxpq.newIndexMaxPQ(cmpimin)
    Taxis["servicio"]=imaxpq.newIndexMaxPQ(cmpimin)
    return Taxis

def addTrip (Taxis,trip):
    #if (trip["trip_seconds"] != "") and (trip["pickup_community_area"] != trip["dropoff_community_area"] ) and (trip["pickup_community_area"] != "") and(trip["dropoff_community_area"] != "") :
    #    origin = trip["pickup_community_area"]
    #    destination = trip["dropoff_community_area"]
    #    start_time = (trip["trip_start_timestamp"])[0:-4]
    #    start_time = start_time.replace("T"," ")
    #    start_time = datetime.datetime.strptime(start_time,'%Y-%m-%d %H:%M:%S') 
    #    start_time = compareTime(start_time)
    #    time = (trip["trip_seconds"])
    #    duration = int(float(time))
    #    if origin != destination:
    #        add_community_area(Taxis,origin,start_time)
    #        add_community_area(Taxis,destination,start_time)
    #        add_connection(Taxis,origin,destination,duration,start_time)
    #updateDateIndex(Taxis["dateIndex"],trip)
    addBrant(Taxis,trip["company"],trip["taxi_id"])
    #addTaxi(Taxis,trip["taxi_id"])

#def addTaxi(Taxis, id):
    #taxi=Taxis["ids"]
    #exist=m.contains(Taxis["ids"],id)
    #if exist:
    #    val=m.get(taxi,id)
    #    val["value"]+=1
    #else:
    #    m.put(taxi,id,1)  

def addBrant(Taxis,company, id):
    companies = Taxis["Brand"]
    existcompany = m.contains(Taxis["Brand"],company)
    if existcompany:
        entry = m.get(companies,company)
        producer = me.getValue(entry)
    else:
        producer = newCompany(company)
        m.put(companies, company, producer)
    lt.addLast(producer["Taxis"], id)
    centi=imaxpq.contains(Taxis["servicio"],producer["name"])
    if centi:
        imaxpq.increaseKey(Taxis["servicio"],producer["name"],lt.size(producer["Taxis"]))
    else:
        imaxpq.insert(Taxis["servicio"],producer["name"],lt.size(producer["Taxis"]))
    companies = producer["hash"]
    existcompany = m.contains(producer["hash"],id)
    if existcompany:
        entry = m.get(companies,id)
        entry["value"]+=1
    else:
        m.put(companies, id, 1)
    centi=imaxpq.contains(Taxis["afiliado"],producer["name"])
    if centi:
        imaxpq.increaseKey(Taxis["afiliado"],producer["name"],m.size(producer["hash"]))
    else:
        imaxpq.insert(Taxis["afiliado"],producer["name"],m.size(producer["hash"]))

    





def newCompany (producername):
    producer = {'name': None , "Taxis": None, }
    producer['name'] = producername
    producer['Taxis'] = lt.newList("ARRAY_LIST",CompareMoviesIds)
    producer["hash"]=m.newMap(maptype='',
                            comparefunction=compareStopIds)
    return producer
def newBrant (brantName):
     None

def updateDateIndex(map,trip):
    start_time = (trip["trip_start_timestamp"])[0:-4]
    start_time = start_time.replace("T"," ")
    dateTrip=datetime.datetime.strptime(start_time,'%Y-%m-%d %H:%M:%S')
    entry =om.get(map,dateTrip.date())
    if entry is None:
        datentry = newDataEntry(trip)
        om.put(map,dateTrip.date() , datentry)
    else:
        datentry = me.getValue(entry)
    addDate(datentry,trip)
def addDate(datentry,trip):
    maxpq=datentry["maxpq"]
    centi=imaxpq.contains(maxpq,trip["taxi_id"])
    if centi:
        val = m.get(maxpq['qpMap'], trip["taxi_id"])
        elem = lt.getElement(maxpq['elements'], val['value'])
        startpoints=elem["index"]
        if trip["trip_total"] =="":
            money=1
        else:
            money=float(trip["trip_total"])
        if trip["trip_miles"] =="":
            miles=1
        else:
            miles=float(trip["trip_miles"])
        elem["info"]["money"]+=money
        if elem["info"]["money"]==0:
            elem["info"]["money"]=1
        elem["info"]["miles"]+=miles
        elem["info"]["services"]+=1
        finalpoint=(elem["info"]["miles"]/elem["info"]["money"])*elem["info"]["services"]
        if finalpoint>=startpoints:
            imaxpq.increaseKey(maxpq,trip["taxi_id"],finalpoint)
        else:
            imaxpq.decreaseKey(maxpq,trip["taxi_id"],finalpoint)
    else:
        imaxpq.insert(maxpq,trip["taxi_id"],0)
        val = m.get(maxpq['qpMap'], trip["taxi_id"])
        elem = lt.getElement(maxpq['elements'], val['value'])
        elem["info"]={"money":0,"miles":0,"services":0}
        if trip["trip_total"] =="":
            money=1
        else:
            money=float(trip["trip_total"])
        elem["info"]["money"]+=money
        if elem["info"]["money"]==0:
            elem["info"]["money"]=1
        if trip["trip_miles"] =="":
            miles=1
        else:
            miles=float(trip["trip_miles"])
        elem["info"]["miles"]+=miles
        elem["info"]["services"]+=1
        point=(elem["info"]["miles"]/elem["info"]["money"])*elem["info"]["services"]
        imaxpq.increaseKey(maxpq,trip["taxi_id"],point)
def newDataEntry(trip):
    entry ={"maxpq":None}
    entry["maxpq"]=imaxpq.newIndexMaxPQ(cmpimin)
    return entry
def create_Hash (Taxis):
    for i in Taxis["lst"]:
        timeHash = datetime.datetime.strptime(i,"%H:%M")
        EachGraph = gr.newGraph(datastructure="ADJ_LIST",
                                directed=True,
                                size=100,
                                comparefunction=compareStopIds)
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
def req11(Taxis,n):
    res=lt.newList('SINGLELINKED', compareDates)
    contador=1
    while contador <=n:
        x=imaxpq.delMax(Taxis["servicio"])
        y=m.get(Taxis['Brand'],x)
        y=me.getValue(y)
        y=lt.size(y["Taxis"])
        dic={"company":x,"cantidad":y}
        lt.addLast(res,dic)
        contador+=1
    return res
    
def req12(Taxis,n):
    res=lt.newList('SINGLELINKED', compareDates)
    contador=1
    while contador <=n:
        x=imaxpq.delMax(Taxis["afiliado"])
        y=m.get(Taxis["Brand"],x)
        y=me.getValue(y)
        y=m.size(y["hash"])
        dic={"company":x,"cantidad":y}
        lt.addLast(res,dic)
        contador+=1
    return res

def MejorHora(Taxis,límite_Inferior,límite_Superior,vertexA,vertexB):
    Mejor = 200000
    lstHours = lt.newList("SINGLE_LINKED")
    for i in Taxis["lst"]:
        timeHash = datetime.datetime.strptime(i,"%H:%M")
        if (timeHash.hour >límite_Inferior.hour  ) and (timeHash.hour  < límite_Superior.hour ):
            lt.addLast(lstHours,timeHash)
        if(timeHash.hour == límite_Inferior.hour and timeHash.minute >= límite_Inferior.minute):
            lt.addLast(lstHours,timeHash)
        if (timeHash.hour == límite_Superior and timeHash.minute <= límite_Superior.minute):
            lt.addLast(lstHours,timeHash)
    listiterator =  it.newIterator(lstHours)
    while it.hasNext(listiterator ):
        start_time = it.next(listiterator)
        Graph = me.getValue(m.get(Taxis["Hash"],start_time.time()))
        dijsktra = djk.Dijkstra(Graph,vertexA)
        if djk.hasPathTo(dijsktra,vertexB):
            path = djk.pathTo(dijsktra,vertexB)
            path = lt.firstElement(path)
            if path["weight"] < Mejor:
                Mejor = path["weight"]
                Tiempo = start_time.time()
    return (Tiempo, Mejor)
   

# ==============================
# Funciones Helper
# ==============================
def req2(Taxis,date,num):
    num=int(num)
    date=om.get(Taxis["dateIndex"],date)
    pq=me.getValue(date)
    pq=(pq["maxpq"])
    contador=1
    res=lt.newList('SINGLELINKED', compareDates)
    while contador <=num:
        lt.addLast(res,imaxpq.delMax(pq))
        contador+=1
    return res
def req21(Taxis,date1,date2,num):
    num=int(num)
    dates=om.values(Taxis["dateIndex"],date1,date2)
    contador=1
    res=lt.newList('SINGLELINKED', compareDates)
    while contador <=num:
        mayor=0
        pos=0
        iter=0
        iterator = it.newIterator(dates)                
        while  it.hasNext(iterator):
            iter+=1
            element = it.next(iterator)
            pq=element["maxpq"]
            x=imaxpq.max(pq)
            if x != None:
                if x>mayor:
                    mayor=x
                    pos =iter
        pq=lt.getElement(dates,pos)
        pq=pq["maxpq"]
        y=imaxpq.delMax(pq)
        lt.addLast(res,y)
        contador+=1
    return res
def cmpimin(value1, value2):
    """
    Compara dos estaciones
    """
    value2 = value2['key']
    if (value1 == value2):
        return 0
    elif (value1 > value2):
        return 1
    else:
        return -1
# ==============================
# Funciones de Comparacion
# ==============================
def compareDates(date1, date2):
    """
    Compara dos ids de accidentes, id es un identificador
    y entry una pareja llave-valor
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
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

def compareStopIds(stop, keyvaluestop):
    """
    Compara dos estaciones
    """
    stopcode = keyvaluestop['key']
    if (stop == stopcode):
        return 0
    elif (stop > stopcode):
        return 1
    else:
        return -1
def compareHour (hour1,hour2):
    if (hour1.hour == hour2.hour) and (hour1.minute == hour2.minute):
        return 0
    elif (hour1.hour > hour2.hour):
        return 1 
    else:
        return -1

def CompareMoviesIds(id1, id2):
    """
    Compara dos ids de peliculas
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareMapMoviesIds(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > (int(identry))):
        return 1
    else:
        return -1