# LABORATORIO 2 - 02: IMC educativo (no es diagnostico)
peso = float(input("Peso en kg: "))
altura = float(input("Altura en metros: "))
if altura <= 0 or peso <= 0:
    print("Error: La altura y el peso deben ser valores positivos.")
else:
    imc = peso / (altura ** 2)
    print("IMC: ", round(imc, 2))
    if imc < 18.5:
        print("bajo")
    elif imc < 25:
        print("habitual")
    else:
        print("alto")   
    
# TAREA 1: Evitar dividir entre cero o valores negativos.
# TAREA 2: Calcular IMC = peso / (altura ** 2).
# TAREA 3: Mostrar IMC con dos decimales.
# TAREA 4: Mostrar 'bajo', 'habitual' o 'alto' con limites 18.5 y 25.
