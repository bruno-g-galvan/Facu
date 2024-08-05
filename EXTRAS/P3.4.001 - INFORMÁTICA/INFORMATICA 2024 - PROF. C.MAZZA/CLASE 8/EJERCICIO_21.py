#Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar la carga de enteros al ingresar el cero. Mostrar finalmente el tamaño de la lista.

lista = []
valor = int(input("Valor - (0 para salir): "))

while valor !=0:
    lista.append(valor)
    valor = int(input("Valor - (0 para salir): "))

print("Tamaño de la lista: ",len(lista))  


#Variante con suma









lista = []
valor = int(input("Valor - (0 para salir): "))
suma = valor

while valor !=0:
    lista.append(valor)
    valor = int(input("Valor - (0 para salir): "))
    suma = suma+valor

print("Tamaño de la lista: ",len(lista))
print("La suma es: ",suma)