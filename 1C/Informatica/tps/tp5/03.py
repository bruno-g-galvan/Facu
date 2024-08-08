#Escribir la función obtener_mes_en_texto, que devuelva una cadena que representa un mes
#expresado en letras según un número entero entre 1 y 12 recibido como parámetro. Si el
#parámetro no es válido, devolver una cadena vacía. Ejemplo: Se invoca
#obtener_mes_en_texto(4) → devuelve “Abril”.

def obtener_mes_en_texto(month):

    if month == 1:
        return "Enero"
    elif month == 2:
        return "Febrero"
    elif month == 3:
        return "Marzo"
    elif month == 4:
        return "Abril"
    elif month == 5:
        return "Mayo"
    elif month == 6:
        return "Junio"
    elif month == 7:
        return "Julio"
    elif month == 8:
        return "Agosto"
    elif month == 9:
        return "Septiembre"
    elif month == 10:
        return "Octubre"
    elif month == 11:
        return "Noviembre"
    elif month == 12:
        return "Diciembre"
    else:
        return " "

mes = int(input("Ingrese el numero de mes entre 1 y 12: "))

print(obtener_mes_en_texto(mes))