#Este es un modelo de menu de opciones

import os # importa las librerias para limpiar la pantalla
os.system("cls") # Esto limpia la pantalla

opcion = 1
while(opcion != 0):
     
     print("--------BIENVENIDO----------")
     print("Menu de Opciones:")
     print("Opción 1")
     print("Opción 2")
     print("Opción 3")
     print("Opción 0 - Salir")

     opcion = int(input("Elija una Opción Correcta: "))
     os.system("cls") # limpia la pantalla
     
     if opcion == 0:
          print("hasta luego...")

     elif opcion == 1:         
          print("Esta es la opcion 1: ")
     elif opcion == 2:         
          print("Esta es la opcion 2: ")
     elif opcion == 3:
          print("Esta es la opcion 3: ")
     else:
      print("Opcion Incorrecta:")
    
        