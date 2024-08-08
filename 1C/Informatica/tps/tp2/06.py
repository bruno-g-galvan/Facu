#Ejercicio 6: Una persona quiere invertir su capital en un banco y quiere saber cuánto dinero gana en un mes si el banco paga 2% mensual. ¿Cuánto ganará en seis meses si deja su dinero invertido?
invest = int(input("Ingrese el dinero a invertir para calcular lo que ganarìa en 6 meses: "))
array_months_earn = [invest]
total_earnings = (invest * 0.02) * 6
print(f"En 6 meses de intereses no compuestos tendrias un total de: {total_earnings + invest}$.")

for i in range(0, 6):
    temp_value = (array_months_earn[i] * 0.02) + array_months_earn[i]
    array_months_earn.append(temp_value)

print("Si tuvieramos intereses compuestos -> ")

for i in range(0, 6):
    print(f"Total de dinero en el mes {i + 1}: {array_months_earn[i]}$")