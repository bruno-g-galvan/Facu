def cargarDatosCiclistas():
    cantidad = int(input("Ingrese el número de competidores: "))
    numeros = []
    tiempos = []

    for i in range(cantidad):
        numero = int(input("Ingrese el número del competidor: "))
        horas = int(input("Ingrese el tiempo en horas: "))
        minutos = int(input("Ingrese el tiempo en minutos: "))
        segundos = int(input("Ingrese el tiempo en segundos: "))

        tiempo_total_segundos = horas * 3600 + minutos * 60 + segundos
        numeros.append(numero)
        tiempos.append(tiempo_total_segundos)

    return numeros, tiempos

def encontrar_ganador(numeros, tiempos):
    
    tiempo_minimo= tiempos[0]
    indice_ganador=0
    
    for i in range(len(tiempos)):
        if tiempos[i]<tiempo_minimo:
            tiempo_minimo=tiempos[i]
            indice_ganador=i
            
    return numeros[indice_ganador], tiempo_minimo

def convertir_tiempo(segundos):
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60
    return horas, minutos, segundos

def calcular_promedio_tiempos(tiempos):
    suma=0
    
    for i in range(len(tiempos)):
        suma+=tiempos[i]
    
    promedio = suma // len(tiempos)
    return promedio

def main():
    numeros, tiempos = cargarDatosCiclistas()
    numero_ganador, tiempo_ganador = encontrar_ganador(numeros, tiempos)

    horas, minutos, segundos = convertir_tiempo(tiempo_ganador)
    print(f"El ganador es el competidor número {numero_ganador} con un tiempo de {horas}h {minutos}m {segundos}s")

    tiempo_record = int(input("Ingrese el tiempo record registrado en segundos: "))
    if tiempo_ganador < tiempo_record:
        print("El ganador batió el record anterior")
    else:
        print("El ganador no batió el record anterior")

    promedio_tiempos = calcular_promedio_tiempos(tiempos)
    horas, minutos, segundos = convertir_tiempo(promedio_tiempos)
    print(f"El tiempo promedio entre todos los ciclistas es {horas}h {minutos}m {segundos}s")

if __name__ == "__main__":
    main()
