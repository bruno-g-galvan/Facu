
#Realizar Python
# Escribir una función para ingresar números
# enteros en una lista y devolverla como valor de
# retorno.
# La cantidad de valores a leer se recibe como
# parámetro.

def cargarLista(cantidad):
    lista=[]
    for i in range(cantidad):
        numero=int(input("Ingrese un numero \n"))
        lista.append(numero)
    return lista 

#Ejercicio 1
#Escribir una función para ingresar desde el teclado una serie de números entre A 
#y B y guardarlos en una lista. En caso de ingresar un valor fuera de rango la 
# función mostrará un mensaje de error y solicitará un nuevo número. Para finalizar la 
#carga se deberá ingresar -1. La función recibe como parámetros los valores de A 
#y B, y devuelve la lista cargada (o vacía, si el usuario no ingresó nada) como 
#valor de retorno. Tener en cuenta que A puede ser mayor, menor o igual a B.

def cargarNumerosEntreExtremos(a,b):
    lista=[]
    
    if a>b: 
        aux=a
        a=b
        b=aux
    bandera=True
    while bandera:
        num=int(input("Ingrese un número\n"))
        if num==-1:
            bandera=False
        elif num<a or num>b:
            print("Valor inválido")
        else:
            lista.append(num)
    return lista
                
#Ejercicio 2: Calcular la suma de los números de la lista.

def calcularSuma(lista):
    total=0
    for i in range(len(lista)):
        total+=lista[i]
    return total 

#Ejercicio 3: Determinar si la lista es capicúa (palíndromo). Una lista capicúa se lee de igual 
#modo de izquierda a derecha y de derecha a izquierda. Por ejemplo, [2, 7, 7, 2] 
#es capicúa, mientras que [2, 7, 5, 2] no lo es.

def determinarCapicua(lista):
    listaInversa=[]
    for i in range(len(lista),0,-1):
        listaInversa.append(lista[i-1])
    
    for i in range(len(lista)):
        if lista[i]!=listaInversa[i]:
            return False
    return True 


#Ejercicio 4: Escribir una función para contar cuántas veces aparece un valor dentro de la 
#lista. La función recibe como parámetros la lista y el valor a buscar, y devuelve 
#un número entero.

def contarApariciones(lista,numero):
    cantidad=0
    for i in range(len(lista)):
        if lista[i]==numero:
            cantidad+=1
    return cantidad

#Desarrollar una función que reciba la lista como parámetro y devuelva una nueva 
#lista con los mismos elementos de la primera, pero en orden inverso. Por 
#ejemplo, si la función recibe [5, 7, 1] debe devolver [1, 7, 5]

def invertirLista(lista):
    listaInversa=[]
    for i in range(len(lista),0,-1):
        listaInversa.append(lista[i-1])
    return listaInversa

#Programa Principal

listaPepe=[7,7,8,9,4,5,6,7]

print("Apariciones",contarApariciones(listaPepe,7))

listita=[1,4,4,2]

print("Es capicua?",determinarCapicua(listita))

min= int(input("Ingrese el valor desde que desea ingresar numeros\n"))
max= int(input("Ingrese el valor hasta que desea ingresar numeros\n"))

lista=cargarNumerosEntreExtremos(min,max)
print(lista)
print("La suma de los valores de la lista es: ",calcularSuma(lista))

"""tamanio=6
lita=[0]*tamanio
cant=int(input("Ingrese la cantidad de elementos que desea que tenga la lista\n"))
listita=cargarLista(cant)



print(listita)    

for i in range(101):
    print(i)

"""
"""
listaNumeros=[]
cont=0

while cont<3:
    numerito=int(input("Ingrese un número\n"))
    listaNumeros.append(numerito)
    cont+=1


print("Los numeros de mayor a menor")
cont=2
while cont>=0:
    print(listaNumeros[cont])
    cont-=1

print("Impresión de lista con for ")
listita=[6,7,8,14,15]

for i in range(len(listita)):
    print(listita[i], end=" ")
   
  
    
    #Leer 50 numeros enteros, calcular su promedio 
    #e imprimir aquellos valores leidos que sean mayores al promedio
   
ELEMENTOS=5
numerosEnteros=[]
suma=0

for i in range(ELEMENTOS):
    numerito=int(input("Ingrese un número\n"))
    numerosEnteros.append(numerito)
    suma+=numerito 

print(numerosEnteros)

promedio=suma/ELEMENTOS

print("El promedio de los números ingresados es: ",promedio)

print("Los valores que se encuentran por encima del promedio son:\n ")
for i in range(len(numerosEnteros)):
    if numerosEnteros[i]>promedio:
        print(numerosEnteros[i])
"""
#Leer un conjunto de números y guardarlos en una lista, finalizando la carga con -1
#Luego buscar el mayor elemento leido, mostrarlo y eliminarlo de la lista. 
#Imprimir la lista antes y despues 
"""
listaNumeros=[]
bandera=True
mayor=0
while bandera:
    numero=int(input("Ingrese un numero\n"))
    if numero==-1:
        bandera=False
    else:
        listaNumeros.append(numero)
        if numero>mayor:
            mayor=numero
    
del listaNumeros[9]

range(5)
"""





