#Ejercicio 10: Un negocio desea saber el importe total recaudado al fin del día, desea contar con un programa
#que pueda ingresar el importe de cada venta realizada. Para indicar que finalizó el día se ingresa
#-1. ¿Cuál fue el monto total vendido y cuántas ventas se realizaron? El importe de cada venta
#realizada debe ser un valor positivo.
values_array = []

while True:
    value = input("Ingrese un valor. Si ya terminó, indíquelo ingresando '-1': ")
    try:
        integer = int(value)
        if value == '-1':
            break
        values_array.append(integer)

    except ValueError:
        print("Solo se aceptan valores enteros, pruebe nuevamente... ")
        continue

print(f"El total de números ingresados fue de {sum(values_array)}.")