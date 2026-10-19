
numero1 = float(input("ingrese el primer numero:"))
numero2 = float(input("ingrese el segundo numero:"))
operacion = input("ingrese la operacion(+,-,*,/):")
banderaSivisonCero = False
if operacion =="+":
    resultado = numero1 + numero2
elif operacion =="-":
    resultado = numero1 - numero2
elif operacion =="*":
    resultado = numero1 * numero2
elif operacion =="/":
    if numero2 ==0:
        banderaSivisonCero = True
    else:
        resultado = numero1 / numero2
if(banderaSivisonCero):
    print(f"error:no se pudo divifir entre cero.")
else:
    print(f"el resultado de{numero1} {operacion}{numero2} es:{resultado}")
# Debe pedir dos numeros y una operacion (+, -, *, /).
# Muestra el resultado.
# Si se intenta dividir entre cero, muestra un aviso en lugar de fallar.
# EXTRA: muestra un mensaje si la operacion no existe.
