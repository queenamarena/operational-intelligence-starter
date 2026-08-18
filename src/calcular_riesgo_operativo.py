from pathlib import Path

import pandas as pd

DATA_PATH = Path("data/operaciones_backoffice.csv")
OUTPUT_PATH = Path("data/operaciones_con_riesgo.csv")

SLA_TARGET_HOURS = 24

if not DATA_PATH.exists():
    raise FileNotFoundError(
        "No se encontró data/operaciones_backoffice.csv. "
        "Ejecutá primero: python src\\generar_datos.py"
    )

df = pd.read_csv(DATA_PATH)

df["tiempo_resolucion_horas"] = pd.to_numeric(
    df["tiempo_resolucion_horas"],
    errors="coerce"
)


def calcular_score_riesgo(row):
    score = 0
    motivos = []

    estado = row["estado"]
    tipo_operacion = row["tipo_operacion"]
    canal = row["canal"]
    tiempo = row["tiempo_resolucion_horas"]

    if estado == "Pendiente":
        score += 25
        motivos.append("operación pendiente")

    if estado == "Observado":
        score += 30
        motivos.append("operación observada o con posible reproceso")

    if pd.notna(tiempo) and tiempo > SLA_TARGET_HOURS:
        score += 30
        motivos.append("fuera de SLA")

    if pd.notna(tiempo) and tiempo > 48:
        score += 20
        motivos.append("tiempo de resolución crítico")

    if tipo_operacion in ["Reclamo", "Liquidacion"]:
        score += 15
        motivos.append("tipo de operación sensible")

    if canal in ["WhatsApp", "Presencial"]:
        score += 10
        motivos.append("canal con mayor fricción operativa")

    return score, ", ".join(motivos) if motivos else "sin alertas relevantes"


def clasificar_riesgo(score):
    if score >= 75:
        return "Crítico"
    if score >= 50:
        return "Alto"
    if score >= 25:
        return "Medio"
    return "Bajo"


def recomendar_accion(nivel_riesgo):
    recomendaciones = {
        "Crítico": "Intervención inmediata, revisión del flujo y asignación prioritaria.",
        "Alto": "Seguimiento operativo diario y análisis de causa raíz.",
        "Medio": "Monitoreo preventivo y control de evolución.",
        "Bajo": "Mantener seguimiento estándar.",
    }

    return recomendaciones[nivel_riesgo]


resultados = df.apply(calcular_score_riesgo, axis=1)

df["score_riesgo"] = resultados.apply(lambda resultado: resultado[0])
df["motivo_riesgo"] = resultados.apply(lambda resultado: resultado[1])
df["nivel_riesgo"] = df["score_riesgo"].apply(clasificar_riesgo)
df["accion_recomendada"] = df["nivel_riesgo"].apply(recomendar_accion)

df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")

print("Scoring de riesgo operativo")
print("=" * 60)
print(f"Operaciones evaluadas: {len(df)}")
print(f"Archivo generado: {OUTPUT_PATH}")

print("\nDistribución por nivel de riesgo:")
print(df["nivel_riesgo"].value_counts().to_string())

print("\nTop operaciones de mayor riesgo:")

columnas_reporte = [
    "id_operacion",
    "tipo_operacion",
    "estado",
    "canal",
    "tiempo_resolucion_horas",
    "score_riesgo",
    "nivel_riesgo",
    "motivo_riesgo",
]

print(
    df[columnas_reporte]
    .sort_values(by="score_riesgo", ascending=False)
    .head(10)
    .to_string(index=False)
)

print("\nConfirmación:")
print("Proceso de scoring de riesgo operativo finalizado correctamente.")