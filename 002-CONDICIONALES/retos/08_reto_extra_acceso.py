# LABORATORIO 2 - 08: RETO EXTRA DESDE CERO
# TAREA 1: Pedir nombre y edad.
# TAREA 2: Preguntar si tiene autorizacion (si/no).
# TAREA 3: Permitir ingreso solo si edad >= 18 Y autorizacion == 'si'.
# TAREA 4: Mostrar motivo cuando no se permita el ingreso.
# TAREA 5: Aceptar 'SI', 'Si' y 'si' usando .lower().
nombre = input("Nombre: ")
edad = int(input("Edad: "))
autorizacion = input("tiene autorizacion (si/no): ").lower()
if edad >= 18 and autorizacion == 'si':
    print("Bienvenido", nombre)
else:
    if edad < 18:
        print("No tiene la edad suficiente para ingresar.")
    if autorizacion != 'si':
        print("No tiene la autorizacion necesaria para ingresar.")