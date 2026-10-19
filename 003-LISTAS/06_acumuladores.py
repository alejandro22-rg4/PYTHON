precios = [12.5, 8.0, 20.0, 4.5]
total = 0
for precio in precios:
    total += precio
print("Total:", total)
print("Precios mayores que 10:", len([p for p in precios if p > 10]))
print("Promedio:", total / len(precios))
print("Total de precios:", len(precios))

# TAREA 1: Contar precios mayores que 10.
# TAREA 2: Calcular el promedio usando total / len(precios).
# TAREA 3: Mostrar total y promedio con dos decimales.
