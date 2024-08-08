#Ejercicio 11: Leer dos números A y B (enteros positivos). Calcular el producto A * B por sumas sucesivas e
#imprimir el resultado. Ejemplo: 4*3 = 4 + 4 + 4 (4 sumado 3 veces).

num1 = int(input("Ingresa el valor: "))
num2 = int(input("Ingresa la cantidad de veces a sumarse: "))
temp = 0

for i in range(0, num2):
    temp += num1
    print(f"Valor en progreso: {temp}")