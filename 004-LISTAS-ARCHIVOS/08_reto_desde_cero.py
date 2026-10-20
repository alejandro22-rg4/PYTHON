# LABORATORIO PUENTE - Reto final: clasificador simulado

# RETO DESDE CERO (sin leer carpetas todavia)
# Usa esta lista:
archivos = ["FACTURA_001.XML", "pedido_02.xml", "nota.txt", "inventario_03.xml", "factura_04.xml", "sin_tipo.xml"]
archivos.append("nuevo_archivo.xml")
archivos.append("otro_archivo.XML")
factura = 0
pedido = 0
inventario = 0
otro = 0
for archivo in archivos:
    nombre = archivo.lower()
    if nombre.endswith(".xml"):
        if nombre.startswith("factura"):
            print(nombre, "-> FACTURA")
            factura += 1
        elif nombre.startswith("pedido"):
            print(nombre, "-> PEDIDO")
            pedido += 1
        elif nombre.startswith("inventario"):
            print(nombre, "-> INVENTARIO")
            inventario += 1
        else:
            print(nombre, "-> OTRO")
            otro += 1
    if nombre.endswith(".xml"):
        print(archivos, "->.XML")
print("Total de XML:", len([nombre for nombre in archivos if nombre.lower().endswith(".xml")]))
print("Total de FACTURA:", len([nombre for nombre in archivos if nombre.lower().endswith(".xml") and nombre.lower().startswith("factura")]))
print("Total de PEDIDO:", len([nombre for nombre in archivos if nombre.lower().endswith(".xml") and nombre.lower().startswith("pedido")]))
print("Total de INVENTARIO:", len([nombre for nombre in archivos if nombre.lower().endswith(".xml") and nombre.lower().startswith("inventario")]))
print("Total de OTRO:", len([nombre for nombre in archivos if nombre.lower().endswith(".xml") and not (nombre.lower().startswith("factura") or nombre.lower().startswith("pedido") or nombre.lower().startswith("inventario"))]))
# TAREA 1: Recorre los nombres con for.
# TAREA 2: Muestra solo los XML (sin importar mayusculas).
# TAREA 3: Clasifica cada XML como FACTURA, PEDIDO, INVENTARIO u OTRO.
# TAREA 4: Muestra el total de XML y el total de cada categoria.
# TAREA 5: Agrega dos nombres nuevos y comprueba el resultado.
