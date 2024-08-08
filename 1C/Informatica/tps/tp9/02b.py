matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
n = 1

for f in range (4):
    matriz[3-f][f] = n
    n = n * 3
for fila in matriz:
    print(fila)
