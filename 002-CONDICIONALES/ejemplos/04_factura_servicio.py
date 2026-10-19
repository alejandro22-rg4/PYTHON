# LABORATORIO 2 - 04: Factura ficticia
horas = float(input("Horas de trabajo: "))
tarifa = 12.50
repuestos = float(input("Costo de repuestos: "))
if horas < 0 or repuestos < 0:
    print("Error: Las horas y el costo de repuestos deben ser valores positivos.")
else:
    subtotal = horas * tarifa + repuestos
    if subtotal >= 100:
        descuento = subtotal * 0.08
    else:
        descuento = 0
    total = subtotal - descuento
    print("subtotal: $", round(subtotal, 2))
    print("descuento: $", round(descuento, 2))
    print("total: $", round(total, 2))
# TAREA 1: Validar que horas y repuestos no sean negativos.
# TAREA 2: Si subtotal >= 100, aplicar 8% de descuento.
# TAREA 3: Mostrar subtotal, descuento y total con dos decimales.
