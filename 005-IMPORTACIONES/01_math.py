import math

numero = 81
numero=int(input("Ingresa un número positivo: "))
print("Raíz cuadrada:", math.sqrt(numero))
print("Redondeo hacia arriba:", math.ceil(4.2))
print("Redondeo hacia abajo:", math.floor(4.8))
radio = float(input("Ingresa el radio del círculo: "))
area = math.pi * radio ** 2
print("Área del círculo:", round(area, 2))
# TAREA 1: Solicita un número positivo con input() y calcula su raíz cuadrada.
# TAREA 2: Calcula el área de un círculo con radio ingresado por el usuario.
# Fórmula: math.pi * radio ** 2
# TAREA 3: Muestra el área con dos decimales usando round().
