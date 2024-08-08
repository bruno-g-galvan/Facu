#Ejercicio 9:Ingresar números, hasta que la suma de los números pares supere 100. Mostrar Cuántos
#números en total se ingresaron.
values_array = []
suma_total = 0

while True:
    value = input("Ingrese un valor: ")
    try:
        integer = int(value)
        if ((integer / 2) - int(integer / 2)) == 0:
            suma_total += integer
        values_array.append(integer)
        if suma_total > 100:
            break


    except ValueError:
        print("Solo se aceptan valores enteros, pruebe nuevamente... ")
        continue

print(f"El total de números ingresados fue de {len(values_array)}.")