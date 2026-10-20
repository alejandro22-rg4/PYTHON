# LABORATORIO PUENTE - Buscar palabras dentro de textos

mensajes = ["Pedido recibido", "FACTURA pendiente", "Inventario actualizado", "Factura aprobada"]

for mensaje in mensajes:
    print(mensaje)
    print("mensaje que contiene 'factura':")
contador = 0
for mensaje in mensajes:
    if "factura" in mensaje.lower():
        print(mensaje)
        contador += 1
print("Total de mensajes que contienen 'factura':", contador)
# TAREA 1: Imprime solo los mensajes que contengan factura.
# TAREA 2: Ignora mayusculas y minusculas.
# TAREA 3: Cuenta los mensajes encontrados.
