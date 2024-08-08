#Generar simulación de Datos de Viajes
#Una agencia de viajes llamada 'ViajesMundo' desea realizar un control de sus viajes
#disponibles. La agencia ofrece múltiples destinos diferentes y necesita mantener un mínimo de
#asientos disponibles por destino. La capacidad máxima de asientos por destino también está
#limitada. Para simular esta situación, se deben ingresar códigos de destino de cuatro dígitos
#(entre 1000 y 9999) hasta ingresar -1. Para cada código de destino, se simula la cantidad de
#asientos disponibles con un número al azar entre dos límites especificados (el rango puede ser
#creado al azar o por teclado cuidando que sea un rango valido). Si el código ya existe en la lista,
#se debe rechazar.
#Informes:
#Se debe mostrar cuántos destinos tienen menos del mínimo de asientos disponibles y un
#listado por destino y cantidad de asientos disponibles solo de aquellos destinos que tengan
#asientos disponibles.

import random as rd

#Funcion que genera una lista de 3 valores del 0 al 9 la cual actuara como una clave numerica la cual debes adivinar.

def adivinar_clave():
    list_split = []
    cont = 0
    num = 0
    for _ in range(3):
        list_split.append(rd.randint(0,9))

    print('')
    print('Clave generada con exito!')
    while num != -1:
        for i in range((len(list_split))):
            
            while num != -1:
                print('')
                print('Adivine el numero en la posicion', i + 1 , 'de la clave.')

                num = int(input('Ingrese el dígito correcto entre 0 y 9 (-1 para rendirse): '))

                while num != list_split[i] and num != -1:

                    while (num < 0 or 9 < num) and num != -1:
                        
                        num = int(input('Ingrese un digito valido entre 0 y 9 (-1 para rendirse): '))

                    if num != -1:
                        print('')
                        print('------- Error! El dígito no es correcto -------')
                        print('')
                        cont = cont + 1
                        num = int(input('Ingrese el digito correcto entre 0 y 9 (-1 para rendirse): '))

                if num != -1:
                    cont = cont + 1
                    print('')
                    print('---------------- Digito valido! ---------------')
            

        
    if num != -1:
        print('')
        print('----------------- Felicidades! ----------------')
        print('-------------- Permiso concedido --------------')
        print('-------- Tus intentos totales fueron', cont, '-------')
        return True
    else:
        return False

#Funcion que detecta un numero en una lista. En el caso de encontrarlo, devuelve ese valor y sino devuelve -1. 
#Funcionamiento valido ya que la lista solo tendra valores entre 1000 y 9999. 
def num_in_lst(num, lst):
    for i in range(0, len(lst)):
        if lst[i][0] == num:
            return i
    return -1

#Funcion para generar la simulacion de viajes. Entradas: Codigo de destino, minimo de pasajes y maximo de pasajes. 
#Se genera un valor entre 0 y el maximo de pasajes por cada destino que sera el valor de pasajes comprados.
#Este programa funciona hasta que el usuario ingrese -1.
def trip_simulation():

    destino = int(input('Ingrese el codigo de destino (-1 para terminar la ingesta): '))

    while destino != -1:
        if 1000 <= destino and destino <= 9999:
            
            #Validamos si el destino ya se encuentra en la primer posicion de todas las sublistas en lista_viajes.
            if num_in_lst(destino, lista_viajes) == -1:
                sublista = []
                minimo = int(input('Ingrese el minimo numero de viajeros necesarios para confirmar el viaje: '))

                while minimo < 1:
                    minimo = int(input('Ingrese un numero minimo valido mayor o igual a 1: '))

                maximo = int(input('Ingrese el maximo numero de viajeros en el viaje: '))

                while maximo <= minimo:
                    maximo = int(input('Ingrese un numero maximo mayor al minimo ingresado: '))

                #Sublista tendra la siguiente estructura: [cod. de destino, minimo, maximo, pasajes comprados]
                sublista.append(destino)
                sublista.append(minimo)
                sublista.append(maximo)
                sublista.append(rd.randint(0, maximo))

                #Insertamos sublista en lista_viajes. Ejemplo luego de varios destinos insertados: [[1001, 10, 20, 14], [1002, 15, 40, 7], ...]
                lista_viajes.append(sublista)
                print('')
                print('Codigo ingresado con exito!')
                print('')
            else:
                print('')
                print('El codigo de destino ingresado se encuentra utilizado. Intentelo nuevamente.')
                print('')
        else:
            print('')
            print('El codigo no es valido (debe ser entre 1000 y 9999 o -1 para terminar)')
            print('')
        destino = int(input('Ingrese otro codigo de destino (-1 para terminar): '))

#Funcion de informes. 
def reports():

    print('-------------------- Informes ---------------------')
    print('---------------- Total de viajes ------------------')
    print('')

    for i in range(len(lista_viajes)):
        if lista_viajes[i][3] < lista_viajes[i][1]:
            print('---------------------------------------------------')
            print('------------- Codigo de destino', lista_viajes[i][0], '--------------')
            print('----- Estado del viaje: En venta / No aprobado ----')
            print('--------- Numero de pasajes vendidos:', lista_viajes[i][3], '----------')
            print('Numero de pasajes disponibles para este destino:', lista_viajes[i][2] - lista_viajes[i][3])
            print('---------------------------------------------------')
            print('')
        else:
            print('---------------------------------------------------')
            print('------------- Codigo de destino', lista_viajes[i][0], '--------------')
            print('----------- Estado del viaje: Aprobado ------------')
            print('---------------------------------------------------')
            print('')

if adivinar_clave():

    lista_viajes = []

    print('')
    print('1. Generar simulación de “Datos de Viajes”')
    print('2. Ver informes')
    print('3. Salir')
    print('')

    numero = int(input())

    while numero != 3:

        if numero == 1:
            trip_simulation()

        elif numero == 2:
            reports()

        else:  
            print('')
            print('--Ingrese un valor valido dentro de las opciones--')
            print('')
        
        print('1. Generar simulación de “Datos de Viajes”')
        print('2. Ver informes')
        print('3. Salir')
        print('')
        numero = int(input())

else:
    print('-- Ha decidido rendirse. Suerte la proxima! --')

