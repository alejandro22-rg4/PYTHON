from pathlib import Path
import xml.etree.ElementTree as ET

BASE = Path(__file__).resolve().parent.parent
archivo = BASE / "xml_entrada" / "documento_001.xml"
raiz = ET.parse(archivo).getroot()
print("Etiqueta raíz:", raiz.tag)
print("Nombre del archivo:", archivo.name)
print("atributos raíz:", raiz.attrib)

# TAREA: mostrar también los atributos de la raíz y el nombre del archivo.
