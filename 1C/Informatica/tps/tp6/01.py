#Crear una lista con valores al azar entre 1 y 20. Mostrar los elementos que superan el promedio
#de los valores ingresados.
import random

def generator(limit):
    list1 = []
    list2 = []
    sum = 0
    for _ in range(limit):
        random_number = random.randint(1, 20)
        list1.append(random_number)
    
    for i in range(len(list1)):
        sum = list1[i] + sum
    
    prom = sum / len(list1)

    for i in range(len(list1)):
        if list1[i] > prom:
            list2.append(list1[i])

    return prom, list2

limitador = int(input("Ingrese la cantidad de valores que desea que tenga la lista: "))
promedio, lista_final = generator(limitador)

print("El promedio es", promedio, "y los numeros que superan el promedio son", lista_final)
