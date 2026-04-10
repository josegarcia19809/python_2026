## Rellenar valores faltantes con el método fillna
# - El método `fillna` reemplaza los valores faltantes `NaN` con el argumento que se le proporcione.
# - El método `fillna` está disponible tanto en **DataFrames** como en **Series**.
# - Una **Series** extraída es una vista del **DataFrame** original, pero el método `fillna` devuelve una copia.

import pandas as pd

# Leemos el archivo "nba.csv" y lo convertimos en un DataFrame
nba = pd.read_csv("data/nba.csv")

# Mostramos el DataFrame original (antes de limpiar)
print("DataFrame original:")
print(nba)

# dropna(how="all") elimina las filas donde TODOS los valores son NaN
# Es decir, si una fila está completamente vacía, la elimina
nba = nba.dropna(how="all")

# Mostramos el DataFrame después de eliminar filas completamente vacías
print("\nDataFrame después de aplicar dropna(how='all'):")
print(nba)

print("-" * 100)
# Reemplaza TODOS los valores NaN del DataFrame con 0
# IMPORTANTE: esto NO modifica el DataFrame original
print(nba.fillna(0))

# Si queremos ver el resultado correctamente:
print("DataFrame después de nba.fillna(0) (sin reasignar):")
print(nba)

print("-" * 100)
# Reemplaza los valores NaN SOLO en la columna "Salary" con 0
# Aquí sí estamos guardando el resultado en la columna original
nba["Salario"] = nba["Salario"].fillna(0)

print("\nDataFrame después de rellenar NaN en la columna Salary:")
print(nba)

# Reemplaza los valores NaN en la columna "Universidad" por el texto "Unknown"
# fillna() devuelve una copia, pero aquí la estamos reasignando,
# por eso sí se modifica la columna original
nba["Universidad"] = nba["Universidad"].fillna(value="Unknown")

# Mostramos el resultado
print("Columna Universidad después de reemplazar NaN por 'Unknown':")
print(nba["Universidad"].head(16))