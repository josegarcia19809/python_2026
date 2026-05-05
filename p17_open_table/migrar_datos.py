import sqlite3
import pandas as pd

# =========================
# 📂 Cargar archivos CSV
# =========================
df_res = pd.read_csv("data/reservaciones.csv")
df_resenas = pd.read_csv("data/resenas.csv")

# =========================
# 🔌 Conexión a SQLite
# =========================
conexion = sqlite3.connect("data/restaurante.db")
cursor = conexion.cursor()

# =========================
# 👤 Insertar clientes únicos
# =========================
clientes = pd.concat([
    df_res["nombre_cliente"],
    df_resenas["nombre_cliente"]
]).drop_duplicates()

for nombre in clientes:
    cursor.execute(
        "INSERT OR IGNORE INTO clientes (nombre) VALUES (?)",
        (nombre,)
    )

conexion.commit()

# =========================
# 🪑 Insertar mesas únicas
# =========================
mesas = df_res[["numero_mesa", "capacidad"]].drop_duplicates()

for _, fila in mesas.iterrows():
    cursor.execute(
        "INSERT OR IGNORE INTO mesas (numero_mesa, capacidad) VALUES (?, ?)",
        (int(fila["numero_mesa"]), int(fila["capacidad"]))
    )

conexion.commit()

# =========================
# 🔄 Obtener IDs (clientes y mesas)
# =========================
cursor.execute("SELECT id, nombre FROM clientes")
clientes_dict = {nombre: id for id, nombre in cursor.fetchall()}

cursor.execute("SELECT id, numero_mesa FROM mesas")
mesas_dict = {numero: id for id, numero in cursor.fetchall()}

# =========================
# 📅 Insertar reservaciones
# =========================
for _, fila in df_res.iterrows():
    cliente_id = clientes_dict[fila["nombre_cliente"]]
    mesa_id = mesas_dict[fila["numero_mesa"]]

    cursor.execute("""
        INSERT INTO reservaciones (
            cliente_id, mesa_id, fecha,
            hora_inicio, hora_fin,
            numero_personas, estado
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        cliente_id,
        mesa_id,
        fila["fecha"],
        fila["hora_inicio"],
        fila["hora_fin"],
        int(fila["numero_personas"]),
        fila["estado"]
    ))

conexion.commit()

# =========================
# ⭐ Insertar reseñas
# =========================
for _, fila in df_resenas.iterrows():
    cliente_id = clientes_dict[fila["nombre_cliente"]]

    cursor.execute("""
        INSERT INTO resenas (cliente_id, calificacion)
        VALUES (?, ?)
    """, (
        cliente_id,
        int(fila["calificacion"])
    ))

conexion.commit()

# =========================
# 🔍 Verificación rápida
# =========================
print("Clientes:")
cursor.execute("SELECT * FROM clientes")
print(cursor.fetchall())

print("\nMesas:")
cursor.execute("SELECT * FROM mesas")
print(cursor.fetchall())

print("\nReservaciones:")
cursor.execute("SELECT * FROM reservaciones LIMIT 5")
print(cursor.fetchall())

print("\nReseñas:")
cursor.execute("SELECT * FROM resenas")
print(cursor.fetchall())

# =========================
# 🔚 Cerrar conexión
# =========================
conexion.close()