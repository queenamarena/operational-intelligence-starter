import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/operaciones_backoffice.csv")
SLA_TARGET_HOURS = 24

if not DATA_PATH.exists():
    raise FileNotFoundError(
        "No se encontró el archivo data/operaciones_backoffice.csv. "
        "Ejecutá primero: python src\\generar_datos.py"
    )

df = pd.read_csv(DATA_PATH)

df["tiempo_resolucion_horas"] = pd.to_numeric(
    df["tiempo_resolucion_horas"],
    errors="coerce"
)

total_operaciones = len(df)
operaciones_cerradas = df[df["estado"] == "Cerrado"]
operaciones_pendientes = df[df["estado"] == "Pendiente"]
operaciones_observadas = df[df["estado"] == "Observado"]

cerradas_dentro_sla = operaciones_cerradas[
    operaciones_cerradas["tiempo_resolucion_horas"] <= SLA_TARGET_HOURS
]

sla_compliance = (
    len(cerradas_dentro_sla) / len(operaciones_cerradas) * 100
    if len(operaciones_cerradas) > 0
    else 0
)

lead_time_promedio = operaciones_cerradas["tiempo_resolucion_horas"].mean()

print("Operational Intelligence Starter")
print("=" * 45)
print("Total de operaciones:", total_operaciones)
print("Operaciones cerradas:", len(operaciones_cerradas))
print("Backlog pendiente:", len(operaciones_pendientes))
print("Operaciones observadas:", len(operaciones_observadas))
print("SLA objetivo:", SLA_TARGET_HOURS, "horas")
print("Cumplimiento SLA:", round(sla_compliance, 2), "%")
print("Lead Time promedio:", round(lead_time_promedio, 2), "horas")

print("\nOperaciones por tipo:")
print(df["tipo_operacion"].value_counts())

print("\nOperaciones por canal:")
print(df["canal"].value_counts())

print("\nOperaciones por sucursal:")
print(df["sucursal"].value_counts())