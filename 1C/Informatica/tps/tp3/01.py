#Ejercicio 1:Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un mensaje de error indicando que no se puede realizar la operación.
num = int(input("Ingresa el primer valor: "))
div = int(input("Ingresa el segundo valor: "))

try:
    res = num / div
    print(res)
except ZeroDivisionError:
    print("El divisor es 0. Prueba con otro valor.")