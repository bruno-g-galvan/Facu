#Ejercicio 4:
#Leer una medida en metros e imprimir esta medida expresada en centímetros, pulgadas, pies y yardas. Los factores de conversión son:
#1 pie = 12 pulgadas
#1 yarda = 3 pies
#1 pulgada = 2,54 cm.
#1 metro = 100 cm.
medida = int(input("Ingrese medida en metros a convertir: "))
centimetros = medida * 100
pulgadas = centimetros / 2.54
pies = pulgadas / 12
yardas = pies / 3

print("La medida en centimetros es: ", centimetros)
print("La medida en pulgadas es: ", pulgadas)
print("La medida en pies es: ", pies)
print("La medida en yardas es: ", yardas)