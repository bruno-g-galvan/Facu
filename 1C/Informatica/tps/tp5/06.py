#Leer un número correspondiente a un año e imprimir un mensaje indicando si es bisiesto o no.
#Se recuerda que un año es bisiesto cuando es divisible por 4. Sin embargo, aquellos años que
#sean divisibles por 4 y también por 100 no son bisiestos, a menos que también sean divisibles
#por 400. Por ejemplo, 1900 no fue bisiesto, pero sí el 2000.

def anio_biciesto(year):
    leap_year = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = True
        else:
            leap_year = True
    return leap_year

anio = int(input("Ingrese el anio a analizar: "))

while anio < 1600 or 10000 < anio:
    anio = int(input("Ingrese un anio valido: "))

if anio_biciesto(anio):
    print("Fecha valida.")
else:
    print("Fecha invalida.")
