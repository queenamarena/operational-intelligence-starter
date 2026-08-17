# Operational Intelligence Starter
# Analisis operativo con datos simulados

project_name = "Operational Intelligence Starter"
area = "Back Office Operations"

operations = [
    {"id": 1, "type": "Emision", "status": "Cerrado", "resolution_hours": 12},
    {"id": 2, "type": "Renovacion", "status": "Cerrado", "resolution_hours": 20},
    {"id": 3, "type": "Reclamo", "status": "Pendiente", "resolution_hours": None},
    {"id": 4, "type": "Liquidacion", "status": "Cerrado", "resolution_hours": 36},
    {"id": 5, "type": "Mora", "status": "Observado", "resolution_hours": 48},
    {"id": 6, "type": "Emision", "status": "Cerrado", "resolution_hours": 8},
    {"id": 7, "type": "Renovacion", "status": "Pendiente", "resolution_hours": None},
    {"id": 8, "type": "Reclamo", "status": "Cerrado", "resolution_hours": 30},
]

sla_target_hours = 24

total_operations = len(operations)

closed_operations = [
    operation for operation in operations
    if operation["status"] == "Cerrado"
]

pending_operations = [
    operation for operation in operations
    if operation["status"] == "Pendiente"
]

observed_operations = [
    operation for operation in operations
    if operation["status"] == "Observado"
]

closed_within_sla = [
    operation for operation in closed_operations
    if operation["resolution_hours"] <= sla_target_hours
]

sla_compliance = len(closed_within_sla) / len(closed_operations) * 100

average_lead_time = sum(
    operation["resolution_hours"] for operation in closed_operations
) / len(closed_operations)

print("Proyecto:", project_name)
print("Area analizada:", area)
print("-" * 40)

print("Total de operaciones:", total_operations)
print("Operaciones cerradas:", len(closed_operations))
print("Backlog pendiente:", len(pending_operations))
print("Operaciones observadas:", len(observed_operations))
print("SLA objetivo:", sla_target_hours, "horas")
print("Cumplimiento SLA:", round(sla_compliance, 2), "%")
print("Lead Time promedio:", round(average_lead_time, 2), "horas")