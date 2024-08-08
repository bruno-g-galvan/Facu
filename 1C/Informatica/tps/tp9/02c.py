matriz = []
n = 8

for f in range (4):
    matriz.append([])
    for c in range (4):
        matriz[f].append(n)
    n = n // 2
    
print (matriz)