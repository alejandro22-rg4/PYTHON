from pathlib import Path
import xml.etree.ElementTree as ET

BASE = Path(__file__).resolve().parent.parent
raiz = ET.parse(BASE / "xml_entrada" / "documento_001.xml").getroot()
codigo = raiz.findtext("infoTributaria/codDoc")
if codigo == "01":
    print("Factura")
elif codigo == "04":
    print("Nota de Crédito")
elif codigo == "05":
    print("Nota de Débito")
elif codigo == "06":
    print("Guía de Remisión")
elif codigo == "07":
    print("Comprobante de Retención")
else:
    print("Documento desconocido")
# TAREA: agregar los códigos 04, 05, 06 y 07; manejar desconocidos.
