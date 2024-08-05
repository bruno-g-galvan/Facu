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
    
    cant_metros = int(input("Ingrese cantidad de metros de la propiedad: "))
    valor_total = cant_metros*2000
    
    if valor_total > 200000:
        porcentaje = (valor_total*5)/100
        valor_final = valor_total + porcentaje
        comision = (valor_final*8)/100
        print("El valor total de la propiedad mas impuesto es: U$S",valor_final)
        print("El valor de la comisión es: U$S",comision)
    else:
         comision = (valor_total*8)/100
         print("El valor total de la propiedad sin impuesto es: U$S",valor_total)   
         print("El valor de la comisión es: U$S",comision)


    
        
    
    
    