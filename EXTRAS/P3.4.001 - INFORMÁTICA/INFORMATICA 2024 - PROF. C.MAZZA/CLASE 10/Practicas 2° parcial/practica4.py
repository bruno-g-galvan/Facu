#Crear un menu de opciones segun el siguiente detalle
#Opción 1 = Declarar una lista vacia. Mostrar un mensaje "Lista declarada"
#Opción 2 = solicitar al usuario que ingrese 3 elementos numericos a la lista (utilizar un bucle for)
#Opción 3 = solicitar al usuario que ingrese un nuevo elemento
#Opcion 4 = Mostrar la lista con un bucle mostrando la posicion y el valor
import os 
os.system("cls")
opcion = 1
while(opcion != 0):
     
     print("--------BIENVENIDO----------")
     print("Menu de Opciones:")
     print("Opción 1 - Declarar una lista vacia")
     print("Opción 2 - Cargar la lista con 3 elementos numéricos ")
     print("Opción 3 - Agregar un nuevo elemento")
     print("Opción 4 - Mostrar la lista:  POSICION - ELEMENTO") 
     print("Opción 0 - Salir")

     opcion = int(input("Elija una Opción Correcta: "))
     os.system("cls") # limpia la pantalla
     
     if opcion == 0:
          print("hasta luego...")
     elif opcion == 1:
        lista3 = [] 
        print("La lista vacia fue declarada...")         
     elif opcion == 2:          
        print("Ingresar 3 elemento a la lista: ")
        for x in range (3):
            valor = int(input("Ingrese valor: "))
            lista3.append(valor)
     elif opcion == 3:
          nuevo = int(input("Ingrese un nuevo valor: "))
          lista3.append(nuevo)
          largo = len(lista3)
     elif opcion == 4:
          for x in range (largo):
              print("Posicion: ",x," - Elemento: ",lista3[x])
     else:
      print("Opcion Incorrecta:")