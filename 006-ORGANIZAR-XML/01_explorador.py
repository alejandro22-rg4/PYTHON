from pathlib import Path

BASE = Path(__file__).resolve().parent
print(BASE)
ORIGEN = BASE / "archivos_practica"
SALIDA = BASE / "salida"
SALIDA.mkdir(exist_ok=True)
contador_txt=0
for ruta in sorted(ORIGEN.iterdir()):
    if ruta.is_file()and ruta.suffix == ".txt":
        contador_txt += 1
        print(f"Nombre: {ruta.stem} | Extensión: {ruta.suffix}")
print(f"\nTotal de archivos .txt encontrados: {contador_txt}")

# TAREA 1: mostrar solo archivos .txt.
# TAREA 2: mostrar nombre y extensión (.suffix).
# TAREA 3: mostrar cuántos archivos se encontraron.
