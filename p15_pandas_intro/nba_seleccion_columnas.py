# nba_seleccion_columnas

import pandas as pd

nba = pd.read_csv("data/nba.csv")

print(nba.head())

print("-" * 100)
print("Seleccionar la columna Salario usando sintaxis de atributo")
print(nba.Salario)
print("-" * 100)

# Ejercicios
# Seleccionar la columna Nombre usando sintaxis de atributo
# Seleccionar la columna Equipo usando sintaxis de atributo
# Seleccionar la columna Posición usando sintaxis de atributo

print("-" * 100)
print("Seleccionar la columna Salario usando corchetes")
print(nba["Salario"])
print("-" * 100)

# Ejercicios
# Seleccionar la columna Altura usando corchetes
# Seleccionar la columna Peso usando corchetes
# Seleccionar la columna Universidad usando corchetes

print("-" * 100)
print("Seleccionar una columna y guardarla en una variable")
nombres = nba["Nombre"]
print(nombres)
print("-" * 100)

# Ejercicios
# Extrae la columna "Equipo" del DataFrame y asígnala a la variable equipos.
# Extrae la columna "Posición" del DataFrame y asígnala a la variable posiciones.
# Extrae la columna "Salario" del DataFrame y asígnala a la variable salarios.
# Imprime cada variable en pantalla.

print("-" * 100)
print("Seleccionar múltiples columnas directamente")
print("-" * 100)
seleccion = nba[["Equipo", "Salario"]]
print(seleccion.head())

print("-" * 100)
print("Seleccionar múltiples columnas usando una lista con los nombres")
print("-" * 100)
columnas = ["Equipo", "Altura", "Salario"]
seleccion = nba[columnas]
print(seleccion.head())
