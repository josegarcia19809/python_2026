import sqlite3

# Conexión (si no existe, se crea el archivo)
conexion = sqlite3.connect("data/restaurante.db")

cursor = conexion.cursor()

# 👤 Tabla: clientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE
)
""")

# 🪑 Tabla: mesas
cursor.execute("""
CREATE TABLE IF NOT EXISTS mesas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_mesa INTEGER NOT NULL UNIQUE,
    capacidad INTEGER NOT NULL
)
""")

# 📅 Tabla: reservaciones
cursor.execute("""
CREATE TABLE IF NOT EXISTS reservaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    mesa_id INTEGER NOT NULL,
    fecha DATE NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    numero_personas INTEGER NOT NULL,
    estado TEXT NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (mesa_id) REFERENCES mesas(id)
)
""")

# ⭐ Tabla: resenas
cursor.execute("""
CREATE TABLE IF NOT EXISTS resenas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    calificacion INTEGER NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
)
""")

# Guardar cambios
conexion.commit()

# Consultar tablas creadas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = cursor.fetchall()

print("Tablas en la base de datos:")
for tabla in tablas:
    print(tabla)

# Cerrar conexión
conexion.close()