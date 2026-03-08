# Asignar posiciones o rankings con el método rank 🏆📊
#
# El método rank se utiliza para asignar una posición
# numérica a cada valor dentro de una Serie (Series) de pandas.
#
# Es como hacer una clasificación o ranking,
# por ejemplo para saber:
# - quién tiene el salario más alto 💰
# - quién es el más alto 📏
# - o quién pesa más ⚖️
#
# Pandas asigna un número de posición a cada valor
# dependiendo de su lugar en el orden.
#
# Algo importante es que cuando existen valores iguales,
# pandas les asigna el mismo ranking.
#
# Cuando esto sucede, se genera un pequeño "salto"
# en los números del ranking.
#
# Ejemplo sencillo:
# Valores: 100, 90, 90, 80
#
# Ranking:
# 100 → 1
# 90  → 2
# 90  → 2
# 80  → 4
#
# Observa que el número 3 se "salta" porque
# dos valores compartieron el mismo ranking.
#
# 💡 Este método es muy útil para analizar datos,
# crear clasificaciones o identificar rápidamente
# los valores más altos o más bajos en un conjunto de datos.

import pandas as pd

nba = pd.read_csv("data/nba.csv")
nba["Salario"] = nba["Salario"].fillna(0).astype(int)

print("Asignar un ranking a los jugadores según su Salario")
print(nba["Salario"].rank())
print()

print("Asignar un ranking al Salario en orden ascendente (de menor a mayor)")
print(nba["Salario"].rank(ascending=True))
print()

print(
    "Asignar un ranking al Salario en orden descendente (de mayor a menor) y convertirlo a número entero")
print(nba["Salario"].rank(ascending=False).astype(int))
print()

print(
    "Crear una nueva columna llamada 'Ranking Salario' con la posición de cada jugador según su salario")
nba["Ranking Salario"] = nba["Salario"].rank(ascending=False).astype(int)
print(nba)
print()

print("Mostrar los 10 jugadores con mayor salario")
print(nba.sort_values("Salario", ascending=False).head(10))
