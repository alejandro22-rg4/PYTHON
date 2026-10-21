import statistics

precios = [12.50, 20.00, 7.75, 35.00, 18.25]
precios.append(22.50)  
precios.append(15.00)  
print("Promedio:", statistics.mean(precios))
print("Mediana:", statistics.median(precios))
print("Precio mayor:", max(precios))
print("Precio menor:", min(precios))
count_superior = 0
for precio in precios:
    if precio > statistics.mean(precios):
        count_superior += 1
print("Precios que superan el promedio:", count_superior)

# TAREA 1: Muestra la mediana con statistics.median().
# TAREA 2: Muestra el precio mayor y menor con max() y min().
# TAREA 3: Cuenta cuántos precios superan el promedio usando for e if.
# TAREA 4: Agrega dos precios nuevos y repite los cálculos.
