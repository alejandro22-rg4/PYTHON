# Calculadora de precios de TechStore
producto = input("Producto: ")
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
subtotal = precio * cantidad
descuentofijo = subtotal * 0.10
print("descuento fijo:", descuentofijo)
porcentaje =int (input("porcentaje:"))
if 0 <=porcentaje <=100:
  descuento = subtotal * porcentaje/100
  total=subtotal-descuento
  print("Producto:", producto)
  print(f"Subtotal: ${subtotal:.2f}")
  print(f"descuento: ${descuento:.2f}")
  print(f"total: ${total:.2f}")
else:
  print("mensaje de que no es valido")

# TAREA 1: aplica un descuento fijo del 10 %.
# TAREA 2: pide el porcentaje al usuario.
# TAREA 3: muestra subtotal, descuento y total con dos decimales.
