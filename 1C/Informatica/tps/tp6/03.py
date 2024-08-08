#Crear una lista con N valores al azar en un rango desde y hasta ingresado también desde el
#teclado. Imprimir el valor mínimo y el lugar que ocupa. Tener en cuenta que el mínimo puede
#estar repetido, en cuyo caso deberán mostrarse todas las posiciones que ocupe. No utilizar la
#función min, index o find de Python, debe resolver el algoritmo, puede crear sus propias
#funciones o resolverlo sin funciones.
import random

def list_filler(start, finish, lenght):
    list1 = []
    for _ in range(lenght):
        list1.append(random.randint(start, finish))
    
    return list1

def detector(lst):
    min_value = lst[0]
    indexes = [0]  

    for i in range(1, len(lst)):
        if lst[i] < min_value:
            min_value = lst[i]
            indexes = [i]  
        elif lst[i] == min_value:
            indexes.append(i)

    return min_value, indexes

desde = int(input("Ingrese el valor desde el cual se produciran valores: "))

while desde < 0:
    desde = int(input("Ingrese un valor positivo valido: "))

hasta = int(input("Ingrese el valor hasta el cual se produciran valores (debe ser mayor al ingresado anteriormente): "))

while hasta < desde:
    hasta = int(input("Ingrese un valor positivo valido mayor al ingresado anteriormente: "))

longitud = int(input("Ingrese la longitud de la cadena: "))

while longitud < 0:
    longitud = int(input("Ingrese un valor positivo valido: "))

lista = list_filler(desde, hasta, longitud)

print(lista)

minimo, indices = detector(lista)
print("Se detecto", minimo, "como el minimo numero en el/los indice/s de la lista" ,indices)
