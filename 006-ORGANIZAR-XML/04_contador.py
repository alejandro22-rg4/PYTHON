from pathlib import Path

BASE = Path(__file__).resolve().parent
ORIGEN = BASE / "archivos_practica"
SALIDA = BASE / "salida"
SALIDA.mkdir(exist_ok=True)
contador_txt = 0
contador_csv = 0
contador_xml = 0
for ruta in ORIGEN.iterdir():
    if ruta.is_file():
     if ruta.suffix == ".txt":
            contador_txt += 1
    elif ruta.suffix == ".csv":
            contador_csv += 1
    elif ruta.suffix == ".xml":
            contador_xml += 1
print("=== RESUMEN DE ARCHIVOS ENCONTRADOS ===")
print(f"Archivos .txt: {contador_txt}")
print(f"Archivos .csv: {contador_csv}")
print(f"Archivos .xml: {contador_xml}")
print(f"----------------------------------------")
print(f"Total general: {contador_txt + contador_csv + contador_xml}")


# TAREA 1: contar .txt, .csv y .xml por separado.
# TAREA 2: mostrar los totales al final.
