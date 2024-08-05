import random

def cargarLista(cantidad):
    lista=[]
    
    for i in range(cantidad):
        lista.append(random.randint(1,100))
    return lista

def busquedaSecuencial(lista,dato):
    i=0
    
    while i<len(lista) and lista[i]!=dato:
        i+=1
    
    if i< len(lista):
        return i
    else:
        return -1


def imprimirLista(lista):
    for i in range(len(lista)):
        print(lista[i], end=" ")
        
        
def metodoSeleccion(lista):
    largo=len(lista)
    for i in range(largo-1):
        for j in range(i+1,largo):
            if lista[i]>lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
                
                
                
#Programa Principal
cant = int(input("¿Cuantos elementos desea cargar en la lista?\n"))
lista=cargarLista(cant)
imprimirLista(lista)

numBuscar = int(input("\nIngrese el valor que desea buscar\n"))

posicion= busquedaSecuencial(lista,numBuscar)

if posicion>=0:
    print("El elemento se encontro en la siguiente posicion: ",posicion)
else:
    print("El elemento no se encontro en la lista")
    
    


