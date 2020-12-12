import config
from DISClib.DataStructures import indexheapmax as h
assert config

"""
Implementación de una cola de prioridad indexada orientada a menor

Este código está basados en la implementación
propuesta por R.Sedgewick y Kevin Wayne en su libro
Algorithms, 4th Edition
"""


def newIndexMaxPQ(cmpfunction):
    """
    Crea un cola de prioridad indexada orientada a menor

    Args:
        cmpfunction: La funcion de comparacion
    Returns:
       Una nueva cola de prioridad indexada
    Raises:
        Exception
    """
    return h.newIndexHeapmax(cmpfunction)


def isEmpty(iminpq):
    """
    Informa si una cola de prioridad indexada es vacia

    Args:
        iminpq: La cola de prioridad indexada a revisar
    Returns:
       True si esta vacia
    Raises:
        Exception
    """
    return(h.isEmpty(iminpq))


def size(iminpq):
    """
    Retorna el número de elementos en la cola de prioridad indexada

    Args:
        iminpq: La cola de prioridad indexada a revisar
    Returns:
       El numero de elementos
    Raises:
        Exception
    """
    return(h.size(iminpq))


def insert(iminpq, key, index):
    """
    Inserta la llave key con prioridad index

    Args:
        iheap: La cola de prioridad
    Returns:
       La cola de prioridad con la nueva paraja indexada
    Raises:
        Exception
    """
    return h.insert(iminpq, key, index)


def delMax(imaxpq):
    """
    Elimina el elemento de mayor prioridad

    Args:
        iheap: El heap a revisar
    Returns:
       El numero de elementos
    Raises:
        Exception
    """
    return (h.delMax(imaxpq))


def decreaseKey(imaxpq, key, newindex):
    """
    Decrementa el indice de un llave

    Args:
        iheap: El heap a revisar
        key: la llave a decrementar
        newindex: El nuevo indice de la llave
    Returns:
       El numero de elementos
    Raises:
        Exception
    """
    return h.decreaseKey(imaxpq, key, newindex)


def increaseKey(imaxpq, key, newindex):
    """
    Incrementa el indice de un llave

    Args:
        iheap: El heap a revisar
        key: la llave a incrementar
        newindex: El nuevo indice de la llave
    Returns:
       El numero de elementos
    Raises:
        Exception
    """
    return h.increaseKey(imaxpq, key, newindex)


def max(imaxpq):
    """
    Retorna la llave de mayor prioridad

    Args:
        iheap: El heap a revisar
    Returns:
       El numero de elementos
    Raises:
        Exception
    """
    return h.max(imaxpq)


def contains(imaxpq, element):
    """
    Indica si la llave key se encuentra en el heap

    Args:
        iheap: El heap a revisar
    Returns:
       El numero de elementos
    Raises:
        Exception
    """
    return h.contains(imaxpq, element)