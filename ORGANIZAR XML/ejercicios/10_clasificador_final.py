"""RETO FINAL: construir un clasificador seguro de comprobantes XML.

TAREAS:
1. Recorrer todos los .xml de xml_entrada.
2. Leer cada XML con ElementTree y obtener infoTributaria/codDoc.
3. Identificar códigos 01, 04, 05, 06 y 07.
4. Crear subcarpetas dentro de xml_clasificados según el tipo.
5. Copiar sin sobrescribir archivos existentes; no mover ni borrar.
6. Guardar XML mal formados en invalidos y desconocidos en desconocidos.
7. Mostrar un resumen final de copias, omitidos e inválidos.
8. EXTRA: investigar el XML envuelto en <autorizacion> (documento_023.xml).

Solo usar rutas relativas a este proyecto mediante Path(__file__).
"""
# Escribe tu programa aquí.
from pathlib import Path
import xml.etree.ElementTree as ET
import shutil
BASE = Path(__file__).resolve().parent.parent
entrada = BASE / "xml_entrada"
salida = BASE / "xml_clasificados"
nombres_carpetas = {
    "01": "facturas",
    "04": "notas_credito",
    "05": "notas_debito",
    "06": "guias_remision",
    "07": "retenciones",
    "desconocidos": "desconocidos",
    "invalidos": "invalidos"
}

for carpeta in nombres_carpetas.values():
    (salida / carpeta).mkdir(parents=True, exist_ok=True)
copias_exitosas = 0
omitidos = 0
total_invalidos = 0
for archivo in sorted(entrada.glob("*.xml")):
    destino_carpeta = None
    try:
        arbol = ET.parse(archivo)
        raiz = arbol.getroot()
        codigo = raiz.findtext("infoTributaria/codDoc")
        comprobante_tag = raiz.find(".//comprobante")
        if comprobante_tag is not None and comprobante_tag.text:
                try:
                    sub_raiz = ET.fromstring(comprobante_tag.text.strip())
                    codigo = sub_raiz.findtext("infoTributaria/codDoc")
                except ET.ParseError:
                    pass
        if codigo in ["01", "04", "05", "06", "07"]:
            destino_carpeta = salida / nombres_carpetas[codigo]
        else:
            destino_carpeta = salida / "desconocidos"    
    except ET.ParseError:
       
        destino_carpeta = salida / "invalidos"
        total_invalidos += 1
    if destino_carpeta:
        archivo_destino = destino_carpeta / archivo.name
        if not archivo_destino.exists():
            shutil.copy2(archivo, archivo_destino)
            copias_exitosas += 1
        else:
            omitidos += 1
print("\n" + "="*30)
print("     RESUMEN FINAL DE CLASIFICACIÓN     ")
print("="*30)
print(f"Total de archivos procesados/copiados: {copias_exitosas}")
print(f"Omitidos (ya existían en destino): {omitidos}")
print(f"XML inválidos detectados: {total_invalidos}")
print("="*30) 