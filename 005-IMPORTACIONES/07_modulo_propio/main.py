import operaciones
print("Resta:", operaciones.restar(10, 4))
multiplicacion = operaciones.multiplicar(3, 7)
print("Multiplicación:", multiplicacion)
print("Suma:", operaciones.sumar(5, 3))
precio = float(input("Ingresa el precio del producto: "))
descuento = float(input("Ingresa el porcentaje de descuento: "))
porcentaje_decimal = descuento / 100
precio_final = operaciones.descuento(precio, porcentaje_decimal)
print("Precio final con descuento:", round(precio_final, 2))



# TAREA 4: Pide dos números y prueba restar() y multiplicar().
# TAREA 5: Pide precio y porcentaje y prueba descuento().
# Ejecuta main.py desde esta misma carpeta.
