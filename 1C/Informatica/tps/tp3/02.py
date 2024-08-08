#Ejercicio 2:Leer un número entero e imprimir un mensaje indicando si es par, impar o es cero.
num = int(input("Ingresa el valor a determinar: "))

if num == 0:
    print("El valor es 0.")
elif (num / 2) - int(num / 2) != 0:
    print("El valor es impar.")
else:
    print("El valor es par.")