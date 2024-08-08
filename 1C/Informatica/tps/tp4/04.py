#Ejercicio 4:Se desea ingresar la nota de 5 alumnos y mostrar su promedio.
total = 0

for i in range(1, 6):
    note = float(input(f"Ingrese la nota del alumno número {i}: "))
    total += note

promedio = (total / 5)
print(f"El promedio es de: {promedio}")