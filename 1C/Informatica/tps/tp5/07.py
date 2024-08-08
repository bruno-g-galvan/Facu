#Desarrollar una función que reciba tres números enteros positivos y verifique si
#corresponden a una fecha gregoriana válida (día, mes, año). Devolver True o False
#según la fecha sea correcta o no. Realizar también un programa para verificar el
#comportamiento de la función.

def validar_fecha(day, month, year):
    valid_date = False

    if 1582 < year:
        if month in (1, 3, 5, 7, 8, 10, 12):
            if 0 < day and day <= 31:
                valid_date = True
        elif month in (4, 6, 9, 11):
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


num1 = int(input("Ingrese el primer valor entero positivo: "))

while num1 < 0:
    num1 = int(input("Ingrese un valor positivo valido: "))

num2 = int(input("Ingrese el segundo valor entero positivo: "))

while num2 < 0:
    num2 = int(input("Ingrese un valor positivo valido: "))

num3 = int(input("Ingrese el tercer valor entero positivo: "))

while num3 < 0:
    num3 = int(input("Ingrese un valor positivo valido: "))

if validar_fecha(num1, num2, num3):
    print("Fecha valida.")
else:
    print("Fecha invalida.")
