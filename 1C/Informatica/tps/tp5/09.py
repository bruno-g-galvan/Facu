#Desarrollar un programa generar N números al azar de un dígito, positivos. N se ingresa por teclado. Para
#cada valor al azar, mostrar el valor creado y su factorial (utilizar la función creada en el ejercicio1).

import random

def fact(value):
    cont = 1
    for i in range(1, value + 1):
        cont = cont * i
    return cont

def random_value(value):
    for _ in range(value):
        random_number = random.randint(1, 20)
        print("El valor es", random_number, "y su factorial es:", fact(random_number))

number = int(input("Ingrese el valor N para generar N valores al azar y sus factorial: "))

random_value(number)