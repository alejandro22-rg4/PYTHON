from pathlib import Path

BASE = Path(__file__).resolve().parent
ORIGEN = BASE / "archivos_practica"
SALIDA = BASE / "salida"
SALIDA.mkdir(exist_ok=True)
print("=== Búsqueda en 'soporte.txt' ===")
palabra_usuario = input("Ingresa la palabra que deseas buscar: ").strip()
archivo_soporte = ORIGEN / "soporte.txt"
if archivo_soporte.is_file():
    texto = archivo_soporte.read_text(encoding="utf-8")
    if palabra_usuario.lower() in texto.lower():
        print(f"¡Éxito! La palabra '{palabra_usuario}' SÍ se encuentra en soporte.txt")
    else:
        print(f"La palabra '{palabra_usuario}' NO se encuentra en soporte.txt")
print("\n" + "=" * 40 + "\n")
print("=== Búsqueda global en todos los archivos .txt ===")
palabra_global = input("Ingresa la palabra a buscar en todos los archivos: ").strip()

print(f"\nArchivos que contienen '{palabra_global}':")
contador_coincidencias = 0

for ruta in sorted(ORIGEN.iterdir()):
    if ruta.is_file() and ruta.suffix == ".txt":
        contenido_archivo = ruta.read_text(encoding="utf-8")
    if palabra_global.lower() in contenido_archivo.lower():
            print(f"  ✔ {ruta.name}")
            contador_coincidencias += 1
    if contador_coincidencias == 0:
      print("  (Ningún archivo .txt contiene esta palabra)")
# TAREA 1: buscar una palabra introducida por teclado.
# TAREA 2: buscar sin importar mayúsculas.
# TAREA 3: revisar todos los TXT e imprimir cuáles la contienen.
