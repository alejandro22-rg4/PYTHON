# RETO: crea tu programa desde cero.
nombre=input("nombre:")
nota1=float(input("nota 1:"))
nota2=float(input("nota 2:"))
nota3=float(input("nota 3:"))
if(0<=nota1<=10 and 0<= nota2<=10 and 0<=nota3 <=10):
  promedio = (nota1 + nota2 + nota3)/3
  if promedio>=7:
     resultado= "aprobado"
  else:
    resultado= "reprobado"
  print(f"{nombre},tu promedio es: {promedio:.2f}.resultado:{resultado}")
else:
 print("alguna nota no es del 0 al 10.")
# 1. Solicita nombre y tres notas de 0 a 10.
# 2. Calcula el promedio.
# 3. Muestra "Aprobado" si el promedio es >= 7, si no "Reprobado".
# 4. Muestra nombre y promedio con dos decimales.
# EXTRA: avisa si alguna nota esta fuera del rango 0 a 10.