
#Objetivo: cargar la información de legajos y notas de los alumnos
#Parametros de entrada: ninguno
#Parámetros de salida: dos listas, una con las notas de los alumnos y otro con los legajos de los alumnos 
def cargar_datos():
    bandera=True
    legajos=[]
    notas=[]
    
    while bandera:
        legajo= int(input("Ingrese el número de legajo\n"))
        if legajo==-1:
            bandera=False
        else:
            nota = int(input("Ingrese su nota\n"))
            
            while nota<1 or nota>10:
                print("Nota inválida. Debe estar entre 1 y 10.")
                nota = nota(input("Ingrese su nota\n"))
            legajos.append(legajo)
            notas.append(nota)
    return legajos, notas


def calcular_aprobados_desaprobados(notas):
    aprobados=0
    desaprobados=0
    
    for i in range(len(notas)):
        if notas[i]>=4:
            aprobados+=1
        else:
            desaprobados+=1
    return aprobados, desaprobados

def calcularPromedio(legajos,notas):
    suma=0
    alumnosSuperanPromedio=[]
    
    for i in range(len(notas)):
        suma+=notas[i]
        
    promedio=suma/len(notas)
    
    for i in range(len(notas)):
        if notas[i]>promedio:
            alumnosSuperanPromedio.append(legajos[i])
    
    
    return promedio, alumnosSuperanPromedio

    
def mostrarDatosOrdenados(legajos,notas):
    for i in range(len(legajos)):
        for j in range(0,len(legajos)-i-1):
            if legajos[j]>legajos[j+1]:
                legajos[j],legajos[j+1] =  legajos[j+1],legajos[j]
                notas[j],notas[j+1]= notas[j+1],notas[j]
    
    for i in range(len(legajos)):
        print("Legajo: ",legajos[i],"Notas: ",notas[i])


def main():
    legajos,notas=cargar_datos()
    aprobados,desaprobados=calcular_aprobados_desaprobados(notas)
    
    print("La cantidad de alumnos aprobados es: ",aprobados)
    print("La cantidad de alumnos desaprobados es: ",desaprobados)
    
    promedio,alumnosSuperanPromedio= calcularPromedio(legajos,notas)
    
    print("El promedio de notas del curso es: ",promedio)
    print("Legajos que superan el promedio:")
    for i in range(len(alumnosSuperanPromedio)):
        print(alumnosSuperanPromedio[i])
    
    mostrarDatosOrdenados(legajos,notas)
    




if __name__=="__main__":
    main()
        
        
    
