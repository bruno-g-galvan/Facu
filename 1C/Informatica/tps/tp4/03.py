#Ejercicio 3:Mostrar las tablas de multiplicar (entre 1 y 10) del número 4. ¿Cómo cambiaría el algoritmo
#para que el usuario pueda decidir la tabla de multiplicar a mostrar?
number = int(input("Ingresa un valor entero: "))

for i in range(1, 11):
    print(f"{i} x {number}: {i * number}")