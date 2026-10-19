# LABORATORIO 2 - 07: DESDE CERO
# TAREA 1: Solicitar peso del paquete en kg y distancia en km.
# TAREA 2: Validar peso > 0 y distancia > 0.
# TAREA 3: Tarifa base: $3 si peso <= 2; $6 si <= 5; $10 si > 5.
# TAREA 4: Agregar $2 si distancia > 50 km.
# TAREA 5: Mostrar costo final con dos decimales.
print("Envio de paquetes")
peso = float(input("Peso del paquete en kg: "))
distancia = float(input("Distancia en km: "))
if peso <= 0 or distancia <= 0:
    print("Error: El peso y la distancia deben ser valores positivos.")             
else:       
    if peso <= 2:
        tarifa = 3.00
    elif peso <= 5:
        tarifa = 6.00
    else:
        tarifa = 10.00
    if distancia > 50:
        tarifa += 2.00
    print("Costo final: $", round(tarifa, 2))
    
