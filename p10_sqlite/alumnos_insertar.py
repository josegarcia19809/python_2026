import sqlite3

# Conexión
conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS alumnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    edad INTEGER
)
""")

# -----------------------------
# 1️⃣ Insertar con executemany
# -----------------------------

lista_alumnos_1 = [
    ("Carlos", 21),
    ("Lucía", 20),
    ("Pedro", 23)
]

cursor.executemany(
    "INSERT INTO alumnos (nombre, edad) VALUES (?, ?)",
    lista_alumnos_1
)

# -----------------------------
# 2️⃣ Insertar con ciclo for
# -----------------------------

lista_alumnos_2 = [
    ("Sofía", 19),
    ("Miguel", 22),
    ("Elena", 21)
]

for alumno in lista_alumnos_2:
    cursor.execute(
        "INSERT INTO alumnos (nombre, edad) VALUES (?, ?)",
        alumno
    )

# Guardar cambios
conexion.commit()

# Mostrar resultados
cursor.execute("SELECT * FROM alumnos")
registros = cursor.fetchall()

print("Lista completa de alumnos:")
for alumno in registros:
    print(alumno)

# Cerrar conexión
conexion.close()
