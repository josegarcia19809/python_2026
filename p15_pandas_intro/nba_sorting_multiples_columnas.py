# Ordenar un DataFrame con el método sort_values II 📊✨
#
# También es posible ordenar un DataFrame utilizando
# varias columnas al mismo tiempo.
#
# Para hacerlo, el parámetro "by" debe recibir
# una lista con los nombres de las columnas.
#
# Pandas ordenará los datos siguiendo el orden
# en que aparecen las columnas en la lista:
# primero por la primera columna, luego por la segunda,
# después por la tercera, y así sucesivamente.
#
# Ejemplo de idea:
# ordenar primero por "Equipo" 🏀
# y después por "Salario" 💰
#
# El parámetro "ascending" permite decidir
# si el orden será ascendente o descendente.
#
# Si se usa un solo valor booleano:
# True  → todas las columnas se ordenan de forma ascendente ⬆️
# False → todas las columnas se ordenan de forma descendente ⬇️
#
# También es posible pasar una lista de valores booleanos
# para definir el tipo de orden en cada columna.
#
# ⚠️ Importante:
# La cantidad de valores en la lista "ascending"
# debe coincidir con la cantidad de columnas
# indicadas en la lista "by".
#
# 💡 Ejemplo conceptual:
# ordenar por ["Equipo", "Salario"]
# con [True, False]
#
# Esto significa:
# - Equipo → orden ascendente
# - Salario → orden descendente
#
# Este tipo de ordenamiento es muy útil para
# analizar mejor los datos cuando hay
# varias características importantes.

import pandas as pd

nba = pd.read_csv("data/nba.csv")

print(nba.head())

print(
    "Ordenar los jugadores primero por Equipo y después por Nombre (orden ascendente por defecto)")
print(nba.sort_values(["Equipo", "Nombre"]))
print()

print("Ordenar los jugadores por Equipo y Nombre usando el parámetro by")
print(nba.sort_values(by=["Equipo", "Nombre"]))
print()

print("Ordenar por Equipo y Nombre en orden ascendente")
print(nba.sort_values(by=["Equipo", "Nombre"], ascending=True))
print()

print("Ordenar por Equipo y Nombre en orden descendente")
print(nba.sort_values(by=["Equipo", "Nombre"], ascending=False))
print()

print("Ordenar por Equipo (ascendente) y Nombre (descendente)")
print(nba.sort_values(by=["Equipo", "Nombre"], ascending=[True, False]))
print()

print("Ordenar jugadores por Posición y luego por Salario (orden ascendente por defecto)")
print(nba.sort_values(["Posición", "Salario"]))
print()

print("Ordenar por Posición y Salario en orden ascendente")
print(nba.sort_values(["Posición", "Salario"], ascending=True))
print()

print("Ordenar por Posición y Salario en orden descendente")
print(nba.sort_values(["Posición", "Salario"], ascending=False))
print()

print("Ordenar por Posición (ascendente) y Salario (descendente)")
print(nba.sort_values(["Posición", "Salario"], ascending=[True, False]))
print()

print("Ordenar por Posición (descendente) y Salario (ascendente)")
print(nba.sort_values(["Posición", "Salario"], ascending=[False, True]))
print()

print("Guardar el DataFrame ordenado por Posición (descendente) y Salario (ascendente)")
nba = nba.sort_values(["Posición", "Salario"], ascending=[False, True])
print(nba)
