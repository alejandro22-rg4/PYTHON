# LABORATORIO PUENTE - Detectar y corregir errores

archivos = ["uno.xml", "DOS.XML", "tres.txt"]

# Este programa debe contar los XML. Corrige los errores
# de sintaxis y logica sin eliminar elementos de la lista.
contador = 0
for archivo in archivos:
    if archivo.lower().endswith(".xml"):
        contador = contador + 1
print("XML encontrados:", contador)
