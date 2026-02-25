# Lista de calificaciones del examen parcial
parciales = [80, 91, 78]

# Lista de calificaciones del examen final
finales = [98, 89, 53]

# Lista de estudiantes
estudiantes = ['dan', 'ang', 'kate']

# ---------------------------------------------------------
# Devuelve un diccionario con {estudiante: calificación más alta}
# USANDO COMPRENSIÓN DE DICCIONARIO
# Resultado esperado: {'dan': 98, 'ang': 91, 'kate': 78}
# ---------------------------------------------------------

# zip(estudiantes, parciales, finales) agrupa:
# ('dan', 80, 98), ('ang', 91, 89), ('kate', 78, 53)

calificaciones_finales = {
    t[0]: max(t[1], t[2])  # t[0] = estudiante, t[1] y t[2] = calificaciones
    for t in zip(estudiantes, parciales, finales)
}

print(calificaciones_finales)

print("-" * 100)

# ---------------------------------------------------------
# Devuelve el mismo diccionario {estudiante: calificación más alta}
# USANDO map() + lambda
# ---------------------------------------------------------

# zip(parciales, finales) genera pares:
# (80,98), (91,89), (78,53)

# map() aplica una función a cada par
# lambda pair: max(pair) obtiene la mayor calificación

calificaciones_finales = dict(
    zip(
        estudiantes,
        map(
            lambda par: max(par),  # Obtiene la nota más alta de cada par
            zip(parciales, finales)
        )
    )
)

print(calificaciones_finales)

print("-" * 100)

# ---------------------------------------------------------
# Devuelve un diccionario con {estudiante: promedio}
# Resultado esperado:
# {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
# ---------------------------------------------------------

# lambda par: (par[0] + par[1]) / 2 calcula el promedio

promedios = dict(
    zip(
        estudiantes,
        map(
            lambda par: (par[0] + par[1]) / 2,  # Promedio de parcial y final
            zip(parciales, finales)
        )
    )
)

print(promedios)
