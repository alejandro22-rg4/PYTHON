from pathlib import Path
import shutil

BASE = Path(__file__).resolve().parent.parent
origen = BASE / "xml_entrada" / "documento_001.xml"
destino = BASE / "xml_clasificados" / "copias_prueba"
destino.mkdir(parents=True, exist_ok=True)
archivo_destino = destino / origen.name
if not archivo_destino.exists():
    shutil.copy2(origen, archivo_destino)
    print("¡Archivo copiado con éxito:", archivo_destino.name, "!")
else:
    print("El archivo ya existe en el destino. No se sobrescribió.")
# TAREA: copiar documento_001.xml sin sobrescribir archivos existentes.
# Utiliza shutil.copy2 y verifica si el destino ya existe.
