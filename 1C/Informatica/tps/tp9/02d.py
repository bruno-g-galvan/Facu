matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
n = 1

for f in range (4):
    if f%2 == 0:
        for c in range (4):
            if c%2 == 0:
                matriz[f][c] = 0
            else:
                matriz[f][c] = n
                n = n + 1
    else:
        for c in range (4):
            if c%2 == 0:
                matriz[f][c] = n
                n = n + 1
            else:
                matriz[f][c] = 0
for fila in matriz:
    print(fila)