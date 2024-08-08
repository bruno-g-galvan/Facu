#Dado un número entero, calcular su factorial. Ejemplo: fact(4) = 4*3*2*1 = 24.

def fact(value):
    cont = 1
    for i in range(1, value + 1):
        cont = cont * i
    return cont


number = int(input("Ingrese el valor a analizar: "))

print("El factorial del valor es:", fact(number))
