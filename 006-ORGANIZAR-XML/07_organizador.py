from pathlib import Path

BASE = Path(__file__).resolve().parent
ORIGEN = BASE / "archivos_practica"
SALIDA = BASE / "salida"
SALIDA.mkdir(exist_ok=True)

import shutil
extensiones = {
    ".txt": SALIDA / "TXT",
    ".csv": SALIDA / "CSV",
    ".xml": SALIDA / "XML"
}
for carpeta in extensiones.values():
    carpeta.mkdir(exist_ok=True)
for archivo in ORIGEN.iterdir():
    if archivo.is_file():
        ext = archivo.suffix.lower()
        if ext in extensiones:
            destino_dir = extensiones[ext]
            destino_archivo = destino_dir / archivo.name
        if not destino_archivo.exists():
                shutil.copy2(archivo, destino_archivo)
# TAREA: crear en salida las carpetas TXT, CSV y XML.
# Copiar los archivos de archivos_practica según su extensión.
# No mover ni eliminar originales; no sobrescribir copias.
