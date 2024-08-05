print("____PROCESO DE REGISTRO_____")
usuario_reg = input("Ingrese usuario a registrar: ")
password_reg = input("Ingrese contraseña: ")
print("Registro exitoso...")

print("-------------------------------------")

print("____PROCESO DE VALIDACION_____")

usuario = input("Ingrese usuario: ")
password = input("Ingrese contraseña: ")

if(usuario != usuario_reg or password != password_reg):
    print("Usuario o contraseña incorrecto...")
else:
    print("Bienvenido: ",usuario_reg)
    
    cant_dias = int(input("Ingrese cantidad de dias de alquiler: "))
    valor_total = cant_dias*30000
    
    if cant_dias < 15:
        valor_final = valor_total + 2000
        comision = (valor_final*20)/100
        print("El valor total del alquiler mas limpieza es: $",valor_final)
        print("El valor de la comisión es: $",comision)
    else:
         comision = (valor_total*8)/100
         print("El valor total del alquiler es: $",valor_total)   
         print("El valor de la comisión es: U$S",comision)


    
        
    
    
    