import sqlite3

# Conexión
conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

# -----------------------------
# 1️⃣ fetchone()
# -----------------------------
# Buscar un alumno por ID

cursor.execute("SELECT * FROM alumnos WHERE id = ?", (1,))
alumno = cursor.fetchone()

print("Resultado con fetchone():")
print(alumno)

# -----------------------------
# 2️⃣ fetchall()
# -----------------------------
# Obtener todos los alumnos

cursor.execute("SELECT * FROM alumnos")
todos = cursor.fetchall()

print("\nResultado con fetchall():")
for registro in todos:
    print(registro)

# -----------------------------
# 3️⃣ fetchall() con condición
# -----------------------------
# Alumnos mayores de 20 años

cursor.execute("SELECT * FROM alumnos WHERE edad > ?", (20,))
mayores = cursor.fetchall()

print("\nAlumnos mayores de 20:")
for registro in mayores:
    print(registro)

# -----------------------------
# 4️⃣ fetchone() con agregación
# -----------------------------
# Obtener promedio de edad

cursor.execute("SELECT AVG(edad) FROM alumnos")
promedio = cursor.fetchone()

print("\nPromedio de edad:")
print(promedio[0])

# Cerrar conexión
conexion.close()
