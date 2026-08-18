# Analítica Operativa para Gestión de Back Office

Proyecto de analítica operativa desarrollado con Python, SQL, SQLite y visualizaciones para analizar indicadores clave de gestión, cumplimiento de SLA, backlog, tiempos de resolución y oportunidades de mejora en procesos de back office.

## Problema de negocio

Muchas organizaciones operan con baja visibilidad sobre su carga de trabajo, tareas pendientes, tiempos de respuesta y cuellos de botella del proceso.

Este proyecto simula un entorno operativo de back office y analiza indicadores clave para apoyar la toma de decisiones, la mejora continua y el control de calidad del servicio.

El objetivo es transformar datos operativos en información útil para la gestión, permitiendo identificar demoras, priorizar acciones y mejorar el desempeño del proceso.

## Objetivos

- Analizar la carga operativa.
- Medir backlog y tareas pendientes.
- Calcular cumplimiento de SLA.
- Identificar cuellos de botella.
- Generar visualizaciones básicas.
- Ejecutar consultas SQL desde Python.
- Construir un proyecto profesional de portfolio en analítica operativa.

## Herramientas

- Python
- Pandas
- Matplotlib
- SQL
- SQLite
- Git
- GitHub
- VS Code

## KPIs analizados

- **Throughput:** cantidad de operaciones procesadas.
- **Lead Time:** tiempo total desde el ingreso de una operación hasta su cierre.
- **Backlog:** trabajo acumulado pendiente de resolución.
- **SLA Compliance:** porcentaje de operaciones resueltas dentro del tiempo esperado.
- **Casos observados:** operaciones que requieren revisión, reproceso o análisis adicional.
- **Cuellos de botella:** tipos de operación, canales o sucursales que generan demoras.

## Project Structure

```text
operational-intelligence-starter/
│
├── data/
│   └── operaciones_backoffice.csv
│
├── images/
│   ├── operaciones_por_estado.png
│   ├── operaciones_por_canal.png
│   └── lead_time_por_tipo.png
│
├── src/
│   ├── generar_datos.py
│   ├── analizar_operaciones.py
│   ├── visualizar_operaciones.py
│   └── primer_analisis.py
│
├── sql/
│   └── consultas_operativas.sql
│
├── README.md
├── requirements.txt
└── .gitignore
```
> Nota: la carpeta `data/` está ignorada por Git para evitar subir datos sensibles o información operativa real. El dataset utilizado en este proyecto es simulado.

## Cómo ejecutar el proyecto
## Ejecución rápida

Para ejecutar todo el flujo completo del proyecto:

```bash
python src/run_pipeline.py
```

Este comando genera el dataset simulado, crea la base SQLite, ejecuta el análisis operativo, corre las consultas SQL y genera las visualizaciones.
## Flujo del proyecto
```markdown
## Capa SQL

El proyecto incluye consultas SQL para analizar la información operativa desde una base SQLite local.

Las consultas permiten obtener:

- Total de operaciones.
- Operaciones por estado.
- Backlog pendiente.
- Operaciones cerradas.
- Cumplimiento de SLA.
- Lead Time promedio.
- Operaciones por tipo.
- Operaciones por canal.
- Operaciones por sucursal.
- Casos fuera de SLA.

Esto demuestra la capacidad de analizar datos tanto con Python como con SQL, dos herramientas clave para roles de Data Analyst, Business Intelligence y mejora de procesos.

El proyecto sigue una secuencia simple de análisis operativo:

1. Se genera un dataset simulado de operaciones de back office.
2. Se crea una base SQLite local a partir del dataset.
3. Se ejecutan consultas SQL para obtener KPIs operativos.
4. Se realiza análisis con Pandas.
5. Se generan visualizaciones para interpretar los resultados.

```text
generar datos simulados
↓
crear base SQLite
↓
ejecutar consultas SQL
↓
analizar KPIs con Pandas
↓
generar visualizaciones
Instalar dependencias:

```bash
pip install -r requirements.txt
```

Generar el dataset simulado:

```bash
python src/generar_datos.py
````markdown
Crear la base SQLite:

```bash
python src/crear_base_sqlite.py