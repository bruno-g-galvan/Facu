#Hacer un programa que permita ingresar los años de fabricación de las unidades de una
#empresa de transporte urbano de pasajeros. Al finalizar dicho ingreso (año cero), el programa
#debe informar el porcentaje de vehículos que tienen menos de 5 años de antigüedad.
i = 1
count = 0
anios_fab_array = []

while True:
    anio_fab = int(input(f"Ingrese el anio de fabricacion de la unidad numero {i} (ingrese 0 para terminar): "))
    if anio_fab == 0:
        break
    elif anio_fab >= 1886 or anio_fab <= 2024:
        anios_fab_array.append(anio_fab)
    else:
        print("Anio invalido, vuela a intentarlo.")

for i in anios_fab_array:
    if i >= 2019:
        count += 1

print(f"El porcentaje de unidades con menos de 5 anios de antiguedad es de {(count * 100) / len(anios_fab_array)}%")


