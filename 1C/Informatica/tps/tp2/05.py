#Ejercicio 5: Una inmobiliaria paga a sus vendedores un salario base, más una comisión fija por cada venta realizada, más el 5% del valor de esas ventas. Realizar un programa que imprima el número del vendedor y el salario que le corresponde en un determinado mes. Se leen por teclado el número del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.
sellers_quantity = int(input("Ingrese la cantidad de vendedores en su empresa: "))
array_sellers = [] 
array_sells = []
array_total_sells = []
fixed_commission = 2500

for i in range(0, sellers_quantity):
    name = str(input(f"Ingrese en nombre de su {i + 1}º vendedor: "))
    array_sellers.append(name)
    sell = int(input(f"Ingrese la cantidad de ventas realizadas por {name}: "))
    array_sells.append(sell)
    total = int(input(f"Ingrese el valor total de estas ventas de {name}: "))
    array_total_sells.append(total)


for i in range(0, sellers_quantity):
    total_commissions = array_sells[i] * fixed_commission
    percentage_earned = array_total_sells[i] * 0.05
    total_earnings = percentage_earned + total_commissions
    print(f"Al vendedor {array_sellers[i]} le corresponde {total_earnings}$ de ganancias.")