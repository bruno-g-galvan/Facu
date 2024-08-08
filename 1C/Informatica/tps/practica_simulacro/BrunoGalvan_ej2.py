#Dada la sucesión 1000, 999, 997,994,990 ……en donde cada valor se obtiene por la resta de valor anterior menos la ubicación en la serie:  
#1000  
#1000-1 =999  
#999-2=997  
#997-3=994  
#994-4=990  
#Mostrar términos hasta que la suma de ellos supere un tope e informar si término ubicado en el último lugar de la sucesión es un numero primo. 
var1 = 1000
var2 = 0
i = 0
print(var2)

not_prime = False

#La suma de valores maxima seria 29820 luego de 44 sumas consecutivas de valores. Luego de este punto la funcion tiende al menos infinito. 
#Por esta naturaleza, el valor tope debe estar comprendido entre 0 y 29820. 
#En el caso que se precise solventar esta caida hacia los valores negativos se debe sumar al contador var2 el modulo de var1 - i.

tope = int(input("Ingrese el tope comprendido entre 0 y 29820: "))

while tope > var2:
    var1 = var1 - i
    var2 += var1
    print(var2)
    print(i)
    i += 1

i = 0

print(f"El numero maximo es: {var2}")

for i in range (2, int(var2/2)):
    if var2 % i == 0:
        not_prime = True

if not_prime:
    print(f"El numero no es primo.")
else:
    print(f"El numero es primo.")