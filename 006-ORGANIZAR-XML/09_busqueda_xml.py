from pathlib import Path

BASE = Path(__file__).resolve().parent
ORIGEN = BASE / "archivos_practica"
SALIDA = BASE / "salida"
SALIDA.mkdir(exist_ok=True)
print("=== BÚSQUEDA DE TEXTO EN ARCHIVOS XML ===")
palabra_usuario = input("Ingresa la palabra que deseas buscar (ej. factura, pedido, inventario): ").strip()

print(f"\nResultados para '{palabra_usuario}':")
contador_encontrados = 0
for ruta in sorted(ORIGEN.iterdir()):
    if ruta.is_file() and ruta.suffix == ".xml":
        contenido_texto = ruta.read_text(encoding="utf-8")
        if palabra_usuario.lower() in contenido_texto.lower():
            print(f"  ✔ {ruta.name}")
            contador_encontrados += 1
if contador_encontrados == 0:
    print("  (Ningún archivo XML contiene la palabra ingresada)")
# TAREA 1: pedir una palabra (factura, pedido, inventario).
# TAREA 2: leer los archivos XML como texto.
# TAREA 3: mostrar los nombres de archivos que contienen esa palabra.
# TAREA 4: buscar sin distinguir mayúsculas/minúsculas.
# Importante: buscar texto no es lo mismo que interpretar etiquetas XML.
