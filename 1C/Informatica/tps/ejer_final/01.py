#Ejercicio 1:
#Desarrollar un programa que lea las ventas efectuadas por una farmacia. Por cada venta se
#ingresa el importe a pagar y un código indicador (O, E ó T).
#• Si el código es O, significa que corresponde a una obra social (se abona sólo en
#efectivo), le corresponde un 40% de descuento.
#• Si el código es E, significa que se abona en efectivo, le corresponde un 10% de
#descuento.
#• Si el código es T, significa que se abona con tarjeta, le corresponde un 15% de recargo.
#• Al terminar el día se ingresa un importe -1
#
#Se pide informar:
#a) Total de operaciones y monto del día.
#b) Total de operaciones y total de montos en efectivo, discriminando cuáles fueron por
#obra social y cuáles no.
#c) Cuál fue el mayor monto dentro de las ventas efectuadas en Efectivo.
#NOTA: El total de montos debe ser el efectivamente cobrado luego de efectuar los descuentos
#o recargos correspondientes.
#d) Crear una lista con los importes únicos (no debe repetir importes), ordenados de
#mayor a menor indicando en un comentario el nombre del método y cómo funciona el
#mismo.
#Crear al menos dos funciones para resolver el problema.

def ingesta_compras(number, condition, main_list):

    sub_lista = []

    if condition == "O":
        number = number - (number * 0.4)
    elif condition == 'E':
        number = number - (number * 0.1)
    elif condition == 'T':
        number = number + (number * 0.15)

    sub_lista.append(number)
    sub_lista.append(condition)
    main_list.append(sub_lista)
    print(main_list)

def informe_compras(main_list):
    total_income = 0
    for i in range(len(main_list)):
        total_income = total_income + main_list[i][0]
    
    print("El total de operaciones fue de", len(main_list), "y el monto total fue de", total_income)

    cash_income = 0
    cash_counter = 0
    health_care_cash_income = 0
    health_care_counter = 0
    max_cash_earning = 0
    for i in range(len(main_list)):
        if main_list[i][1] == 'E':
            cash_income = cash_income + main_list[i][0]
            cash_counter = cash_counter + 1
            if max_cash_earning < main_list[i][0]:
                max_cash_earning = main_list[i][0]
        elif main_list[i][1] == 'O':
            health_care_cash_income = health_care_cash_income + main_list[i][0]
            health_care_counter = health_care_counter + 1
            if max_cash_earning < main_list[i][0]:
                max_cash_earning = main_list[i][0]
    
    print("El total de operaciones en efectivo fue de", cash_counter + health_care_counter)
    print("El monto total de efectivo fue de", cash_income + health_care_cash_income)
    print("El total de operaciones con obra social fue de", health_care_counter)
    print("El total de operaciones solo en efectivo sin obra social fue de", cash_counter)
    print("El monto total de operaciones con obra social fue de", health_care_cash_income)
    print("El monto total de operaciones solo en efectivo sin obra social fue de", cash_income)
    

#Burbujeo desc
def ord_bubble_desc(lst):
    for _ in range(0, len(lst)):
        for i in range(1, len(lst)):
            #Cambio de > a <=
            if lst[i] > lst[i - 1]:
                aux = lst[i]
                lst[i] = lst[i - 1]
                lst[i - 1] = aux

    return lst    

condicion = input("Indique si la primer compra fue con Obra Social (O), en Efectivo (E) o con Tarjeta (T): ")

while condicion != 'O' and condicion != 'E' and condicion != 'T':
    condicion = input("Ingrese un valor valido (O, E o T): ")

numero = int(input("Ingrese el valor de la primer compra (-1 para terminar): "))

while numero <= 0 and numero != -1:
    numero = int(input("Ingrese el valor valido mayor a cero para la primer compra (-1 para terminar): "))

if numero != -1:

    lista_compras = []

    while numero != -1:
        ingesta_compras(numero, condicion, lista_compras)

        condicion = input("Indique si la compra fue con Obra Social (O), en Efectivo (E) o con Tarjeta (T): ")

        while condicion != 'O' and condicion != 'E' and condicion != 'T':
            condicion = input("Ingrese un valor valido (O, E o T): ")

        numero = int(input("Ingrese el valor de otra compra (-1 para terminar): "))

        while numero <= 0 and numero != -1:
            numero = int(input("Ingrese el valor valido mayor a cero para la compra (-1 para terminar): "))

    informe_compras(lista_compras)

    lista_importes = []

    for i in range(len(lista_compras)):
        lista_importes.append(lista_compras[i][0])

    print(ord_bubble_desc(lista_importes))
        
else:
    print("No se ingresaron valores de compra.")
