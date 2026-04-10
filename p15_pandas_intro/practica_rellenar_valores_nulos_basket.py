## Rellenar valores faltantes con el método fillna

import pandas as pd

# Leemos el archivo del equipo de basket
basket = pd.read_csv("data/estadisticas_equipo_basket.csv")

# Mostramos el DataFrame original
print("DataFrame original:")
print(basket)

# Eliminamos filas completamente vacías
basket = basket.dropna(how="all")

print("\nDataFrame después de aplicar dropna(how='all'):")
print(basket)

print("-" * 100)

# Reemplaza TODOS los valores NaN del DataFrame con 0 (no modifica el original)
print(basket.fillna(0))

print("DataFrame después de basket.fillna(0) (sin reasignar):")
print(basket)

print("-" * 100)

# Reemplaza valores NaN en la columna "Canastas anotadas"
basket["Canastas anotadas"] = basket["Canastas anotadas"].fillna(0)

print("\nDataFrame después de rellenar NaN en 'Canastas anotadas':")
print(basket)

# Reemplaza valores NaN en la columna "Jugador" con texto
basket["Jugador"] = basket["Jugador"].fillna(value="Desconocido")

print("Columna Jugador después de reemplazar NaN por 'Desconocido':")
print(basket["Jugador"].head(20))
