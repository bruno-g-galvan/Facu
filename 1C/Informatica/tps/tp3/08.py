#Ejercicio 8:Diseñar un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo
#básico y su antigüedad en años. Si es soltero se le incrementa el sueldo en 5% del salario bruto
#por cada año de antigüedad, mientras que si es casado se le incrementa el sueldo en 7% del
#bruto por cada año de antigüedad. También se le realizan los siguientes descuentos: Jubilación:
#11%, Obra Social: 3%, Sindicato: 3%.
#Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y estado civil (‘s’ o
#‘c’). Se debe informar: (reemplazar los 9 por los valores que correspondan)
sueldo = int(input("Sueldo bruto percibido: "))
antiguedad = int(input("Antiguedad en años: "))
estado_civil = input("Estado civil (S o C): ")

if estado_civil == 'S':
    incremento_antiguedad = antiguedad * (sueldo * 0.05)
else:
    incremento_antiguedad = antiguedad * (sueldo * 0.07)

sueldo += incremento_antiguedad
sueldo -= (sueldo * 0.11)
sueldo -= (sueldo * 0.03)
sueldo -= (sueldo * 0.03)

print(f"El sueldo neto resultante seria de: {round(sueldo)}$")



