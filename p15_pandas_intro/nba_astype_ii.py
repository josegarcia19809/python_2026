# ## El método astype category
# - El tipo `category` es ideal para columnas que tienen un número limitado de valores únicos.
# - El método `nunique` devuelve una **Series** con la cantidad de valores únicos en cada columna.
# - Con el tipo `category`, pandas no crea un valor separado en memoria para cada "celda".
#   En su lugar, las celdas apuntan a una sola copia por cada valor único.

import pandas as pd

nba = pd.read_csv("data/nba.csv").dropna(how="all")

print("DataFrame después de eliminar filas completamente vacías:")
print(nba)

# Cuenta cuántos valores únicos existen en la columna "Equipo"
print("Cantidad de equipos únicos:")
print(nba["Equipo"].nunique())

# Cuenta cuántos valores únicos hay en cada columna del DataFrame
print("\nCantidad de valores únicos por columna:")
print(nba.nunique())

# 🎯 ¿Para qué sirve esto?
# 
# Si una columna tiene pocos valores únicos (por ejemplo Equipo o Posición), es buena candidata para:
# 
# nba["Equipo"] = nba["Equipo"].astype("category")
# 
# Porque mejora el uso de memoria y rendimiento.

print("**" * 50)
print(nba.info())

# Convertimos la columna "Posición" al tipo category
# Esto es útil cuando la columna tiene pocos valores únicos (por ejemplo: PG, SG, SF, PF, C)
nba["Posición"] = nba["Posición"].astype("category")

# Convertimos la columna "Equipo" al tipo category
# Ideal porque el número de equipos es limitado (aprox. 30)
nba["Equipo"] = nba["Equipo"].astype("category")

# Verificamos los tipos de datos después de la conversión
print("Tipos de datos después de convertir a category:")
print(nba.dtypes)

print("**" * 50)
print(nba.info())

# 🔎 ¿Qué hace astype("category")?
#
# Convierte la columna en un tipo especial llamado category.
#
# En lugar de guardar el texto repetido muchas veces, guarda una sola copia de cada valor único.
#
# Las filas solo apuntan a esa copia.
#
# Reduce el uso de memoria.
#
# Puede mejorar el rendimiento en operaciones de agrupación (groupby).
#
# 🎯 ¿Cuándo conviene usarlo?
#
# Cuando una columna:
#
# Tiene pocos valores distintos.
#
# Repite mucho los mismos valores.
#
# Representa categorías (equipos, posiciones, estados, etc.).
#
# 💡 Si haces:
print("**" * 50)
print(nba["Equipo"].cat.categories)

# Podrás ver todas las categorías almacenadas internamente.
