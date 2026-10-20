# LABORATORIO PUENTE - Recorrer una lista de productos

productos = ["Teclado", "Mouse", "Monitor", "Impresora", "Webcam"]
productos.append("Micrófono")
productos.append("Auriculares")
print("Lista de productos:",productos)
mensajes = [
 "producto de alta calidad.",
    "producto con garantía de 2 años.",
    "este producto es compatible con multiples sistemas.",
    "producto nuevo en stock.",
    "producto en oferta.",
    "producto con soporte técnico.",
    "producto con garantía de 1 año."
]

for producto in productos:
    print("Producto:", producto)
    print("Mensaje:", mensajes[productos.index(producto)])
    print("Total de productos:", len(productos))

# TAREA 1: Agrega dos productos a la lista.
# TAREA 2: Muestra un mensaje diferente para cada producto.
# TAREA 3: Al final muestra cuantos productos hay con len().
