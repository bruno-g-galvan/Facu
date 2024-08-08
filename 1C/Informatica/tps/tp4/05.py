#Ejercicio 5:Se ingresan N números enteros. Determinar el promedio de los números pares.
values_array = []


while True:
    value = input("Ingrese un valor a promediar. Si ya terminó, indíquelo ingresando 'Listo': ")
    try:
        integer = int(value)
        values_array.append(integer)

    except ValueError:
        if value == "Listo":
            break
        else:
            print("Solo se aceptan valores enteros, pruebe nuevamente... ")
            continue
print(f"El promedio es {sum(values_array) / len(values_array)}.")