sueldo = int(input("Ingresar Sueldo: "))
antiguedad = int(input("Ingrese Antiguedad: "))

if(sueldo < 500 and antiguedad < 10):
    sueldo_total = sueldo + (sueldo * 5)/100
    print("Sueldo con el 5% de aumento es: ",sueldo_total)
    
elif(sueldo < 500 and antiguedad >= 10):
    sueldo_total = sueldo + (sueldo * 20)/100
    print("Sueldo con el 20% de aumento es: ",sueldo_total)
else:
    print("Sueldo total sin aumentos: ",sueldo)
    
    
    