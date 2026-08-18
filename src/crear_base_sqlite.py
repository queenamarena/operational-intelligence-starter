import sqlite3
from pathlib import Path

import pandas as pd

CSV_PATH = Path("data/operaciones_backoffice.csv")
DB_PATH = Path("data/operaciones.db")
TABLE_NAME = "operaciones_backoffice"

if not CSV_PATH.exists():
    raise FileNotFoundError(
        "No se encontró data/operaciones_backoffice.csv. "
        "Ejecutá primero: python src\\generar_datos.py"
    )

df = pd.read_csv(CSV_PATH)

connection = sqlite3.connect(DB_PATH)

df.to_sql(
    TABLE_NAME,
    connection,
    if_exists="replace",
    index=False
)

connection.close()

print("Base SQLite creada correctamente.")
print(f"Archivo generado: {DB_PATH}")
print(f"Tabla creada: {TABLE_NAME}")
print(f"Registros cargados: {len(df)}")