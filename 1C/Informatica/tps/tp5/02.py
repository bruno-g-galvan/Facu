#Diseñar una función para mostrar un título filas de asteriscos, la longitud de la fila de asteriscos
#y el texto del título se recibe como parámetro. Ejemplo: titulo(“Ejercicio 3”, 15)

def title(title, lenght):
    for i in range(lenght):
        print("*", end="")
    print()
    print(title)
    for i in range(lenght):
        print("*", end="")
    print()


titulo = input("Ingrese el titulo: ")
aste = int(input("Ingrese la longitud de asteriscos: "))

title(titulo, aste)