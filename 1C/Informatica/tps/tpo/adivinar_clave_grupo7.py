import random as rd

#Funcion que genera una lista de 3 valores del 0 al 9 la cual actuara como una clave numerica la cual debes adivinar.

def adivinar_clave():
    list_split = []
    cont = 0

    for _ in range(3):
        list_split.append(rd.randint(0,9))

    print('')
    print('Clave generada con exito!')

    for i in range((len(list_split))):
        print('')
        print('Adivine el numero en la posicion', i + 1 , 'de la clave.')
    
        num = int(input('Ingrese el dígito correcto entre 0 y 9 (-1 para rendirse): '))

        while num != list_split[i]:

            while num < 0 or 9 < num:
                if num == -1:
                    print('------------ Tus intentos fueron', cont, '-----------')
                    return False
                
                num = int(input('Ingrese un digito valido entre 0 y 9 (-1 para rendirse): '))

            print('')
            print('------- Error! El dígito no es correcto -------')
            print('')
            cont = cont + 1
            num = int(input('Ingrese el digito correcto entre 0 y 9 (-1 para rendirse): '))
        
        cont = cont + 1
        print('')
        print('---------------- Digito valido! ---------------')
        

    print('')
    print('----------------- Felicidades! ----------------')
    print('-------------- Permiso concedido --------------')
    print('-------- Tus intentos totales fueron', cont, '-------')
    return True