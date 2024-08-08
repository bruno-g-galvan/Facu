#Ejercicio 7: Leer un período en segundos e imprimirlo expresado en días, horas, minutos y segundos. Por ejemplo, 200000 segundos equivalen a 2 días, 7 horas, 33 minutos y 20 segundos.
seconds_ingested = int(input("Ingrese la cantidad de segundos a transformar: "))
days = seconds_ingested / 84600
hours = (days - int(days)) * 24
minutes = (hours - int(hours)) * 60
seconds = (minutes - int(minutes)) * 60
print(f"La cantidad de {seconds_ingested} segundos es de {int(days)} dias, {int(hours)} horas, {int(minutes)} minutos y {int(seconds)} segundos.")