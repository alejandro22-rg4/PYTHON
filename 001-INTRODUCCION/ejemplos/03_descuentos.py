# Condiciones: ejecuta con 30, 80, 150 y 250.
subtotal = float(input("Subtotal de compra: "))

if subtotal < 50:
    descuento=subtotal*0
if subtotal >=50 and subtotal <100:
    descuento = subtotal * 0.05
if subtotal >= 100 and subtotal <200:
    descuento = subtotal * 0.10
if subtotal >=200:
    descuento = subtotal * 0.15    
total = subtotal - descuento
print(f"Subtotal: ${subtotal:.2f}")
print(f"descuento: ${descuento:.2f}")
print(f"total: ${total:.2f}") 
if subtotal <0:
 print("error:el subtotal no puede ser negativo.")
# TAREA: aplica 0 % si es menor que 50;
# 5 % entre 50 y 99.99; 10 % entre 100 y 199.99;
# 15 % desde 200. Muestra el total final.
