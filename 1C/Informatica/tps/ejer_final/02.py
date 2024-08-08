#Ejercicio 2:
#1. Escribir una función que reciba como parámetros dos números enteros A y B y retorne
#la suma de los números enteros comprendidos entre A y B, ambos incluidos.
#2. Escribir también un programa para leer y validar ambos números, llamar a la función y
#mostrar el resultado. (Se resuelve sin el uso de listas)

def nums_in_btw(number1, number2):
    counter = 0

    if number1 < number2:
        for i in range(number1, number2 + 1):
            counter = counter + i
    elif number1 > number2:
        for i in range(number2, number1 + 1):
            counter = counter + i

    return counter


num1 = int(input("Ingrese el primer valor entero: "))

while num1 <= 0:
    num1 = int(input("Ingrese el valor valido mayor a cero: "))

num2 = int(input("Ingrese el segundo valor entero: "))

while num2 <= 0:
    num2 = int(input("Ingrese el valor valido mayor a cero: "))

print(nums_in_btw(num1, num2))