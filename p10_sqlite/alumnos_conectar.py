import sqlite3

# Conexión (si no existe, se crea el archivo)
conexion = sqlite3.connect("escuela.db")

cursor = conexion.cursor()

# Crear una tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS alumnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    edad INTEGER
)
""")

# Insertar datos
cursor.execute("INSERT INTO alumnos (nombre, edad) VALUES (?, ?)", ("Ana", 20))
cursor.execute("INSERT INTO alumnos (nombre, edad) VALUES (?, ?)", ("Luis", 22))
cursor.execute("INSERT INTO alumnos (nombre, edad) VALUES (?, ?)", ("María", 19))

# Guardar cambios
conexion.commit()

# Consultar datos
cursor.execute("SELECT * FROM alumnos")
registros = cursor.fetchall()

print("Lista de alumnos:")
for alumno in registros:
    print(alumno)

# Cerrar conexión
conexion.close()
