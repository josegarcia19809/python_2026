-- 1️⃣ Rendimiento por ciudad
-- 👉 ¿Qué ciudad genera mayor ingreso semanal total?
SELECT ciudad, SUM(Ingreso_Semanal) AS total_ingreso
FROM cafeterias
GROUP BY ciudad
ORDER BY total_ingreso DESC
LIMIT 1;

-- 2️⃣ Cafeterías más eficientes
-- 👉 ¿Qué cafetería tiene el mayor ingreso promedio por cliente?

SELECT Cafeteria,
       AVG(
           CASE
               WHEN Clientes_Semana = 0 THEN NULL
               ELSE Ingreso_Semanal * 1.0 / Clientes_Semana
           END
       ) AS ingreso_por_cliente
FROM cafeterias
GROUP BY Cafeteria
ORDER BY ingreso_por_cliente DESC
LIMIT 1;


-- 3️⃣ Relación ventas vs clientes
-- 👉 ¿Qué cafeterías venden más bebidas por cliente?

SELECT Cafeteria,
       AVG(
           CASE
               WHEN Clientes_Semana = 0 THEN NULL
               ELSE Bebidas_Vendidas * 1.0 / Clientes_Semana
           END
       ) AS bebidas_por_cliente
FROM cafeterias
GROUP BY Cafeteria
ORDER BY bebidas_por_cliente DESC
LIMIT 1;


-- 4️⃣ Identificación de bajo rendimiento
-- 👉 ¿Qué cafeterías tienen ingresos por debajo del promedio general?

SELECT DISTINCT Cafeteria
FROM cafeterias
WHERE Ingreso_Semanal < (
    SELECT AVG(Ingreso_Semanal)
    FROM cafeterias
);
