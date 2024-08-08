"""
Ejercicio 1: 
Desarrollar  cada  una  de  las  siguientes  funciones  y  escribir  un  programa  que  permita  verificar  su 
funcionamiento, imprimiendo la matriz luego de invocar a cada función: 
 
a. Cargar números enteros en una matriz de N x N, ingresando los datos desde 
teclado. 
c. Intercambiar dos filas, cuyos números se reciben como parámetro. 
d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro. 
e. Calcular el promedio de los elementos de una fila, cuyo número se recibe como 
parámetro. 
f. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número 
se recibe como parámetro.
"""

import random as rd
import numpy as np


#a
def carga_matriz (filas, columnas):
    matriz_1 = []
    for i in range (filas):
        fila = []
        for j in range (columnas):
            fila.append(rd.randint(1, 100))
        matriz_1.append(fila)
    return matriz_1

filas = int(input('Ingrese el numero de filas deseado: '))
columnas = int(input('Ingrese el numero de columnas deseado: '))
matriz_1 = carga_matriz(filas, columnas)

#print(matriz_1)
print(np.matrix(matriz_1))

#B. Intercambiar dos filas, cuyos números se reciben como parámetro.
"""
def row_switcher (a, b, c):
    var_temp1 = ()
    var_temp1 = a[b]
    a[b] = a[c]
    a[c] = var_temp1
    return a


row_switch1 = int(input(f"Ingrese la fila a cambiar. El valor debe ser entre 0 y {filas-1}: "))
row_switch2 = int(input(f"Ingrese la segunda fila a cambiar. El valor debe ser entre 0 y {filas-1}, exceptuando {row_switch1}: "))
row_switcher(matriz_1, row_switch1, row_switch2)
print(np.matrix(matriz_1))
"""

#C. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
"""
#Esta version cambia un valor (fila, columna) por otro:
#def column_switcher (a, b, c, d, e):
#    var_temp2 = ()
#    var_temp2 = a[b][c]
#    a[b][c] = a[d][e]
#    a[d][e] = var_temp2
#    return a

#rowcol_1 = int(input(f"Ingrese la fila del primer valor a cambiar. El valor debe ser entre 0 y {filas-1}: "))
#rowcol_2 = int(input(f"Ingrese la fila del segundo valor a cambiar. El valor debe ser entre 0 y {filas-1}: "))
#column_switch1 = int(input(f"Ingrese la columna del primer valor a cambiar. El valor debe ser entre 0 y {columnas-1}: "))
#column_switch2 = int(input(f"Ingrese la columna del segundo valor a cambiar. El valor debe ser entre 0 y {columnas-1}, exceptuando {column_switch1}: "))
#column_switcher(matriz_1, row_switch1, column_switch1, row_switch2, column_switch2)
#print(np.matrix(matriz_1))
"""

#C_v2. Cambia una columna por otra
"""
def column_switcher (a, b, c):
    for i in range(len(a)):
        var_temp2 = a[i][b]
        a[i][b] = a[i][c]
        a[i][c] = var_temp2
    return a

#rowcol_1 = int(input(f"Ingrese la fila del primer valor a cambiar. El valor debe ser entre 0 y {filas-1}: "))
#rowcol_2 = int(input(f"Ingrese la fila del segundo valor a cambiar. El valor debe ser entre 0 y {filas-1}: "))
column_switch1 = int(input(f"Ingrese la columna del primer valor a cambiar. El valor debe ser entre 0 y {columnas-1}: "))
column_switch2 = int(input(f"Ingrese la columna del segundo valor a cambiar. El valor debe ser entre 0 y {columnas-1}, exceptuando {column_switch1}: "))
column_switcher(matriz_1, column_switch1, column_switch2)
print(np.matrix(matriz_1))
"""

#D. Calcular el promedio de los elementos de una fila, cuyo número se recibe como parámetro.
"""
def prom_fila (a, b):
    acum_fila = 0
    for i in range(len(a[b])):
        acum_fila = acum_fila + a[b][i]
    print(acum_fila)
    promedio = acum_fila/len(a[b])
    return promedio
fila_acumulada = int(input(f"Ingrese la fila de los valores a promediar. El valor debe ser entre 0 y {filas-1}: "))
print(prom_fila(matriz_1, fila_acumulada))
"""
#E. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.

def prom_columna (a, b):
    acum_columna = 0
    acum_impares = 0
    for i in range(len(a)):
        if a[i][b] % 2 != 0:
            acum_columna = acum_columna + a[i][b]
            acum_impares = acum_impares +1 

    print(acum_columna)
    promedio = acum_columna/acum_impares
    return promedio
columna_acumulada = int(input(f"Ingrese la fila de los valores a promediar. El valor debe ser entre 0 y {columnas-1}: "))
print(prom_columna(matriz_1, columna_acumulada))

