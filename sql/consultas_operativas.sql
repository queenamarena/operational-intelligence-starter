-- Operational Intelligence Starter
-- Consultas SQL para análisis operativo

-- 1. Total de operaciones
SELECT COUNT(*) AS total_operaciones
FROM operaciones_backoffice;

-- 2. Operaciones por estado
SELECT 
    estado,
    COUNT(*) AS cantidad
FROM operaciones_backoffice
GROUP BY estado
ORDER BY cantidad DESC;

-- 3. Backlog pendiente
SELECT COUNT(*) AS backlog_pendiente
FROM operaciones_backoffice
WHERE estado = 'Pendiente';

-- 4. Operaciones cerradas
SELECT COUNT(*) AS operaciones_cerradas
FROM operaciones_backoffice
WHERE estado = 'Cerrado';

-- 5. Cumplimiento SLA
SELECT 
    ROUND(
        SUM(CASE 
            WHEN estado = 'Cerrado' AND tiempo_resolucion_horas <= 24 THEN 1 
            ELSE 0 
        END) * 100.0 /
        SUM(CASE 
            WHEN estado = 'Cerrado' THEN 1 
            ELSE 0 
        END),
        2
    ) AS sla_compliance_percentage
FROM operaciones_backoffice;

-- 6. Lead time promedio
SELECT 
    ROUND(AVG(tiempo_resolucion_horas), 2) AS lead_time_promedio
FROM operaciones_backoffice
WHERE estado = 'Cerrado';

-- 7. Operaciones por tipo
SELECT 
    tipo_operacion,
    COUNT(*) AS cantidad
FROM operaciones_backoffice
GROUP BY tipo_operacion
ORDER BY cantidad DESC;

-- 8. Operaciones por canal
SELECT 
    canal,
    COUNT(*) AS cantidad
FROM operaciones_backoffice
GROUP BY canal
ORDER BY cantidad DESC;

-- 9. Operaciones por sucursal
SELECT 
    sucursal,
    COUNT(*) AS cantidad
FROM operaciones_backoffice
GROUP BY sucursal
ORDER BY cantidad DESC;

-- 10. Casos fuera de SLA
SELECT 
    id_operacion,
    tipo_operacion,
    sucursal,
    canal,
    tiempo_resolucion_horas
FROM operaciones_backoffice
WHERE estado = 'Cerrado'
  AND tiempo_resolucion_horas > 24
ORDER BY tiempo_resolucion_horas DESC;