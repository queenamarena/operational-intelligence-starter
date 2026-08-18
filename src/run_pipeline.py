import subprocess
import sys
from pathlib import Path

scripts = [
    "src/generar_datos.py",
    "src/crear_base_sqlite.py",
    "src/analizar_operaciones.py",
    "src/ejecutar_consultas_sql.py",
    "src/visualizar_operaciones.py",
]

print("Iniciando pipeline de analítica operativa")
print("=" * 60)

for script in scripts:
    script_path = Path(script)

    if not script_path.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {script}")

    print(f"\nEjecutando: {script}")
    print("-" * 60)

    subprocess.run([sys.executable, str(script_path)], check=True)

print("\nPipeline ejecutado correctamente.")
print("Datos, base SQLite, análisis, consultas SQL y visualizaciones generadas.")