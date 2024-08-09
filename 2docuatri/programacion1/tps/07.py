# Describir una función diasiguiente(dia, mes año) que reciba como 
# parámetro una fecha cualquiera expresada por tres enteros y calcule 
# y devuelva otros tres enteros correspondientes el día siguiente al 
# dado. Utilizando esta función sin modificaciones ni agregados, 
# desarrollar programas que permitan:
# a.Sumar N días a una fecha.
# b.Calcular la cantidad de días existentes entre dos fechas cualesquiera.

def validarFecha(day, month, year):
    valid_date = False

    if 1582 < year:
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if 0 < day and day <= 31:
                valid_date = True
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if 0 < day and day <= 30:
                valid_date = True
        elif month == 2:

        #Checkea si el anio es biciesto
            leap_year = False
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        leap_year = True
                else:
                    leap_year = True
            
            if leap_year:
                if 0 < day and day <= 29:
                    valid_date = True
            else:
                if 0 < day and day <= 28:
                    valid_date = True
    
    return valid_date

dia = int(input("Ingrese el dia de su fecha: "))

mes = int(input("Ingrese el mes de su fecha: "))

anio = int(input("Ingrese el anio de su fecha: "))

if validarFecha(dia, mes, anio):
    print("La fecha es valida.")
else:
    print("La fecha no es valida.")