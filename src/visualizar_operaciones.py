import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_PATH = Path("data/operaciones_backoffice.csv")
IMAGES_PATH = Path("images")

SLA_TARGET_HOURS = 24

if not DATA_PATH.exists():
    raise FileNotFoundError(
        "No se encontró data/operaciones_backoffice.csv. "
        "Ejecutá primero: python src\\generar_datos.py"
    )

IMAGES_PATH.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

df["tiempo_resolucion_horas"] = pd.to_numeric(
    df["tiempo_resolucion_horas"],
    errors="coerce"
)

# Gráfico 1: operaciones por estado
estado_counts = df["estado"].value_counts()

plt.figure()
estado_counts.plot(kind="bar")
plt.title("Operaciones por estado")
plt.xlabel("Estado")
plt.ylabel("Cantidad")
plt.tight_layout()
plt.savefig(IMAGES_PATH / "operaciones_por_estado.png")
plt.close()

# Gráfico 2: operaciones por canal
canal_counts = df["canal"].value_counts()

plt.figure()
canal_counts.plot(kind="bar")
plt.title("Operaciones por canal")
plt.xlabel("Canal")
plt.ylabel("Cantidad")
plt.tight_layout()
plt.savefig(IMAGES_PATH / "operaciones_por_canal.png")
plt.close()

# Gráfico 3: lead time por tipo de operación
closed_df = df[df["estado"] == "Cerrado"]

lead_time_by_type = closed_df.groupby("tipo_operacion")[
    "tiempo_resolucion_horas"
].mean().sort_values(ascending=False)

plt.figure()
lead_time_by_type.plot(kind="bar")
plt.title("Lead Time promedio por tipo de operación")
plt.xlabel("Tipo de operación")
plt.ylabel("Horas promedio")
plt.tight_layout()
plt.savefig(IMAGES_PATH / "lead_time_por_tipo.png")
plt.close()

print("Visualizaciones generadas en la carpeta images:")
print("- operaciones_por_estado.png")
print("- operaciones_por_canal.png")
print("- lead_time_por_tipo.png")