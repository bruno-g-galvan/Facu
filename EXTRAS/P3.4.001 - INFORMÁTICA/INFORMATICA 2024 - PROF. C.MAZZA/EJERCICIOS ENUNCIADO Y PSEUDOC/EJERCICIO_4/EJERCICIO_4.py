num1 = int(input("ingrese un valor: "))
porcentaje1 = int(input("ingrese el porcentaje a calcular: "))

resultado1 = (num1*porcentaje1)/100
porcentaje2 = 100-porcentaje1

resultado2 = (num1*porcentaje2)/100

print("El ",porcentaje1," porciento de", num1, " es: ",resultado1)
print("El ",porcentaje2," porciento de", num1, " es: ",resultado2)
