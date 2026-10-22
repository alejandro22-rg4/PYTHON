from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
carpeta = BASE / "xml_entrada"
for archivo in sorted(carpeta.glob("*.xml")):
    print(archivo.name)
contador = 0
for archivo in sorted(carpeta.glob("*.xml")):
    tamano = archivo.stat().st_size
    print(f"{archivo.name} -> {tamano} bytes")
    contador += 1

print(f"\nTotal de archivos XML encontrados: {contador}")
# TAREA: contar XML y mostrar tamaño en bytes.
