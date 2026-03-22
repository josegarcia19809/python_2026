import pandas as pd
import numpy as np

# Leer el archivo CSV
df = pd.read_csv("data/cafeterias.csv")

# Reemplazar valores nulos por 0
df = df.fillna(0)

# Mostrar las primeras filas
print(df)


# 1️⃣ Rendimiento por ciudad
# 👉 ¿Qué ciudad genera mayor ingreso semanal total?
ingreso_ciudad = df.groupby("Ciudad")["Ingreso_Semanal"].sum()

print("Ciudad con mayor ingreso: ")
top_ciudad = ingreso_ciudad.idxmax()
max_ingreso = ingreso_ciudad.max()

print(top_ciudad, max_ingreso)

# 2️⃣ Cafeterías más eficientes
# Reemplazar 0 por NaN para evitar división entre cero
df["Clientes_Semana"] = df["Clientes_Semana"].replace(0, np.nan)

# Calcular ingreso por cliente
df["ingreso_por_cliente"] = df["Ingreso_Semanal"] / df["Clientes_Semana"]

# Opcional: reemplazar NaN por 0 si lo deseas
df["ingreso_por_cliente"] = df["ingreso_por_cliente"].fillna(0)

# Agrupar
eficiencia = df.groupby("Cafeteria")["ingreso_por_cliente"].mean()

top_cafeteria = eficiencia.idxmax()
max_valor = eficiencia.max()

print()
print("👉 ¿Qué cafetería tiene el mayor ingreso promedio por cliente?")
print(top_cafeteria, max_valor)


# 3️⃣ Relación ventas vs clientes
# 👉 ¿Qué cafeterías venden más bebidas por cliente?

# Evitar división entre cero sin modificar la columna original
df["bebidas_por_cliente"] = df["Bebidas_Vendidas"] / df["Clientes_Semana"].replace(0, np.nan)

# Opcional: reemplazar NaN por 0
df["bebidas_por_cliente"] = df["bebidas_por_cliente"].fillna(0)

# Agrupar por cafetería
ventas_cliente = df.groupby("Cafeteria")["bebidas_por_cliente"].mean()

top_ventas = ventas_cliente.idxmax()
max_ventas = ventas_cliente.max()

print()
print("👉 ¿Qué cafeterías venden más bebidas por cliente?")
print(top_ventas, max_ventas)

# 4️⃣ Identificación de bajo rendimiento (corregido)
# 👉 ¿Qué cafeterías tienen ingresos por debajo del promedio general?
# Asegurar que no haya nulos (por si vienen del paso anterior)
df["Ingreso_Semanal"] = df["Ingreso_Semanal"].fillna(0)

# Calcular promedio general
promedio_general = df["Ingreso_Semanal"].mean()

# Filtrar cafeterías por debajo del promedio
bajo_rendimiento = df[df["Ingreso_Semanal"] < promedio_general]

# Obtener nombres únicos
cafeterias_bajo = bajo_rendimiento["Cafeteria"].unique()

print()
print("👉 ¿Qué cafeterías tienen ingresos por debajo del promedio general?")
print(cafeterias_bajo)