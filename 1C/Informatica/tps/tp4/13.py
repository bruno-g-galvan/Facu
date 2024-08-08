#Ejercicio 13: Hacer un programa que permita ingresar un número natural n. Informar si n es un término de la
#serie de Fibonacci. En este caso indicar en que posición de la serie se encuentra.
#Ejemplo: 1, 1, 2, 3, 5, 8 ... . Si el número ingresado es 4, el número no pertenece a la serie.
#Si el número es 5, este pertenece a la serie y su orden es 5.
#(Ley de formación de los términos en dicha serie: los dos primeros términos son 1 y cada uno
#de los demás es igual a la suma de los dos anteriores).
fibo_array = [0, 1, 1]
value = int(input("Ingrese un valor: "))
i = 0
while True:
    fibo_array.append(fibo_array[i + 1] + fibo_array[i + 2])
    if fibo_array[i] == value:
        print("El número pertenece a la secuencia de Fibonacci.")
        break
    elif fibo_array[i] > value:
        print("El número no pertenece a la secuencia de Fibonacci. ")
        break
    i += 1
    
