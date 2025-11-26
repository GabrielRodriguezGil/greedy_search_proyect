"""Modulo que contiene la funcion buscar_mejor_estación"""


# Definiremos una primera función que buscara la mejor estacion posible dentro del diccionario.

def buscar_mejor_estacion(estaciones, estados_cubiertos):
    estados_cubiertos = set(estados_cubiertos)
    mejor_estacion = ""
    mayor_num_cubierto = 0
    for estacion, estados_estacion in estaciones.items():

        nuevos_estados = estados_estacion - estados_cubiertos # definimos los nuevos estados que cubre esta estación.
       
        if len(nuevos_estados) > mayor_num_cubierto:
            mejor_estacion = estacion
            mayor_num_cubierto = len(nuevos_estados)

    return mayor_num_cubierto,mejor_estacion