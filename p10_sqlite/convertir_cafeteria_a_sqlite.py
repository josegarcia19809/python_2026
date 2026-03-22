import pandas as pd
import sqlite3

# Leer el archivo CSV
df = pd.read_csv("data/cafeterias.csv")

# Reemplazar valores nulos por 0
df = df.fillna(0)

# Mostrar las primeras filas
print(df)

# Crear conexión a SQLite (se crea el archivo si no existe)
conn = sqlite3.connect("data/cafeterias.db")

# Guardar el DataFrame como tabla
df.to_sql("cafeterias", conn, if_exists="replace", index=False)

# Cerrar conexión
conn.close()