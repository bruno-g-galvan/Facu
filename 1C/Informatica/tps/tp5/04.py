#Desarrolla una función que retorne la cantidad de divisores de un número entero positivo.

def divisor(number):
    i = 1
    counter = 0
    for i in range(1, number):
        if number % i == 0:
            counter = counter + 1
    return counter

numero = int(input("Ingrese el numero a evaluar: "))

print("La cantidad de divisores para este numero es de: ", divisor(numero))