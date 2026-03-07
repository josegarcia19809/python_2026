# Ordenar un DataFrame con el método sort_values 📊🔎
#
# El método sort_values se utiliza para ordenar un DataFrame
# según los valores de una o varias columnas.
#
# Por defecto, el orden es ascendente ⬆️
# (alfabético cuando se trata de texto).
#
# El primer parámetro, llamado "by", indica la columna
# o columnas por las que se quiere ordenar el DataFrame.
#
# Si solo se va a ordenar por una columna,
# simplemente se escribe el nombre de la columna como texto.
#
# El parámetro "ascending" permite elegir el tipo de orden:
# True  → orden ascendente ⬆️
# False → orden descendente ⬇️
#
# El parámetro "na_position" permite decidir dónde colocar
# los valores faltantes (NaN) dentro del ordenamiento:
# "first" → los NaN aparecen al inicio
# "last"  → los NaN aparecen al final
#
# 💡 Tip: Este método es muy útil para analizar datos rápidamente,
# por ejemplo ordenar ventas de mayor a menor,
# organizar nombres alfabéticamente o encontrar
# los valores más altos o más bajos de un conjunto de datos.

import pandas as pd

nba = pd.read_csv("data/nba.csv")

print(nba.head())

print("Ordenar los jugadores por Nombre (orden ascendente por defecto)")
print(nba.sort_values("Nombre"))
print()

print("Ordenar los jugadores por Nombre usando el parámetro by")
print(nba.sort_values(by="Nombre"))
print()

print("Ordenar los jugadores por Nombre en orden ascendente")
print(nba.sort_values(by="Nombre", ascending=True))
print()

print("Ordenar los jugadores por Nombre en orden descendente")
print(nba.sort_values(by="Nombre", ascending=False))
print()

print("Ordenar los jugadores por Salario (de menor a mayor)")
print(nba.sort_values("Salario"))
print()

print("Ordenar los jugadores por Salario (de mayor a menor)")
print(nba.sort_values("Salario", ascending=False))
print()

print("Ordenar por Salario colocando los valores faltantes (NaN) al final")
print(nba.sort_values("Salario", na_position="last"))
print()

print("Ordenar por Salario colocando los valores faltantes (NaN) al inicio")
print(nba.sort_values("Salario", na_position="first"))
print()

print("Ordenar por Salario de mayor a menor y colocando los NaN al inicio")
print(nba.sort_values("Salario", na_position="first", ascending=False))