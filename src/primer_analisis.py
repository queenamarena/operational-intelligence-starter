# Operational Intelligence Starter
# Primer script de análisis operativo

project_name = "Operational Intelligence Starter"
area = "Back Office Operations"

kpi_focus = [
    "Throughput",
    "Lead Time",
    "Backlog",
    "SLA Compliance"
]

print("Proyecto:", project_name)
print("Área analizada:", area)
print("KPIs iniciales:")

for kpi in kpi_focus:
    print("-", kpi)