#Definimos una lista con tres elementos:
lista = [10,20,30]  
#Mostramos la lista
print(lista)
#Imprimimos la cantidad de elementos que tiene la lista, en nuestro caso lo definimos con 3:
print (len(lista))
#Agregamos una nuevo elemento al final de la lista llamando al método append:
lista.append(100)
#Si llamamos nuevamente a la función len y le pasamos el nombre de nuestra lista ahora retorna un 4:
print (len(lista))

#Imprimimos ahora el primer y cuarto elemento de la lista (recordar que se numeran a partir de cero):

print("este es el primer elemento: ",lista[0])
print("este es el cuarto elemento: ",lista[3])



