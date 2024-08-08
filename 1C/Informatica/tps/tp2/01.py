#Ejercicio 1: Las variables guardan datos de diferente tipo y permiten cambiar su valor. Dadas dos variables numéricas A y B, que el usuario debe ingresar por teclado, se pide:
#Diseñar el algoritmo para resolver los siguientes problemas y escriba el pseudocodigo o diagrama de flujo.
#a.Mostrar el mensaje “Hola Mundo”.
#b.Ingresar el nombre del usuario del programa y saludarlo. Ejemplo: Si el usuario se llama Juan, se debe mostrar el mensaje “Hola Juan”.
#c.Ingresar dos números y mostrar la suma y la diferencia.
#d.Ingresar tres números y mostrar el promedio.
#e.Ingresar el monto de una factura y calcular el IVA (21%).
#f.Duplicar el valor que poseen y mostrarlo por pantalla.
#g.Intercambiar los valores de ambas variables y mostrar cuánto valen al final las dos variables.

#a
print("Hola mundo")

#b
name = str(input("Ingresa el nombre: "))
print(f"Hola {name}")

#c
num1 = float(input("Ingresa el primer valor: "))
num2 = float(input("Ingresa el segundo valor: "))
print(f"La suma es: {num1 + num2}")
print(f"La resta es: {num1 - num2}")

#d
num1 = float(input("Ingresa el primer valor: "))
num2 = float(input("Ingresa el segundo valor: "))
num3 = float(input("Ingresa el tercer valor: "))
print(f"El promedio es: {(num1 + num2 + num3) / 3}")

#e
monto = float(input("Ingresa el monto: "))
print(f"EL IVA de ese monto seria de {monto * 0.21}.")

#f
valor = float(input("Ingresa el monto: "))
print(f"El doble es: {valor * 2}")

#g
num1 = input("Escribe tu primera variable: ")
num2 = input("Escribe tu segunda variable: ")
temp = num1
num1 = num2
num2 = temp
print(f"Primera variable: {num1}. Segunda variable: {num2}")
