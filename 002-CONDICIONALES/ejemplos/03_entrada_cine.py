# LABORATORIO 2 - 03: Entradas al cine
edad = int(input("Edad: "))
cantidad = int(input("Cantidad de entradas: "))
precio = 5.00
print("Total inicial:", precio * cantidad)
if edad <= 12:
    precio = 3.00
elif edad >= 65:
    precio = 4.00
total = precio * cantidad
print("Precio unitario: $", round(precio, 2))
print("Total: $", round(total, 2))
# TAREA 1: Si la edad es menor de 12, precio = 3.
# TAREA 2: Si la edad es 65 o mas, precio = 4.
# TAREA 3: Para el resto, precio = 5.
# TAREA 4: Validar que edad >= 0 y cantidad > 0.
# TAREA 5: Mostrar precio unitario y total con dos decimales.
