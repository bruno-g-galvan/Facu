matriz = []
n = 1

for f in range (4):
    matriz.append([])
    for c in range (4):
        if f == c:
            matriz[f].append(n)
        else:
            matriz[f].append(0)
    n = n + 2
    
print (matriz)


