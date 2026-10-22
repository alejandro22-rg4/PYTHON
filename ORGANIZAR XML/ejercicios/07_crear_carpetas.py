from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
salida = BASE / "xml_clasificados"
salida.mkdir(exist_ok=True)
subcarpetas = [
    "facturas",
    "notas_credito",
    "notas_debito",
    "guias_remision",
    "retenciones",
    "desconocidos",
    "invalidos"
]
for sub in subcarpetas:
    (salida / sub).mkdir(exist_ok=True)

print("¡Subcarpetas creadas exitosamente!")
# TAREA: crear subcarpetas facturas, notas_credito, notas_debito,
# guias_remision, retenciones, desconocidos e invalidos.
