#Crear tres listas y ordenarlas en forma ascendente utilizando un método para cada lista:
#métodos de selección, inserción y burbujeo. ¿Qué cambia para ordenar en forma
#descendente?

import modlists

#Seleccion asc
def ord_selection_asc(lst):
    aux = 0
    for i in range(len(lst)):
        min = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min]:
                min = j

        if min != i:
            aux = lst[i]
            lst[i] = lst[min]
            lst[min] = aux

    return lst

#Insercion asc
def ord_insertion_asc(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1

        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j + 1] = key

    return lst

#Burbujeo asc
def ord_bubble_asc(lst):
    for _ in range(0, len(lst)):
        for i in range(1, len(lst)):
            if lst[i] <= lst[i - 1]:
                aux = lst[i]
                lst[i] = lst[i - 1]
                lst[i - 1] = aux

    return lst

#Seleccion desc
def ord_selection_desc(lst):
    aux = 0
    for i in range(len(lst)):
        min = i
        for j in range(i + 1, len(lst)):

            #Cambio de < a >
            if lst[j] > lst[min]:
                min = j

        if min != i:
            aux = lst[i]
            lst[i] = lst[min]
            lst[min] = aux

    return lst

#Insercion desc
def ord_insertion_desc(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1

        #Cambio de < a >=
        while j >= 0 and key >= lst[j]:
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j + 1] = key

    return lst

#Burbujeo desc
def ord_bubble_desc(lst):
    for _ in range(0, len(lst)):
        for i in range(1, len(lst)):
            #Cambio de > a <=
            if lst[i] > lst[i - 1]:
                aux = lst[i]
                lst[i] = lst[i - 1]
                lst[i - 1] = aux

    return lst

desde = int(input("Ingrese desde que numero desea generar los valores (por ejemplo 1): "))
hasta = int(input("Ingrese hasta que numero desea generar los valores (por ejemplo 20): "))

longitud = int(input("Ingrese el valor de numeros enteros que desea en la lista: "))

lista1 = modlists.generate_random_lst(desde, hasta, longitud)
print("Lista1 generada con exito.")
print(lista1)

longitud = int(input("Ingrese el valor de numeros enteros que desea en la lista: "))

lista2 = modlists.generate_random_lst(desde, hasta, longitud)
print("Lista2 generada con exito.")
print(lista2)

longitud = int(input("Ingrese el valor de numeros enteros que desea en la lista: "))

lista3 = modlists.generate_random_lst(desde, hasta, longitud)
print("Lista3 generada con exito.")
print(lista3)

print("---")
print("Lista1 ordenada ascendentemente usando seleccion:")
print(ord_selection_asc(lista1))

print("---")
print("Lista1 ordenada descendientemente usando seleccion:")
print(ord_selection_desc(lista1))

print("---")
print("Lista2 ordenada ascendentemente usando insercion:")
print(ord_insertion_asc(lista2))

print("---")
print("Lista2 ordenada descendientemente usando insercion:")
print(ord_insertion_desc(lista2))

print("---")
print("Lista3 ordenada ascendentemente usando burbujeo:")
print(ord_bubble_asc(lista3))

print("---")
print("Lista3 ordenada descendientemente usando burbujeo:")
print(ord_bubble_desc(lista3))



