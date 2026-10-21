import string
import random
print("Generador de códigos aleatorios",random.choice(string.ascii_uppercase + string.digits)) 
caracteres = string.ascii_uppercase + string.digits
print("Caracteres disponibles:", caracteres)
print("Letras disponibles:", string.ascii_uppercase)
print("Dígitos disponibles:", string.digits)
for i in range(3):
    codigo = ''.join(random.choice(caracteres) for _ in range(6))
    print("Código generado:", codigo)

# TAREA 1: Combina letras mayúsculas y dígitos en una variable llamada caracteres.
# TAREA 2: Genera un código ficticio de 6 caracteres usando random.choice().
# TAREA 3: Muestra tres códigos distintos con un bucle for.
# IMPORTANTE: Estos códigos son solo para practicar, NO son contraseñas seguras.
