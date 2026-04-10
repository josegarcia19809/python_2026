import pandas as pd

basket = pd.read_csv("data/estadisticas_equipo_basket.csv").dropna(how="all")

print("DataFrame después de eliminar filas completamente vacías:")
print(basket)

# Cantidad de posiciones únicas
print("Cantidad de posiciones únicas:")
print(basket["Posición"].nunique())

# Cantidad de valores únicos por columna
print("\nCantidad de valores únicos por columna:")
print(basket.nunique())

print("*" * 50)
print(basket.info())

# Convertir la columna Posición a tipo category
basket["Posición"] = basket["Posición"].astype("category")

# Verificar tipos de datos
print("Tipos de datos después de convertir a category:")
print(basket.dtypes)

print("*" * 50)
print(basket.info())

# Mostrar categorías
print("Categorías de la columna Posición:")
print(basket["Posición"].cat.categories)
