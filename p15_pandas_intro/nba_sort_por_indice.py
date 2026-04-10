# Ordenar un DataFrame usando su índice 📊🔢
#
# El método sort_index se utiliza para ordenar
# un DataFrame según los valores de su índice.
#
# El índice es la columna especial que aparece
# al lado izquierdo del DataFrame y que identifica
# cada fila.
#
# Cuando usamos sort_index, pandas reorganiza
# todas las filas siguiendo el orden de ese índice.
#
# Por ejemplo, si el índice tiene números:
# 3, 1, 4, 2
#
# Después de usar sort_index quedará ordenado así:
# 1, 2, 3, 4
#
# Esto es útil cuando el índice representa
# posiciones, identificadores o algún tipo
# de etiqueta que queremos organizar.
#
# 💡 En resumen:
# sort_index ordena el DataFrame basándose
# en el índice y no en los valores de las columnas.

import pandas as pd

nba = pd.read_csv("data/nba.csv")

print("Ordenar el DataFrame primero por Equipo y después por Nombre")
nba = nba.sort_values(["Equipo", "Nombre"])
print(nba)
print()

print("Ordenar el DataFrame usando su índice (orden ascendente por defecto)")
print(nba.sort_index())
print()

print("Ordenar el índice de forma ascendente")
print(nba.sort_index(ascending=True))
print()

print("Ordenar el índice de forma descendente")
print(nba.sort_index(ascending=False))
print()

print("Guardar el DataFrame ordenado por índice en orden descendente")
nba = nba.sort_index(ascending=False)
print(nba)
