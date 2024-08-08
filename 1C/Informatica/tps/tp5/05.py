#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y
#quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El
#programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el
#cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 500$ y si
#es mayor de 18 años, 1000$

def precio_entradas(age):
    if age < 4:
        return "Gratis"
    elif 4 <= age <= 18:
        return "500$"
    else:
        return "1000$"

edad = int(input("Ingrese la edad del cliente: "))

while edad < 0 or 100 < edad:
    edad = int(input("Ingrese una edad valida entre 0 y 100: "))

print("La precio de tu entrada es:", precio_entradas(edad))