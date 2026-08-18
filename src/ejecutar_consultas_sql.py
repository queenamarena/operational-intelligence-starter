import sqlite3
from pathlib import Path

import pandas as pd

DB_PATH = Path("data/operaciones.db")
SQL_PATH = Path("sql/consultas_operativas.sql")

if not DB_PATH.exists():
    raise FileNotFoundError(
        "No se encontró data/operaciones.db. "
        "Ejecutá primero: python src\\crear_base_sqlite.py"
    )

if not SQL_PATH.exists():
    raise FileNotFoundError(
        "No se encontró sql/consultas_operativas.sql."
    )


def obtener_titulo_y_query(bloque_sql):
    lineas = bloque_sql.strip().splitlines()

    titulo = "Consulta SQL"
    query_lineas = []

    for linea in lineas:
        linea_limpia = linea.strip()

        if linea_limpia.startswith("--"):
            titulo = linea_limpia.replace("--", "").strip()
        elif linea_limpia:
            query_lineas.append(linea)

    query = "\n".join(query_lineas).strip()
    return titulo, query


with open(SQL_PATH, "r", encoding="utf-8") as archivo:
    contenido_sql = archivo.read()

bloques_sql = [
    bloque.strip()
    for bloque in contenido_sql.split(";")
    if bloque.strip()
]

conexion = sqlite3.connect(DB_PATH)

print("Resultados de consultas SQL")
print("=" * 50)

for bloque in bloques_sql:
    titulo, query = obtener_titulo_y_query(bloque)

    if query.lower().startswith("select"):
        print(f"\n{titulo}")
        print("-" * 50)

        resultado = pd.read_sql_query(query, conexion)
        print(resultado.to_string(index=False))

conexion.close()