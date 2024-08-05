import random

# Cargar una lista con números al azar entre 1 y 100,
# donde la cantidad de elementos será ingresada
# por el usuario.
# Luego se solicita leer un valor y buscarlo en la lista
# mediante una función, devolviendo su ubicación o
# -1 si no se la encuentra
def cargarLista(cantidad):
    lista=[]
    for i in range(cantidad):
        numero=random.randint(1,100)
        lista.append(numero)
    return lista

def busqSecuencial(lista,valor):
    for i in range(len(lista)):
        if valor==lista[i]:
            return i
    return -1

#Programa Principal
cuantos=int(input("Ingrese la cantidad de dados que desea lanzar?\n"))
while cuantos>0:
    dado=random.randint(1,6)
    print(dado,end=" ")
    cuantos-=1
    
lista1=[9,8,5,6,3,2,1]
lista2=[]
print("\n Ejercicio 2 ")
for i in range(len(lista1)):
    lista2.append(lista1[i])
lista2.append(10)

print(lista1)
print(lista2)


#Invocación Ejercicio 2
cantElementos=int(input("Ingrese la cantidad de elementos de la lista\n"))
lista=cargarLista(cantElementos)
print(lista)

print("Busqueda :")
print(busqSecuencial(lista,61))