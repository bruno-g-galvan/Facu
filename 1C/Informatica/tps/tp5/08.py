#Desarrollar una función para ingresar del teclado un número entero y validar que sea positivo,
#debe retornar el valor.

def divisor(number):
    if 0 < number:
        return "El numero", number, "es positivo."
    else:
        return "El numero", number, "no es positivo."

numero = int(input("Ingrese el numero a evaluar: "))

print(divisor(numero))
