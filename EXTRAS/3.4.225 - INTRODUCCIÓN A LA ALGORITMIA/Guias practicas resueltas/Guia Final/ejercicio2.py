def cargarDatos():
    unidades=[]
    superficies=[]
    
    for i in range(5):
        bandera=False
        
        while not bandera:
            unidad= int(input("Ingrese el número de unidad:\n"))
            duplicado=False
            for i in range(len(unidades)):
                    if unidades[i]==unidad:
                        duplicado=True
                        print("Numero de unidad duplicado. Ingrese otro número")
            if duplicado==False:
                bandera=True
        superficie=float(input("Ingrese la superficie del departamento:\n"))
        
        unidades.append(unidad)
        superficies.append(superficie)
    return unidades, superficies


def calcularPromedioExpensas(superficies,valorPorM2):
    
    suma=0
    
    for i in range(len(superficies)):
        suma+=superficies[i]*valorPorM2
    
    promedio=suma/len(superficies)
    
    return promedio

def ordenarPorSuperficie(unidades, superficies):
    
    for i in range(len(superficies)):
        for j in range(0, len(superficies)-i-1):
            if superficies[j]<superficies[j+1]:
                aux=superficies[j]
                superficies[j]=superficies[j+1]
                superficies[j+1]=aux
                aux2= unidades[j]
                unidades[j]=unidades[j+1]
                unidades[j+1]=aux2

def mostrarLista(unidades,superficie):
    print("Listado de unidades ordenados por superficie en m2 mayor a menor:\n")
    for i in range(len(unidades)):
        print("Unidad ",unidades[i]," Superficie: ", superficie[i] )
        

def main():
    unidades, superficies=cargarDatos()
    
    valorPorM2= float(input("Ingrese el valor de expensas por metro cuadrado\n"))
    
    print("El promedio de expensas a pagar es: ",calcularPromedioExpensas(superficies,valorPorM2))
    
    ordenarPorSuperficie(unidades,superficies)
    mostrarLista(unidades,superficies)
    
    
    
    
    
if __name__=="__main__":
    main()