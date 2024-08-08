#Dada una lista ordenada de números llamada A y un nuevo número N, desarrollar un programa
#que agregue el elemento N dentro de la lista A, respetando el ordenamiento existente. El
#programa deberá detectar automáticamente si el ordenamiento es ascendente o descendente
#antes de realizar la inserción. No utilizar facilidades de Python para resolver, crear el algoritmo
#para insertar un elemento en una lista.

import modlists

#Burbujeo asc
def ord_bubble_asc(lst):
    for _ in range(0, len(lst)):
        for i in range(1, len(lst)):
            if lst[i] < lst[i - 1]:
                aux = lst[i]
                lst[i] = lst[i - 1]
                lst[i - 1] = aux

    return lst

#Burbujeo desc
def ord_bubble_desc(lst):
    for _ in range(0, len(lst)):
        for i in range(1, len(lst)):
            if lst[i] > lst[i - 1]:
                aux = lst[i]
                lst[i] = lst[i - 1]
                lst[i - 1] = aux

    return lst

def num_insert(num, lst):
    if lst[0] > lst[1]: #Desc
        for i in range(0, len(lst) - 1):
            if num >= lst[i]:
                    aux = lst[i]
                    lst[i] = num
                    num = lst[i + 1]
                    lst[i + 1] = aux
        lst.append(num)
    else: #Asc
        for i in range(0, len(lst) - 1):
            if num <= lst[i]:
                    aux = lst[i]
                    lst[i] = num
                    num = lst[i + 1]
                    lst[i + 1] = aux
        lst.append(num)
    return lst

lista = []
cont = 0
numero = int(input("Ingrese un numero para rellenar la lista (-1 termina la ingesta): "))

while numero != -1:
    if modlists.num_in_lst(numero, lista):
        print("Numero repetido en lista, pruebe nuevamente.")
    else:
        lista.append(numero)
    numero = int(input("Ingrese un numero para rellenar la lista (-1 termina el programa): "))

print("Lista sin valores repetidos:", lista)
ordenamiento = int(input("Ingrese 0 o 1 para elegir entre ordenamiento asc o desc respectivamente: "))

while ordenamiento != 0 and ordenamiento != 1:
    ordenamiento = int(input("Ingrese 0 o 1 para elegir entre ordenamiento asc o desc respectivamente: "))

if ordenamiento == 0:
    print("Lista ordenada ascendentemente usando burbujeo:", ord_bubble_asc(lista))
else:
    print("Lista ordenada descendentemente usando burbujeo:", ord_bubble_desc(lista))

numero = int(input("Ingrese un numero para insertar dentro de la lista ordenada: "))

print("Lista con el numero insertada:", num_insert(numero, lista))



