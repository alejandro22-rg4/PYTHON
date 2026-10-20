
nombres = ["  FACTURA.XML ", " pedido.xml", "INVENTARIO.XML  ", " reporte.TXT "]

for nombre in nombres:
    print(nombre.strip())
print("nombres normalizados:")
for nombre in nombres:
    nombre_normalizado = nombre.strip().lower()
print(nombre_normalizado)
print("nombres normalizados que son XML:")
for nombre in nombres:
    nombre_normalizado = nombre.strip().lower()
    if nombre_normalizado.endswith(".xml"):
        print(nombre_normalizado)
# TAREA 1: Usa strip() y lower() para normalizar cada nombre.
# TAREA 2: Imprime solo los nombres normalizados que sean XML.
# TAREA 3: Muestra el nombre original y el normalizado.
