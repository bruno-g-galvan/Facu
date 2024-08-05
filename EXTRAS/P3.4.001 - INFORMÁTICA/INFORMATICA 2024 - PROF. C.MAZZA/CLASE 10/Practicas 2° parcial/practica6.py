#Crear un menu de opciones con el siguiente detalle
#OPCION 1 - CREAR LISTA DE EMPLEADOS VACIA
#OPCION 2 - CARGAR 5 EMPLEADOS - POSICION ES EL NRO DE LEGAJO (EL VALOR DE X) 
#OPCION 3 - MOSTRAR LA LISTA EN FORMA HORIZONTAL
#OPCION 4 - MOSTRAR LA LISTA CON UN BUCLE CON EL NUMERO DE LEGAJO
#OPCION 5 - AGREGAR UN NUEVO EMPLEADO


import os # importa las librerias para limpiar la pantalla
os.system("cls") # Esto limpia la pantalla
opcion = 1
while(opcion != 0):
     
     print("--------BIENVENIDO----------")
     print("Menu de Opciones:")
     print("Opción 1 - CREAR LISTA DE EMPLEADOS VACIA")
     print("Opción 2 - CARGAR 5 EMPLEADOS - POSICION ES EL NRO DE LEGAJO (EL VALOR DE X) DESDE 100")
     print("Opción 3 - MOSTRAR LA LISTA EN FORMA HORIZONTAL ")
     print("Opcion 4 - MOSTRAR LA LISTA CON UN BUCLE CON EL NUMERO DE LEGAJO")
     print("Opcion 5 - AGREGAR EMPLEADO ")
     print("Opción 0 - Salir")

     opcion = int(input("Elija una Opción Correcta: "))
     os.system("cls") # limpia la pantalla
     
     if opcion == 0:
          print("hasta luego...")

     elif opcion == 1:
        lista_empleados = []
        print("La lista de empleados fue declarada...")
     elif opcion == 2:
           for x in range(5):
            empleado = input( "Apellido:")
            lista_empleados.append(empleado)
           largo = len(lista_empleados)
           os.system("cls")
     elif opcion == 3:
          print(lista_empleados)
          
     elif opcion == 4:
          for x in range (largo):
               print("Legajo: ",x," - Empleado: ",lista_empleados [x])  
               
     elif opcion == 5:
          nuevo = input("Ingrese nuevo empleado:")
          lista_empleados.append(nuevo)
          largo = largo+1      
     else:
      print("Opcion Incorrecta:")
    
        