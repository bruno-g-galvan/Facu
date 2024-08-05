#Declarar una lista con 5 elementos numericos
# crear un menu de opciones segun el siguiente detalle
#Opción 1 = Mostrar la lista (horizontal)
#Opción 2 = Mostrar el primer elemento de la lista
#Opción 3 = Mostrar la lista ordenada

import os 
os.system("cls")
lista1 = [5,9,0,11,25]
opcion = 1
while(opcion != 0):
     print("--------BIENVENIDO----------")
     print("Menu de Opciones:")
     print("Opción 1 - Mostrar la lista (horizontal)")
     print("Opción 2 - Mostrar el primer elemento de la lista ")
     print("Opción 3 - Mostrar la lista ordenada")
     print("Opción 0 - Salir")

     opcion = int(input("Elija una Opción Correcta: "))
     os.system("cls") # limpia la pantalla
     
     if opcion == 0:
          print("hasta luego...")

     elif opcion == 1:
        print("Mostrando lista 1...") 
        print(lista1)
     elif opcion == 2:          
        print("El primer elemento de la lista es: ",lista1[0])
     elif opcion == 3:
          lista1.sort()  
          print("Mostrando la lista ordenada...")        
          print(lista1)
     else:
      print("Opcion Incorrecta:")