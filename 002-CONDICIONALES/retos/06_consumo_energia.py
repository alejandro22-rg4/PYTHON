# LABORATORIO 2 - 06: DESDE CERO
# TAREA 1: Pedir nombre del dispositivo.
# TAREA 2: Pedir potencia en watts y horas de uso por dia.
# TAREA 3: Calcular kWh diarios: (watts * horas) / 1000.
# TAREA 4: Calcular kWh en 30 dias.
# TAREA 5: Pedir costo por kWh y calcular costo mensual.
# TAREA 6: Validar que los numeros sean no negativos y horas <= 24.
# TAREA 7: Mostrar resultados con dos decimales.
print("Consumo de energia electrica")
nombre = input("Nombre del dispositivo: ")
potencia = float(input("Potencia en watts: "))
horas = float(input("Horas de uso por dia: "))
if potencia < 0 or horas < 0 or horas > 24:
    print("Error: La potencia y las horas deben ser valores positivos, y las horas no pueden exceder 24.")
else:
    kwh_diarios = (potencia * horas) / 1000
    kwh_mensuales = kwh_diarios * 30
    costo_kwh = float(input("Costo por kWh: "))
    costo_mensual = kwh_mensuales * costo_kwh
    print("Consumo diario: ", round(kwh_diarios, 2), "kWh")
    print("Consumo mensual: ", round(kwh_mensuales, 2), "kWh")
    print("Costo mensual: $", round(costo_mensual, 2))
    if potencia <0 or horas <0 or horas >24:
        print("Error: La potencia y las horas deben ser valores positivos, y las horas no pueden exceder 24.")  