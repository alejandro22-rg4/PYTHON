compras = []
while True:
    print("\n1. Agregar  2. Ver  3. Salir 4. Buscar")
    opcion = input("Opcion: ")
    if opcion == "1":
        producto = input("Producto: ").strip()
        if producto:
            compras.append(producto)
    elif opcion == "2":
        print(compras)
    elif opcion == "3":
        break
    elif opcion == "4":
        producto_a_buscar = input("Producto a buscar: ").strip().lower()
        encontrados = [p for p in compras if p.lower() == producto_a_buscar]
        if encontrados:
            print("Producto encontrado:", encontrados)
        else:
            print("Producto no encontrado")
    else:
        print("Opcion invalida")
print("Cantidad de productos:", len(compras))
# TAREA 1: Mostrar los productos numerados con enumerate(compras, start=1).
# TAREA 2: Agregar opcion 4 para buscar un producto (ignorar mayusculas).
# TAREA 3: Mostrar la cantidad de productos al salir.
