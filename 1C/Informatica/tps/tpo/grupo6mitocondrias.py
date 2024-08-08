import random

def adivinar_clave():
    num1= random.randint(0,9)
    num2= random.randint(0,9)
    num3= random.randint(0,9)
    intentos= 0
    continuar = 1
    while continuar != 0 and continuar!= 4:
        while continuar == 1:
            intentonum1 = int(input("Ingrese el primer numero (-1 para abandonar): "))
            intentos= 1 + intentos
            if intentonum1 == -1:
                continuar = 0
            elif intentonum1 == num1:
                print("El número ingresado es el primer valor de la contra.")
                continuar = 2
            else:
                print("El número ingresado NO es el primer valor de la contra.")
        while continuar == 2:
            intentonum2 = int(input("Ingrese el segundo numero (-1 para abandonar): "))
            intentos= 1 + intentos
            if intentonum2 == -1:
                continuar = 0
            elif intentonum2 == num2:
                print("El número ingresado es el segundo valor de la contra.")
                continuar = 3
            else:
                print("El número ingresado NO es el segundo valor de la contra.")
        while continuar == 3:
            intentonum3 = int(input("Ingrese el tercer numero (-1 para abandonar): "))
            intentos= 1 + intentos
            if intentonum3 == -1:
                continuar = 0
            elif intentonum3 == num3:
                print("El número ingresado es el tercer valor de la contra.")
                continuar = 4
                print("yeyyyyyyyyyyyyyyyyyy adivinaste")
                print("La contra es", num1,num2,num3)
            else:
                print("El número ingresado NO es el tercer valor de la contra.")

    

    
    if continuar == 4:
        print("la cantidad de intentos fue:", intentos)
        return True
    if continuar != 4:
        print("la cantidad de intentos fue:", intentos)
        return False
    