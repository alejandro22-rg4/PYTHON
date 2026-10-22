from pathlib import Path
import xml.etree.ElementTree as ET

BASE = Path(__file__).resolve().parent.parent
raiz = ET.parse(BASE / "xml_entrada" / "documento_001.xml").getroot()
print("Código:", raiz.findtext("infoTributaria/codDoc"))
print("Razón Social:", raiz.findtext(".//razonSocial"))
print("Fecha de Emisión:", raiz.findtext(".//fechaEmision"))
print("Valor Total:", raiz.findtext(".//importeTotal"))
# TAREA: mostrar razón social, fecha de emisión y valor total.
