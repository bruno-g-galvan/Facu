#Ejercicio 12: Leer dos números naturales A y B. Calcular AB mediante productos sucesivos y mostrar el
#resultado. Ejemplo: 4^3 = 4 * 4 * 4 (4 multiplicado 3 veces).

num1 = int(input("Ingresa el valor: "))
num2 = int(input("Ingresa la cantidad de veces a multiplicarse: "))
count = 0
temp = num1

for i in range(1, num2):
    count = temp * num1
    temp = count
    print(f"Valor en progreso: {count}")