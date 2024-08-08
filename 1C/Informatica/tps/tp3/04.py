#Ejercicio 4:Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, aprobó o debe recuperar.
#• Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
#• Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
#• Se debe recuperar cuando al menos una de las dos notas es menor a 4.
primer_parcial = float(input("Ingresa la nota de tu primer parcial: "))
segundo_parcial = float(input("Ingresa la nota de tu segundo parcial: "))

if primer_parcial >= 7 and segundo_parcial >= 7:
    print("Promociona.")
elif primer_parcial >= 4 and segundo_parcial >= 4:
    print("Aprueba, no promociona.")
else:
    print("Desaprueba. Debe recuperar.")