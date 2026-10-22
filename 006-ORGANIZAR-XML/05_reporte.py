from pathlib import Path

BASE = Path(__file__).resolve().parent
ORIGEN = BASE / "archivos_practica"
SALIDA = BASE / "salida"
SALIDA.mkdir(exist_ok=True)

archivos = [p for p in ORIGEN.iterdir() if p.is_file()]
print("Documentos encontrados:", len(archivos))
archivo_reporte = SALIDA / "reporte_archivos.txt"
contador = 1
while archivo_reporte.exists():
    archivo_reporte = SALIDA / f"reporte_archivos_{contador}.txt"
    contador += 1
contenido = f"Total de archivos encontrados: {archivos}\n"
contenido += "========================================\n"
contenido += "Lista de archivos:\n"

for p in sorted(archivos):
    contenido += f"- {p.name}\n"
archivo_reporte.write_text(contenido, encoding="utf-8")
print(f"Reporte generado exitosamente en: {archivo_reporte.name}")  
# TAREA 1: crear reporte_archivos.txt en salida.
# TAREA 2: escribir total y lista de nombres.
# TAREA 3: evitar sobrescribir un reporte existente.
