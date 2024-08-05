import random

#Cargar una lista con números al azar entre 1 y 100, 
# donde la cantidad de elementos será ingresada por el usuario. 
#Luego se solicita leer un valor y buscarlo en la lista 
# mediante una función, devolviendo su ubicación o -1 si no se la encuentra

def cargarLista(cantidad):
    lista=[]
    
    for i in range(cantidad):
        lista.append(random.randint(1,100))
    return lista 

def buscarElemento(lista,elemento):
    for i in range(len(lista)):
        if lista[i]==elemento:
            return i 
    return -1
"""    i=0
    while i<len(lista) and lista[i]!=elemento:
        i+=1
        
    if i<len(lista):
        return i
    else: 
        return -1
"""


"""cuantos= int(input("Ingrese la cantidad de dados que desea arrojaar\n"))

for i in range(cuantos):
    dado=random.randint(1,6)
    print(dado, end=" ")"""

#Programa Principal
cantidad= int(input("Ingrese la cantidad de elementos que desea que tenga la lista\n"))

lista=cargarLista(cantidad)

print(lista)
numeroBuscado=int(input("Ingrese el número que desea buscar en la lista\n"))

posicion=buscarElemento(lista,numeroBuscado)


if posicion>=0:
    print("El numero se encuentra en la posición ",posicion)
else:
    print("El numero no se encuentra en la lista")
    
