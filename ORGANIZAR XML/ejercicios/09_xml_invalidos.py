from pathlib import Path
import xml.etree.ElementTree as ET

BASE = Path(__file__).resolve().parent.parent
carpeta = BASE / "xml_entrada"
for archivo in sorted(carpeta.glob("*.xml")):
    try:
        raiz = ET.parse(archivo).getroot()
        print(archivo.name, "OK", raiz.tag)
    except ET.ParseError:
        print(archivo.name, "XML mal formado")
codigo = raiz.findtext("infoTributaria/codDoc")
codigos_conocidos = ["01", "04", "05", "06", "07"]
        
if codigo in codigos_conocidos:
    print(archivo.name, "-> Válido y conocido (codDoc:", codigo, ")")
else:
 print(archivo.name, "-> Válido pero DESCONOCIDO (codDoc:", codigo, ")")
# TAREA: distinguir XML válido pero desconocido (codDoc no reconocido)
# de XML mal formado. No borrar ni alterar documentos.
