#Ejercicio 1:Un número abundante o número excesivo es un número entero en el que la suma de sus divisores propios (todos los divisores excepto el propio número) 
#es mayor que dicho número. Por ejemplo, 12 es un número abundante porque la suma de sus divisores (1, 2, 3, 4 y 6) es 16, que es mayor que 12. Sin embargo 10 no 
#es un número abundante porque la suma de sus divisores (1, 2 y 5) es 8, que es menor que 10. Desarrollar un algoritmo para ingresar un número entero cualquiera 
#e informar si se trata de un número abundante o no. Desarrolle la prueba de escritorio para validar el algoritmo.



number = int(input("Ingrese el valor a evaluar: "))
i = 1
sum = 0

while i in range(1, number):

    if number % i == 0:
        sum = sum + i

    i = i + 1

if number < sum:
    print("abundante ", number, " - ", sum)