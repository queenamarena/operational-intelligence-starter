# Operational Intelligence Starter

Python, SQL and Business Intelligence project focused on operational analytics, KPIs, SLA, backlog and process improvement.

## Business Problem

Many organizations operate with limited visibility over workload, pending tasks, response times and process bottlenecks. This project simulates a back-office operational environment and analyzes key indicators to support better decision-making.

The goal is to transform raw operational data into actionable insights for management, process improvement and service quality control.

## Objectives

- Analyze operational workload.
- Measure backlog and pending tasks.
- Calculate SLA compliance.
- Identify process bottlenecks.
- Generate basic visualizations.
- Build a professional data analytics portfolio project.

## Tools

- Python
- Pandas
- Matplotlib
- SQL
- Git
- GitHub
- VS Code

## KPIs

- **Throughput:** number of processed operations.
- **Lead Time:** time from request creation to closure.
- **Backlog:** pending workload.
- **SLA Compliance:** percentage of cases resolved within expected time.
- **Rework / Observed Cases:** percentage of cases requiring review.
- **Bottlenecks:** areas, channels or operation types causing delays.

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

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Generar el dataset simulado:

```bash
python src/generar_datos.py
```