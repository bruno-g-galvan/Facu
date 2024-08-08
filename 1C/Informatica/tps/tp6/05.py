#Cargar dos listas A y B del mismo tamaño, N elementos al azar entre 1 y 99, realizar :


import random

def list_filler(lenght):
    list1 = []
    for _ in range(lenght):
        random_number = random.randint(1, 20)
        list1.append(random_number)
    
    return list1

#a. Suma A+B en una tercer lista, ejemplo.
def sum_lists(list1, list2):
    list3 = []
    for i in range(0, len(list1)):
        list3.append((list1[i] + list2[i]))

    return list3

#b. Concatenación de A con B, en una lista C (No usar facilidades de Python, resolver el algoritmo).
def concat_lists(list1, list2):
    list3 = []
    for i in list1:
        list3.append(i)
    for i in list2:
        list3.append(i)

    return list3

#c. Concatenación de A con B invertido, en una lista C.
def concat_lists_b_inverted(list1, list2):
    list3 = []
    for i in list1:
        list3.append(i)
    for i in range(len(list2), 0, -1):
        list3.append(list2[i - 1])

    return list3

#d. Crear otra lista C que contenga los elementos de A y B intercalados, comenzando por A.
def concat_lists_interspersed(list1, list2):
    list3 = []
    for i in range(0, len(list1)):
        list3.append(list1[i])
        list3.append(list2[i])

    return list3


longitud = int(input("Ingrese la longitud de las 2 listas: "))

lista1 = list_filler(longitud)
lista2 = list_filler(longitud)

print(lista1)
print(lista2)

print("Ejercicio A")
print(sum_lists(lista1, lista2))

print("Ejercicio B")
print(concat_lists(lista1, lista2))

print("Ejercicio C")
print(concat_lists_b_inverted(lista1, lista2))

print("Ejercicio D")
print(concat_lists_interspersed(lista1, lista2))