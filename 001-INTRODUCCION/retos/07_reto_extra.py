# RETO EXTRA: calculadora de envio de TechStore.
numero = float(input("ingrese el subtotal de la compra:"))
ciudad = input("ingrese la ciudad(quito u otras):")
if numero >= 100:
     envio = 0
elif numero < 100 and ciudad.lower() =="quito":
     envio = 3
else:
    envio =6
total = numero + envio
print(f"Subtotal: ${numero:.2f}")
print(f"costo de envio: ${envio:.2f}")
print(f"total: ${total:.2f}")
# Pide el subtotal de compra y la ciudad (Quito u otra).
# Si subtotal >= 100: envio gratis.
# Si subtotal < 100 y ciudad es Quito: envio $3.
# Si subtotal < 100 y es otra ciudad: envio $6.
# Muestra subtotal, envio y total.
# EXTRA: admite "quito", "QUITO" y "Quito".
