# RETO DESDE CERO (sin codigo inicial)
productos = ["Mouse", "Teclado", "Monitor"]
cantidades = [12, 3, 0]
total_unidades = 0
for i in range(len(productos)):
    producto=productos[i]
    cantidad=cantidades[i]
    total_unidades += cantidad
    print("Producto:", producto, "Cantidad:", cantidad)
    if cantidad == 0:
        print("Agotado")
    elif 1 <= cantidad <= 5:
        print("Stock bajo")
    else:
        print("Disponible") 
print("Total de unidades:", total_unidades)
productos.append(input("Nuevo producto: "))
cantidades.append(int(input("Cantidad del nuevo producto: ")))
print("cantidad de productos:", len(productos))
# Crea dos listas relacionadas:
# productos = ["Mouse", "Teclado", "Monitor"]
# cantidades = [12, 3, 0]
# 1. Recorre las listas usando range(len(productos)).
# 2. Muestra nombre y cantidad de cada producto.
# 3. Si cantidad es 0, muestra "Agotado".
# 4. Si cantidad esta entre 1 y 5, muestra "Stock bajo".
# 5. Si cantidad es mayor a 5, muestra "Disponible".
# 6. Calcula el total de unidades.
# EXTRA: Permite agregar un nuevo producto y su cantidad.
