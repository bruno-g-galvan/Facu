"""Escribir un programa para ingresar tres números naturales que corresponden a las
longitudes de tres segmentos e informar si conforman un triángulo y si lo hacen, de qué tipo
es.
Para ello se deberá:
a. Ingresar la longitud de cada segmento. Verificar que sean naturales.
b. Verificar que los tres lados conformen un triángulo (ver teorema).
c. En caso de haberse comprobado que es posible formar un triángulo, informar si el
triángulo es equilátero (tres lados iguales), isósceles (dos lados iguales) o escaleno (todos
los lados diferentes).
Teorema de la desigualdad del triángulo: Este teorema simplemente establece que la
suma de dos de los lados del triángulo debe ser mayor al tercer lado. Si esto es verdad en
todas las combinaciones (tres), entonces es un triángulo."""

a = int(input("Ingrese la longitud del primer lado: "))
b = int(input("Ingrese la longitud del segundo lado: "))
c = int(input("Ingrese la longitud del tercer lado: "))


if a <= 0 or b <= 0 or c <= 0:
    print("Las longitudes deben ser números naturales.")
else:
    if a + b > c and a + c > b and b + c > a:
        if a == b and b== c and a==c:
            print("Se forma un triángulo equilátero.")
        elif a == b or a == c or b == c:
            print("Se forma un triángulo isósceles.")
        else:
            print("Se forma un triángulo escaleno.")
    else:
        print("Los segmentos no forman un triángulo.")
