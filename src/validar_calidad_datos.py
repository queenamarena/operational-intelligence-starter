from pathlib import Path

import pandas as pd

DATA_PATH = Path("data/operaciones_backoffice.csv")

if not DATA_PATH.exists():
    raise FileNotFoundError(
        "No se encontró data/operaciones_backoffice.csv. "
        "Ejecutá primero: python src\\generar_datos.py"
    )

df = pd.read_csv(DATA_PATH)

print("Validación de calidad de datos")
print("=" * 60)

total_registros = len(df)
duplicados = df.duplicated().sum()
valores_nulos = df.isnull().sum()
columnas = df.columns.tolist()

columnas_esperadas = [
    "id_operacion",
    "fecha_ingreso",
    "fecha_cierre",
    "tipo_operacion",
    "estado",
    "sucursal",
    "canal",
    "tiempo_resolucion_horas",
]

columnas_faltantes = [
    columna for columna in columnas_esperadas
    if columna not in columnas
]

df["tiempo_resolucion_horas"] = pd.to_numeric(
    df["tiempo_resolucion_horas"],
    errors="coerce"
)

tiempos_negativos = df[
    df["tiempo_resolucion_horas"] < 0
]

estados_validos = ["Cerrado", "Pendiente", "Observado"]
estados_invalidos = df[
    ~df["estado"].isin(estados_validos)
]

ids_duplicados = df[
    df.duplicated(subset=["id_operacion"], keep=False)
]

print(f"Total de registros: {total_registros}")
print(f"Registros duplicados completos: {duplicados}")
print(f"Columnas faltantes: {columnas_faltantes if columnas_faltantes else 'Ninguna'}")
print(f"IDs duplicados: {len(ids_duplicados)}")
print(f"Tiempos negativos: {len(tiempos_negativos)}")
print(f"Estados inválidos: {len(estados_invalidos)}")

print("\nValores nulos por columna:")
print(valores_nulos.to_string())

errores_criticos = (
    duplicados
    + len(columnas_faltantes)
    + len(ids_duplicados)
    + len(tiempos_negativos)
    + len(estados_invalidos)
)

print("\nResultado de validación")
print("-" * 60)

if errores_criticos == 0:
    print("VALIDACIÓN APROBADA: el dataset cumple las reglas básicas de calidad.")
else:
    print("VALIDACIÓN CON OBSERVACIONES: revisar inconsistencias antes de usar el dataset.")

print("\nConfirmación:")
print("Proceso de validación finalizado correctamente.")