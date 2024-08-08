#Desarrollar un programa que genere un número entero al azar de cuatro cifras y proponerle al
#usuario que lo descubra, ingresando valores repetidamente hasta hallarlo. En cada intento el
#programa mostrará mensajes indicando si el número ingresado es mayor o menor que el valor
#secreto. Permitir que el usuario abandone al ingresar -1. Informar la cantidad de intentos realizada
#al terminar el juego. Utilizar la función creada en el ejercicio 8 para resolver el problema.
import random

def adivinador(number):
    counter = 1
    while number != random_number and number != -1:
        if 1000 <= number and number <= 9999:
            if number < random_number:
                number = int(input("Mala suerte! Ingrese un valor mayor: "))
            elif number > random_number:
                number = int(input("Mala suerte! Ingrese un valor menor: "))
            counter = counter + 1
        else:
            number = int(input("Ingrese un valor valido entre 1000 y 9999: "))
    if number != -1:
        print("El valor era", number, "e intentaste", counter, "veces.")
    else:
        print("Termina el programa.")


random_number = random.randint(1000, 1005)
numero = int(input("Numero al azar generado! Adivinelo: "))

adivinador(numero)

    


