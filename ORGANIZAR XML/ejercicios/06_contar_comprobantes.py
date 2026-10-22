from pathlib import Path
import xml.etree.ElementTree as ET

BASE = Path(__file__).resolve().parent.parent
carpeta = BASE / "xml_entrada"
conteo = {}
for archivo in sorted(carpeta.glob("*.xml")):
    try:
        raiz = ET.parse(archivo).getroot()
        codigo = raiz.findtext("infoTributaria/codDoc") or "SIN_CODIGO"
        conteo[codigo] = conteo.get(codigo, 0) + 1
    except ET.ParseError:
        print("XML inválido:", archivo.name)
print(conteo)
xml_invalidos = 0
nombres_documentos = {
    "01": "Factura",
    "04": "Nota de Crédito",
    "05": "Nota de Débito",
    "06": "Guía de Remisión",
    "07": "Comprobante de Retención",
    "SIN_CODIGO": "Sin código"
}

for archivo in sorted(carpeta.glob("*.xml")):
    try:
        raiz = ET.parse(archivo).getroot()
        codigo = raiz.findtext("infoTributaria/codDoc") or "SIN_CODIGO"
        conteo[codigo] = conteo.get(codigo, 0) + 1
    except ET.ParseError:
        print("XML inválido:", archivo.name)
        xml_invalidos += 1

print("\n--- Resumen de Comprobantes ---")
for codigo, cantidad in conteo.items():
    nombre = nombres_documentos.get(codigo, "Documento desconocido")
    print(f"- {nombre} (Código {codigo}): {cantidad}")

print(f"\nTotal de XML inválidos encontrados: {xml_invalidos}")
# TAREA: mostrar los códigos con su nombre y contar los XML inválidos.
