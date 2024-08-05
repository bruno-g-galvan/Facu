
#Objetivo: cargar la información de legajos y notas de los alumnos
#Parametros de entrada: ninguno
#Parámetros de salida: dos listas, una con las notas de los alumnos y otro con los legajos de los alumnos 
def cargar_datos():
    bandera=True
    matriz=[[],[]]
    
    while bandera:
        legajo= int(input("Ingrese el número de legajo\n"))
        if legajo==-1:
            bandera=False
        else:
            nota = int(input("Ingrese su nota\n"))
            
            while nota<1 or nota>10:
                print("Nota inválida. Debe estar entre 1 y 10.")
                nota = nota(input("Ingrese su nota\n"))
            matriz[0].append(legajo)
            matriz[1].append(nota)
    return matriz


def calcular_aprobados_desaprobados(matriz):
    aprobados=0
    desaprobados=0
    
    for i in range(len(matriz[0])):
        if matriz[1][i]>=4:
            aprobados+=1
        else:
            desaprobados+=1
    return aprobados, desaprobados

def calcularPromedio(matriz):
    suma=0
    alumnosSuperanPromedio=[]
    
    for i in range(len(matriz)):
        suma+=matriz[1][i]
        
    promedio=suma/len(matriz[0])
    
    for i in range(len(matriz[0])):
        if matriz[1][i]>promedio:
            alumnosSuperanPromedio.append(matriz[0][i])
    
    
    return promedio, alumnosSuperanPromedio

    
def mostrarDatosOrdenados(matriz):
    for i in range(len(matriz[0])):
        for j in range(0,len(matriz[0])-i-1):
            if matriz[0][j]>matriz[0][j+1]:
                matriz[0][j],matriz[0][j+1] =  matriz[0][j+1],matriz[0][j]
                matriz[1][j],matriz[1][j+1]= matriz[1][j+1],matriz[1][j]
    
    for i in range(len(matriz[0])):
        print("Legajo: ",matriz[0][i],"Notas: ",matriz[1][i])


def main():
    matriz=cargar_datos()
    aprobados,desaprobados=calcular_aprobados_desaprobados(matriz)
    
    print("La cantidad de alumnos aprobados es: ",aprobados)
    print("La cantidad de alumnos desaprobados es: ",desaprobados)
    
    promedio,alumnosSuperanPromedio= calcularPromedio(matriz)
    
    print("El promedio de notas del curso es: ",promedio)
    print("Legajos que superan el promedio:")
    for i in range(len(alumnosSuperanPromedio)):
        print(alumnosSuperanPromedio[i])
    
    mostrarDatosOrdenados(matriz)
    




if __name__=="__main__":
    main()
        
        
    
