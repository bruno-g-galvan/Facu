
num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))
print("Menu de opciones: 1-SUMA / 2-RESTA / 3-PRODUCTO / 4-DIVISION...")

try:  
    opcion = int(input("Elija una opción: "))    
    match opcion:
        case 1:
            resultado = num1+num2
            print("El resultado de la suma es: ",resultado)
        case 2:
            resultado = num1-num2
            print("El resulado de la resta es: ",resultado)
        case 3:
            resultado = num1*num2
            print("El resultado de la multiplicacion es: ",resultado)              
        case 4:
         if num2 != 0:
             resultado = num1/num2
             print("El resultado de la division es: ",resultado)
         else:
            print("No se puede dividir por Cero...")
        case _:
            print("Opcion Incorrecta...")
except ValueError:
            print("Por favor digite un numero....")