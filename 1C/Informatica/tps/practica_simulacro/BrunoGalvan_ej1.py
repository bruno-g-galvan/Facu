#En un colegio se van ingresando los siguientes datos para evaluar el resultado de un curso de N alumnos.  
#Se ingresa la siguiente información por cada alumno:  
#libreta nro: debe ser un valor entre 1000 y 10000 
#Nota_Parc1: valor aleatorio entre 0 y 10 
#Nota_Parc2: valor aleatorio entre 0 y 10 
#
#Por fin de proceso informar: 
#A – Cantidad de alumnos aprobados con los dos parciales igual a 7 o más 
#B – Porcentaje de alumnos desaprobados (los dos parciales menos de 4) 
#C – cuál es el parcial que hay más alumnos para recuperar. 
#D – Cuantos deben recuperar ambos parciales.

#ADVERTENCIA: No existe validacion de varios reingresos de notas para el mismo alumno
alumnos_promocionados = 0
alumnos_desaprobados = 0
parcial_1_desaprobado = 0
parcial_2_desaprobado = 0
counter = 0

nrm_libreta = int(input("Ingrese el numero de libreta del alumno para el cual desea ingresar notas de parcial (0 si desea terminar): "))

while nrm_libreta != 0:
    
    while nrm_libreta < 1000 or nrm_libreta > 10000:
        nrm_libreta = int(input("Ingrese un numero valido de numero de libreta del alumno para el cual desea ingresar notas de parcial (0 si desea terminar): "))

    nota_p_1 = int(input("Ingrese la nota del primer parcial: "))

    while nota_p_1 < 0 or nota_p_1 > 10:
        nota_p_1 = int(input("Ingrese una nota valida del primer parcial: "))
    
    nota_p_2 = int(input("Ingrese la nota del segundo parcial: "))

    while nota_p_2 < 0 or nota_p_2 > 10:
        nota_p_2 = int(input("Ingrese una nota valida del segundo parcial: "))

    if nota_p_1 >= 7 and nota_p_2 >= 7:
        alumnos_promocionados += 1

    if nota_p_1 < 4 and nota_p_2 < 4:
        alumnos_desaprobados += 1

    if nota_p_1 < 4:
        parcial_1_desaprobado += 1     

    if nota_p_2 < 4:
        parcial_2_desaprobado += 1
    
    counter += 1

    nrm_libreta = int(input("Ingrese el numero de libreta del alumno para el cual desea ingresar notas de parcial (0 si desea terminar): "))

print(f"Alumnos aprobados con los dos parciales igual a 7 o más: {alumnos_promocionados}")
print(f"Porcentaje de alumnos desaprobados: {(alumnos_desaprobados * 100) / counter}%")
if parcial_1_desaprobado > parcial_2_desaprobado:
    print(f"El primer parcial tiene mas alumnos para recuperar.")
elif parcial_1_desaprobado < parcial_2_desaprobado:
    print(f"El segundo parcial tiene mas alumnos para recuperar.")
else:
    print(f"Ambos parciales tienen el mismo numero de alumnos a recuperar.")
print(f"{alumnos_desaprobados} deben recuperar ambos parciales.")



