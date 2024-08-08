#Ejercicio 8:Un banco necesita para sus cajeros de la sucursal un programa que lea una cantidad de dinero que desea retirar el cliente e imprima a cuántos billetes equivale, considerando que existen billetes de $1000, $500, $200, $100, $50, $20 y el resto en monedas. Desarrollar dicho programa de tal forma que se minimice la cantidad de billetes entregados por el cajero
money = int(input("Ingrese la cantidad de dinero a retirar sin centavos: "))
currency_array = [1000, 500, 200, 100, 50, 20]

if money < 20:
    print(f"El cajero nos daria {money} monedas de 1 peso.")
else:
    thousands = int(money / currency_array[0])
    five_hundreds = int((money - (thousands * currency_array[0])) / currency_array[1])
    two_hundreds = int((money - (thousands * currency_array[0]) - (five_hundreds * currency_array[1])) / currency_array[2])
    hundreds = int((money - (thousands * currency_array[0]) - (five_hundreds * currency_array[1]) - (two_hundreds * currency_array[2])) / currency_array[3])
    fifths = int((money - (thousands * currency_array[0]) - (five_hundreds * currency_array[1]) - (two_hundreds * currency_array[2]) - (hundreds * currency_array[3])) / currency_array[4])
    twenties = int((money - (thousands * currency_array[0]) - (five_hundreds * currency_array[1]) - (two_hundreds * currency_array[2]) - (hundreds * currency_array[3]) - (fifths * currency_array [4])) / currency_array[5])
    rest = int((money - (thousands * currency_array[0]) - (five_hundreds * currency_array[1]) - (two_hundreds * currency_array[2]) - (hundreds * currency_array[3]) - (fifths * currency_array [4]) - (twenties * currency_array[5])))

print(f"El cajero nos daria {thousands} billetes de 1000$, {five_hundreds} de 500$, {two_hundreds} de 200$, {hundreds} de 100$, {fifths} de 50$, {twenties} de 20$ y {rest} en monedas de 1 peso.")
