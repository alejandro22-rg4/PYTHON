# LABORATORIO 2 - 01: Conversor de temperatura
# Ejecuta este programa y completa los retos.
celsius = float(input("Temperatura en Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Fahrenheit:", round(fahrenheit, 2))
celsius_converted = (fahrenheit - 32) * 5 / 9
print("Celsius:", round(celsius_converted, 2))
if fahrenheit < 32:
    print("Hace frio")
elif fahrenheit < 68:
    print("Esta fresco")
else:
    print("Hace calor")
# TAREA 1: Mostrar el resultado con dos decimales.
# TAREA 2: Pedir una temperatura en Fahrenheit y convertirla a Celsius.
# TAREA 3: Mostrar ambas conversiones con mensajes claros.
