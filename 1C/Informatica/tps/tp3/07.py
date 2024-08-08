#Ejercicio 7:Leer tres números correspondientes al día, mes y año de una fecha e imprimir un mensaje
#indicando si la fecha es válida o no.
dia = int(input("Ingrese el dia a analizar: "))
mes = int(input("Ingrese el mes a analizar: "))
anio = int(input("Ingrese el año a analizar: "))

if ((anio / 4) - int(anio / 4)) == 0 and ((anio / 100) - int(anio / 100)) == 0 and ((anio / 400) - int(anio / 400)) == 0:
    print("Es un año biciesto.")
    anio_biciesto = True
elif ((anio / 4) - int(anio / 4)) == 0 and ((anio / 100) - int(anio / 100)) != 0:
    print("Es un año biciesto.")
    anio_biciesto = True
else:
    print("No es un año biciesto.")
    anio_biciesto = False

##Enero: 31 días
##Febrero: 28 o 29 días (si es año bisiesto)
##Marzo: 31 días
##Abril: 30 días
##Mayo: 31 días 
##Junio: 30 días 
##Julio: 31 días
##Agosto: 31 días
##Septiembre: 30 días
##Octubre: 31 días
##Noviembre: 30 días
##Diciembre: 31 días

days_of_months = [31 ,29 ,31 ,30 ,31 ,30 ,31 ,31 ,30 ,31 ,30, 31]

if anio < 1601:
    print(f"La fecha {dia}/{mes}/{anio} no es válida. El año debe ser mayor a 1601.")
elif mes < 1 or mes > 12:
    print(f"La fecha {dia}/{mes}/{anio} no es válida. El mes debe ser un numero entre 1 y 12.")
elif dia < 1 or dia > days_of_months[mes - 1]:
    print(f"La fecha {dia}/{mes}/{anio} no es válida. El dia debe ser mayor a 1 y menor a {days_of_months[mes - 1]}.")
elif mes == 2 and dia == days_of_months[1] and anio_biciesto == False:
    print(f"La fecha {dia}/{mes}/{anio} no es válida.")
else:
    print(f"La fecha {dia}/{mes}/{anio} es válida.")