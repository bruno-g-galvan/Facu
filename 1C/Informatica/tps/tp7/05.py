#Crear una lista sin elementos repetidos, ordenarla por un método a elección y mostrar por
#pantalla. Ingresar por teclado números positivos hasta ingresar -1, indicar en qué posición se
#encuentra utilizando búsqueda binaria si el valor se no encuentra mostrar un mensaje
#aclaratorio. Al finalizar las búsquedas informar cuántas búsquedas resultaron satisfactorias.

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
print("Lista ordenada ascendentemente usando burbujeo:", ord_bubble_asc(lista))


numero = int(input("Ingrese el numero que desea identificar en la lista (-1 termina el programa): "))

while numero != -1:
    if modlists.bin_search_val(numero, lista):
        print("El numero se encuentra en la lista.")
        cont = cont + 1
    else:
        print("El numero no se encuentra en la lista.")
    numero = int(input("Ingrese el numero que desea identificar en la lista (-1 termina el programa): "))

print("Las busquedas exitosas fueron:", cont)



