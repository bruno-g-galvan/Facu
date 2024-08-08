#Ejercicio 6:Leer N números enteros e imprimir el mayor y en qué orden fue ingresado.
values_array = []

while True:
    value = input("Ingrese un valor. Si ya terminó, indíquelo ingresando 'Listo': ")
    try:
        integer = int(value)
        values_array.append(integer)

    except ValueError:
        if value == "Listo":
            break
        else:
            print("Solo se aceptan valores enteros, pruebe nuevamente... ")
            continue
print(f"El mayor número ingresado fue {max(values_array)} y su posición fue {(values_array.index(max(values_array))) + 1}.")