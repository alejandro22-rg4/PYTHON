from pathlib import Path
import xml.etree.ElementTree as ET

BASE = Path(__file__).resolve().parent.parent
raiz = ET.parse(BASE / "xml_entrada" / "documento_001.xml").getroot()
contador = 0
for elemento in raiz.iter():
    if elemento.text and elemento.text.strip():
        print(elemento.tag, "=", elemento.text.strip())
        contador += 1
print("\nTotal de etiquetas con contenido:", contador)
# TAREA: mostrar solo etiquetas con contenido y contar cuántas hay.
