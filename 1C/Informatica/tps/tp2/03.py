#Ejercicio 3:Tres personas invierten dinero para fundar una empresa (no necesariamente en partes iguales). Calcular qué porcentaje invirtió cada una.
num1 = int(input("Inversión 1: "))
num2 = int(input("Inversión 2: "))
num3 = int(input("Inversión 3: "))
num_total = num1 + num2 + num3

prom1 = (num1 * 100) / num_total
prom2 = (num2 * 100) / num_total
prom3 = (num3 * 100) / num_total

print("La inversión 1 fue un", prom1,"%")
print("La inversión 2 fue un", prom2,"%")
print("La inversión 3 fue un", prom3,"%")