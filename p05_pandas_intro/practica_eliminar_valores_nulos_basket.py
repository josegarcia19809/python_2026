## Eliminar filas con valores faltantes

import pandas as pd

basket = pd.read_csv("data/estadisticas_equipo_basket.csv")

print(basket.head(30))

# Pandas usa la designación NaN para representar valores faltantes.

# Elimina las filas que tengan AL MENOS un valor faltante (comportamiento por defecto).
print("dropna() -> Elimina filas con cualquier NaN")
print(basket.dropna())
print("-" * 50)

# Hace exactamente lo mismo que el anterior.
print('dropna(how="any") -> Elimina filas con cualquier NaN')
print(basket.dropna(how="any"))
print("-" * 50)

# Elimina únicamente las filas donde TODOS los valores sean NaN.
print('dropna(how="all") -> Elimina filas donde todos los valores son NaN')
print(basket.dropna(how="all"))
print("-" * 50)

# Elimina filas donde la columna "Canastas anotadas" tenga valores NaN.
print('dropna(subset=["Canastas anotadas"]) -> Elimina filas con NaN en "Canastas anotadas"')
print(basket.dropna(subset=["Canastas anotadas"]))
print("-" * 50)

# Elimina filas donde "Canastas anotadas" o "Asistencias" tengan valores NaN.
print(
    'dropna(subset=["Canastas anotadas", "Asistencias"]) -> Elimina filas con NaN en esas columnas'
)

print(basket.dropna(subset=["Canastas anotadas", "Asistencias"]))
print("-" * 50)
