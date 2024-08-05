# Escribir un programa para ingresar por teclado los años de antigüedad de cada socio de un
# club.
# El club posee 3 categorías, dependiendo de la cantidad de años que tenga cada socio.
# Categoría 1 (1 a 12 años de antigüedad)
# Categoría 2 (13 a 25 años de antigüedad)
# Categoría 3 (26 años o más).
# El fin de los datos se indica ingresando -1.
# Se solicita imprimir un informe que contenga:
# - Cantidad total de personas que son socios del club.
# - Cantidad de socios por categoría.
# - Promedio de antigüedad de todos los socios de cada categoría


bandera=True
categoria1=0
antcat1=0
categoria2=0
antcat2=0
categoria3=0
antcat3=0
totSocios=0

while bandera:
     antiguedad=int(input("Ingrese la antiguedad del socio\n"))
     
     if antiguedad==-1:
         bandera=False
     elif antiguedad<0:
         print("Valor inválido")
     elif antiguedad>=1 and antiguedad<=12:
         categoria1+=1
         totSocios+=1
         antcat1+=antiguedad
     elif antiguedad>=13 and antiguedad<=26:
         categoria2+=1
         totSocios+=1
         antcat2+=antiguedad
     elif antiguedad>26:
         categoria3+=1
         totSocios+=1
         antcat3+=antiguedad


if totSocios>0:
    print("La cantidad de socios total ingresada es ",totSocios)
    print("La cantidad de socios de la categoria 1 es: ",categoria1)
    print("La cantidad de socios de la categoria 2 es: ",categoria2)
    print("La cantidad de socios de la categoria 3 es: ",categoria3)
else:
    print("No ingreso datos correctos")
    

if categoria1>0:
    print("El promedio de las edades de los socios correspondientes a categoria 1 es ",(antcat1/categoria1))
if categoria2>0:
    print("El promedio de las edades de los socios correspondientes a categoria 2 es ",(antcat2/categoria2))
if categoria3>0:
    print("El promedio de las edades de los socios correspondientes a categoria 3 es ",(antcat3/categoria3))   
    

# Un pastelero sabe que cada chocotorta requiere 500 grs de galletitas de chocolate, 400 grs
# de dulce de leche y 180 grs de queso crema.
# Desarrollar un programa que lea por teclado la cantidad de cada ingrediente en kilos e
# informar cuántas chocotortas pueden prepararse, y cuánto de cada ingrediente sobra al
# final.


galletitas_kg = float(input("Ingrese la cantidad de galletitas de chocolate en kilos: "))
dulce_de_leche_kg = float(input("Ingrese la cantidad de dulce de leche en kilos: "))
queso_crema_kg = float(input("Ingrese la cantidad de queso crema en kilos: "))

galletitas_gramos= galletitas_kg*1000
dulce_de_leche_gramos=dulce_de_leche_kg*1000
queso_crema_gramos=queso_crema_kg*1000

chocotortas_posibles = 0

while galletitas_gramos>=500 and dulce_de_leche_gramos>=400 and queso_crema_gramos>=180:
    chocotortas_posibles += 1
    galletitas_gramos -= 500
    dulce_de_leche_gramos -= 400
    queso_crema_gramos -= 180
    

print("Se pueden preparar", chocotortas_posibles, "chocotortas.")

print("Sobran", galletitas_gramos, "gramos de galletitas de chocolate.")
print("Sobran", dulce_de_leche_gramos, "gramos de dulce de leche.")
print("Sobran", queso_crema_gramos, "gramos de queso crema.")      



# Se solicita realizar un programa que lea un número por teclado.
# Dicho número, que deberá estar entre 2 y 9, será utilizado por el programa como múltiplo.
# Una vez que se conoce el múltiplo, se deberá solicitar ahora por teclado la carga de
# números enteros positivos, terminando la carga con -1.
# Se solicita lo siguiente:
# - A cada número ingresado, indicar si es o no múltiplo.
# - Devolver la cantidad total de números ingresados que son múltiplos del primero.
# - Indicar el múltiplo mayor y el múltiplo menor ingresado.


multiplo = int(input("Ingrese un número entre 2 y 9 que será tomado como múltiplo: "))

while multiplo < 2 or multiplo > 9:
    print("Número fuera de rango. Por favor, ingrese un número entre 2 y 9.")
    multiplo = int(input("Ingrese un número entre 2 y 9: "))

multiplo_mayor = multiplo
multiplo_menor = None
cantidad_multiplos = 0


bandera=True

while bandera:
    numero = int(input("Ingrese un número entero positivo (o -1 para terminar): "))
    
    if numero==-1:
        bandera=False
    elif numero<0:
        print("Ingreso un número negativo. Reingrese por favor")
    elif numero % multiplo == 0:
        print(numero, "es múltiplo de", multiplo)
        cantidad_multiplos += 1
        if numero > multiplo_mayor:
            multiplo_mayor = numero
        if  multiplo_menor is None or numero<multiplo_menor:
            multiplo_menor=numero


if cantidad_multiplos>0:       
    print("Cantidad total de números ingresados que son múltiplos de", multiplo, ":", cantidad_multiplos)
    print("El múltiplo mayor ingresado es:", multiplo_mayor)
if multiplo_menor!=None:
    print("El múltiplo menor ingresado es:", multiplo_menor)