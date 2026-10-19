clave_correcta = "python123"  # Clave ficticia para practicar
intentos = 0
while intentos < 3:
    clave = input("Escribe la clave de practica: ")
    intentos += 1
    if clave == clave_correcta:
        print("Correcto")
        break
    print("Intenta nuevamente")
print("Intentos utilizados:", intentos)
if intentos == 3:
    print("Intentos agotados")
# TAREA 1: Mostrar cuantos intentos se utilizaron.
# TAREA 2: Si no se acierta tras 3 intentos, mostrar "Intentos agotados".
