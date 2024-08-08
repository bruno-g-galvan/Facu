#Escribir una función para crear una lista con N valores ingresados desde el teclado, hasta
#ingresar -1. La lista no debe aceptar valores repetidos, rechazarlos si esto sucede. No utilizar el
#operador IN, crear su propia función existe para detectar si un elemento ya se encuentra en una
#lista.
import modlists

lista = []
numero = int(input("Ingrese un numero para rellenar la lista (-1 termina el programa): "))

while numero != -1:
    if modlists.num_in_lst(numero, lista):
        print("Numero repetido en lista, pruebe nuevamente.")
    else:
        lista.append(numero)
    numero = int(input("Ingrese un numero para rellenar la lista (-1 termina el programa): "))

print("Lista sin valores repetidos:", lista)

