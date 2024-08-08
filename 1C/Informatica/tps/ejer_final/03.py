#Ejercicio 3:
#1. Escribir un programa para ingresar dos números enteros que corresponden a las
#coordenadas de un punto x e y.
#Informar a qué cuadrante pertenece.
#Permitir el ingreso de N puntos de coordenadas. N se solicita al usuario al inicio del
#programa.
#Al finalizar informar cuántos números se ingresaron del cuadrante I.

n = int(input("Ingrese la cantidad de coordenadas que analizara: "))

while n <= 0:
    n = int(input("Ingrese el valor valido mayor a cero: "))

counter = 0

for i in range (n):
    print("Analizamos la coordenada numero", i + 1)
    x = int(input("Ingrese el valor para x: "))
    y = int(input("Ingrese el valor para y: "))

    if 0 < x and 0 < y:
        counter = counter + 1

print("La cantidad de coordenadas en el cuadrante I fue de", counter)

#2. Escribir un programa para ingresar dos números enteros sin resolver la multiplicación
#indicar el signo de la operación.
#Permitir el ingreso de N valores para analizar. N se solicita al usuario al inicio del
#programa. 

n = int(input("Ingrese la cantidad de casos que analizara: "))

while n <= 0:
    n = int(input("Ingrese el valor valido mayor a cero: "))

for i in range (n):
    print("Ahora la operacion", i + 1)
    num1 = int(input("Ingrese el primer valor: "))
    num2 = int(input("Ingrese el segundo valor: "))

    if 0 < num1 and 0 < num2:
        print("Positivo")
    elif 0 > num1 and 0 > num2:
        print("Positivo")
    elif 0 == num1 or 0 == num2:
        print("Neutro")
    else:
        print("Negativo")

