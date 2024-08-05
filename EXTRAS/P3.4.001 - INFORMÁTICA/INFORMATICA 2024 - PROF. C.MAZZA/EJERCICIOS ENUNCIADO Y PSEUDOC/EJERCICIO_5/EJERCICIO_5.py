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
       
    
