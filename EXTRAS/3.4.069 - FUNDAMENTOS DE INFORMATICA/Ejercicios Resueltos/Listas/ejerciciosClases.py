import random
#1) Crear una lista vacia y agregar números del 1 al 10 usando un bucle for
def crearLista():
    lista=[]
    for i in range(1,11):
        lista.append(i)
    return lista
#Rellenar una lista con números enteros entre 0 y 100 obtenidos al azar e imprimir el valor mínimo y el lugar que ocupa. Tener en cuenta que el mínimo puede 
#estar repetido, en cuyo caso deberán mostrarse todas las posiciones en las que  se encuentre. La carga de datos termina cuando se obtenga un 0 como número 
#al azar, el que no deberá cargarse en la lista
#Función para cargar lista aleatoria
def cargarLista():
    print("Ingreso a la función")
    lista=[]
    bandera=True
    while bandera:
        numero=random.randint(0,100)
        if numero==0:
            bandera=False
        else: 
            lista.append(numero)
    return lista


def buscarMinimo(lista):
    minimo=None
    posiciones=[]
    
    for i in range(len(lista)):
        if minimo==None or lista[i]<minimo:
            minimo=lista[i]
            
    for i in range(len(lista)):
        if lista[i]==minimo:
            posiciones.append(i)
    return minimo,posiciones 


#Crear una lista de N números generados al azar entre 
# 0 y 100 pero sin elementos repetidos. 
# El valor de N se ingresa por teclado. 
# Resolver este problema utilizando dos estrategias distintas:
#Impidiendo el agregado de elementos repetidos
# Eliminando los duplicados luego de generar la lista. Asegurarse que la 
# cantidad final de elementos sea la solicitada

def cargarListaConElementos(n):
    lista=[]
    while len(lista)<n:
        numero=random.randint(0,100)
        presente=False
        contador=0
        while presente==False and contador<len(lista):
            if(lista[contador]==numero):
                presente=True
            contador+=1
        if not presente:
            lista.append(numero)
    return lista   


def eliminarDuplicados(lista):
    posInicial=0
    while posInicial<len(lista):
        posMasUno=posInicial+1
        while posMasUno<len(lista):
            if lista[posMasUno]==lista[posInicial]:
                del lista[posMasUno]
            else:
                posMasUno+=1
        posInicial+=1
    
    return lista 
                
    
        
def creaarLista(n):
    lista=[]
    for i in range(n):
        num=random.randint(1,16)
        while num in lista:
            num=random.randint(1,16)
        lista.append(num)
           
    return lista
 

 
    

        
    



#2) Realizar una función que sume todos los valores de una lista
def sumarLista(lista):
    suma=0
    for i in range(len(lista)):
        suma+=lista[i]
    return suma 

#3) Realizar una función que informe el máximo de una lista
def informarMaximo(lista):
        max=lista[0]
        for i in range(len(lista)):
            if lista[i]>max:
                max=lista[i]
        return max
#4) Implementar una función que busque un valor en la lista y retorne su índice o -1 si no se encuentra
def busqSecuencial(lista,valor):
    for i in range(len(lista)):
        if valor==lista[i]:
            return i
    return -1

#7) Encontrar el segundo mayor número en una lista 
def encontrarSegundoMayor(lista):
    if len(lista)<2:
        return -1 
    else:
        max=informarMaximo(lista)
        segundoMaximo=None 
        for i in range(len(lista)):
             if (segundoMaximo==None and lista[i]!=max) or (lista[i]<max and lista[i]>segundoMaximo):   
                segundoMaximo=lista[i]
        return segundoMaximo
    
    
    

#Programa Principal
#Invocación Ejercicio 1
print("Ejercicio 1")
lista= crearLista()
print(lista)

#Invocación Ejercicio 2
print("Ejercicio 2")
print(sumarLista(lista))

#Invocación Ejercicio 3
print("Ejercicio 3")
if len(lista)==0:
    print("Error ")
else:
    print(informarMaximo(lista))   
    
#Invocación Ejercicio 7
print("Ejercicio 7")
print(encontrarSegundoMayor([15,15,9,5,6,14,8,7,16,23,23]))

print("Invocar ejercicio 8")

lista=cargarLista()
print(lista)


print("Buscar Minimo")
print(buscarMinimo(lista))


print("Solucion eliminando duplicados")
print(creaarLista(15))