# LABORATORIO PUENTE - Clasificar documentos por su nombre

archivos = ["factura_01.xml", "pedido_02.xml", "inventario.xml", "FACTURA_03.XML", "otros.xml"]

for archivo in archivos:
    nombre = archivo.lower()
    print("Revisando:", nombre)
print("Clasificación de archivos:")
for archivo in archivos:
    nombre = archivo.lower()
    if nombre.startswith("factura"):
        print(archivo, "-> FACTURA")
    elif nombre.startswith("pedido"):
        print(archivo, "-> PEDIDO")
    elif nombre.startswith("inventario"):
        print(archivo, "-> INVENTARIO")
    else:
        print(archivo, "-> SIN CLASIFICAR")

# TAREA 1: Si empieza por factura, imprime 'FACTURA'.
# TAREA 2: Si empieza por pedido, imprime 'PEDIDO'.
# TAREA 3: Si empieza por inventario, imprime 'INVENTARIO'.
# TAREA 4: Para cualquier otro nombre, imprime 'SIN CLASIFICAR'.
