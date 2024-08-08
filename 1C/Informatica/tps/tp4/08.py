#Ejercicio 8:Escribir un algoritmo que lea números enteros hasta que se ingrese un 0, y muestre el máximo,
#el mínimo (sin considerar el 0) y la media (promedio) de todos ellos.
values_array = []

while True:
    value = input("Ingrese un valor. Si ya terminó, indíquelo ingresando '0': ")
    try:
        integer = int(value)
        if value == '0':
            break
        values_array.append(integer)

    except ValueError:
        print("Solo se aceptan valores enteros, pruebe nuevamente... ")
        continue
print(f"El mayor número ingresado fue {max(values_array)}, el menor valor fue {min(values_array)} y el promedio general fue de {sum(values_array) / len(values_array)}.")