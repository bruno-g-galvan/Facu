
salario = int(input("Ingrese el salario del trabajador: "))
cant_hhee = int(input("Ingrese cantidad de horas extras: "))

try:
    opcion = int(input("Ingrese la categoria:"))
    
    match opcion:
        case 1:
            total_hhee = cant_hhee * 30
            total_sueldo = total_hhee + salario    
            print("El sueldo total del empleado es: ",total_sueldo)   
        case 2:
            total_hhee = cant_hhee * 38
            total_sueldo = total_hhee + salario    
            print("El sueldo total del empleado es: ",total_sueldo)
        case 3:
            total_hhee = cant_hhee * 50
            total_sueldo = total_hhee + salario    
            print("El sueldo total del empleado es: ",total_sueldo)
        case 4:
            total_hhee = cant_hhee * 70
            total_sueldo = total_hhee + salario    
            print("El sueldo total del empleado es: ",total_sueldo)        
        case _:
            print("Opción Incorrecta...")              
            
       
    
except ValueError:
    print("Ingrese un digito numerico...")
    
   