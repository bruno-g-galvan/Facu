#Ejercicio 7:Se ingresan N letras. Determinar la cantidad de vocales ingresadas.
character_array = []

while True:
    char = input("Ingrese la letra. Si ya terminó, indíquelo ingresando 'Listo': ")

    try:
        integer = str(char)
        if char[:1] == char and (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
            character_array.append(char)
        elif char == "Listo":
            break
        else:
            print("Solo se aceptan valores string de longitud 1, pruebe nuevamente... ")
            continue
    except ValueError:
        print("Solo se aceptan valores string de longitud 1, pruebe nuevamente... ")
        continue

print(f"La cantidad de vocales ingresadas fue de {len(character_array)}.")