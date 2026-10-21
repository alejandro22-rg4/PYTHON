from datetime import date

hoy = date.today()
print("Fecha de hoy:", hoy)
print("Día:", hoy.day)
print("Mes:", hoy.month)
print("Año:", hoy.year)
fecha_usuario = input("Ingresa una fecha (YYYY-MM-DD): ")
año, mes, dia = map(int, fecha_usuario.split('-'))
fecha_usuario = date(año, mes, dia)
diferencia = fecha_usuario - hoy
print("Diferencia en días:", diferencia.days)   

# TAREA 1: Muestra por separado el día, mes y año de hoy.
# TAREA 2: Solicita un año, mes y día para una fecha futura o pasada.
# TAREA 3: Crea la fecha con date(anio, mes, dia).
# TAREA 4: Muestra cuántos días hay entre la fecha indicada y hoy.
# PISTA: diferencia = fecha - hoy; diferencia.days
