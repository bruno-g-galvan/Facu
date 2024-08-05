import os 
os.system("cls")
opcion = 1
while(opcion != 0):
     
     print("--------BIENVENIDO----------")
     print("Menu de Opciones:")
     print("Opción 1 - Declarar una lista vacia")
     print("Opción 2 - Ingresar el importe de 5 terrenos a la venta ")
     print("Opción 3 - Mostrar la lista de Terrenos")
     print("Opción 4 - Mostrar el valor del terreno mas caro") 
     print("Opción 5 - Mostrar los 2 terreno mas económicos de la lista") 
     print("Opción 6 - Mostrar el promedio de los valores ingresados")      
     print("Opción 0 - Salir")

     opcion = int(input("Elija una Opción Correcta: "))
     os.system("cls") # limpia la pantalla
     
     if opcion == 0:
          print("hasta luego...")
     elif opcion == 1:
        terrenos = [] 
        print("La lista de terrenos vacia fue declarada...")         
     elif opcion == 2:          
        print("Ingresar el precio de 5 terrenos a la venta: ")
        for x in range (5):
            precio = int(input("Ingrese Precio: "))
            terrenos.append(precio)
     elif opcion == 3:
         for x in range(5):
             print("POSICION: ",x," - Valor: ",terrenos[x])
     elif opcion == 4:
         terrenos.sort(reverse=True)
         print("El valor del terreno mas caro es: ",terrenos[0])
     elif opcion == 5:
          for x in range (2):
           print("Precio:",terrenos[x])    
           
     elif opcion == 6:
          suma = 0
          promedio = 0 
          for x in range(5):
            suma = suma + terrenos[x]      
          promedio = suma/len(terrenos)     
          print("El promedio es: ",promedio)
                
     else:
      print("Opcion Incorrecta:")