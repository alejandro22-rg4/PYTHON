from pathlib import Path

BASE = Path(__file__).resolve().parent
ORIGEN = BASE / "archivos_practica"
SALIDA = BASE / "salida"
SALIDA.mkdir(exist_ok=True)
print("Leyendo 'soporte.txt' ===")
archivo = ORIGEN / "soporte.txt"
if archivo.is_file():
    print(archivo.read_text(encoding="utf-8"))
else:
    print("[AVISO] El archivo 'soporte.txt' no se encuentra en el directorio.\n")

print("=" * 40 + "\n")
print("Búsqueda interactiva")
nombre_usuario = input("Ingresa el nombre del archivo .txt que deseas leer: ").strip()
if not nombre_usuario.endswith(".txt"):
    nombre_usuario += ".txt"

archivo_objetivo = ORIGEN / nombre_usuario
if archivo_objetivo.is_file():
    print(f"\nContenido de '{nombre_usuario}':")
    print(archivo.read_text(encoding="utf-8"))
else:
    print(f"\n[AVISO] El archivo '{nombre_usuario}' no existe en la carpeta de origen.")
# TAREA 1: leer soporte.txt.
# TAREA 2: solicitar el nombre de un .txt y leerlo solo si está en ORIGEN.
# TAREA 3: mostrar un aviso si no existe.
