#Crear un menu de opciones segun el siguiente detalle
#Opción 1 = Crear lista de subastas (vacia)
#Opción 2 = Ingresar oferta
#Opción 3 = Indicar cual fue la oferta mas alta
#Opción 4 = Indicar cual fue la oferta mas baja
#Opcion 5 = Mostrar el promedio
import os 
os.system("cls")
opcion = 1
while(opcion != 0):
     
     print("--------BIENVENIDO----------")
     print("Menu de Opciones:")
     print("Opción 1 - Crear lista de subastas (vacia)")
     print("Opción 2 - Ingresar 5 ofertas ")
     print("Opción 3 - Indicar cual fue la oferta mas alta")
     print("Opción 4 - Indicar cual fue la oferta mas baja") 
     print("Opcion 5 - Mostrar el promedio de las ofertas ingresadas")
     print("Opción 0 - Salir")

     opcion = int(input("Elija una Opción Correcta: "))
     os.system("cls") # limpia la pantalla
     
     if opcion == 0:
          print("hasta luego...")
     elif opcion == 1:
        subastas = [] 
        print("La lista de subastas vacias fue declarada...")         
     elif opcion == 2:          
        print("Ingresar 5 ofertas: ")
         
        for x in range (5):
           oferta = int(input("Ingrese Oferta: "))
           subastas.append(oferta)
     elif opcion == 3:
          mayor_oferta = subastas[0]
          for x in range(1,5):
               if subastas[x]>mayor_oferta:
                    mayor_oferta = subastas[x] 
          print("La oferta mas alta fue: ",mayor_oferta)          
                             
     elif opcion == 4:          
        menor_oferta = subastas[0]
        for x in range(1,5):
               if subastas[x]<menor_oferta:
                    menor_oferta = subastas[x] 
        print("La oferta mas baja fue: ",menor_oferta)          
     elif opcion == 5:
          suma = 0
          for x in range(5):
            suma = suma+subastas[x]
          promedio = suma/5         
          print("El promedio es: ",promedio)               
     else:
      print("Opcion Incorrecta:")