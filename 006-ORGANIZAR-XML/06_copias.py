from pathlib import Path
import shutil
BASE = Path(__file__).resolve().parent
ORIGEN = BASE / "archivos_practica"
SALIDA = BASE / "salida"
SALIDA.mkdir(exist_ok=True)
RESPALDO = SALIDA / "respaldo"
RESPALDO.mkdir(exist_ok=True)

print("Iniciando proceso de copiado de archivos .txt...")
for ruta in ORIGEN.iterdir():
    if ruta.is_file() and ruta.suffix == ".txt":
     archivo_destino = RESPALDO / ruta.name
    if archivo_destino.exists():
            print(f"  [Omitido] {ruta.name} ya existe en el respaldo.")
    else:
     shutil.copy2(ruta, archivo_destino)
     print(f"  ✔ Copiado exitosamente: {ruta.name}")
print("\nProceso de respaldo finalizado.")   
# TAREA 1: crear carpeta salida/respaldo.
# TAREA 2: copiar los TXT con shutil.copy2().
# TAREA 3: si la copia existe, omitirla.
