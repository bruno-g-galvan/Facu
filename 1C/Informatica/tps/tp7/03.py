#Escribir una función para devolver la posición que ocupa un valor pasado como parámetro,
#utilizando búsqueda secuencial en una lista desordenada. La función debe devolver -1 si el
#elemento no se encuentra en la lista.

import modlists

desde = int(input("Ingrese desde que numero desea generar los valores (por ejemplo 1): "))
hasta = int(input("Ingrese hasta que numero desea generar los valores (por ejemplo 20): "))
longitud = int(input("Ingrese el valor de numeros enteros que desea en la lista: "))

lista = modlists.generate_random_lst(desde, hasta, longitud)
print("Lista generada con exito.")

numero = int(input("Ingrese ahora el valor a buscar en esta lista y su posicion en ella: "))
indice = modlists.num_in_lst_index(numero, lista)
if indice != -1:
    print("La primer aparicion de ese numero es en el indice:", indice)
else:
    print("El numero no se encuentra en la lista.")