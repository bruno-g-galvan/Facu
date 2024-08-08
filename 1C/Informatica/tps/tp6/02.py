#Crear una lista con valores positivos desde el teclado hasta ingresar -1. Luego recorrer la lista
#para duplicar el valor de aquellos elementos que sean menores al promedio de los valores
#ingresados.

import random

def list_filler():
    list1 = []
    number = int(input("Ingrese un valor para ingresar en la lista o -1 para terminar: "))
    while number != -1:
        if number > 0:
            list1.append(number)
            number = int(input("Ingrese un valor positivo o -1 para terminar: "))
        else:
            number = int(input("Ingrese un valor positivo valido o -1 para terminar: "))
    return list1

def prom_generator(list):
    sum = 0
    for i in list:
        sum = i + sum
        prom = sum / len(list)
    
    return prom

def duplicator(prom, list):

    list2 = list[:]
    for i in range(len(list2)):
        if list2[i] < prom:
            list2[i] *= 2

    return list2


lista = list_filler()
promedio = prom_generator(lista)

lista2 = duplicator(promedio, lista)

print("La lista sin analizar es", lista, ". El promedio es", promedio, "y la lista con valores duplicados es", lista2)






#limitador = int(input("Ingrese la cantidad de valores que desea que tenga la lista: "))
#promedio, lista_final = generador(limitador)
#
#print("El promedio es", promedio, "y los numeros que superan el promedio son", lista_final)