import csv

operations = [
    [1, "2026-08-01", "2026-08-02", "Emision", "Cerrado", "Sucursal Norte", "WhatsApp", 12],
    [2, "2026-08-01", "2026-08-03", "Renovacion", "Cerrado", "Sucursal Centro", "Email", 20],
    [3, "2026-08-02", "", "Reclamo", "Pendiente", "Sucursal Sur", "Web", ""],
    [4, "2026-08-02", "2026-08-05", "Liquidacion", "Cerrado", "Sucursal Norte", "Presencial", 36],
    [5, "2026-08-03", "", "Mora", "Observado", "Sucursal Centro", "WhatsApp", 48],
    [6, "2026-08-03", "2026-08-03", "Emision", "Cerrado", "Sucursal Sur", "Web", 8],
    [7, "2026-08-04", "", "Renovacion", "Pendiente", "Sucursal Norte", "Email", ""],
    [8, "2026-08-04", "2026-08-06", "Reclamo", "Cerrado", "Sucursal Centro", "WhatsApp", 30],
]

headers = [
    "id_operacion",
    "fecha_ingreso",
    "fecha_cierre",
    "tipo_operacion",
    "estado",
    "sucursal",
    "canal",
    "tiempo_resolucion_horas",
]

with open("data/operaciones_backoffice.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(operations)

print("Dataset simulado creado en data/operaciones_backoffice.csv")