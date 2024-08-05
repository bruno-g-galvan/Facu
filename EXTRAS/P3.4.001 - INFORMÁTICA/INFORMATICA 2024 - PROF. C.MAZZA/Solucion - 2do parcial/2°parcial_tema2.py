import os 
os.system("cls")
opcion = 1
while(opcion != 0):
     
     print("--------BIENVENIDO----------")
     print("Menu de Opciones:")
     print("Opción 1 - Declarar una lista vacia")
     print("Opción 2 - Ingresar el importe de 4 U.F a la venta ")
     print("Opción 3 - Mostrar la lista de Unidades Funcionales")
     print("Opción 4 - Mostrar el valor de la U.F. más económica") 
     print("Opción 5 - Mostrar el valor de las 3 U.F. más caras de la lista") 
     print("Opción 6 - Mostrar el promedio de los valores ingresados")      
     print("Opción 0 - Salir")

     opcion = int(input("Elija una Opción Correcta: "))
     os.system("cls") # limpia la pantalla
     
     if opcion == 0:
          print("hasta luego...")
     elif opcion == 1:
        depto = [] 
        print("La lista de UF vacia fue declarada...")         
     elif opcion == 2:          
        print("Ingresar el precio de 4 UF a la venta: ")
        for x in range (4):
            precio = int(input("Ingrese Precio: "))
            depto.append(precio)
     elif opcion == 3:
         for x in range(4):
             print("UF: ",x," - Valor: ",depto[x])
     elif opcion == 4:
         depto.sort()
         print("El valor de la UF más económica es: ",depto[0])
     elif opcion == 5:
          for x in range (2,4):
           print("Precio:",depto[x])    
           
     elif opcion == 6:
          suma = 0
          promedio = 0 
          for x in range(4):
            suma = suma + depto[x]      
          promedio = suma/len(depto)     
          print("El promedio es: ",promedio)
                
     else:
      print("Opcion Incorrecta:")