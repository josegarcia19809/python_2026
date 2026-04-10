## Eliminar filas con valores faltantes

import pandas as pd

nba = pd.read_csv("data/nba.csv")

print(nba.head(30))

# Pandas usa la designación NaN para representar valores faltantes.

# Elimina las filas que tengan AL MENOS un valor faltante (comportamiento por defecto).
print("dropna() -> Elimina filas con cualquier NaN")
print(nba.dropna())
print("-" * 50)

# Hace exactamente lo mismo que el anterior: elimina filas con cualquier NaN.
print('dropna(how="any") -> Elimina filas con cualquier NaN')
print(nba.dropna(how="any"))
print("-" * 50)

# Elimina únicamente las filas donde TODOS los valores sean NaN.
print('dropna(how="all") -> Elimina filas donde todos los valores son NaN')
print(nba.dropna(how="all"))
print("-" * 50)

# Elimina filas donde la columna "Universidad" tenga valores NaN.
print('dropna(subset=["Universidad"]) -> Elimina filas con NaN en "Universidad"')
print(nba.dropna(subset=["Universidad"]))
print("-" * 50)

# Elimina filas donde "Universidad" o "Salario" tengan valores NaN.
# Solo evalúa esas columnas para decidir si elimina la fila.
print(
    'dropna(subset=["Universidad", "Salario"]) -> Elimina filas con NaN en Universidad o Salario')
print(nba.dropna(subset=["Universidad", "Salario"]))
print("-" * 50)
