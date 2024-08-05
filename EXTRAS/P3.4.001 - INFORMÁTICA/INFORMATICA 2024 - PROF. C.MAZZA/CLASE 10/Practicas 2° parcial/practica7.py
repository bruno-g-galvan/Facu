#Crear un menu de opciones segun el siguiente detalle
#Opción 1 = Declarar una lista vacia. Mostrar un mensaje "Lista declarada"
#Opción 2 = Solicitar al usuario que ingrese los Valores de 6 propiedades a la venta y cargarlos en una lista (utilizar un bucle for)
#Opción 3 = Ordenar la lista de mayor a menor - Mostrar mensaje "Lista ordenada"
#Opcion 4 = Mostrar los 3 primeros valores mas altos
#Opcion 5 = Mostrar los 3 valores mas bajos
#Opcion 6 = Mostrar el promedio de TODAS las propiedades ingresadas

import os 
os.system("cls")
opcion = 1
while(opcion != 0):
     
     print("--------BIENVENIDO----------")
     print("Menu de Opciones:")
     print("Opción 1 - Declarar una lista vacia")
     print("Opción 2 - Ingresar el importe de 6 propiedades a la venta ")
     print("Opción 3 - Ordenar la lista")
     print("Opción 4 - Mostrar los primeros 3 valores mas altos") 
     print("Opción 5 - Mostrar los primeros 3 valores mas bajos") 
     print("Opción 6 - Mostrar el promedio") 
     
     print("Opción 0 - Salir")

     opcion = int(input("Elija una Opción Correcta: "))
     os.system("cls") # limpia la pantalla
     
     if opcion == 0:
          print("hasta luego...")
     elif opcion == 1:
        propiedades = [] 
        print("La lista vacia fue declarada...")         
     elif opcion == 2:          
        print("Ingresar el precio de 6 Propiedades a la venta: ")
        for x in range (6):
            precio = int(input("Ingrese Precio: "))
            propiedades.append(precio)
     elif opcion == 3:
        
         propiedades.sort(reverse=True)
         print("La lista fue ordenada de menor a mayor...")
     elif opcion == 4:
          for x in range (3):
              print("Precio:",propiedades[x])
              
     elif opcion == 5:
          propiedades.sort()
          for x in range (3):
           print("Precio:",propiedades[x])    
           
     elif opcion == 6:
          suma = 0
          promedio = 0 
          for x in range(6):
            suma = suma + propiedades[x]      
          promedio = suma/len(propiedades)     
          print("El promedio es: ",promedio)
                
     else:
      print("Opcion Incorrecta:")