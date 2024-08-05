"""Una escuela recibe un subsidio del Estado Nacional según la cantidad de alumnos que
estudien en ella.
Por cada alumno de nivel inicial recibe mensualmente $800, por cada alumno de nivel
primario recibe $1200, mientras que por cada alumno de nivel medio recibe $2100.
Elaborar un programa para leer las edades de los alumnos que concurren a la escuela,
finalizando la lectura cuando se ingrese un 0 (cero) como edad. (5 ptos)
Luego se pide: Imprimir un informe que muestre para cada nivel de enseñanza, el monto
total y la cantidad de alumnos. 
Teniendo en cuenta que:

Desde 1 hasta 5 es nivel inicial con un subsidio de $800
Desde 6 hasta 12 es nivel primario con un subsidio de $1200
Desde 13 hasta 17 es nivel secundario con un subsidio de $2100"""

total_inicial = 0
total_primario = 0
total_secundario = 0
cant_inicial = 0
cant_primario = 0
cant_secundario = 0
bandera=True

while bandera:

    edad = int(input("Ingrese la edad del alumno (0 para salir): "))
    
    if edad==0:
        print("Gracias por usar nuestro sistema")
        bandera=False
    elif edad>=1 and edad <= 5:
        total_inicial += 800
        cant_inicial += 1
    elif edad>=6 and edad <= 12:
        total_primario += 1200
        cant_primario += 1
    elif edad>=13 and edad <= 17:
        total_secundario += 2100
        cant_secundario += 1
    else:
        print("Edad no válida. Ingrese una edad entre 1 y 17.")


print("\nInforme:")
print("Nivel Inicial - Total: $", total_inicial, "- Cantidad de Alumnos:", cant_inicial)
print("Nivel Primario - Total: $", total_primario, "- Cantidad de Alumnos:", cant_primario)
print("Nivel Medio - Total: $", total_secundario, "- Cantidad de Alumnos:", cant_secundario)
