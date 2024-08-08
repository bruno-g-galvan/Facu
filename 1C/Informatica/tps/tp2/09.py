#Ejercicio 9:Escribir un programa para convertir un número binario de 4 cifras en un número decimal. Se ingresa como un solo número entero de cuatro dígitos.
#Ayuda: Dado un número binario, se toma de a un dígito a la vez, de menor a mayor comenzando por el índice 0 y se multiplica por (2x) donde x corresponde a la posición del dígito. Estos resultados se suman.
#Ejemplo: 1 0 1 12 = 1 * 20 + 1 * 21 + 0 * 22 + 1 * 23 = 1110
binary_value = str(input("Escribe el valor en binario a transformar: "))
final_sum = 0
temp_array = []
final_array = []

for i in range(0, len(binary_value)):
    value = binary_value[i:i+1]
    temp_array.append(int(value))

inverted_array = temp_array[::-1]

print(f"Valores en array: {temp_array[::-1]}")

for i in range(0, len(binary_value)):
    final_sum += inverted_array[i] * (2 ** i)

print(f"El valor en base 10 es: {final_sum}")
