#Construir una lista llamada SECUENCIAS con N números enteros al azar entre 1 y 20. Esta lista se
#caracterizará porque sus valores deben encontrarse divididos en secuencias de números
#separadas por ceros, cuya suma no sea mayor que 20. Para eso se deberá agregar un elemento
#de valor 0 a fin de separar cada secuencia de la siguiente, cuidando que ninguna secuencia sume
#más de 20. Agregar un 0 adicional al final de la lista y mostrar la lista obtenida por pantalla.
#Ejemplo:

#Lista original:
#5 2 9 6 4 15 3 19 12 1 5
#Resultado:
#5 2 9 0 6 4 0 15 3 0 19 0 12 1 5 0

#A partir de la lista SECUENCIAS generada en el ejercicio anterior, mostrar la secuencia más larga
#almacenada en la misma. Si hubiera varias secuencias con la misma longitud máxima deberán
#mostrarse todas las que correspondan.
import modlists as modlists

def separator(lst):
    sequences = []
    counter = 0
    for i in range(0, len(lst)):
        counter = counter + lst[i]
        if counter > 20:
            sequences.append(0)
            counter = lst[i]
        sequences.append(lst[i])

    return sequences

def splitter(lst):
    result = []
    current_subarray = []

    for i in range(0, len(lst)):
        if lst[i] == 0:
            result.append(current_subarray)
            current_subarray = []
        else:
            current_subarray.append(lst[i])

    if len(current_subarray) != 0:
        result.append(current_subarray)

    return result

def detector(lst):
    max_lenght = 0
    counter = 0
    position = []

    for i in range(0, len(lst)):
        if max_lenght <= len(lst[i]):
            max_lenght = len(lst[i])
            counter = counter + 1
    
    for i in range(0, len(lst)):
        if len(lst[i]) == max_lenght:
            position.append(lst[i])

    return position

desde = int(input("Ingrese desde que numero desea generar los valores (ingresar 1): "))
hasta = int(input("Ingrese hasta que numero desea generar los valores (ingresar 20): "))
longitud = int(input("Ingrese el valor de numeros enteros que desea en la lista: "))

secuencias = modlists.generate_random_lst(desde, hasta, longitud)
print("--Secuencia generada--")
print(secuencias)

secuencias_divididas = separator(secuencias)
print("--Secuencias con 0's--")
print(secuencias_divididas)

secuencia_dividida = splitter(secuencias_divididas)
print("--Secuencia/s mas larga/s--")
print(detector(secuencia_dividida))






