# LABORATORIO PUENTE - Filtrar nombres por extension

archivos = ["factura.xml", "ventas.csv", "PEDIDO.XML", "notas.txt", "inventario.xml"]

for nombre in archivos:
    print(nombre)
print("archivos con extension .xml:")
for nombre in archivos:
    if nombre.endswith(".xml") or nombre.endswith(".XML"):
        print(nombre)
print("Total de archivos con extension .xml:", len([nombre for nombre in archivos if nombre.endswith(".xml") or nombre.endswith(".XML")]))
# TAREA 1: Muestra solo los nombres que terminan en .xml.
# TAREA 2: Haz que tambien reconozca .XML.
# TAREA 3: Cuenta cuantos XML aparecen.