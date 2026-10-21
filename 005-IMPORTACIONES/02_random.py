import random
secreto = random.randint(1, 11)
print("El programa eligió un número del 1 al 11")
intentos = 0
while intentos < 3:
    intento = int(input("Adivina el número: "))
    intentos += 1
    if intento == secreto:
        print("¡Felicidades! Adivinaste el número.")
        break
    elif intento < secreto:
        print("El número es mayor. Intenta de nuevo.")
    else:
        print("El número es menor. Intenta de nuevo.")
    if intentos == 3:
        print("Lo siento, has agotado tus intentos. El número era:", secreto)

# TAREA 1: Pide al usuario un intento usando int(input()).
# TAREA 2: Indica si acertó, o si el intento fue mayor o menor.
# TAREA 3: Permite hasta 3 intentos usando while.
# TAREA 4: Si adivina, termina el ciclo con break.
