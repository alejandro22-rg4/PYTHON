from pathlib import Path

BASE = Path(__file__).resolve().parent
ORIGEN = BASE / "archivos_practica"
SALIDA = BASE / "salida"
SALIDA.mkdir(exist_ok=True)
contador_xml = 0

print("=== LECTURA DE ARCHIVOS XML ===\n")
for ruta in sorted(ORIGEN.iterdir()):
    if ruta.is_file() and ruta.suffix == ".xml":
        contador_xml += 1
        print(f"--- Archivo: {ruta.name} ---")
        contenido = ruta.read_text(encoding="utf-8")
        print(contenido)
        print("-" * 40)
print(f"\nTotal de archivos XML leídos: {contador_xml}")
# TAREA 1: mostrar el contenido de todos los .xml.
# TAREA 2: indicar el nombre antes de cada contenido.
# TAREA 3: contar cuántos XML se leyeron.
