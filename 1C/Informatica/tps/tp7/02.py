#Escribir una función para crear una lista con N valores al azar en un rango desde y hasta que se
#recibe por parametro. Retorna la lista creada
import modlists

desde = int(input("Ingrese desde que numero desea generar los valores (por ejemplo 1): "))
hasta = int(input("Ingrese hasta que numero desea generar los valores (por ejemplo 20): "))
longitud = int(input("Ingrese el valor de numeros enteros que desea en la lista: "))

lista = modlists.generate_random_lst(desde, hasta, longitud)

print("Lista:", lista)

